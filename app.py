import streamlit as st
import os

# --- Configurations ---
DATA_DIR = "data"
st.set_page_config(page_title="Local Learning App", page_icon="📚", layout="wide")

st.title("📚 My Local Learning App")

# Ensure data directory exists
if not os.path.exists(DATA_DIR):
    os.makedirs(DATA_DIR)
    st.warning(f"Data directory '{DATA_DIR}' was not found. I created one for you. Please add your lesson folders there.")

# Get list of lesson folders
def get_lessons():
    if not os.path.exists(DATA_DIR):
        return []
    folders = [f for f in os.listdir(DATA_DIR) if os.path.isdir(os.path.join(DATA_DIR, f))]
    return sorted(folders)

lessons = get_lessons()

if not lessons:
    st.info("No lessons found. Please add folders inside the `data/` directory. Each folder should contain a video file (e.g., .mp4) and a script file (e.g., .txt).")
else:
    # Sidebar for navigation
    st.sidebar.header("Navigation")
    selected_lesson = st.sidebar.selectbox("Select a Lesson", lessons)

    if selected_lesson:
        st.header(f"📖 {selected_lesson}")

        lesson_path = os.path.join(DATA_DIR, selected_lesson)
        files = os.listdir(lesson_path)

        # Find video and text files
        video_files = [f for f in files if f.endswith(('.mp4', '.webm', '.ogg'))]
        text_files = [f for f in files if f.endswith(('.txt', '.md'))]

        # Display Video
        if video_files:
            video_path = os.path.join(lesson_path, video_files[0])
            st.subheader("Video")
            try:
                st.video(video_path)
            except Exception as e:
                st.error(f"Error loading video: {e}")
        else:
            st.warning("No video file (.mp4, .webm, .ogg) found in this lesson folder.")

        st.divider()

        # Display Script
        if text_files:
            text_path = os.path.join(lesson_path, text_files[0])
            st.subheader("Script / Notes")
            try:
                with open(text_path, 'r', encoding='utf-8') as text_file:
                    content = text_file.read()
                st.markdown(content)
            except Exception as e:
                st.error(f"Error reading script file: {e}")
        else:
            st.warning("No script file (.txt, .md) found in this lesson folder.")
