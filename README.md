# 🌿 AI-Powered Photosynthesis Content Generator

This Streamlit app helps teachers and students generate educational materials on photosynthesis using a local AI model.

## ✨ Features
- Generate Lesson Plans, Study Notes, Quizzes, Glossary Terms, and Fun Facts
- Choose difficulty tone (Beginner, Intermediate, Advanced)
- Review and edit generated quizzes
- Export generated content to `.txt` files

## 🛠️ How to Run

1. Clone the repository:
   ```
   git clone https://github.com/your-username/photosynthesis-generator.git
   cd photosynthesis-generator
   ```

2. Create and activate a virtual environment:
   ```
   python -m venv venv
   source venv/bin/activate     # On Windows: venv\Scripts\activate
   ```

3. Install requirements:
   ```
   pip install -r requirements.txt
   ```

4. Run the app:
   ```
   streamlit run project.py
   ```

## 🧠 Model
Uses a local GPT-2 model from Hugging Face via `transformers`. No external API key required.

## 📄 License
MIT License
