# Dashi3
Dashiboard 


# For those getting a connection error with Microsoft SQL, check the version that it's running on. For SQL2012 the server could still be running on TLS1.0 or 1.1 instead of 1.2 
# the new minimum version. To resolve this go, once inside the container bash, update /etc/ssl/openssl.cnf to use tls 1.0
# The setting should be at the bottom of the config
