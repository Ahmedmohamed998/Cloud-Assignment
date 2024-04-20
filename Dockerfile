FROM python
WORKDIR /app
COPY require.txt .
RUN pip install -r require.txt
RUN python -c "import nltk; nltk.download('stopwords'); nltk.download('punkt')"
COPY . /app/
COPY paragraphs.txt /app
CMD [ "python3", "app.py" ]
