# 🔧 Troubleshooting Guide

If you're getting the "ModuleNotFoundError: No module named 'flask'" error, here are the steps to fix it:

## 🚨 Quick Fix

1. **Clean any existing builds:**
   ```bash
   rm -rf build/ dist/
   ```

2. **Install dependencies first:**
   ```bash
   pip install -r requirements.txt
   ```

3. **Force recreate the app:**
   ```bash
   briefcase create --force
   ```

4. **Build and run:**
   ```bash
   briefcase build
   briefcase run
   ```

## 🐛 Common Issues and Solutions

### Issue: "ModuleNotFoundError: No module named 'flask'"

**Cause**: Briefcase isn't properly bundling Flask dependencies.

**Solution**:
```bash
# Method 1: Clean rebuild
rm -rf build/ dist/
briefcase create --force
briefcase build
briefcase run

# Method 2: If still failing, try development mode first
briefcase dev  # This should work
# Then try building again
briefcase create --force
briefcase build
```

### Issue: "Application quit abnormally!"

**Cause**: Dependencies not properly included in bundle.

**Solution**:
```bash
# Check that your virtual environment has all dependencies
pip install -r requirements.txt

# Verify Flask is installed
python -c "import flask; print(flask.__version__)"

# Clean rebuild
briefcase create --force
briefcase build --force
```

### Issue: Qt/PyQt5 related errors

**Cause**: System Qt conflicts or missing system dependencies.

**Solution**:

**macOS:**
```bash
# Install system Qt (if needed)
brew install qt@5

# Clean rebuild
briefcase create --force
```

**Linux:**
```bash
# Install system dependencies
sudo apt-get install python3-pyqt5 python3-pyqt5.qtwebengine

# Clean rebuild
briefcase create --force
```

**Windows:**
```bash
# Usually works out of the box, but if issues:
# Clean rebuild
briefcase create --force
```

## 🔍 Debug Steps

### 1. Test Development Mode First
```bash
# This should always work
briefcase dev
```
If this fails, there's an issue with your dependencies or code.

### 2. Check Bundle Contents (macOS)
```bash
# After building, check what's in the app bundle
ls -la "build/flask_pywebview_app/macos/app/Flask PyWebView App.app/Contents/Resources/app/"

# Check if Flask is included
find "build/" -name "*flask*" -type d
```

### 3. Verbose Build
```bash
# Get more detailed build output
briefcase build --force -v
```

## ✅ Verification Steps

After fixing, verify everything works:

```bash
# 1. Development mode should work
briefcase dev

# 2. Build should complete without errors
briefcase build

# 3. App should run without module errors
briefcase run

# 4. Package should create distribution files
briefcase package
```

## 🆘 If Nothing Works

Try this nuclear option:

```bash
# 1. Completely clean everything
rm -rf build/ dist/ .briefcase/

# 2. Recreate virtual environment
deactivate
rm -rf venv/
python -m venv venv
source venv/bin/activate  # or venv\Scripts\activate on Windows

# 3. Reinstall everything
pip install briefcase
pip install -r requirements.txt

# 4. Fresh start
briefcase create
briefcase build
briefcase run
```

## 📞 Getting Help

If you're still having issues:

1. **Check the Briefcase logs** in `.briefcase/logs/`
2. **Post an issue** with the full error traceback
3. **Include your platform** (macOS version, Python version, etc.)

The key is that `briefcase dev` should **always** work - it runs your app directly without packaging. If that fails, the issue is with your Python environment, not Briefcase packaging.
