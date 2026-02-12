# Streamlit App Entry Point for Streamlit Cloud
import sys
import os
import runpy

# Get the app directory path
app_dir = os.path.join(os.path.dirname(os.path.abspath(__file__)), 'app')

# Add app directory to Python path so config.py and utils.py can be found
sys.path.insert(0, app_dir)

# Run app.py directly
runpy.run_path(os.path.join(app_dir, 'app.py'), run_name='__main__')