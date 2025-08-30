# CLAUDE.md

This file provides guidance to Claude Code (claude.ai/code) when working with code in this repository.

## Development Commands

### Environment Setup
```bash
# Create conda environment
conda create -n myenv python==3.12.9
conda activate myenv

# Install dependencies
pip install -r src/requirements.txt

# Setup environment variables
cp src/.env.example src/.env
# Edit .env file with your OPENAI_API_KEY and other settings
```

### Running the Application
```bash
# Standard FastAPI server
cd src
uvicorn main:app --reload --host 127.0.0.1 --port 8000

# Quick run script
cd src
python run.py
```

## Architecture Overview

This is a FastAPI-based RAG (Retrieval-Augmented Generation) application for document processing and question answering.

### Core Structure
- **FastAPI Application**: Main entry point in `src/main.py`
- **Router-based Architecture**: API routes organized under `/api/v1`
  - `routes/base.py`: Health/info endpoints
  - `routes/data.py`: File upload and processing endpoints
- **Controller Pattern**: Business logic separated into controllers
  - `DataController`: File validation and upload handling
  - `ProcessController`: Document processing and text chunking using LangChain
  - `ProjectController`: Project/directory management
- **Configuration**: Pydantic Settings-based config in `helpers/config.py`

### Key Features
- **File Processing**: Supports TXT, PDF, CSV, Excel files up to 10MB
- **Document Chunking**: Uses LangChain's RecursiveCharacterTextSplitter
- **Project Organization**: Files organized by project_id directories
- **Environment Configuration**: Settings managed via .env file

### File Processing Flow
1. Upload file via `/api/v1/data/upload/{project_id}`
2. File validation (type, size) in `DataController`
3. Unique file naming and storage
4. Process chunks via `/api/v1/data/process/{project_id}`
5. Content extraction using appropriate LangChain loaders (TextLoader, PyMuPDFLoader, UnstructuredExcelLoader)
6. Text splitting into configurable chunks with overlap

### Environment Variables
Required variables in `.env`:
- `OPENAI_API_KEY`: OpenAI API key for LLM integration
- `APP_NAME`, `APP_VERSION`: Application metadata
- `FILE_ALLOWED_TYPES`: Supported MIME types (list format)
- `FILE_MAX_SIZE`: Maximum file size in MB
- `FILE_DEFAULT_CHUNK_SIZE`: File read chunk size in bytes

### Testing
POSTMAN collection available at `src/assets/Rag_App_test.postman_collection.json`