import streamlit as st
import re
from transformers import pipeline
import torch

st.title("📘 Photosynthesis Content Generator")
st.subheader("Grade 7 Educational Materials")

# Sidebar selections
content_type = st.sidebar.radio(
    "Select Content Type",
    ["Lesson Plan", "Study Notes", "Glossary Terms", "Fun Facts", "Quiz"]
)

difficulty = st.sidebar.selectbox(
    "Select Difficulty Tone",
    ["Easy", "Medium", "Hard"],
    help="Choose the difficulty level for the generated content"
)

max_tokens = st.sidebar.slider("Max Tokens", min_value=50, max_value=300, value=150)

# Prompt templates and difficulty descriptions
base_prompts = {
    "Lesson Plan": "Create a lesson plan for teaching photosynthesis to Grade 7 students. Include objectives, materials, and activities.",
    "Study Notes": "Summarize photosynthesis for Grade 7 students using bullet points.",
    "Glossary Terms": "Define key terms related to photosynthesis for Grade 7 students (e.g., chlorophyll, carbon dioxide).",
    "Fun Facts": "List 5 fun or surprising facts about photosynthesis that would interest Grade 7 students.",
    "Quiz": "Generate 5 multiple-choice quiz questions about photosynthesis for Grade 7 learners."
}

difficulty_descriptions = {
    "Easy": "Use simple words and examples suitable for younger learners.",
    "Medium": "Include moderate detail and scientific terms but keep it accessible.",
    "Hard": "Include in-depth scientific concepts and advanced terminology."
}

def create_prompt(content_type, difficulty_tone):
    prompt = base_prompts.get(content_type, "")
    if prompt:
        prompt += " " + difficulty_descriptions.get(difficulty_tone, "")
    return prompt

# Load model once with caching
@st.cache_resource
def load_generator():
    device = 0 if torch.cuda.is_available() else -1
    return pipeline("text-generation", model="gpt2", device=device)

with st.spinner("Loading model, please wait..."):
    generator = load_generator()

def ai_generate(prompt):
    try:
        result = generator(
            prompt,
            max_new_tokens=max_tokens,
            temperature=0.7,
            top_p=0.95,
            repetition_penalty=1.2,
            do_sample=True,
            num_return_sequences=1
        )
        return result[0]["generated_text"]
    except Exception as e:
        return f"Error generating content: {e}"

# Quiz parsing function
def parse_quiz(raw_text):
    pattern = r"(\d+)\.\s*(.*?)\n((?:[A-D]\).*\n){4})Answer:\s*([A-D])"
    matches = re.findall(pattern, raw_text, re.MULTILINE)
    questions = []
    for num, question, options, answer in matches:
        opts = options.strip().split('\n')
        questions.append({
            "number": num,
            "question": question.strip(),
            "options": [o[3:].strip() for o in opts],
            "answer": answer
        })
    return questions

def display_fun_facts():
    fun_facts_list = [
        "🌞 Plants are nature’s solar panels—they turn sunlight into food!",
        "🌵 The “resurrection plant” can survive years without water and come back to life!",
        "🍃 Photosynthesis keeps our air fresh by producing oxygen.",
        "🎋 Bamboo grows super fast thanks to photosynthesis working overtime.",
        "🌍 The Amazon rainforest produces about 20% of the world's oxygen — the 'lungs of the Earth.'",
        "✨ Some plants glow in the dark, which is called bioluminescence!",
        "💧 Cactus plants perform photosynthesis differently to survive deserts.",
        "🍂 Leaves change color in autumn because photosynthesis slows down.",
        "🌊 Ocean algae produce more oxygen than all forests combined.",
        "🔋 Scientists are trying to copy photosynthesis to create clean energy like plant-powered batteries!"
    ]

    st.markdown("### 🌟 Fun Facts About Photosynthesis 🌟")
    for fact in fun_facts_list:
        st.markdown(f"- <span style='color:green'>{fact}</span>", unsafe_allow_html=True)

    st.markdown("---")
    st.markdown("**Which fun fact surprised you the most?**")
    surprise = st.radio("Choose one:", fun_facts_list, index=0)
    st.write(f"Awesome! You chose: _{surprise}_ 🎉")

# Main logic
if content_type == "Quiz":
    st.header("🔎 Quiz Generator with Review & Export")

    if st.button("🎯 Generate Quiz"):
        prompt = create_prompt("Quiz", difficulty)
        raw_quiz = ai_generate(prompt)
        st.text_area("📝 Raw AI-Generated Quiz Text", raw_quiz, height=300)
        st.session_state['raw_quiz'] = raw_quiz

    if 'raw_quiz' in st.session_state:
        quiz_data = parse_quiz(st.session_state['raw_quiz'])
        if not quiz_data:
            st.error("No valid questions found. Please check the AI output format.")
        else:
            show_answers = st.checkbox("Show Correct Answers", value=False)

            st.header("✍️ Review & Edit Quiz Questions")
            edited_quiz = []

            for q in quiz_data:
                st.markdown(f"### Question {q['number']}")
                question_text = st.text_input(f"Question {q['number']}", q['question'], key=f"q{q['number']}")
                options = []
                for i, opt in enumerate(q['options']):
                    option_text = st.text_input(f"Option {chr(65+i)}", opt, key=f"q{q['number']}o{i}")
                    options.append(option_text)

                if show_answers:
                    answer = st.selectbox(
                        f"Correct Answer for Question {q['number']}",
                        ['A', 'B', 'C', 'D'],
                        index=ord(q['answer']) - 65,
                        key=f"ans{q['number']}"
                    )
                else:
                    st.markdown(f"Correct Answer for Question {q['number']}: **Hidden**")
                    answer = q['answer']

                edited_quiz.append({
                    "number": q['number'],
                    "question": question_text,
                    "options": options,
                    "answer": answer
                })

            if st.button("💾 Export Quiz as TXT"):
                lines = []
                for q in edited_quiz:
                    lines.append(f"{q['number']}. {q['question']}")
                    for i, opt in enumerate(q['options']):
                        lines.append(f"{chr(65+i)}) {opt}")
                    lines.append(f"Answer: {q['answer']}\n")
                quiz_text_export = "\n".join(lines)

                st.download_button(
                    label="Download Quiz Text File",
                    data=quiz_text_export,
                    file_name="photosynthesis_quiz.txt",
                    mime="text/plain"
                )

elif content_type == "Fun Facts":
    display_fun_facts()

else:
    st.header(f"📝 {content_type} Generator")

    user_prompt = st.text_area(f"{content_type} Prompt",
                               value=create_prompt(content_type, difficulty),
                               height=150)

    if st.button(f"Generate {content_type}"):
        generated_content = ai_generate(user_prompt)
        st.text_area(f"Generated {content_type}", generated_content, height=300)

        st.download_button(
            f"Download {content_type} as TXT",
            generated_content,
            file_name=f"{content_type.lower().replace(' ', '_')}.txt",
            mime="text/plain"
        )
