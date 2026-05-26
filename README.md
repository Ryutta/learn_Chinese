# Local Learning App

This is a local, personal Streamlit app that allows you to easily view your saved educational content (videos and scripts) in one place.

## How to use

1. **Install requirements:**
   You will need Python and Streamlit installed.
   ```bash
   pip install streamlit
   ```

2. **Add your content:**
   Place your lessons inside the `data/` folder. Create a new folder for each lesson. For example:
   ```
   data/
   ├── Lesson 1/
   │   ├── video.mp4
   │   └── script.txt
   ├── Lesson 2/
   │   ├── lesson2.mp4
   │   └── notes.md
   ```

   - Supported video formats: `.mp4`, `.webm`, `.ogg`
   - Supported script/notes formats: `.txt`, `.md`

3. **Run the app:**
   Start the Streamlit app from your terminal:
   ```bash
   streamlit run app.py
   ```
   The app will automatically open in your web browser. Use the sidebar to select a lesson.
