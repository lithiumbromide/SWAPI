# SOLIDWORKS API Knowledge Base for Codex and Claude

Language: [English](README.md) | Русский

Проект превращает официальную документацию SOLIDWORKS API из `.chm` в локальную базу Markdown-документов, компактный индекс и Agent Skills, чтобы Codex, Claude Code и claude.ai помогали писать VBA-макросы, C# add-in приложения и инструменты для PDM Professional, не загружая в контекст десятки тысяч файлов документации.

Этот публичный репозиторий содержит скрипты пайплайна, корпус `markdown/` и индекс `llm_index/`, сгенерированные из справки SOLIDWORKS API 2026, и навыки (skills) в `.claude/skills/`. В корпусе 56 129 документов в 49 модулях (см. [llm_index/manifest.json](llm_index/manifest.json)); в 2026 добавились модули `swvisualizeapi` и `swvisualizeapiVB6`, а `API_GB` — вторая сборка справки SOLIDWORKS PDM Professional API. Оригинальные `.chm` файлы и промежуточные HTML-файлы не публикуются.

Код проекта распространяется под MIT License и может использоваться в коммерческих проектах. Сгенерированный Markdown и данные навыков могут содержать материалы, производные от официальной документации SOLIDWORKS API; см. [NOTICE.md](NOTICE.md).

## Структура проекта

```text
.
├── .claude/skills/       # Agent Skills, см. ниже
├── api/                  # исходные .chm файлы одной версии SOLIDWORKS API, не коммитятся
├── extracted/            # полная распаковка CHM, генерируется, не коммитится
├── API_HTML/             # только .htm/.html из extracted/, генерируется, не коммитится
├── markdown/             # Markdown-документация, один файл на один логический API-объект, генерируется
├── llm_index/            # компактные индексы и граф связей поверх markdown/, генерируется
├── dist/                 # zip-архивы навыков от package_skills.py, игнорируется Git
├── scripts/              # описаны в scripts/README.md
│   ├── unpack_chm_recursive.sh
│   ├── unpack_chm_recursive.ps1
│   ├── run_pipeline.ps1
│   ├── pipeline_common.py
│   ├── collect_html.py
│   ├── convert_sw_api_docs.py
│   ├── build_llm_index.py
│   ├── build_skill_data.py
│   ├── compare_index.py
│   ├── package_skills.py
│   ├── skill_data.json   # распределение модулей, бюджеты и правила упаковки по навыкам
│   └── skill_runtime/    # канонический swapi.py с LICENSE.txt и NOTICE.md, которые копируются в навыки
├── AGENTS.md             # общие инструкции для Codex и Claude Code
├── CLAUDE.md             # импортирует AGENTS.md и добавляет заметки для Claude Code
├── NOTICE.md
├── LICENSE
├── requirements.txt
├── README.md
└── README.ru.md
```

## Зависимости

Скриптам пайплайна нужен Python 3.10+ и пакеты из `requirements.txt`; скрипты навыков и `swapi.py` используют только стандартную библиотеку. Команды в этом README используют `python3`; в Windows вместо него используйте `.venv\Scripts\python.exe`.

### Linux

```bash
python3 -m pip install -r requirements.txt
```

Для распаковки CHM нужен `extract_chmLib` из `chmlib`:

| Дистрибутив | Команда |
| --- | --- |
| Debian/Ubuntu | `sudo apt install libchm-bin` |
| Fedora | `sudo dnf install chmlib` |
| Arch Linux | `sudo pacman -S chmlib` |

Проверка: `which extract_chmLib`. Если пакет в вашем дистрибутиве не содержит `extract_chmLib`, установите `chmlib` из исходников или используйте любой совместимый CHM extractor, который умеет команду вида `extract_chmLib input.chm output_directory`.

### Windows (7-Zip + venv)

Установите [7-Zip](https://www.7-zip.org/), чтобы `7z.exe` был в `PATH` или в `C:\Program Files\7-Zip`, затем создайте venv проекта из корня репозитория:

```powershell
py -3 -m venv .venv
.venv\Scripts\python.exe -m pip install -r requirements.txt
```

`scripts/run_pipeline.ps1` делает это сам, если venv или пакетов нет.

## Полный пайплайн

Выполняйте все шаги из корня репозитория. Параметры и защитные проверки каждого скрипта описаны в [scripts/README.md](scripts/README.md).

### 1. Положить CHM

Сложите `.chm` файлы нужной версии SOLIDWORKS API в `api/`, например:

```text
api/sldworksapi.chm
api/sldworksapivb6.chm
api/swconst.chm
api/cworksapi.chm
```

### 2. Распаковать CHM рекурсивно

```bash
./scripts/unpack_chm_recursive.sh api extracted
```

В Windows запустите `.\scripts\unpack_chm_recursive.ps1 -InputDir api -OutputDir extracted`. Оба распаковщика распаковывают и `.chm`, вложенные в уже распакованные CHM.

### 3. Собрать только HTML

```bash
python3 scripts/collect_html.py extracted -o API_HTML --clean
```

Этот шаг удаляет картинки, CSS, JS и другие не-HTML файлы, сохраняя структуру каталогов.

### 4. Конвертировать HTML в Markdown

```bash
python3 scripts/convert_sw_api_docs.py API_HTML -o markdown --clean
```

Конвертер специализирован под формат SOLIDWORKS/Innovasys help:

- удаляет служебную навигацию;
- сохраняет заголовки, секции, таблицы, списки;
- превращает блоки Syntax в fenced code blocks;
- добавляет YAML-метаданные;
- сохраняет связи через Markdown-ссылки.

### 5. Построить индекс для LLM

```bash
python3 scripts/build_llm_index.py markdown -o llm_index --api-version 2026
```

Индекс нужен не для RAG, а для дешёвой навигации:

- сначала найти символ;
- затем найти интерфейс/соседей;
- затем открыть только нужные Markdown-файлы.

### Запуск одной командой в Windows

После шага 1 выполните шаги 2-5 одной командой; при переходе на новую версию API добавьте `-CleanExtract`. `-Force` и остальные параметры описаны в [scripts/README.md](scripts/README.md#run_pipelineps1).

```powershell
.\scripts\run_pipeline.ps1 -ApiVersion 2026
```

## Быстрая проверка

```bash
find markdown -type f -name '*.md' | wc -l
grep -E '"(api_version|document_count|module_count)"' llm_index/manifest.json
python3 scripts/compare_index.py <previous llm_index> llm_index
```

Число файлов должно совпадать с `document_count`; `compare_index.py` печатает изменения по модулям относительно предыдущей сборки.

## Agent Skills

`.claude/skills/` содержит три навыка:

| Навык | Назначение | Zip-архив |
| --- | --- | --- |
| `solidworks-api` | Поиск по API настольного SOLIDWORKS (включая Document Manager, Simulation и API дополнений) и VBA-макросы, C#/VB.NET add-in, отдельные приложения и инструменты Document Manager на его основе | да |
| `solidworks-pdm-api` | Поиск по API SOLIDWORKS PDM Professional (включая PDM Web API и устаревший Workgroup PDM API) и add-in хранилища, task add-in, отдельные инструменты для хранилища и клиенты Web API | да |
| `swapi-corpus-maintainer` | Перегенерация корпуса, индекса, данных навыков и zip-архивов этого репозитория | нет, работает только внутри этого репозитория |

Каждый навык с zip-архивом содержит компактный индекс справки 2026 в `data/` и `scripts/swapi.py` — CLI, который за несколько строк отвечает на запросы по сигнатурам, перечислениям, типам выбора, документам и примерам и проверяет код на устаревшие или неверно написанные члены.

### Claude Code

Claude Code находит навыки, когда этот репозиторий открыт как проект или добавлен в сессию другого проекта через `claude --add-dir <путь к этому репозиторию>`. Навык загружается, когда запрос подходит под его описание, например «Напиши VBA-макрос, который экспортирует все конфигурации активной детали в STEP» или «Добавь PreState hook в мой PDM add-in».

### claude.ai

Соберите zip-архивы, как описано в разделе [Проверка и упаковка](#проверка-и-упаковка), затем в claude.ai откройте Customize > Skills и загрузите `dist/solidworks-api.zip` или `dist/solidworks-pdm-api.zip` без изменений. В корне каждого архива лежит папка навыка.

### Режимы работы swapi.py

`swapi.py` отвечает на любой запрос из встроенного `data/` и никогда не устанавливает пакеты, поэтому оба навыка полностью работают без сети. Загружаются только полные документы и примеры, которых нет во встроенных данных, в таком порядке: из локальной копии этого репозитория, через `git show` в этой копии, если файла нет в рабочем дереве, и из raw-файлов GitHub по ref, записанному в `data/manifest.json` (таймаут 6 секунд, с кешем, отключается через `SWAPI_OFFLINE=1`); если ни один источник не ответил, печатается встроенная краткая запись с пометкой об этом. `swapi.py where` показывает режим: `local`, `git`, `remote` или `bundled`; переменные окружения перечислены в [scripts/README.md](scripts/README.md#skill_runtime).

### Генерируемые и рукописные файлы

| Файлы | Происхождение |
| --- | --- |
| `SKILL.md`, `references/`, `assets/` и `evals/` в каждом навыке | пишутся вручную |
| `scripts/skill_runtime/` и `scripts/skill_data.json` | пишутся вручную, единственный источник |
| `data/`, `scripts/swapi.py`, `LICENSE.txt` и `NOTICE.md` в каждом навыке с zip-архивом | генерируются `scripts/build_skill_data.py` и коммитятся, чтобы навыки работали офлайн из клона |

Редактируйте только рукописные файлы, остальное генерируйте заново.

### Проверка и упаковка

```bash
python3 scripts/package_skills.py --validate-only
claude plugin validate .claude/skills
python3 scripts/package_skills.py
```

Первая команда выполняет проверки проекта, перечисленные в [scripts/README.md](scripts/README.md#package_skillspy), вторая — собственный валидатор Claude Code, третья снова всё проверяет и записывает воспроизводимые zip-архивы и `SHA256SUMS` в `dist/`.

### После обновления корпуса

Выполните [полный пайплайн](#полный-пайплайн), затем перегенерируйте данные навыков и упакуйте их:

```bash
python3 scripts/build_skill_data.py --previous <previous .claude/skills>
python3 scripts/package_skills.py --validate-only
python3 scripts/package_skills.py
```

`<previous .claude/skills>` — копия навыков до обновления, например извлечённая из `git archive HEAD .claude/skills`; по ней `--previous` записывает `data/changes.tsv` с членами, которые с тех пор добавлены, устарели, удалены или изменены. Навык `swapi-corpus-maintainer` следует тому же порядку и дополнительно покрывает evals и релизы.

## Как подключать к Codex и Claude Code

Откройте этот репозиторий как workspace или добавьте его рядом с вашим VBA/C# проектом: второй папкой в multi-root workspace VS Code/VSCodium или через `claude --add-dir`. Codex следует [AGENTS.md](AGENTS.md); Claude Code читает [CLAUDE.md](CLAUDE.md), который импортирует `AGENTS.md`, и использует навыки.

Пример запроса:

```text
Use the SOLIDWORKS API knowledge base in this workspace.
Follow AGENTS.md.
I am writing a VBA macro. Find the correct API docs before writing code.
```

Для C# add-in:

```text
Follow AGENTS.md.
I am writing a C# SOLIDWORKS add-in.
Prefer .NET API docs and C# syntax blocks.
```

## Как пользоваться индексом вручную

Команды поиска приведены в [AGENTS.md](AGENTS.md#fast-commands), а файлы индекса описаны в [llm_index/README.md](llm_index/README.md).

## Рекомендации для GitHub

Коммитьте скрипты, документацию, `markdown/`, `llm_index/` и `.claude/skills/` вместе со сгенерированными данными. Держите `api/`, `extracted/`, `API_HTML/` и `dist/` вне Git, потому что они большие, воспроизводимые или получены из лицензионных CHM-файлов. Если не хотите хранить сгенерированные данные в Git-истории, публикуйте `markdown/` и `llm_index/` как release artifacts; zip-архивы навыков всегда публикуются в релизах, а не в Git.
