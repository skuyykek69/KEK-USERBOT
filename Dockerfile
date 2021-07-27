# Using Python Slim-Buster
FROM xluxz/geezproject:buster
# Lah U cp Atur atur
# Geez-UserBot
#
RUN git clone -b KEK-Userbot https://github.com/skuyykek69/KEK-Userbot /root/userbot
RUN mkdir /root/userbot/.bin
RUN pip install --upgrade pip setuptools
WORKDIR /root/userbot

#Install python requirements
RUN pip3 install -r https://raw.githubusercontent.com/skuyykek69/KEK-Userbot/KEK-Userbot/requirements.txt

EXPOSE 80 443

# Finalization
CMD ["python3","-m","userbot"]
