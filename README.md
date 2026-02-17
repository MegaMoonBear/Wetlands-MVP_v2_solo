# Wetlands MVP v2 Solo

A minimal viable product for wetland education that uses AI vision to analyze and describe wetland images, helping users learn about water ecosystems and their importance.

## 📋 Table of Contents
- [Overview](#overview)
- [Setup Guide](#setup-guide)
- [Dependencies](#dependencies)
- [Usage Instructions](#usage-instructions)
- [API Keys](#api-keys)
- [Deployment Instructions](#deployment-instructions)
- [Developer Notes](#developer-notes)
- [Troubleshooting](#troubleshooting)

## Overview

This project is an educational tool that:
- **Visitors**: Learn about water and wetlands importance through AI-powered image analysis
- **Uploaders**: Gain understanding of water issues and wetlands' role through interactive photo analysis

The current MVP demonstrates AI capability by:
1. Manually placing images in `/backend/images_preUpload/`
2. Hardcoding filenames in FastAPI
3. Sending image paths to Ollama (LLaVA vision model)
4. Receiving AI-generated descriptions focused on wetland education
5. Returning structured JSON responses
6. Displaying results (future React frontend integration)

## 🛠 Setup Guide

### Prerequisites
- Python 3.8+
- Ollama installed locally
- LLaMA 3.2 Vision model (`llama3.2-vision`)

### Installation Steps

1. **Clone the repository**
   ```bash
   git clone <repository-url>
   cd Wetlands-MVP_v2_solo
   ```

2. **Install Python dependencies**
   ```bash
   pip install fastapi uvicorn ollama
   ```

3. **Install and setup Ollama**
   ```bash
   # Install Ollama (visit https://ollama.ai for platform-specific instructions)
   # Pull the required vision model
   ollama pull llama3.2-vision
   ```

4. **Verify Ollama is running**
   ```bash
   ollama serve
   ```

## 📦 Dependencies

### Required Python Packages
- `fastapi` - Web framework for building APIs
- `uvicorn` - ASGI server for FastAPI
- `ollama` - Python client for Ollama AI models

### AI Models
- `llama3.2-vision` - Vision-language model for image analysis

### Future Dependencies (Planned)
- PostgreSQL database
- React frontend
- File upload handling
- Authentication system

## 🚀 Usage Instructions

### Running the Backend

1. **Start the FastAPI server**
   ```bash
   cd backend
   uvicorn main:app --host 127.0.0.1 --port 8000 --reload
   ```

2. **Test the API**
   - Open browser to `http://127.0.0.1:8000`
   - Should see: `{"message": "Hello, World!"}`

### Image Analysis

1. **Place image files** in [`backend/images_preUpload/`](backend/images_preUpload/)

2. **Update image path** in [`model_RAG_response.py`](backend/model_RAG_response.py):
   ```python
   image_path = 'images_preUpload/your-image-name.png'
   ```

3. **Run image analysis**
   ```bash
   cd backend
   python model_RAG_response.py
   ```

### Expected Output
The AI will provide:
- Image description with common names (not scientific)
- Educational fact suitable for 10-second reading
- Focus on wetland ecosystems and water importance

## 🔑 API Keys

### Current Setup
- No external API keys required
- Uses local Ollama installation

### Future Requirements
- Database connection credentials (`.env` file)
- Potential cloud AI service keys
- Image storage service credentials

## 🚀 Deployment Instructions

### Local Development
```bash
# Terminal 1: Start Ollama
ollama serve

# Terminal 2: Start FastAPI
cd backend
uvicorn main:app --host 127.0.0.1 --port 8000 --reload
```

### Production Deployment (Future)
1. **Environment Setup**
   - Configure production database
   - Set up environment variables
   - Install dependencies on server

2. **Server Configuration**
   ```bash
   uvicorn backend.main:app --host 0.0.0.0 --port 8000
   ```

3. **Database Setup**
   - PostgreSQL configuration
   - Migration scripts
   - Connection pooling

## 👥 Developer Notes

### Project Structure
```
Wetlands-MVP_v2_solo/
├── backend/
│   ├── main.py              # FastAPI application entry point
│   ├── model_RAG_response.py # AI image analysis logic
│   ├── image_util.py        # Base64 encoding utilities
│   ├── images_preUpload/    # Image storage directory
│   └── documentation/       # Project documentation
├── README.md
├── LICENSE
```

### Key Files
- [`main.py`](backend/main.py) - FastAPI routes and server configuration
- [`model_RAG_response.py`](backend/model_RAG_response.py) - Ollama integration and prompt engineering
- [`image_util.py`](backend/image_util.py) - Image processing utilities

### Development Priorities
1. **Next Phase Options**:
   - File upload functionality
   - Database integration
   - User authentication
   - Frontend development (React)

2. **Code Quality**:
   - Add error handling
   - Implement logging
   - Create unit tests
   - API documentation

### Prompt Engineering
The AI prompt is designed to:
- Act as a nature guide focused on wetlands
- Provide 5th-grade level explanations (10-second read time)
- Emphasize ecological importance of wetlands
- Avoid encouraging risky behavior near water

## 🔧 Troubleshooting

### Common Issues

**1. Ollama Connection Failed**
```bash
# Solution: Ensure Ollama is running
ollama serve
# Check if model is available
ollama list
```

**2. Image File Not Found**
- Verify image path in [`model_RAG_response.py`](backend/model_RAG_response.py)
- Check file exists in `images_preUpload/` directory
- Ensure correct file permissions

**3. FastAPI Import Errors**
```bash
# Solution: Install missing dependencies
pip install fastapi uvicorn
```

**4. Model Not Available**
```bash
# Solution: Pull the required model
ollama pull llama3.2-vision
```

### Debug Steps
1. Check Ollama service status
2. Verify Python environment and packages
3. Confirm image file paths and permissions
4. Review error logs in terminal output

### Getting Help
- Check [`documentation/`](backend/documentation/) folder for detailed guides
- Review code comments for implementation details
- Test with sample images in `images_preUpload/`

## 📍 Recommended Test Locations
As noted in [`Sites_recomm_preGIS.md`](backend/documentation/Sites_recomm_preGIS.md):
- Wolf River Greenway locations
- Bridge and culvert areas with safe access
- Areas suitable for educational photography

---

**Note**: This is an MVP focused on demonstrating AI capabilities. Future versions will include full web application functionality, user uploads, and comprehensive wetland education features.