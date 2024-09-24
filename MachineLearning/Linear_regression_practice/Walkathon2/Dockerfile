
FROM --platform=linux/amd64 python:3.9-slim

WORKDIR /app

COPY . /app

RUN pip install --no-cache-dir -r requirments.txt

# EXPOSE $PORT

CMD exec uvicorn model_app:app --port=$PORT --host=0.0.0.0 

# Docket build command
# docker build  -t fapi:vi

#  Docker run command
# docker run -p 80:80 fapi-lr:v1


# tag the build to push into dockerhub
# docker tag fapi-lr:v1 balamurugande/fapi-lr:v1

# pushing to dockerhub
# docker push balamurugande/fapi-lr:v1
