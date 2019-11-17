FROM python:alpine 

LABEL maintainer="dpeng1@gmail.com"

# run update
RUN apk update

# install git
RUN apk add --no-cache coreutils git openssh openrc supervisor curl

# openssh conf
RUN echo "Port 2222" >> /etc/ssh/sshd_config && \
echo "PermitRootLogin yes" >> /etc/ssh/sshd_config && \
/usr/bin/ssh-keygen -A && \
echo "root:Docker!" | /usr/sbin/chpasswd

# install dropzone
RUN pip install flask Flask-Dropzone
COPY src /app

# add configs and scripts
ADD conf/supervisord.conf /etc/supervisord.conf
ADD scripts/start.sh /start.sh
RUN chmod 755 /start.sh

EXPOSE 5000 2222

CMD ["/start.sh"]
