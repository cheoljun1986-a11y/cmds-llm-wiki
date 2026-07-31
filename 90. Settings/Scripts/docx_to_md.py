# ============================================================
# 90. Settings/Scripts/docx_to_md.py
#
# 이 파일이 하는 일:
#   Word 문서(.docx)를 마크다운(.md)으로 바꿔 줍니다.
#   LLM Wiki 의 /ingest 는 마크다운만 다룰 수 있어서, 워드 파일을 Inbox 에
#   넣었을 때 먼저 이 스크립트로 변환한 뒤 ingest 를 진행합니다.
#
#   markitdown 이나 pandoc 같은 외부 프로그램을 설치하지 않아도 됩니다.
#   .docx 는 사실 압축(ZIP) 파일이고 그 안에 XML 이 들어 있어서,
#   파이썬에 기본 포함된 기능만으로 읽어낼 수 있습니다.
#
# 쓰는 방법 (터미널에서):
#   python "90. Settings/Scripts/docx_to_md.py" "00. Inbox/보고서.docx"
#     -> 같은 폴더에 "보고서.md" 를 만듭니다.
#
#   python "90. Settings/Scripts/docx_to_md.py" 입력.docx -o 출력.md
#     -> 출력 파일 이름을 직접 정합니다.
#
#   문서 안에 그림이 있으면 "80. References/Attachments/" 로 함께 빼냅니다.
#
# 무엇을 살려내나:
#   - 제목 (개요 수준을 읽어 #, ##, ### 로 변환)
#   - 문단, 굵은 글씨, 기울임
#   - 글머리 기호 / 번호 목록
#   - 표 (마크다운 표로 변환)
#   - 그림 (파일로 빼내고 ![[파일명]] 으로 연결)
#
# 무엇을 못 살리나 (한계):
#   - 글자 색, 글꼴, 정교한 칸 병합 같은 시각적 서식
#   - 도형, 차트, 수식은 [도형], [차트] 같은 표시만 남습니다
#   -> 그래서 변환 품질(conversion-fidelity)은 보통 medium 으로 봅니다.
# ============================================================

import argparse
import os
import re
import sys
import zipfile
import xml.etree.ElementTree as ET


# Word 문서의 XML 은 "이름공간(namespace)" 이라는 접두사를 씁니다.
# 아래는 자주 쓰는 이름공간 주소들입니다. 태그를 찾을 때 이 주소가 필요합니다.
NS = {
    "w": "http://schemas.openxmlformats.org/wordprocessingml/2006/main",
    "r": "http://schemas.openxmlformats.org/officeDocument/2006/relationships",
    "a": "http://schemas.openxmlformats.org/drawingml/2006/main",
    "wp": "http://schemas.openxmlformats.org/drawingml/2006/wordprocessingDrawing",
}


def parse_xml_safely(xml_bytes: bytes, where: str):
    """
    XML 을 읽어들이되, 악의적으로 만들어진 파일로부터 스스로를 보호합니다.

    왜 이런 검사가 필요한가:
      XML 에는 '엔티티' 라는 축약 기능이 있는데, 이걸 겹겹이 중첩하면
      작은 파일 하나로 메모리를 폭발시킬 수 있습니다(billion laughs 공격).
      바깥 파일을 몰래 읽어 가는 공격(XXE)도 같은 통로를 씁니다.
      두 공격 모두 <!DOCTYPE ...> 선언이 있어야만 성립합니다.

      Word 가 만드는 문서에는 DOCTYPE 이 들어가지 않습니다. 그래서
      "DOCTYPE 이 보이면 읽지 않는다" 는 규칙만으로 정상 문서는 그대로 두고
      위험한 파일만 걸러낼 수 있습니다.

    입력:
      - xml_bytes: 읽어들일 XML 원본 바이트
      - where: 문제가 생겼을 때 알려줄 위치 이름 (예: 'word/document.xml')
    출력:
      - 파싱된 XML 최상위 요소
    """
    # 앞부분만 확인해도 충분합니다. DOCTYPE 은 항상 문서 맨 앞에 옵니다.
    head = xml_bytes[:2048].lstrip()
    if b"<!DOCTYPE" in head.upper() or b"<!ENTITY" in xml_bytes[:8192].upper():
        raise ValueError(
            "이 문서 안의 %s 에 위험할 수 있는 DOCTYPE/ENTITY 선언이 들어 있어 "
            "읽기를 중단했습니다.\n"
            "정상적인 Word 파일에는 이런 선언이 없습니다. 파일 출처를 확인해 주세요." % where
        )
    return ET.fromstring(xml_bytes)


def w(tag_name: str) -> str:
    """
    'w:p' 같은 짧은 이름을 XML 이 실제로 쓰는 긴 이름으로 바꿔 줍니다.

    입력:
      - tag_name: 'p', 'tbl' 처럼 w 이름공간에 속한 태그 이름
    출력:
      - '{긴주소}p' 형태의 문자열 (ElementTree 가 이해하는 형식)
    """
    return "{%s}%s" % (NS["w"], tag_name)


def get_attr(element, tag_name: str, attr_name: str = "val"):
    """
    자식 태그 하나를 찾아 그 속성값을 돌려줍니다. 없으면 None 을 돌려줍니다.

    입력:
      - element: 뒤질 XML 요소
      - tag_name: 찾을 자식 태그 이름 (예: 'pStyle')
      - attr_name: 읽어올 속성 이름 (기본값 'val')
    출력:
      - 속성값 문자열, 또는 없으면 None
    """
    found = element.find(w(tag_name))
    if found is None:
        return None
    return found.get(w(attr_name))


def detect_heading_level(paragraph) -> int:
    """
    이 문단이 제목인지, 몇 단계 제목인지 알아냅니다.

    왜 두 가지 방법을 쓰나:
      한글판 Word 는 제목 스타일 이름을 '제목 1' 이나 '1' 로 저장합니다.
      영문판은 'Heading1' 입니다. 스타일 이름에만 의존하면 한글 문서에서
      제목을 통째로 놓칩니다. 그래서 언어와 상관없는 '개요 수준(outlineLvl)'
      을 먼저 보고, 없을 때만 스타일 이름을 봅니다.

    입력:
      - paragraph: w:p (문단) XML 요소
    출력:
      - 1~6 사이의 정수 (제목 단계). 제목이 아니면 0.
    """
    properties = paragraph.find(w("pPr"))
    if properties is None:
        return 0

    # 방법 1) 개요 수준 — 0 이 가장 큰 제목이므로 +1 해서 1단계로 맞춥니다.
    outline_value = get_attr(properties, "outlineLvl")
    if outline_value is not None and outline_value.isdigit():
        level = int(outline_value) + 1
        if 1 <= level <= 6:
            return level

    # 방법 2) 스타일 이름 — 영문/한글 두 표기를 모두 받아 줍니다.
    style_name = get_attr(properties, "pStyle")
    if style_name:
        match = re.search(r"(?:heading|제목)\s*(\d)", style_name, re.IGNORECASE)
        if match:
            level = int(match.group(1))
            if 1 <= level <= 6:
                return level
        # 스타일 이름이 그냥 숫자 하나인 경우도 제목으로 취급합니다.
        if style_name.isdigit() and 1 <= int(style_name) <= 6:
            return int(style_name)

    return 0


def is_list_paragraph(paragraph) -> bool:
    """
    이 문단이 글머리 기호나 번호가 붙은 목록 항목인지 알려줍니다.

    입력:
      - paragraph: w:p (문단) XML 요소
    출력:
      - True / False
    """
    properties = paragraph.find(w("pPr"))
    if properties is None:
        return False
    return properties.find(w("numPr")) is not None


def get_list_indent(paragraph) -> int:
    """
    목록 항목이 몇 단계 안쪽으로 들어가 있는지 알려줍니다. (0 = 가장 바깥)

    입력:
      - paragraph: w:p (문단) XML 요소
    출력:
      - 0 이상의 정수
    """
    properties = paragraph.find(w("pPr"))
    if properties is None:
        return 0
    numbering = properties.find(w("numPr"))
    if numbering is None:
        return 0
    level_value = get_attr(numbering, "ilvl")
    if level_value is not None and level_value.isdigit():
        return int(level_value)
    return 0


def merge_adjacent_emphasis(text: str) -> str:
    """
    바로 붙어 있는 굵게/기울임 구간을 하나로 합쳐 줍니다.

    왜 필요한가:
      Word 는 같은 서식이라도 글자 조각을 잘게 나눠 저장할 때가 많습니다.
      (맞춤법 검사 표시, 편집 이력 등이 원인입니다.)
      그대로 두면 '**1.** **목적** **(Objective)**' 처럼 지저분해지므로,
      '**1. 목적 (Objective)**' 로 합쳐 줍니다.

    입력:
      - text: 변환된 마크다운 한 줄
    출력:
      - 굵게/기울임이 정리된 문자열
    """
    # '**' 로 닫고 곧바로 '**' 로 다시 여는 경우 → 사이의 공백만 남기고 합칩니다.
    #
    # 기울임(*) 은 일부러 건드리지 않습니다.
    # 굵게 표시가 '**' 두 글자라서, 기울임용 규칙을 함께 쓰면 굵게의 여는 '**' 를
    # '빈 기울임 쌍' 으로 잘못 알아보고 지워 버리는 문제가 있었습니다.
    text = re.sub(r"\*\*(\s*)\*\*", r"\1", text)
    return text


def escape_markdown(text: str) -> str:
    """
    마크다운에서 특별한 뜻을 갖는 기호가 원문에 있을 때, 그대로 보이도록 처리합니다.

    입력:
      - text: 원문 글자
    출력:
      - 안전하게 처리된 글자
    """
    # 표 안에서 세로줄(|)은 칸 구분으로 오해되므로 반드시 막아 줍니다.
    return text.replace("|", "\\|")


def read_run_text(run, image_map: dict) -> str:
    """
    글자 조각(run) 하나를 읽어 마크다운 문자열로 돌려줍니다.

    'run' 은 Word 가 같은 서식이 이어지는 구간을 묶어 놓은 단위입니다.
    굵게/기울임 같은 서식이 여기에 붙어 있습니다.

    입력:
      - run: w:r XML 요소
      - image_map: 그림 관계ID -> 저장된 파일명 을 담은 사전
    출력:
      - 마크다운 문자열 (빈 문자열일 수 있음)
    """
    # 이 조각의 서식(굵게/기울임)을 먼저 확인합니다.
    run_properties = run.find(w("rPr"))
    is_bold = False
    is_italic = False
    if run_properties is not None:
        # <w:b/> 태그가 있으면 굵게. 단 val="0" 이면 해제된 것입니다.
        bold_tag = run_properties.find(w("b"))
        if bold_tag is not None and bold_tag.get(w("val")) not in ("0", "false"):
            is_bold = True
        italic_tag = run_properties.find(w("i"))
        if italic_tag is not None and italic_tag.get(w("val")) not in ("0", "false"):
            is_italic = True

    # 이 조각 안의 내용을 순서대로 모읍니다.
    collected = []
    for child in run:
        tag = child.tag

        if tag == w("t"):
            # 실제 글자입니다.
            collected.append(child.text or "")

        elif tag == w("tab"):
            collected.append("\t")

        elif tag == w("br"):
            # 줄바꿈. 마크다운에서 줄을 바꾸려면 공백 두 개 + 개행이 필요합니다.
            collected.append("  \n")

        elif tag == w("drawing"):
            # 그림입니다. 어떤 그림 파일인지 관계ID(r:embed)로 찾아냅니다.
            image_name = find_image_name(child, image_map)
            if image_name:
                collected.append("![[%s]]" % image_name)
            else:
                collected.append("[그림]")

        elif tag == w("object") or tag == w("pict"):
            collected.append("[도형]")

    text = "".join(collected)
    if not text.strip():
        # 내용이 공백뿐이면 서식을 붙이지 않고 그대로 돌려줍니다.
        return text

    # 서식 기호는 앞뒤 공백 바깥에 붙어야 마크다운이 제대로 렌더됩니다.
    leading_spaces = text[: len(text) - len(text.lstrip())]
    trailing_spaces = text[len(text.rstrip()) :]
    core = text.strip()

    if is_bold:
        core = "**%s**" % core
    if is_italic:
        core = "*%s*" % core

    return leading_spaces + core + trailing_spaces


def find_image_name(drawing_element, image_map: dict):
    """
    그림 태그에서 실제 저장된 이미지 파일명을 찾아 줍니다.

    입력:
      - drawing_element: w:drawing XML 요소
      - image_map: 관계ID -> 저장 파일명 사전
    출력:
      - 파일명 문자열, 못 찾으면 None
    """
    # a:blip 태그의 r:embed 속성이 그림의 관계ID 입니다.
    for blip in drawing_element.iter("{%s}blip" % NS["a"]):
        relation_id = blip.get("{%s}embed" % NS["r"])
        if relation_id and relation_id in image_map:
            return image_map[relation_id]
    return None


def read_paragraph_text(paragraph, image_map: dict) -> str:
    """
    문단 하나의 모든 글자를 이어 붙여 돌려줍니다. (하이퍼링크 포함)

    입력:
      - paragraph: w:p XML 요소
      - image_map: 그림 관계ID -> 파일명 사전
    출력:
      - 마크다운 문자열
    """
    pieces = []
    for child in paragraph:
        if child.tag == w("r"):
            pieces.append(read_run_text(child, image_map))
        elif child.tag == w("hyperlink"):
            # 링크 안에도 글자 조각들이 들어 있습니다.
            for run in child.findall(w("r")):
                pieces.append(read_run_text(run, image_map))

    # 조각들을 이어 붙인 뒤, 잘게 나뉜 굵게/기울임을 하나로 합칩니다.
    return merge_adjacent_emphasis("".join(pieces))


def convert_table(table_element, image_map: dict) -> list:
    """
    표 하나를 마크다운 표로 바꿔 줄 목록을 돌려줍니다.

    입력:
      - table_element: w:tbl XML 요소
      - image_map: 그림 관계ID -> 파일명 사전
    출력:
      - 문자열 리스트 (각 항목이 마크다운 한 줄)
    """
    rows = []
    for table_row in table_element.findall(w("tr")):
        cells = []
        for table_cell in table_row.findall(w("tc")):
            # 한 칸 안에 문단이 여러 개일 수 있으니 모두 이어 붙입니다.
            cell_paragraphs = []
            for paragraph in table_cell.findall(w("p")):
                text = read_paragraph_text(paragraph, image_map).strip()
                if text:
                    cell_paragraphs.append(text)
            # 칸 안의 줄바꿈은 <br> 로 바꿔야 표가 깨지지 않습니다.
            cell_text = "<br>".join(cell_paragraphs)
            cells.append(escape_markdown(cell_text))
        if cells:
            rows.append(cells)

    if not rows:
        return []

    # 칸 수가 행마다 다를 수 있으므로 가장 긴 행에 맞춥니다.
    column_count = max(len(row) for row in rows)
    for row in rows:
        while len(row) < column_count:
            row.append("")

    lines = []
    # 첫 줄을 머리행으로 씁니다.
    lines.append("| " + " | ".join(rows[0]) + " |")
    lines.append("|" + "---|" * column_count)
    for row in rows[1:]:
        lines.append("| " + " | ".join(row) + " |")
    return lines


def extract_images(docx_zip, media_dir: str, name_prefix: str) -> dict:
    """
    문서 안에 든 그림들을 지정한 폴더로 빼냅니다.

    입력:
      - docx_zip: 열려 있는 .docx ZipFile 객체
      - media_dir: 그림을 저장할 폴더 경로 (없으면 만듭니다)
      - name_prefix: 저장할 파일명 앞에 붙일 말 (다른 문서 그림과 안 섞이게)
    출력:
      - 관계ID -> 저장된 파일명 사전. 그림이 없으면 빈 사전.
    """
    # 1) 문서가 참조하는 그림의 "관계ID <-> 내부 경로" 대응표를 읽습니다.
    try:
        rels_xml = docx_zip.read("word/_rels/document.xml.rels")
    except KeyError:
        # 관계 파일이 없는 문서도 있습니다. 그림이 없다는 뜻이므로 그냥 넘어갑니다.
        return {}

    rels_root = parse_xml_safely(rels_xml, "word/_rels/document.xml.rels")
    relation_to_path = {}
    for relationship in rels_root:
        rel_type = relationship.get("Type", "")
        if rel_type.endswith("/image"):
            rel_id = relationship.get("Id")
            target = relationship.get("Target", "")
            # Target 은 'media/image1.png' 처럼 상대 경로로 적혀 있습니다.
            internal_path = "word/" + target.lstrip("/").replace("../", "")
            relation_to_path[rel_id] = internal_path

    if not relation_to_path:
        return {}

    # 2) 실제로 파일을 꺼내 저장합니다.
    os.makedirs(media_dir, exist_ok=True)
    image_map = {}
    for rel_id, internal_path in relation_to_path.items():
        try:
            image_bytes = docx_zip.read(internal_path)
        except KeyError:
            # 대응표에는 있는데 실제 파일이 없는 경우 — 건너뜁니다.
            print("[주의] 그림 파일을 찾지 못했습니다: %s" % internal_path)
            continue

        extension = os.path.splitext(internal_path)[1] or ".png"
        saved_name = "%s-%s%s" % (name_prefix, rel_id, extension)
        saved_path = os.path.join(media_dir, saved_name)
        with open(saved_path, "wb") as image_file:
            image_file.write(image_bytes)
        image_map[rel_id] = saved_name

    return image_map


def convert_docx_to_markdown(docx_path: str, media_dir: str, name_prefix: str) -> str:
    """
    .docx 파일 하나를 통째로 마크다운 문자열로 바꿔 줍니다.

    입력:
      - docx_path: 워드 파일 경로
      - media_dir: 그림을 빼낼 폴더 경로
      - name_prefix: 빼낸 그림 파일명 앞에 붙일 말
    출력:
      - 마크다운 전체 문자열
    """
    if not os.path.isfile(docx_path):
        raise FileNotFoundError(
            "워드 파일을 찾을 수 없습니다: %s\n"
            "경로를 다시 확인해 주세요. 공백이 있으면 따옴표로 감싸야 합니다." % docx_path
        )

    try:
        docx_zip = zipfile.ZipFile(docx_path)
    except zipfile.BadZipFile:
        raise ValueError(
            "이 파일은 올바른 .docx 가 아닙니다: %s\n"
            "혹시 옛날 .doc 형식이라면, Word 에서 열어 '다른 이름으로 저장 > .docx' 로 "
            "바꾼 뒤 다시 시도해 주세요." % docx_path
        )

    with docx_zip:
        if "word/document.xml" not in docx_zip.namelist():
            raise ValueError(
                "문서 본문(word/document.xml)이 들어 있지 않습니다: %s\n"
                "파일이 손상되었을 수 있습니다." % docx_path
            )

        # 1) 그림부터 빼냅니다. (본문에서 그림을 만나면 파일명을 바로 쓸 수 있게)
        image_map = extract_images(docx_zip, media_dir, name_prefix)

        # 2) 본문 XML 을 읽습니다.
        document_xml = docx_zip.read("word/document.xml")

    root = parse_xml_safely(document_xml, "word/document.xml")
    body = root.find(w("body"))
    if body is None:
        raise ValueError("문서 본문이 비어 있습니다: %s" % docx_path)

    output_lines = []

    # 본문의 자식들을 "나온 순서대로" 훑습니다. 순서를 지켜야 표와 글의 위치가 맞습니다.
    for element in body:

        if element.tag == w("p"):
            text = read_paragraph_text(element, image_map).rstrip()

            # 빈 문단은 문단 사이 간격으로만 씁니다. (빈 줄이 계속 쌓이지 않게)
            if not text.strip():
                if output_lines and output_lines[-1] != "":
                    output_lines.append("")
                continue

            heading_level = detect_heading_level(element)
            if heading_level > 0:
                output_lines.append("")
                output_lines.append("#" * heading_level + " " + text.strip())
                output_lines.append("")
                continue

            if is_list_paragraph(element):
                indent = get_list_indent(element)
                output_lines.append("\t" * indent + "- " + text.strip())
                continue

            output_lines.append(text.strip())
            output_lines.append("")

        elif element.tag == w("tbl"):
            table_lines = convert_table(element, image_map)
            if table_lines:
                output_lines.append("")
                output_lines.extend(table_lines)
                output_lines.append("")

    # 빈 줄이 3개 이상 이어지면 2개로 줄입니다. (읽기 좋게)
    markdown_text = "\n".join(output_lines)
    markdown_text = re.sub(r"\n{3,}", "\n\n", markdown_text)
    return markdown_text.strip() + "\n"


def main():
    """
    터미널에서 이 스크립트를 직접 실행했을 때 동작하는 부분입니다.
    """
    parser = argparse.ArgumentParser(
        description="Word(.docx) 파일을 마크다운(.md)으로 바꿉니다."
    )
    parser.add_argument("input", help="변환할 .docx 파일 경로")
    parser.add_argument(
        "-o", "--output",
        help="저장할 .md 경로 (생략하면 입력 파일과 같은 위치, 같은 이름)",
    )
    parser.add_argument(
        "--media-dir",
        default=None,
        help="문서 속 그림을 빼낼 폴더 (생략하면 출력 파일 옆의 attachments 폴더)",
    )
    parser.add_argument(
        "--media-prefix",
        default=None,
        help="빼낸 그림 파일명 앞에 붙일 말 (생략하면 입력 파일 이름)",
    )
    args = parser.parse_args()

    input_path = args.input

    # 출력 경로가 없으면 입력 파일 옆에 같은 이름으로 만듭니다.
    if args.output:
        output_path = args.output
    else:
        base_name = os.path.splitext(input_path)[0]
        output_path = base_name + ".md"

    # 그림 폴더가 없으면 출력 파일 옆의 attachments 폴더를 씁니다.
    if args.media_dir:
        media_dir = args.media_dir
    else:
        media_dir = os.path.join(os.path.dirname(os.path.abspath(output_path)), "attachments")

    # 그림 파일명 앞에 붙일 말이 없으면 입력 파일 이름을 씁니다.
    if args.media_prefix:
        name_prefix = args.media_prefix
    else:
        name_prefix = os.path.splitext(os.path.basename(input_path))[0]

    try:
        markdown_text = convert_docx_to_markdown(input_path, media_dir, name_prefix)
    except (FileNotFoundError, ValueError) as error:
        # 원인과 해결법을 한글로 알려주고, 조용히 실패하지 않게 종료 코드를 남깁니다.
        print("[실패] %s" % error)
        sys.exit(1)

    with open(output_path, "w", encoding="utf-8") as output_file:
        output_file.write(markdown_text)

    line_count = markdown_text.count("\n") + 1
    character_count = len(markdown_text)
    print("[OK] 변환을 마쳤습니다.")
    print("  입력 : %s" % input_path)
    print("  출력 : %s" % output_path)
    print("  분량 : %d 줄 / %d 글자" % (line_count, character_count))


if __name__ == "__main__":
    main()
