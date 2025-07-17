# Simple RNN Sequence Predictor

A Streamlit web app that uses a trained RNN model to predict the next number in a sequence.

## How to Use

1. Clone this repository:
```bash
git clone https://github.com/yourusername/rnn_sequence_predictor.git
cd rnn_sequence_predictor
```

2. Install requirements:
```bash
pip install -r requirements.txt
```

3. Place `simple_rnn_model.h5` in the same directory.

4. Run the app:
```bash
streamlit run app.py
```

## Deployment

To deploy on [Streamlit Cloud](https://streamlit.io/cloud):
- Upload all files to a GitHub repo.
- Create a new app on Streamlit Cloud from that repo.
- It will auto-install from `requirements.txt` and run `app.py`.