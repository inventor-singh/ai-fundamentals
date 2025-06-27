# Installation Guide

## 🌟 **Recommended: Zero Setup Required!**

### Google Colab (Best for Beginners)
The easiest way to get started - **no installation needed!**

1. Click any "Open in Colab" button in the README
2. The notebook opens in your browser
3. **All packages install automatically** when you run the first cells
4. Start learning immediately!

**Why Colab?**
- ✅ Zero setup time
- ✅ Free GPU access for advanced lessons  
- ✅ Automatic package management
- ✅ Save to your Google Drive
- ✅ Share easily with others

---

## 💻 **Local Installation (Advanced Users)**

### Prerequisites
- Python 3.8 or higher
- pip package manager

### Quick Setup
```bash
# Clone the repository
git clone https://github.com/YOUR_USERNAME/ai-mastery-from-scratch.git
cd ai-mastery-from-scratch

# Launch Jupyter (packages install automatically in notebooks)
jupyter notebook
```

### Optional: Pre-install Everything
If you want to pre-install all packages (not required):
```bash
# Create virtual environment (recommended)
python -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate

# Install all packages
pip install -r requirements.txt
```

---

## 🚀 **How It Works**

Each notebook is **completely self-contained**:

1. **Open any notebook** (locally or in Colab)
2. **Run the first cell** - it installs required packages automatically
3. **Start learning** - everything just works!

### Sample Installation Cell (in every notebook):
```python
# 📦 Simple package installation
print("🚀 Installing packages...")

!pip install numpy>=1.21.0 --quiet
!pip install matplotlib>=3.5.0 --quiet
!pip install seaborn>=0.11.0 --quiet

print("🎉 Ready to learn!")
```

## Troubleshooting

### Common Issues

**Issue**: `ModuleNotFoundError` when importing packages
**Solution**: Make sure you've activated your virtual environment and installed requirements

**Issue**: Jupyter not opening
**Solution**: Try `python -m jupyter notebook` instead

**Issue**: Plots not showing
**Solution**: Add `%matplotlib inline` at the top of your notebook cells

**Issue**: Memory errors with large datasets
**Solution**: Consider using Google Colab for more memory

### Getting Help
- Check our [FAQ](faq.md)
- Open an [issue on GitHub](https://github.com/YOUR_USERNAME/ai-mastery-from-scratch/issues)
- Join our [discussions](https://github.com/YOUR_USERNAME/ai-mastery-from-scratch/discussions)
