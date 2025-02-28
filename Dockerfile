FROM busybox

COPY ./www /www

RUN chmod -R 755 /www && chmod +x /www/cgi-bin/*

EXPOSE 80

CMD [ "/bin/httpd","-f", "-p", "80", "-h", "/www", "-c", "/www/cgi-bin" ]
 
