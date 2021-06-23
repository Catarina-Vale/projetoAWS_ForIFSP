FROM public.ecr.aws/lambda/python:3.8

COPY app.py ./

RUN python3.8 -m pip install requests

RUN python3.8 -m pip install bs4


# Command can be overwritten by providing a different command in the template directly.
CMD ["app.lambda_handler"]
