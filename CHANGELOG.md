# Changelog

All notable changes to DraftSmith will be documented in this file.

## [1.0.0] - 2025-08-19

### Added
- Initial release of DraftSmith desktop application
- AI-powered content creation platform
- Native desktop interface using pywebview
- Cross-platform support (Windows, macOS, Linux)
- Flask-based web backend
- Multiple AI model support (OpenAI, Anthropic, Google)
- Persona-based content generation
- Draft management and revision system

### Fixed
- Fixed pywebview startup issues with platform-specific backend selection
- Resolved dependency conflicts with Qt backend on Linux/Windows
- Fixed webview.start() API compatibility with pywebview 2.4

### Technical
- Uses Qt backend on Linux and Windows for consistent behavior
- Uses native Cocoa backend on macOS for optimal performance
- Eliminates system dependencies (webkit2gtk) on Linux