# Lead Generation Tool

This tool extracts company data (depends on the headers) from websites and process it into csv or excel, I am using Gemini 2.0 Flash and a streamlit package for simple UI

📄 **[Read the Full Report](report.md)**  
🎥 **[Watch Demo Video](https://www.loom.com/share/fe9bc08c2dd944588599b9120fbbbdf9?sid=89f269ae-c755-4e95-b5d3-ca24607b758b**  

## Installation

### Prerequisites
- Python 3.11+
- Gemini API Key
- Installing requirements.txt


### Steps

1. **Clone Repository**
   ```bash
   git clone https://github.com/alrizkipascar/interview-challenge.git
   cd repo
   ```

2. **Create Virtual Environment**
   ```bash
   uv venv --python 3.11
   # For Mac/Linux:
   source .venv/bin/activate

   # For Windows:
   .venv\Scripts\activate
   ```

3. **Install Dependencies**
   ```bash
   uv pip install -r requirements.txt
   ```

4. **Set Up API Keys**
   - Create API Key for gemini
   - Set the Gemini API Key as an environment variable:
     ```bash
     export GEMINI_API_KEY="your-api-key"
     ```


## Usage

1. **Run the Lead Generation UI**
   ```bash
   python -m streamlit run UI.py
   ```

2. **Let The Program Process it**
   - Upload the file
   - Wait for the result out
   - Download the result
