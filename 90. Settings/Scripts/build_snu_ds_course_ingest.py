"""Build progressive course-ingest manifests and Wiki navigation pages.

This script deliberately does not extract or rewrite the original course files.
It inventories the immutable mixed-format corpus and creates course-level
scaffolds that can be promoted lecture by lecture later.
"""

from __future__ import annotations

import os
import subprocess
from collections import Counter, defaultdict
from pathlib import Path


ROOT = Path(__file__).resolve().parents[2]
CORPUS = ROOT / "10. Raw Sources" / "17.seoul_univ_ds"
RAW_OUT = ROOT / "10. Raw Sources" / "13. Books"
GUIDE_OUT = ROOT / "20. Wiki" / "23. Guides"
MAP_OUT = ROOT / "20. Wiki" / "24. Maps"
DATE = "2026-07-31"
PURPOSE = "수업 · 코스워크 — 서울대학교 데이터사이언스 강의자료를 과목별 학습·복습 자산으로 컴파일"


COURSES = [
    {
        "root_prefix": "Advanced techniques in LLMs & Retrieval-Augmented Generation_",
        "slug": "advanced-llms-rag",
        "title": "서울대 데이터사이언스 - 고급 LLM 및 RAG",
        "course": "Advanced Techniques in LLMs & Retrieval-Augmented Generation",
        "instructor": "서봉원",
        "description": "A progressive course guide to advanced LLM application development, embeddings, retrieval-augmented generation, LangChain, LangGraph, prompt engineering, and agent engineering.",
        "topics": [
            "LLM 응용 개론과 생성형 AI 동향",
            "텍스트 임베딩과 벡터 데이터베이스",
            "Basic RAG와 Advanced RAG",
            "LangChain과 LangGraph",
            "프롬프트 엔지니어링",
            "Agent Engineering과 실습",
        ],
    },
    {
        "root_prefix": "Computer Vision_",
        "slug": "computer-vision",
        "title": "서울대 데이터사이언스 - 컴퓨터 비전",
        "course": "Computer Vision",
        "instructor": "주한별",
        "description": "A progressive course guide covering classical computer vision, multiview geometry, deep convolutional networks, detection, pose estimation, and generative models.",
        "topics": [
            "필터, 엣지, HOG, SIFT, Bag of Words",
            "Hough transform, PCA, tracking, segmentation",
            "Homography, camera model, calibration, triangulation",
            "Structure from Motion과 Bundle Adjustment",
            "딥러닝·CNN 구조와 전이학습",
            "객체 탐지, 2D·3D 자세 추정, VAE",
        ],
    },
    {
        "root_prefix": "Creating Images using Generative AI Methods_",
        "slug": "generative-image-methods",
        "title": "서울대 데이터사이언스 - 생성형 AI 이미지 방법론",
        "course": "Creating Images using Generative AI Methods",
        "instructor": "박재식",
        "description": "A progressive course guide to latent-variable models, score-based modeling, diffusion, flow matching, autoregressive generation, and evaluation of image generators.",
        "topics": [
            "잠재변수 모델과 VAE",
            "Score Matching과 Diffusion Models",
            "DDPM 실습과 classifier-free guidance",
            "Flow Matching과 Gaussianization Flow",
            "Autoregressive 생성 모델",
            "FID 평가와 실시간 비디오 생성",
        ],
    },
    {
        "root_prefix": "Data Mining_",
        "slug": "data-mining",
        "title": "서울대 데이터사이언스 - 데이터 마이닝",
        "course": "Data Mining",
        "instructor": "김용대",
        "description": "A progressive course guide to probability, statistical inference, regression, clustering, dimensionality reduction, missing data, association analysis, and recommendation.",
        "topics": [
            "확률·분포와 통계적 추론",
            "상관관계, 선형회귀, 로지스틱 회귀",
            "벌점화 선형모형과 앙상블",
            "군집분석과 차원축소",
            "결측치 처리와 연관성 분석",
            "추천 알고리즘, 전이학습, 지식 증류",
        ],
    },
    {
        "root_prefix": "Data Structures & Algorithms_",
        "slug": "data-structures-algorithms",
        "title": "서울대 데이터사이언스 - 자료구조와 알고리즘",
        "course": "Data Structures & Algorithms",
        "instructor": "문병로",
        "description": "A progressive course guide to core data structures, sorting, dynamic programming, graphs, shortest paths, search, and computational limits.",
        "topics": [
            "리스트, 스택, 큐, 힙",
            "해시 테이블, 연결 리스트, 이진 탐색 트리",
            "정렬 알고리즘과 비교 실습",
            "동적 계획법",
            "그래프와 Dijkstra 최단경로",
            "A* 탐색과 계산의 한계",
        ],
    },
    {
        "root_prefix": "Reinforcement Learning_",
        "slug": "reinforcement-learning",
        "title": "서울대 데이터사이언스 - 강화학습",
        "course": "Reinforcement Learning",
        "instructor": "원정담",
        "description": "A progressive course guide to Markov decision processes, dynamic programming, model-free learning, function approximation, policy gradients, and deep reinforcement learning.",
        "topics": [
            "강화학습 개론과 MDP",
            "Dynamic Programming",
            "Monte Carlo와 Temporal-Difference 학습",
            "제어와 함수 근사",
            "Dyna와 Policy Gradient",
            "REINFORCE, DQN, Deep RL 실습",
        ],
    },
    {
        "root_prefix": "선형대수,Optimization_",
        "slug": "linear-algebra-optimization",
        "title": "서울대 데이터사이언스 - 선형대수와 최적화",
        "course": "Linear Algebra & Optimization",
        "instructor": "이재욱",
        "description": "A progressive course guide to mathematical foundations for machine learning, with linked lecture, exercise, annotation, and assignment materials in linear algebra and optimization.",
        "topics": [
            "머신러닝을 위한 선형대수",
            "벡터·행렬 기반 수학 기초",
            "최적화 기본 문제와 해법",
            "조교 실습과 풀이 자료",
            "필기·보충 자료의 병렬 비교",
            "최적화 과제 1·2",
        ],
    },
    {
        "root_prefix": "특강-",
        "slug": "special-lectures",
        "title": "서울대 데이터사이언스 - 특강 모음",
        "course": "Special Lectures",
        "instructor": "복수 강연자",
        "description": "A progressive guide to special-topic lectures spanning anomaly detection, cryptography, blockchain, quantum computing, database systems, and abstract reasoning.",
        "topics": [
            "표형·시계열 이상탐지",
            "암호학 기초와 고급 암호",
            "Bitcoin, Ethereum, Blockchain 응용",
            "양자 컴퓨팅 개요",
            "비정형 DB, 데이터 포맷, HTAP",
            "은유와 추상적 사고",
        ],
    },
    {
        "root_prefix": "파이썬,Data Visualization_",
        "slug": "python-data-visualization",
        "title": "서울대 데이터사이언스 - 파이썬과 데이터 시각화",
        "course": "Python & Data Visualization",
        "instructor": "서진욱",
        "description": "A progressive course guide to Python fundamentals, object-oriented programming, NumPy, pandas, Matplotlib, Altair, Spotfire, and information visualization.",
        "topics": [
            "Python 입출력, 조건, 반복, 함수",
            "구조화 자료형과 재귀",
            "객체지향 프로그래밍과 상속",
            "NumPy 벡터·행렬 연산",
            "pandas와 Matplotlib 실습",
            "Altair, Spotfire, 정보시각화",
        ],
    },
]


def yaml_quote(value: str) -> str:
    return '"' + value.replace("\\", "\\\\").replace('"', '\\"') + '"'


def md_safe(value: str) -> str:
    return value.replace("`", "ˋ")


def extended_path(path: Path) -> str:
    absolute = os.path.abspath(path)
    if os.name == "nt" and not absolute.startswith("\\\\?\\"):
        return "\\\\?\\" + absolute
    return absolute


def collect_paths() -> dict[str, list[Path]]:
    result = subprocess.run(
        ["rg", "--files", "-uu", "--", str(CORPUS)],
        cwd=ROOT,
        check=True,
        capture_output=True,
        text=True,
        encoding="utf-8",
    )
    grouped: dict[str, list[Path]] = defaultdict(list)
    for line in result.stdout.splitlines():
        path = Path(line)
        relative = path.relative_to(CORPUS)
        grouped[relative.parts[0]].append(relative)
    return grouped


def match_course_root(grouped: dict[str, list[Path]], prefix: str) -> str:
    matches = [name for name in grouped if name.startswith(prefix)]
    if len(matches) != 1:
        raise RuntimeError(f"Expected one course root for {prefix!r}, got {matches}")
    return matches[0]


def file_size(relative: Path) -> int | None:
    try:
        return os.stat(extended_path(CORPUS / relative)).st_size
    except OSError:
        return None


def format_bytes(value: int) -> str:
    units = ["B", "KiB", "MiB", "GiB"]
    amount = float(value)
    for unit in units:
        if amount < 1024 or unit == units[-1]:
            return f"{amount:.1f} {unit}" if unit != "B" else f"{int(amount)} B"
        amount /= 1024
    return f"{value} B"


def raw_manifest(spec: dict[str, object], course_root: str, files: list[Path]) -> str:
    extension_counts = Counter((path.suffix.lower() or "[no extension]") for path in files)
    basename_groups: dict[str, list[Path]] = defaultdict(list)
    for path in files:
        basename_groups[path.name.casefold()].append(path)
    duplicates = [items for items in basename_groups.values() if len(items) > 1]

    sizes = [(path, file_size(path)) for path in files]
    known_total = sum(size for _, size in sizes if size is not None)
    unreadable = [path for path, size in sizes if size is None]
    empty = [path for path, size in sizes if size == 0]
    binary_only = [
        path
        for path in files
        if path.suffix.lower() in {".zip", ".npz", ".key", ".ppt"}
    ]

    lines = [
        "---",
        "type: raw-source",
        "aliases:",
        f"  - {yaml_quote(str(spec['course']) + ' Course Index')}",
        f"  - {yaml_quote(str(spec['title']))}",
        f"description: {yaml_quote('A progressive source index for the ' + str(spec['course']) + ' course corpus. It preserves the original mixed-format files in place and records an auditable inventory for lecture-by-lecture promotion.')}",
        "author:",
        "  - Codex",
        "model: gpt-5.5",
        "effort: high",
        f"date created: {DATE}",
        f"date modified: {DATE}",
        f"date ingested: {DATE}",
        "tags:",
        "  - raw-source",
        "  - course-materials",
        "  - snu-data-science",
        "  - progressive-ingest",
        f"source: {yaml_quote('10. Raw Sources/17.seoul_univ_ds/' + course_root)}",
        "category: Books",
        "status: stub",
        f"collectionPurpose: {yaml_quote(PURPOSE)}",
        f"course: {yaml_quote(str(spec['course']))}",
        f"instructor: {yaml_quote(str(spec['instructor']))}",
        f"fileCount: {len(files)}",
        'sourceFormat: "mixed"',
        'conversionFidelity: "inventory-only"',
        "---",
        "",
        f"# {spec['title']} — Course Source Index",
        "",
        "> [!info] Progressive ingest",
        f">\t원본 {len(files)}개는 `{md_safe('10. Raw Sources/17.seoul_univ_ds/' + course_root)}`에 그대로 보존한다. 이 인덱스는 파일을 재작성하지 않고 구조와 범위만 등록한 `status: stub` 스캐폴드다.",
        "",
        "## Collection Purpose",
        "",
        f"\t- {PURPOSE}",
        "",
        "## Original Content",
        "",
        f"\t- 원본 위치: `{md_safe('10. Raw Sources/17.seoul_univ_ds/' + course_root)}`",
        f"\t- 파일 수: {len(files)}",
        f"\t- 확인된 전체 크기: {format_bytes(known_total)}",
        "\t- 원본 형식은 PDF, notebook, slide, code, data, archive를 포함하며 이 단계에서는 내용 추출을 수행하지 않았다.",
        "",
        "## Format Inventory",
        "",
    ]
    for extension, count in sorted(extension_counts.items()):
        lines.append(f"\t- `{extension}`: {count}")

    lines.extend(["", "## Review Flags", ""])
    if duplicates:
        lines.append("\t- 같은 과목 안에서 파일명이 중복되는 후보:")
        for items in duplicates:
            joined = " / ".join(md_safe(path.as_posix()) for path in items)
            lines.append(f"\t\t- `{joined}`")
    else:
        lines.append("\t- 같은 과목 안의 중복 파일명 후보 없음.")
    if binary_only:
        lines.append(
            f"\t- 텍스트 자동 추출 대상에서 제외한 바이너리·압축 파일: {len(binary_only)}개 (`.zip`, `.npz`, `.key`, `.ppt`)."
        )
    if empty:
        lines.append(f"\t- 0바이트 파일: {len(empty)}개.")
        for path in empty:
            lines.append(f"\t\t- `{md_safe(path.as_posix())}`")
    if unreadable:
        lines.append(f"\t- 크기 메타데이터를 읽지 못한 장기 경로 파일: {len(unreadable)}개.")
    if not binary_only and not empty and not unreadable:
        lines.append("\t- 크기 확인 단계에서 추가 오류 없음.")

    lines.extend(["", "## File Inventory", ""])
    for path, size in sorted(sizes, key=lambda item: item[0].as_posix().casefold()):
        size_label = format_bytes(size) if size is not None else "size unavailable"
        lines.append(f"\t- `{md_safe(path.as_posix())}` — {size_label}")

    lines.extend(
        [
            "",
            "## Promotion Rule",
            "",
            "\t- 실제로 읽거나 과제에 사용하는 강의 파일만 후속 `/ingest` 대상으로 지정한다.",
            "\t- 승격 시 해당 파일의 텍스트·코드·표를 추출하고 `conversionFidelity`를 다시 기록한다.",
            "\t- 현재 인덱스의 목록은 원본 위치와 파일명을 확인하기 위한 감사 가능한 스냅샷으로 유지한다.",
            "",
            "## Related",
            "",
            f"\t- [[{spec['title']}]]",
            "\t- [[MOC-서울대학교 데이터사이언스 코스워크]]",
            "",
        ]
    )
    return "\n".join(lines)


def guide_page(spec: dict[str, object], raw_name: str, file_count: int) -> str:
    topics = "\n".join(f"\t- {topic}" for topic in spec["topics"])
    return "\n".join(
        [
            "---",
            "type: wiki-page",
            "aliases:",
            f"  - {yaml_quote(str(spec['course']))}",
            f"  - {yaml_quote(str(spec['course']) + ' Coursework')}",
            f"description: {yaml_quote(str(spec['description']))}",
            "author:",
            "  - Codex",
            "model: gpt-5.5",
            "effort: high",
            f"date created: {DATE}",
            f"date modified: {DATE}",
            "tags:",
            "  - guide",
            "  - course",
            "  - snu-data-science",
            "  - coursework",
            "source:",
            f'  - "[[{raw_name}]]"',
            "related:",
            '  - "[[MOC-서울대학교 데이터사이언스 코스워크]]"',
            "confidence: medium",
            "layer: guides",
            "explored: false",
            "claimType: mixed",
            "evidenceScope: single-source",
            "verificationStatus: unverified",
            "disputed: false",
            "---",
            "",
            f"# {spec['title']}",
            "",
            f"{spec['instructor']} 교수(또는 담당 강연자)의 `{spec['course']}` 강의자료를 수업·코스워크 관점에서 탐색하기 위한 페이지다. 현재는 파일명과 폴더 구조를 기반으로 만든 스캐폴드이며, 강의 본문을 완전히 읽거나 검증한 상태는 아니다.",
            "",
            "## Learning Spine",
            "",
            topics,
            "",
            "## Materials Snapshot",
            "",
            f"\t- 등록 파일: {file_count}개",
            f"\t- 원본 인덱스: [[{raw_name}]]",
            "\t- 상태: 점진형 인제스트 스캐폴드",
            "\t- 본문 추출: 미수행",
            "",
            "## Coursework Use",
            "",
            "\t- 강의 순서를 복원하고 주차별 복습 대상을 고른다.",
            "\t- 과제·실습 파일은 대응 강의자료와 함께 묶어 읽는다.",
            "\t- 실제로 읽은 자료만 별도 승격하여 개념·방법 페이지로 컴파일한다.",
            "",
            "## Evidence Boundary",
            "",
            "> [!warning] Unverified scaffold",
            ">\t이 페이지의 범위는 파일명과 디렉터리 구조에서 확인되는 주제에 한정된다. 세부 주장, 수식, 실험 결과, 강의자의 관점은 개별 파일 승격 전까지 인용하지 않는다.",
            "",
            "## Related",
            "",
            "\t- [[MOC-서울대학교 데이터사이언스 코스워크]]",
            f"\t- [[{raw_name}]]",
            "",
        ]
    )


def moc_page(specs_with_raw: list[tuple[dict[str, object], str, int]]) -> str:
    course_links = "\n".join(
        f"\t- [[{spec['title']}]] — {spec['instructor']} · {count}개 파일"
        for spec, _, count in specs_with_raw
    )
    sources = "\n".join(f'  - "[[{raw_name}]]"' for _, raw_name, _ in specs_with_raw)
    return "\n".join(
        [
            "---",
            "type: moc",
            "aliases:",
            '  - "SNU Data Science Coursework"',
            '  - "서울대 DS 코스워크"',
            'description: "A map of content for nine Seoul National University data science course-material clusters, organized for progressive study and lecture-by-lecture promotion."',
            "author:",
            "  - Codex",
            "model: gpt-5.5",
            "effort: high",
            f"date created: {DATE}",
            f"date modified: {DATE}",
            "tags:",
            "  - moc",
            "  - snu-data-science",
            "  - coursework",
            "  - progressive-ingest",
            "topic: 서울대학교 데이터사이언스 코스워크",
            "source:",
            sources,
            "related:",
            '  - "[[MOC-LLM Wiki Guide]]"',
            "---",
            "",
            "# MOC — 서울대학교 데이터사이언스 코스워크",
            "",
            "서울대학교 데이터사이언스 과정의 9개 강의자료 묶음을 수업·코스워크용으로 탐색하는 지도다. 전체 원본은 불변 상태로 보존하고, 실제 학습 대상만 강의 파일 단위로 승격한다.",
            "",
            "## Course Map",
            "",
            course_links,
            "",
            "## Suggested Study Paths",
            "",
            "### 기초 경로",
            "",
            "\t- [[서울대 데이터사이언스 - 파이썬과 데이터 시각화]]",
            "\t- [[서울대 데이터사이언스 - 선형대수와 최적화]]",
            "\t- [[서울대 데이터사이언스 - 자료구조와 알고리즘]]",
            "",
            "### 모델링 경로",
            "",
            "\t- [[서울대 데이터사이언스 - 데이터 마이닝]]",
            "\t- [[서울대 데이터사이언스 - 컴퓨터 비전]]",
            "\t- [[서울대 데이터사이언스 - 강화학습]]",
            "",
            "### 생성형 AI 경로",
            "",
            "\t- [[서울대 데이터사이언스 - 생성형 AI 이미지 방법론]]",
            "\t- [[서울대 데이터사이언스 - 고급 LLM 및 RAG]]",
            "\t- [[서울대 데이터사이언스 - 특강 모음]]",
            "",
            "## Ingest Boundary",
            "",
            "\t- 현재 완료: 원본 위치 보존, 전 파일 인벤토리, 과목별 주제 지도.",
            "\t- 현재 제외: PDF·PPTX·IPYNB의 전면 텍스트 추출, 강의 내용 요약, 세부 개념 페이지 양산.",
            "\t- 후속 승격: 실제 수강·복습 순서에 맞춰 개별 파일을 선택해 `/ingest`.",
            "",
        ]
    )


def main() -> None:
    grouped = collect_paths()
    RAW_OUT.mkdir(parents=True, exist_ok=True)
    GUIDE_OUT.mkdir(parents=True, exist_ok=True)
    MAP_OUT.mkdir(parents=True, exist_ok=True)

    specs_with_raw: list[tuple[dict[str, object], str, int]] = []
    total_files = 0
    for spec in COURSES:
        course_root = match_course_root(grouped, str(spec["root_prefix"]))
        files = grouped[course_root]
        total_files += len(files)
        raw_name = f"{DATE}-snu-ds-{spec['slug']}-course-index"
        raw_path = RAW_OUT / f"{raw_name}.md"
        guide_path = GUIDE_OUT / f"{spec['title']}.md"
        raw_path.write_text(raw_manifest(spec, course_root, files), encoding="utf-8")
        guide_path.write_text(guide_page(spec, raw_name, len(files)), encoding="utf-8")
        specs_with_raw.append((spec, raw_name, len(files)))

    if total_files != 306:
        raise RuntimeError(f"Expected 306 source files, inventoried {total_files}")

    moc_path = MAP_OUT / "MOC-서울대학교 데이터사이언스 코스워크.md"
    moc_path.write_text(moc_page(specs_with_raw), encoding="utf-8")

    print(f"courses={len(specs_with_raw)}")
    print(f"source_files={total_files}")
    print(f"raw_manifests={len(specs_with_raw)}")
    print(f"wiki_guides={len(specs_with_raw)}")
    print("mocs=1")


if __name__ == "__main__":
    main()
