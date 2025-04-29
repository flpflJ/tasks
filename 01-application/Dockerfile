FROM python:3.13-slim
RUN pip install uvicorn fastapi
ENV AUTHOR="Vsevolod Ursta"
WORKDIR /api
COPY simple_api.py .
EXPOSE 8000/tcp
CMD ["uvicorn", "simple_api:app", "--host", "0.0.0.0", "--port", "8000"]
