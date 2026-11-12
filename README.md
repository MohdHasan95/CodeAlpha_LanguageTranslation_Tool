# CodeAlpha Language Translation Tool

**Artificial Intelligence Internship — Task 1**

A desktop language translation application built using Python and Tkinter.

## Features
- Text input and translated output panels
- Source language selection with auto-detection
- Target language selection
- 20 selectable languages plus auto-detect
- Translate, swap, clear and copy-result buttons
- Helpful validation and error messages

## Requirements
- Python 3.9 or newer
- Internet connection
- Tkinter (normally included with Windows Python)
- `deep-translator` package

## Setup and run
Open a terminal in the project folder:

```bash
py -m pip install -r requirements.txt
py main.py
```

On systems without the `py` launcher, use `python` instead.

## Demo
1. Type `Hello, how are you?`
2. Set source to English and target to Hindi.
3. Click **Translate**.
4. Try **Copy Result** and **Swap**.

## Implementation note
This project uses the `deep-translator` GoogleTranslator integration, which accesses a translation service over the internet. It is **not** the official paid Google Cloud Translation API and may be subject to service changes or rate limits. No API key is required for this implementation.

## Internship
CodeAlpha repository naming format: `CodeAlpha_ProjectName`.

**Note:** Translation needs to be tested with an active internet connection before recording the LinkedIn demo.
