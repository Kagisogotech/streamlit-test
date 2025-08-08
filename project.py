import streamlit as st
import re

st.title("Grade 7 Educational Materials📘")
st.subheader("📚Photosynthesis Content Generator")

content_type = st.sidebar.radio(
    "Select Content Type",
    ["Lesson Plan", "Study Notes", "Glossary Terms", "Fun Facts", "Quiz"]
)

difficulty = st.sidebar.selectbox(
    "Select Difficulty Tone",
    ["Easy", "Medium", "Hard"],
    index=1,
    help="Choose the difficulty level for the generated content"
)

# --- Updated placeholder AI generator (vary outputs by difficulty) ---
def ai_generate(content_type, difficulty):
    # Simple variations by difficulty for demonstration
    dummy_outputs = {
        "Lesson Plan": {
            "Easy": """📚 **Grade 7 Lesson Plan (Easy): Introduction to Photosynthesis**

Objectives:
- Understand the basics of photosynthesis.
- Identify sunlight, water, and carbon dioxide as ingredients.
- Learn what plants produce during photosynthesis.

Materials:
- Pictures of plants
- Simple diagrams

Activities:
- Discuss how plants make food in simple terms.
- Draw a plant and label parts.

""",
            "Medium": """📚 **Grade 7 Lesson Plan (Medium): Introduction to Photosynthesis**

Objectives:
- Explain the photosynthesis process.
- Identify inputs (sunlight, water, carbon dioxide) and outputs (oxygen, glucose).
- Understand the role of chlorophyll and chloroplasts.

Materials:
- Real leaves or images
- Plant cell diagrams
- Experiment materials (optional)

Activities:
- Warm-up question on plant food.
- Explanation with formula 6CO₂ + 6H₂O → C₆H₁₂O₆ + 6O₂.
- Group drawing and labeling.
- Mini-experiment observing oxygen bubbles.

""",
            "Hard": """📚 **Grade 7 Lesson Plan (Hard): Detailed Photosynthesis Study**

Objectives:
- Analyze the biochemical reactions in photosynthesis.
- Study photosystems I and II and electron transport chain.
- Explore chloroplast structure and pigment functions.

Materials:
- Microscope slides of chloroplasts
- Diagrams of photosynthetic electron transport
- Experimental setup for measuring oxygen output

Activities:
- Detailed lecture on light-dependent and light-independent reactions.
- Group discussion on biochemical pathways.
- Lab experiment measuring photosynthesis rates.

"""
        },
        "Study Notes": {
            "Easy": """- Photosynthesis is how plants make food from sunlight.
- Plants need sunlight, water, and air (carbon dioxide) to do photosynthesis.
- Photosynthesis happens mostly in leaves.
- It makes sugar for the plant to use as energy.
- Oxygen is released into the air during photosynthesis.
""",
            "Medium": """- Photosynthesis happens in chloroplasts, found mostly in leaf cells.
- Chlorophyll (green pigment) absorbs sunlight.
- Sunlight energy is used to combine carbon dioxide (CO₂) from the air and water (H₂O) from the soil to make glucose (C₆H₁₂O₆).
- Oxygen (O₂) is released into the atmosphere as a by-product.
- Word equation: Carbon dioxide + Water + Sunlight → Glucose + Oxygen
- Chemical equation: 6CO₂ + 6H₂O + Sunlight → C₆H₁₂O₆ + 6O₂
- Photosynthesis has two main stages:
  1. Light-dependent reactions – happen in the thylakoid membranes, converting sunlight to ATP and NADPH.
  2. Light-independent reactions (Calvin Cycle) – happen in the stroma, making glucose.
""",
            "Hard": """- Photosynthesis is an endothermic process — it needs energy from sunlight.
- It involves two photosystems:
  - Photosystem II (PSII) – absorbs light, splits water into oxygen, protons, and electrons.
  - Photosystem I (PSI) – absorbs light to energise electrons for NADPH production.
- Light-dependent reactions produce ATP (energy) and NADPH (electron carrier).
- The Calvin Cycle uses ATP and NADPH to fix CO₂ into glucose through enzyme-controlled steps, including RuBisCO.
- The rate of photosynthesis is affected by:
  - Light intensity
  - Carbon dioxide concentration
  - Temperature
- Different plants use different pathways: C3, C4, and CAM photosynthesis, adapted for their environments.
- Photosynthesis is essential for the global carbon and oxygen cycles and is the base of most food chains.
"""
        },
        "Glossary Terms": {
            "Easy": """1. Photosynthesis: How plants make food using sunlight.
2. Chlorophyll: Green stuff in leaves that catches sunlight.
3. Oxygen: Gas plants give off.
""",
            "Medium": """1. Photosynthesis: Process converting light energy to chemical energy.
2. Chlorophyll: Pigment that absorbs light for photosynthesis.
3. Chloroplast: Organelle where photosynthesis happens.
4. Carbon Dioxide: Gas used by plants in photosynthesis.
5. Oxygen: By-product gas released by plants.
""",
            "Hard": """1. Photosynthesis: Conversion of solar energy to chemical energy via photosystems.
2. Chlorophyll a and b: Pigments absorbing light at specific wavelengths.
3. Electron Transport Chain: Series of proteins facilitating electron flow.
4. ATP Synthase: Enzyme generating ATP during light-dependent reactions.
5. Calvin Cycle: Carbon fixation process forming glucose molecules.
"""
        },
        "Fun Facts": {
            "Easy": """🌞 Plants use sunlight to make food!
🌵 Some plants can live without water for a long time!
🍃 Photosynthesis helps clean the air.
""",
            "Medium": """🌞 Plants convert sunlight into chemical energy.
🌵 The resurrection plant survives droughts by photosynthesis adaptation.
🍃 Photosynthesis releases oxygen essential for life.
""",
            "Hard": """🌞 Photosystems I and II are key to capturing light energy.
🌵 CAM plants fix carbon dioxide at night to conserve water.
🍃 Photosynthesis impacts global oxygen and carbon cycles profoundly.
"""
        },
        "Quiz": {
            "Easy": """
1. What do plants need for photosynthesis?  
A) Sunlight  
B) Water  
C) Air  
D) All of the above  
Answer: D  

2. What gas do plants produce?  
A) Carbon dioxide  
B) Oxygen  
C) Nitrogen  
D) Hydrogen  
Answer: B  
""",
            "Medium": """
1. Which organelle performs photosynthesis?  
A) Mitochondria  
B) Chloroplast  
C) Nucleus  
D) Ribosome  
Answer: B  

2. What is the chemical formula for photosynthesis?  
A) 6CO₂ + 6H₂O → C₆H₁₂O₆ + 6O₂  
B) C₆H₁₂O₆ + 6O₂ → 6CO₂ + 6H₂O  
C) 2H₂ + O₂ → 2H₂O  
D) None of the above  
Answer: A  
""",
            "Hard": """
1. What is the primary function of Photosystem II?  
A) Absorb light and split water molecules  
B) Produce glucose  
C) Fix carbon dioxide in Calvin cycle  
D) Generate ATP synthase  
Answer: A  

2. Where does the Calvin cycle occur?  
A) Thylakoid membrane  
B) Stroma of chloroplast  
C) Cytoplasm  
D) Mitochondria  
Answer: B  
"""
        }
    }

    return dummy_outputs.get(content_type, {}).get(difficulty, "No data available for this difficulty.")

# --- Quiz parsing and UI ---
def parse_quiz(raw_text):
    pattern = r"(\d+)\.\s*(.*?)\n((?:[A-D]\).*\n){4})Answer:\s*([A-D])"
    matches = re.findall(pattern, raw_text, re.MULTILINE)
    questions = []
    for num, question, options, answer in matches:
        opts = options.strip().split('\n')
        questions.append({
            "number": num,
            "question": question.strip(),
            "options": [o[3:].strip() for o in opts],  # Remove 'A) ' etc.
            "answer": answer
        })
    return questions

# --- Fun Facts UI with styling and interaction ---
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

# --- Main UI logic ---
if content_type == "Quiz":
    st.header("🔎 Quiz Generator with Review & Export")

    if st.button("🎯 Generate Raw Quiz"):
        raw_quiz = ai_generate("Quiz", difficulty)
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
    prompts = {
        "Lesson Plan": "Lesson Plan",
        "Study Notes": "Study Notes",
        "Glossary Terms": "Glossary Terms"
    }
    prompt = prompts[content_type]

    st.header(f"📝 {content_type} Generator")

    default_prompts = {
        "Lesson Plan": "Create a lesson plan for teaching photosynthesis to Grade 7 students. Include objectives, materials, and activities.",
        "Study Notes": "Summarize photosynthesis for Grade 7 students using bullet points.",
        "Glossary Terms": "Define key terms related to photosynthesis for Grade 7 students (e.g., chlorophyll, carbon dioxide)."
    }

    user_prompt = st.text_area(f"{content_type} Prompt", value=default_prompts[content_type], height=150)

    if st.button(f"Generate {content_type}"):
        generated_content = ai_generate(content_type, difficulty)
        st.text_area(f"Generated {content_type}", generated_content, height=300)

        st.download_button(
            f"Download {content_type} as TXT",
            generated_content,
            file_name=f"{content_type.lower().replace(' ', '_')}.txt",
            mime="text/plain"
        )
