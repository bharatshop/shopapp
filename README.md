## audio support prerequisites
sudo apt-get update
sudo apt-get install ffmpeg

## streamlit_audio_recorder on codespaces
cd streamlit_audio_recorder
streamlit run st_app_main.py --server.enableCORS false --server.enableXsrfProtection false