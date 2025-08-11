# Python Development Guidelines

## 1. Core Architecture Principles

### Hard Quality Indicators
- **File Size## 8. UI/UX Design Guidelines

### Visual Design Principles
- **Style**: Adopt minimalist or Material Design aesthetic
- **Color Scheme**: Use accessible color palettes (4.5:1 contrast ratio minimum)
- **Typography**: Sans-serif fonts (e.g., Roboto) with consistent hierarchy
- **Visual Elements**: Clean, professional layouts avoiding clutter

### Layout Structure
- **Information Hierarchy**: Prioritize primary actions and content
- **Grid System**: Maintain consistent spacing and alignment
- **Responsive Design**: Adapt layouts for different screen sizes
- **Navigation Flow**: Minimize steps between user goals

### User Experience
- **Accessibility**: Support screen readers and keyboard navigation
- **Interaction Feedback**: Provide loading states and error messages
- **Touch Support**: Ensure adequate button sizes (minimum 44px)
- **Microcopy**: Use clear, action-oriented button labels file under 800 lines
- **Directory Structure**: Limit files in each folder layer to no more than 12; organize into multi-layer subfolders if exceeding

### Elegant Architecture Design
Focus on these positive qualities to prevent code quality erosion:

1. **Flexibility**: Design systems that are easy to change without extensive chain reactions
2. **Uniqueness**: Ensure code logic appears in only one place (DRY principle)
3. **Acyclic Dependencies**: Structure modules to avoid circular dependencies
4. **Robustness**: Isolate changes to prevent unexpected breakage in unrelated areas
5. **Clarity**: Write code with clear intent and organized structure
6. **Cohesive Data Grouping**: Combine frequently used parameters into objects
7. **Appropriate Simplicity**: Solve problems with fitting solutions, avoid over-engineering

### Quality Assurance
- **Critical**: Always adhere to hard indicators and prioritize elegant architecture
- **Proactive**: Identify potential code quality issues and suggest optimizations immediately

## 2. Package Management with UV

Use `uv` CLI for all Python project management:
- **Scripts**: `uv run <script>`
- **Dependencies**: `uv add <package>` / `uv remove <package>`
- **Virtual Environments**: `uv venv` / `uv sync`
- **Building**: `uv build`
- **Backend**: Use `hatchling` as build backend

## 3. Python Coding Practices

### Code Organization
- **Architecture**: Follow Model-View-Presenter (MVP) pattern
- **Naming**: Adhere to PEP 8 conventions
- **Type Safety**: Use type hints consistently
- **Modularity**: Extract reusable operations into standalone modules

### Advanced Python Features
- **Standard Library**: Leverage `functools`, `collections`, `itertools`
- **Functional Programming**: Use iterators, generators, `reduce`, `map`, `filter`
- **Performance**: Cache expensive functions with `@functools.lru_cache`
- **Concurrency**: 
  - `asyncio` for I/O-bound operations
  - `threading` for network-bound or wait-heavy tasks
  - `multiprocessing` for CPU-intensive tasks

### Code Quality Standards
- **Function Size**: Refactor blocks exceeding 20 lines into separate functions
- **Naming**: Use action-driven verbs (e.g., `process_data`, `validate_input`)
- **Variables**: Meaningful, contextual names (up to five words)
- **Comments**: Outline code structure and major sections
- **Exception Handling**: Let errors propagate naturally unless explicitly specified

### MVP Architecture Implementation
- **Model**: SQLModel for database models, Pydantic for validation, SQLite3 backend
- **View**: FreeSimpleGUI for UI layouts with modular widgets
- **Presenter**: Event mapping with async functions, non-blocking operations


## 4. Testing and Quality Assurance

### Test-Driven Development
- **Framework**: Use `pytest` for all unit testing
- **Coverage**: Maintain at least 60% test coverage with `coverage.py`
- **Code Style**: Format with `ruff` or `black`
- **Test Enhancement**: Use pytest fixtures and parameterization
- **Mocking**: Use `pytest-mock` for dependency mocking

## 5. Preferred Libraries and Technologies

### Core Libraries
- **Logging**: `loguru` for structured logging
- **Data Validation**: `pydantic` for schema validation
- **Progress Tracking**: `tqdm` for progress bars
- **Retry Logic**: `tenacity` for robust error handling
- **CLI Interface**: `typer` for command-line applications

### Data and I/O
- **Large Files**: `memoryview`, `mmap` for efficient I/O
- **Datasets**: `pandas` or `polars` for data processing
- **HTTP Requests**: `httpx` with async client support
- **Configuration**: TOML for config file management
- **Database**: SQLite3 with SQLModel for ORM

### User Interface
- **GUI Framework**: FreeSimpleGUI for desktop applications
- **Layout**: Modular widget design with event mapping
- **Communication**: Global Queue for thread-safe messaging
- **Async Operations**: Non-blocking UI with progress feedback


## 6. Security and Internationalization

### Security Practices
- **Input Sanitization**: Use `bleach` for user input cleaning
- **Secret Management**: Use `python-dotenv` or `keyring` for credentials
- **API Validation**: Validate inputs with `pydantic` schemas
- **Password Security**: Hash passwords with `bcrypt` or `argon2`

### Unicode Support
- **Character Handling**: Ensure proper Unicode support for non-ASCII text
- **Text Normalization**: Use `ftfy` or `unidecode` for text cleaning
- **Testing**: Validate with multiple languages and character sets

## 7. Documentation and Collaboration

### Documentation Standards
- **API Documentation**: Generate with `Sphinx` or `MkDocs`
- **Docstring Style**: Use Google or NumPy docstring format
- **Version Control**: Maintain changelog for releases
- **Code Comments**: Document architecture decisions and complex logic

## UI/UX design
1. **整体风格与颜值**：
   - 选择一个主题风格：[STYLE_REFERENCE]（例如最小主义或Material Design）。
   - 推荐颜色方案：使用[COLOR_PALETTE]（例如蓝色调以传达信任），确保对比度至少4.5:1以符合可访问性。
   - 字体和图标：采用[FONT_FAMILY]（例如sans-serif字体如Roboto），图标风格为[ICON_STYLE]（例如线条图标），添加微妙阴影或渐变以提升视觉深度。
   - 视觉吸引力：融入[VISUAL_ELEMENTS]（例如背景渐变或英雄图像），确保整体干净、专业，避免 clutter。

2. **布局结构**：
   - 绘制线框描述：顶部[HEADER_ELEMENTS]（例如导航栏），中间[MAIN_CONTENT]（例如卡片式列表），底部[FOOTER_ELEMENTS]（例如按钮栏）。
   - 信息层次：优先显示[PRIMARY_INFO]（例如关键按钮），使用网格系统确保间距一致（至少[SPACING_PX] px）。
   - 响应式设计：描述如何适应[DEVICE_TYPES]（例如手机、平板和桌面），如在小屏上折叠菜单。
   - 导航流：确保用户从[START_POINT]到[END_POINT]只需[MIN_STEPS]步。

3. **易用性与交互**：
   - 用户流：创建persona如[USER_PERSONA]（例如忙碌上班族Emma），并设计交互以解决痛点[USER_PAIN_POINTS]（例如快速输入）。
   - 交互元素：按钮大小至少[BUTTON_SIZE] px，支持触摸；添加反馈如[FEEDBACK_TYPE]（例如加载动画或错误提示）。
   - 包容性：支持[ACCESSIBILITY_FEATURES]（例如屏幕阅读器兼容、键盘导航）。
   - Microcopy：为按钮和标签提供简洁文字，如[EXAMPLE_MICROCOPY]（例如“立即开始”而非“提交”）。