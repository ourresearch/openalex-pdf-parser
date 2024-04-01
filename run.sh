docker stop openalex-pdf-parser && docker rm openalex-pdf-parser
docker run -p 0.0.0.0:80:5000 --detach --env-file ./.env --log-opt max-size=5g --name openalex-pdf-parser openalex-pdf-parser