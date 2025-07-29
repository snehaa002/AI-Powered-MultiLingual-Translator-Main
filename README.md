# 🌍 AI-Powered Multi-Lingual Translator

A sophisticated AI-powered translation application built with Python, featuring a modern Gradio interface and powered by HuggingFace Transformers.

## ✨ Features

- **Multi-Language Support**: Translate between English, Hindi, French, German, and Spanish
- **Modern UI**: Beautiful Gradio interface with custom styling
- **AI-Powered**: Uses T5 model for intelligent translations
- **Fallback System**: High-quality curated translations for common phrases
- **Real-time Translation**: Instant translation with one click
- **Example Phrases**: Quick-start with pre-loaded example sentences

## 🚀 Quick Start

### Prerequisites

- Python 3.11 or earlier (recommended for full compatibility)
- pip package manager

### Installation

1. **Clone the repository**
   ```bash
   git clone https://github.com/snehaa002/AI-Powered-MultiLingual-Translator-Main.git
   cd AI-Powered-MultiLingual-Translator-Main
   ```

2. **Create a virtual environment**
   ```bash
   python -m venv .venv
   
   # On Windows
   .venv\Scripts\activate
   
   # On macOS/Linux
   source .venv/bin/activate
   ```

3. **Install dependencies**
   ```bash
   pip install -r requirements.IBM.txt
   ```

4. **Run the application**
   ```bash
   python IBM_internship.py
   ```

The application will launch in your default web browser at 127.0.0.1:7860

## 🔧 Usage

1. **Enter Text**: Type or paste the text you want to translate
2. **Select Languages**: Choose source and target languages from the dropdowns
3. **Translate**: Click "🚀 Translate Now" or press Enter
4. **Quick Examples**: Use the example buttons for common phrases

### Supported Language Pairs

- 🇺🇸 English ↔ 🇮🇳 Hindi
- 🇺🇸 English ↔ 🇫🇷 French  
- 🇺🇸 English ↔ 🇩🇪 German
- 🇺🇸 English ↔ 🇪🇸 Spanish

## 🏗️ Architecture

### Core Components

- **Translation Engine**: T5 model with intelligent fallback system
- **UI Framework**: Gradio with custom CSS styling
- **Model Backend**: HuggingFace Transformers
- **Fallback System**: Curated high-quality translations

### Files Structure

```
├── IBM_internship.py          # Main application file
├── app.py                     # Alternative entry point
├── requirements.IBM.txt       # Python dependencies
├── test_translation.py        # Translation function tests
├── test_specific.py          # Specific case testing
├── .gitignore                # Git ignore rules
└── README.md                 # Project documentation
```

## 🧪 Testing

Run the included test scripts to verify translation functionality:

```bash
# Test general translation function
python test_translation.py

# Test specific problematic cases
python test_specific.py
```

## ⚠️ Compatibility Notes

### Python 3.13 Compatibility

If you encounter issues with Python 3.13 (especially with `sentencepiece`):

1. **Use Python 3.11 or earlier** (recommended)
2. **Alternative solutions**:
   - Install Visual Studio Build Tools for Windows
   - Use WSL (Windows Subsystem for Linux)
   - Use a Docker container
   - Use the demo mode (works without sentencepiece)

### Demo Mode

The application includes a robust demo mode that works even if some dependencies fail to install. It uses:
- Curated translations for common phrases
- Mock translation system for demonstration
- Full UI functionality

## 🛠️ Development

### Adding New Languages

1. Add language to `language_options` in `IBM_internship.py`
2. Add curated translations to the fallback dictionaries
3. Update the model prompt construction logic

### Extending Translation Pairs

1. Update the prompt construction in the `translate()` function
2. Add corresponding curated translations
3. Test with the provided test scripts

## 📋 Dependencies

- **transformers**: HuggingFace Transformers library
- **torch**: PyTorch for model inference
- **gradio**: Web UI framework
- **sentencepiece**: Tokenization (optional in demo mode)


## 🙏 Acknowledgments

- HuggingFace for the Transformers library
- Google for the T5 model
- Gradio team for the amazing UI framework




---

**Built with ❤️ for the global community** 🌍
