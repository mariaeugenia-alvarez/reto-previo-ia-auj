# AI Challenge Project

This project is divided into two main components:

## Project Structure

### 1. Prompt Component
- **File**: `PROMPT.md`
- Contains the AI prompt configuration and instructions

### 2. Cloud Function Component
- Firebase Cloud Function that can be deployed to Google Cloud Platform
- Located in the `functions/` directory
- Handles the backend logic and API endpoints

## Deployment

To deploy the Cloud Function to Firebase:

```bash
firebase deploy --only functions --project <alias_or_project_id>
```

Replace `<alias_or_project_id>` with your actual Firebase project alias or project ID.

## Prerequisites

- Firebase CLI installed
- Firebase project configured
- Proper authentication set up for your Firebase project

## Getting Started

1. Clone the repository
2. Navigate to the functions directory: `cd functions`
3. Create a Python virtual environment: `python3 -m venv venv`
4. Activate the virtual environment: `source venv/bin/activate`
5. Install dependencies: `pip install -r requirements.txt`
6. Configure your Firebase project
7. Deploy using the command above

## Troubleshooting

### Missing Virtual Environment Error

If you encounter the error `Missing virtual environment at venv directory`, follow these steps:

1. Navigate to the functions directory:
   ```bash
   cd functions
   ```

2. Create the virtual environment:
   ```bash
   python3 -m venv venv
   ```

3. Activate the virtual environment and install dependencies:
   ```bash
   source venv/bin/activate
   pip install -r requirements.txt
   ```

4. Deploy from the project root:
   ```bash
   cd ..
   firebase deploy --only functions --project <alias_or_project_id>
   ```

## Files Structure

```
├── firebase.json          # Firebase configuration
├── PROMPT.md              # AI prompt instructions
├── README.md              # This file
└── functions/
    ├── main.py            # Cloud Function main code
    └── requirements.txt   # Python dependencies
```