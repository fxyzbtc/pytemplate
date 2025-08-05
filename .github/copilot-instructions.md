# Python Development Guidelines

## 1. Python Project Structure
- Manage dependencies using `uv` CLI and `pyproject.toml`.
- Configure `pyproject.toml` with:
  - Entry points for `python -m`.
  - Scripts, homepage, and development dependencies.
  - Resources and data directories inclusion.
- Follow standard PyPI project layout:
  - Include `tests` and library name directories.
  - Avoid nested `src` directory.
- Write a `README.md` with:
  - Project purpose and pain points solved.
  - Installation instructions via `pip`.
  - Usage examples (module, `python -m`, or script).
  - Development guide.
  - Links to homepage, email, `https://deepwiki.com/githubusername/projectname`, and GitHub issues.

## 2. Python Coding Practices
- Adhere to PEP 8 naming conventions.
- Use type hints consistently for code clarity.
- Extract reusable operations into standalone modules.
- Organize code using the Model-View-Presenter (MVP) pattern.
- Leverage advanced Python features:
  - `functools`, `collections`, and `itertools`.
  - Functional programming: iterators, generators, `reduce`, `map`, `filter`, `sort` with key functions.
  - Self-inspection, `random`, context managers, and first-class functions.
- Use threading for network-bound or wait-heavy operations.
- Employ multiprocessing for CPU- or I/O-intensive tasks.
- Include clear comments to outline code structure and major sections.
- Use meaningful, contextual variable names (up to five words).
- Refactor code blocks exceeding 20 lines into separate functions.
- Name functions with action-driven verbs (e.g., `chunk_data`, `preview_file`, `cache_result`).

## 3. Preferred Python Libraries
- Logging: `loguru`.
- Data validation: `pydantic`.
- Progress bars: `tqdm`.
- Database operations: `sqlmodel`, `sqlite3`.
- Large file I/O: `memoryview`, `mmap`.
- Large datasets: `pandas` or `polars`.
- Retry logic: `tenacity`.
- HTTP requests: `httpx` (preferred over `requests`).
- Prefer popular, well-starred GitHub libraries unless they lack capability or reliability.

## 4. Testing and Quality Assurance
- Write unit tests using `pytest` with:
  - Fixtures and parameterization.
  - Debug logging with level enablement.
- Ensure at least 80% test coverage with `coverage.py`.
- Maintain code style with `ruff` or `black`.
- Cache expensive functions with `functools.lru_cache`.
- Implement asynchronous I/O with `asyncio`.

## 5. Documentation and Collaboration
- Generate API documentation using `Sphinx` or `MkDocs`.
- Write docstrings in Google or NumPy style.
- Maintain a changelog for versioned releases.

## 6. Security Practices
- Sanitize user inputs with `bleach` or similar libraries.
- Manage secrets using `python-dotenv` or `keyring`.
- Validate API inputs with `pydantic` schemas.
- Securely hash passwords with `bcrypt` or `argon2`.

## 7. Web Development
- Build full-stack applications with `Django`.
- Implement WebSocket functionality with `aiohttp` or `channels`.
- Use `Jinja2` or similar for templating.

## 8. always use `uv` CLI
- Use `uv` CLI for managing Python projects, including:
  - Running scripts with `uv run`.
  - Installing dependencies with `uv install`.
  - Managing virtual environments with `uv venv`. 

## 9. always consider the unicode support
- Ensure your code handles Unicode characters properly, especially for non-ASCII text.
- Use libraries like `ftfy` or `unidecode` to clean and normalize text.
- Test your application with a variety of languages and character sets.

## 10. other important guidelines
- Always write code with the following hard indicators in mind:
  (1) For dynamic languages like Python, JavaScript, TypeScript, ensure each code file stays under 500 lines as much as possible.
  (3) Limit files in each folder layer to no more than 8. If exceeding, organize into multi-layer subfolders.
- In addition to the hard indicators, always focus on elegant architecture design to promote the following positive qualities and prevent erosion of code quality:
  (1) Flexibility: Design the system to be easy to change, where small modifications do not trigger extensive chain reactions.
  (2) Uniqueness: Ensure code logic appears in only one place, making maintenance straightforward and consistent.
  (3) Acyclic Dependencies: Structure modules to avoid mutual entanglements, enabling easy decoupling, testing, and reuse.
  (4) Robustness: Make modifications in one area without unexpectedly breaking unrelated parts of the system.
  (5) Clarity: Write code with clear intent and organized structure, allowing readers to easily understand its function and design.
  (6) Cohesive Data Grouping: When multiple data items frequently appear together in method parameters, combine them into a single independent object.
  (7) Appropriate Simplicity: Solve problems with fitting solutions, avoiding over-design to keep the system lean and understandable.
- 【Very Important!!】 Whether you are writing code yourself or reading/reviewing others' code, strictly adhere to the above hard indicators and always prioritize elegant architecture design.
- 【Very Important!!】 At any time, if you identify potential issues that could erode code quality (such as deviations from the positive qualities listed), immediately ask the user if optimization is needed and provide reasonable optimization suggestions.

### testing 
1. use pytest and pytest-cov to write unit tests.
2. ensure at least 80% test coverage.
3. use pytest fixtures and parameterization to enhance test efficiency.
4. use pytest-mock for mocking dependencies in tests.