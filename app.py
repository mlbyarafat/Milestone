from flask import Flask, render_template, request, redirect, url_for, session
import os, json, datetime

app = Flask(__name__)
app.secret_key = "supersecret"

# Load languages
LANG_DIR = os.path.join(app.root_path, 'lang')
LANGS = {}
for fname in os.listdir(LANG_DIR):
    if fname.endswith('.json'):
        code = fname.split('.')[0]
        with open(os.path.join(LANG_DIR, fname), encoding='utf-8') as f:
            LANGS[code] = json.load(f)

def get_lang():
    lang = session.get('lang','en')
    if lang not in LANGS: lang = 'en'
    return lang

@app.context_processor
def inject_globals():
    lang = get_lang()
    return dict(t=LANGS[lang], lang=lang, current_year=datetime.datetime.now().year)

@app.route('/set_language', methods=['POST'])
def set_language():
    lang = request.form.get('lang','en')
    session['lang'] = lang
    return redirect(request.referrer or url_for('index'))

@app.route('/')
def index(): return render_template('index.html')
@app.route('/courses')
def courses(): return render_template('course.html')
@app.route('/tutors')
def tutors(): return render_template('tutors.html')
@app.route('/library')
def library(): return render_template('library.html')
@app.route('/stories')
def stories(): return render_template('stories.html')
@app.route('/skills')
def skills(): return render_template('skills.html')
@app.route('/mental')
def mental(): return render_template('mental.html')
@app.route('/quiz')
def quiz(): return render_template('quiz.html')


# --- Auto-added content routes ---
@app.route('/course_python')
def course_python():
    return render_template('course_python.html')

@app.route('/course_webdev')
def course_webdev():
    return render_template('course_webdev.html')

@app.route('/course_datasci')
def course_datasci():
    return render_template('course_datasci.html')

@app.route('/course_ai')
def course_ai():
    return render_template('course_ai.html')

@app.route('/lib_python_ebook')
def lib_python_ebook():
    return render_template('lib_python_ebook.html')

@app.route('/lib_web_cheatsheet')
def lib_web_cheatsheet():
    return render_template('lib_web_cheatsheet.html')

@app.route('/lib_datasci_notes')
def lib_datasci_notes():
    return render_template('lib_datasci_notes.html')

@app.route('/mental_meditation')
def mental_meditation():
    return render_template('mental_meditation.html')

@app.route('/mental_time')
def mental_time():
    return render_template('mental_time_management.html')

@app.route('/quiz_python_detail')
def quiz_python_detail():
    return render_template('quiz_python_detail.html')

@app.route('/quiz_web_detail')
def quiz_web_detail():
    return render_template('quiz_web_detail.html')

@app.route('/skill_python_challenges')
def skill_python_challenges():
    return render_template('skill_python_challenges.html')

@app.route('/skill_frontend_exercises')
def skill_frontend_exercises():
    return render_template('skill_frontend_exercises.html')

@app.route('/story_zero')
def story_zero():
    return render_template('story_zero_to_hero.html')

@app.route('/story_build')
def story_build():
    return render_template('story_building_website.html')

@app.route('/tutor_john')
def tutor_john():
    return render_template('tutor_john_doe.html')

@app.route('/tutor_jane')
def tutor_jane():
    return render_template('tutor_jane_smith.html')

@app.route('/cart')
def cart(): return "Cart page"
@app.route('/login')
def login(): return "Login page"

if __name__ == "__main__":
    app.run(debug=True)
