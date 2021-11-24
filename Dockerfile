FROM python:3.9-buster

# install nginx
RUN apt-get update && apt-get install nginx vim -y --no-install-recommends
COPY nginx.default /etc/nginx/sites-available/default
RUN ln -sf /dev/stdout /var/log/nginx/access.log \
    && ln -sf /dev/stderr /var/log/nginx/error.log

#Install the ODBC driver into the docker instance
# install Microsoft SQL Server requirements.
ENV ACCEPT_EULA=Y
RUN apt-get install curl
RUN apt-get install apt-transport-https
RUN apt-get install nano

# Add SQL Server ODBC Driver 17 for Ubuntu 20
RUN curl https://packages.microsoft.com/keys/microsoft.asc | apt-key add -
RUN curl https://packages.microsoft.com/config/ubuntu/20.04/prod.list > /etc/apt/sources.list.d/mssql-release.list
RUN apt-get update
RUN ACCEPT_EULA=Y apt-get install -y --allow-unauthenticated msodbcsql17
RUN ACCEPT_EULA=Y apt-get install -y --allow-unauthenticated mssql-tools
RUN echo 'export PATH="$PATH:/opt/mssql-tools/bin"' >> ~/.bash_profile
RUN echo 'export PATH="$PATH:/opt/mssql-tools/bin"' >> ~/.bashrc
RUN apt-get -y install unixodbc-dev


# copy source and install dependencies
#forgot to add dashikombu as an app omg!!!! 5hrs in
RUN mkdir -p /opt/app
RUN mkdir -p /opt/app/pip_cache
RUN mkdir -p /opt/app/Dashi3
RUN mkdir -p /opt/app/static
COPY requirements.txt start-server.sh /opt/app/
COPY .pip_cache /opt/app/pip_cache/
COPY Dashi3 /opt/app/Dashi3/
COPY dashikombu /opt/app/dashikombu
COPY static /opt/app/static
WORKDIR /opt/app

RUN apt-get update && apt-get install -y --no-install-recommends \
    unixodbc-dev \
    unixodbc \
    libpq-dev 
RUN pip install -r requirements.txt --cache-dir /opt/app/pip_cache
RUN chown -R www-data:www-data /opt/app




# start server
EXPOSE 8020
EXPOSE 1443
STOPSIGNAL SIGTERM
CMD ["/opt/app/start-server.sh"]


#Need up update conf file to allow tls1.0 
#https://stackoverflow.com/questions/57265913/error-tcp-provider-error-code-0x2746-during-the-sql-setup-in-linux-through-te/57453901#57453901

