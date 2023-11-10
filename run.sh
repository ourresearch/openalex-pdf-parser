docker stop openalex-pdf-parser && docker rm openalex-pdf-parser
docker run -p 0.0.0.0:80:5000 --detach --env-file ./.env --name openalex-pdf-parser openalex-pdf-parser