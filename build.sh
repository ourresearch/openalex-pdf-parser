docker stop openalex-pdf-parser && docker rm openalex-pdf-parser
docker build -t openalex-pdf-parser .
docker run -p 0.0.0.0:80:5000 --detach --privileged --env-file ./.env --log-opt max-size=100m --name openalex-pdf-parser openalex-pdf-parser