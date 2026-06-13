# AI Image Reader - OCR Text Extraction

An AI-powered Python app that extracts printed text from images using Optical Character Recognition. Built with Tesseract OCR + OpenCV.

## 1. Project Overview
This project solves the problem of manually retyping text from images like receipts, book pages, and documents. The app uses Tesseract OCR to “read” images and output editable text in seconds.

**Key Features:**
1. Upload any image and extract text instantly
2. Image pre-processing: grayscale + noise removal for higher accuracy  
3. Save extracted text as .txt file
4. Simple GUI built with Tkinter
5. Works offline - no API keys needed

## 2. Tech Stack & Tools
| **Category** | **Tools** |
| --- | --- |
| **Language** | Python 3.10+ |
| **OCR Engine** | Tesseract OCR |
| **Libraries** | pytesseract, OpenCV, Pillow, Tkinter |
| **Platform** | Windows/Mac/Linux |

## 3. Installation & Setup

**Step 1: Install Tesseract OCR**
1. Windows: Download from [Tesseract GitHub](https://github.com/UB-Mannheim/tesseract/wiki)
2. Mac: `brew install tesseract`
3. Linux: `sudo apt install tesseract-ocr`

**Step 2: Clone repo**
```bash
git clone https://github.com/yourusername/ai-image-reader.git
cd ai-image-reader
