# Flask + pywebview Desktop App with Briefcase

🚀 A professional cross-platform desktop application built with Flask, pywebview, and Qt, packaged with Briefcase for seamless distribution.

## ✨ Features

- **🎯 Cross-platform**: Windows (.msi), macOS (.app), Linux (.AppImage)
- **🌐 Modern web UI**: Beautiful Flask-based interface with responsive design
- **🖥️ Native integration**: pywebview + Qt for native desktop experience
- **📦 Professional packaging**: Briefcase creates proper installers and app bundles
- **🔧 Zero build complexity**: One command builds for all platforms
- **🧪 Built-in testing**: Unit tests included with pytest integration

## 🏗️ Architecture

```
┌─────────────────┐    ┌──────────────────┐    ┌─────────────────┐
│   Web Frontend  │    │   Flask Backend  │    │  Desktop Shell  │
│   (HTML/CSS/JS) │◄──►│   (Python API)   │◄──►│   (pywebview)   │
└─────────────────┘    └──────────────────┘    └─────────────────┘
                                                         │
                                                ┌─────────────────┐
                                                │   Qt Rendering  │
                                                │   (Native GUI)  │
                                                └─────────────────┘
```

## 🚀 Quick Start

### Prerequisites

- **Python 3.11+**
- **Git**

### 1. Clone and Setup

```bash
git clone https://github.com/badri/flask-pywebview-briefcase.git
cd flask-pywebview-briefcase

# Create virtual environment
python -m venv venv

# Activate virtual environment
# Windows:
venv\Scripts\activate
# macOS/Linux:
source venv/bin/activate

# Install Briefcase
pip install briefcase
```

### 2. Development Mode

```bash
# Run in development mode (fast testing)
briefcase dev
```

### 3. Build and Package

```bash
# Create the app scaffold
briefcase create

# Build the app
briefcase build

# Package for distribution
briefcase package

# Run the packaged app
briefcase run
```

## 📦 Distribution Packages

### Windows
- **Output**: `dist/Flask PyWebView App-1.0.0.msi`
- **Type**: Professional MSI installer
- **Features**: Start menu integration, uninstaller, app registry

### macOS  
- **Output**: `dist/Flask PyWebView App-1.0.0.dmg`
- **Type**: Signed .app bundle in DMG
- **Features**: Drag-to-install, Gatekeeper compatible

### Linux
- **Output**: `dist/Flask PyWebView App-1.0.0.AppImage`
- **Type**: Universal Linux executable
- **Features**: Run anywhere, no installation required

## 🛠️ Development Workflow

### Development Commands

```bash
# Fast development testing
briefcase dev

# Run tests
python -m pytest tests/

# Clean build (if needed)
briefcase create --force
```

### Platform-Specific Builds

```bash
# Build for current platform
briefcase package

# Cross-platform builds (via CI/CD)
# See .github/workflows/build.yml
```

### Adding Dependencies

Edit `pyproject.toml` and add to the `requires` list:

```toml
requires = [
    "Flask>=3.1.0",
    "pywebview>=5.3.2",
    "your-new-dependency>=1.0.0"
]
```

## 🎨 Customization

### App Configuration

Edit `pyproject.toml`:

```toml
[tool.briefcase.app.flask_pywebview_app]
formal_name = "Your App Name"
description = "Your app description"
# Update bundle, author, etc.
```

### Adding Routes

In `src/flask_pywebview_app/app.py`:

```python
@app.route('/api/my-endpoint')
def my_endpoint():
    return jsonify({'data': 'your data'})
```

### UI Styling

Modify `src/flask_pywebview_app/resources/templates/index.html` or add CSS/JS files to the `static/` directory.

### App Icon

Add these files:
- `src/flask_pywebview_app/resources/icon.png` (256x256)
- `src/flask_pywebview_app/resources/icon.ico` (Windows)
- `src/flask_pywebview_app/resources/icon.icns` (macOS)

## 🧪 Testing

```bash
# Run all tests
python -m pytest tests/

# Run with coverage
pip install pytest-cov
python -m pytest tests/ --cov=src/flask_pywebview_app

# Test Flask routes specifically
python -m pytest tests/test_app.py -v
```

## 🔧 Platform-Specific Notes

### Windows
- **Requirements**: Visual Studio Build Tools (automatic via Briefcase)
- **Signing**: Add certificate configuration to `pyproject.toml`
- **Distribution**: MSI can be distributed directly or via package managers

### macOS
- **Requirements**: Xcode Command Line Tools
- **Signing**: Configure Apple Developer ID in `pyproject.toml`
- **Distribution**: DMG for direct download, or submit to Mac App Store

### Linux
- **Requirements**: System Qt5 packages (handled automatically)
- **Distribution**: AppImage runs on most distributions
- **Package managers**: Can also build `.deb` packages

## 🚀 CI/CD with GitHub Actions

The repository includes automated builds for all platforms. On every push or tag:

1. **Builds**: Windows MSI, macOS DMG, Linux AppImage
2. **Tests**: Runs test suite on all platforms  
3. **Artifacts**: Uploads distribution packages
4. **Releases**: Auto-creates releases for version tags

### Creating a Release

```bash
git tag v1.0.0
git push origin v1.0.0
```

GitHub Actions will automatically create a release with platform installers.

## 📁 Project Structure

```
flask-pywebview-briefcase/
├── pyproject.toml                       # Briefcase configuration
├── src/
│   └── flask_pywebview_app/
│       ├── __init__.py                  # Package metadata
│       ├── __main__.py                  # Entry point
│       ├── app.py                       # Main application logic
│       └── resources/
│           ├── templates/
│           │   └── index.html          # Web interface
│           ├── static/                 # CSS, JS, images
│           └── icon.png               # App icon
├── tests/
│   ├── __init__.py
│   └── test_app.py                     # Flask route tests
├── .github/
│   └── workflows/
│       └── build.yml                   # CI/CD pipeline
└── README.md
```

## 🆚 vs PyInstaller Approach

| Feature | Briefcase | PyInstaller |
|---------|-----------|-------------|
| **Setup Complexity** | ✅ Simple | ❌ Complex (Docker, scripts) |
| **Cross-platform** | ✅ Native support | ❌ Manual configuration |
| **Professional Packaging** | ✅ MSI, DMG, AppImage | ❌ Basic executables |
| **Dependency Management** | ✅ Automatic | ❌ Manual spec files |
| **Distribution** | ✅ Store-ready | ❌ Manual signing/packaging |
| **Build Time** | ✅ Fast | ❌ Slow (especially Linux) |

## 🤝 Contributing

1. Fork the repository
2. Create a feature branch: `git checkout -b feature/amazing-feature`
3. Make your changes
4. Run tests: `python -m pytest tests/`
5. Test the build: `briefcase dev`
6. Commit: `git commit -m 'Add amazing feature'`
7. Push: `git push origin feature/amazing-feature`
8. Open a Pull Request

## 📄 License

MIT License - see [LICENSE](LICENSE) file for details.

## 🆘 Support

- **Documentation**: [Briefcase docs](https://briefcase.readthedocs.io/)
- **Issues**: [GitHub Issues](https://github.com/badri/flask-pywebview-briefcase/issues)
- **Discussions**: [GitHub Discussions](https://github.com/badri/flask-pywebview-briefcase/discussions)

## 🙏 Acknowledgments

- **BeeWare Project**: For the excellent Briefcase packaging tool
- **pywebview**: For seamless web-to-native integration
- **Flask**: For the robust web framework
- **Qt**: For consistent cross-platform rendering

---

**Ready to build professional desktop apps?** 🚀

```bash
git clone https://github.com/badri/flask-pywebview-briefcase.git
cd flask-pywebview-briefcase
pip install briefcase
briefcase dev
```

**That's it!** No Docker, no complex scripts, just professional results. ✨
