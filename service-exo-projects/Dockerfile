FROM alpine:3.10 as service-exo-projects

LABEL maintainer="Ernesto Serrano <ernesto@exolever.com>"

WORKDIR /projects/service-exo-projects

ENV PYTHONUNBUFFERED=1 \
    LANG=en_US.UTF-8 \
    LC_ALL=en_US.UTF-8 \
    PIPENV_YES=1 \
    SERVICE_NAME=service-exo-projects

# Copying only Pipfile (best with latest versions) to  ptimize docker layer cache build
COPY Pipfile .

# Adding temporary packages, pip installing and cleaning
RUN apk add --no-cache \
        curl \
        python3 \
        py3-openssl \
        py3-cffi \
        py3-cryptography \
        py3-requests \
        py3-psycopg2 \
        postgresql-client \
        ipython \
        libc-dev \
    && \
    apk add --no-cache --virtual .build-deps  \
        git \
        build-base \
        python3-dev \
        libffi-dev \
        curl-dev \
        postgresql-dev \
        zlib-dev \
    && \
    pip3 install pipenv \
    && \
        pip3 install "django<3.0" \
    && \
    pipenv  install --system  --skip-lock \
    && \
    apk del .build-deps --force-broken-world \
    && \
    find /usr/local -depth \
        \( \
            \( -type d -a \( -name test -o -name tests \) \) \
            -o \
            \( -type f -a \( -name '*.pyc' -o -name '*.pyo' \) \) \
        \) -exec rm -rf '{}' + \
    && rm -rf /usr/src/python \
    && rm -rf /root/.cache


# Example of edge alpine install
# apk add --no-cache -X http://dl-cdn.alpinelinux.org/alpine/edge/community ipython \


# Check packages #TODO when this bug will be fixed https://github.com/pypa/pipenv/issues/2783
# RUN pipenv check --system

# Show package versions
RUN pip3 freeze

# Copying rest of files
COPY . .

# Running basic check of django
RUN python3 manage.py check

EXPOSE 8000

CMD sh -f run.sh


ARG SOURCE_BRANCH
ARG SOURCE_TAG
ARG SOURCE_NAME

ENV SOURCE_NAME=$SOURCE_NAME \
    SOURCE_BRANCH=${SOURCE_BRANCH} \
    SOURCE_TAG=${SOURCE_TAG} \
    REDIS_HOST=redis \
    DB_NAME=service_exo_projects \
    DB_USER=exolever \
    DB_PASS=exolever \
    DB_HOST=postgres \
    PIP_DISABLE_PIP_VERSION_CHECK=on \
    VIMEO_TOKEN=540ca8a178c5886adcef9b8b87a1b4b6 \
    VIMEO_CLIENT_ID=22124d0fd1956a2eadfa8cfedaa646683a41aa26 \
    VIMEO_CLIENT_SECRET="86IF4reGKn8vvu4BmlC/GRwsxQRhnwOF6UQWeCvYe++iB8HNIP/B0b3DJtmkwbikVAFVQB+KExK/Fwe+Dd/V063nue5jGAC0aM1AF4ftl9sPP8Bga/PFMdkq402rnRDz" \
    YOUTUBE_API_KEY=AIzaSyCnhi5jTAYiE8tVq91399422GvbxFS8H3Y \
    FILESTACK_KEY=AvvsSOUhSNGp7ybufZ6lbz
