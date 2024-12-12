import streamlit as st
from streamlit_lottie import st_lottie
import requests

# Find more emojis here: https://www.webfx.com/tools/emoji-cheat-sheet/
st.set_page_config(page_title="My Webpage", page_icon=":books:", layout="wide")

# Lottie animation function
def load_lottie_url(url: str):
    r = requests.get(url)
    if r.status_code != 200:
        return None
    return r.json()

# ---- HEADER SECTION ----
with st.container():
    st.subheader("Hi, I am Cariel Faith G. Alduheza  :wave:")
    st.title("A First Year Computer Engineering Student at SNSU")
    st.write("Today, I will teach you the techniques for studying harder and smarter, helping you unlock your full potential.")
st.title("Study Smart! 📚✨")
st.subheader("Supercharge Your Learning with These Fun Study Tips! 🚀")

# Lottie animation for welcome message
lottie_url = "https://assets3.lottiefiles.com/packages/lf20_o9x2ajqk.json"  # Lottie animation for study (you can replace this URL)
lottie_animation = load_lottie_url(lottie_url)
if lottie_animation:
    st_lottie(lottie_animation, speed=1, width=700, height=400, key="welcome")

# Introduction
st.markdown("""
Welcome to **Study Smart!** 🎉  
Learning doesn’t have to be boring or stressful. With the right techniques, you can make studying fun, exciting, and effective! Whether you're preparing for exams or just trying to learn something new, here are some simple and creative study tips that will make a big difference. Let’s get started and transform your study routine! 🌟
""")

# Tips Section with Creative Design

st.markdown("""
## 🎯 5 Fun & Easy Study Tips to Try

Studying isn’t just about reading books—it’s about making things stick in your mind and having fun with the process! Here are some creative techniques to help you study better:

### 1. 🗓️ **Make a Fun Study Schedule**

The first step to studying smart is planning your time. Try breaking your study time into small, manageable chunks with fun breaks in between. Use the **Pomodoro Technique**: study for 25 minutes, then take a 5-minute break to do something fun (like stretching, listening to music, or checking your phone). After four rounds, take a longer break of 15–30 minutes. It’s like a mini reward for your brain! 🎉

> **Tip**: Use a colorful calendar or an app like Google Calendar to visually organize your study time and track your progress. 

### 2. 🔄 **Test Yourself (It’s Like a Game!)**

Instead of just reading your notes, make studying a challenge! **Test yourself** by writing down what you remember or asking a friend to quiz you. Self-quizzing helps you remember better because you are actively recalling information. It’s like playing a memory game with your brain!

> **Pro Tip**: You can use flashcards (physical or apps like Anki) to practice key concepts and test yourself regularly.

> **Example**: If you're learning a new language, write the word in your native language on one side, and the translation on the other. Test yourself throughout the day!

### 3. 🖍️ **Use Colors & Doodles to Remember**

If you like visuals, you’re in luck! **Mind mapping** and **color coding** are fun ways to organize your notes and make them stick in your memory. Draw simple diagrams, use different colors for headings and subheadings, or add little doodles to represent concepts. For example, use a green pen for environmental topics, a red one for important points, and a blue one for definitions.

> **Creative Tip**: Create a “study wall” with your colorful notes and mind maps. This turns your study area into an inspiring space and allows you to visualize your learning.

> **Bonus**: Try using sticky notes to write key ideas and put them around your room for quick, visual reminders.

### 4. 🧘‍♂️ **Take Care of Your Body & Mind**

Did you know that your body and mind are connected? Taking care of yourself helps your brain work better. Make sure to get plenty of sleep, eat healthy foods, and stay hydrated. Also, don’t forget to move! Stretching, walking, or doing quick exercises can help you focus and refresh your mind.

> **Healthy Habit**: Try taking a 5-minute walk after every study session or doing light stretches to increase blood flow to your brain. A relaxed body leads to a sharp mind!

> **Mindfulness**: Practice deep breathing or short mindfulness sessions to calm your mind and improve concentration. Apps like Headspace or Calm can guide you through simple meditation exercises.

### 5. 👯 **Study with Friends**

Studying doesn’t have to be a solo activity! Sometimes, studying with friends can make learning more enjoyable. You can quiz each other, share notes, and help explain things in different ways. **Group study sessions** are great for brainstorming ideas and learning from others.

> **Group Tip**: Create a study group with friends and meet regularly (in person or online). Use platforms like Zoom or Google Meet if you're studying remotely.

> **Collaboration Tip**: Discuss topics with peers or online communities, such as forums or social media groups related to your subject. Talking about what you’re learning helps reinforce concepts!

---

## 🌟 Bonus Tips to Boost Your Learning

- **Stay Positive!** 💪  
  Your mindset matters. Stay confident in your abilities and remind yourself that mistakes are part of the learning process.
  
- **Break Down Complex Topics** 📚  
  Don't overwhelm yourself. Break big topics into smaller, manageable chunks. Focus on mastering one small part at a time.
  
- **Use Technology to Your Advantage** 💻  
  There are tons of apps that can help you study more effectively. Try using **Quizlet** for flashcards, **Trello** for organizing tasks, or **Evernote** for keeping digital notes.

## 💡 Conclusion

Learning doesn’t have to be hard or stressful. With the right study habits and a creative approach, you can make studying enjoyable and more effective. Whether you’re preparing for exams or learning a new skill, these tips will help you stay on track and have fun along the way. Keep experimenting with different techniques and find what works best for you! 🎯

Good luck with your studies, and remember: **Study Smart, Not Hard!** 🌟
""")


lottie_url_end = "https://assets8.lottiefiles.com/packages/lf20_rikjpqjf.json"  # Lottie animation for conclusion (can be replaced)
lottie_animation_end = load_lottie_url(lottie_url_end)
if lottie_animation_end:
    st_lottie(lottie_animation_end, speed=1, width=700, height=400, key="conclusion")

st.markdown("---")

st.markdown("""
**Thanks for reading!** 😊  
Let’s chat if you have any questions, want to share your study tips, or need motivation. Together, we can learn and grow! 📖💡
""")
