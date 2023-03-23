# shopapp

## create virtual environment
```properties
python3 -m venv .venv
source .venv/bin/activate
```

## Run the streamlit app
```properties
cd streamlit_audio_recorder
streamlit run st_app_main.py #( or streamlit run st_app_main.py --server.enableCORS false --server.enableXsrfProtection false if running on codespaces)
```


The app should be access on localhost:8501
