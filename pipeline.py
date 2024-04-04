docker run -it 
    -e POSTGRES_USER="root" 
    -e POSTGRES_PASSWORD="root" 
    -e POSTGRES_DB="ny_taxi" 
    -v /workspaces/challenge1/ny_taxi_postgres_data:/var/lib/postgresql/data 
    -p 5433:5432 
    postgres:13


pgcli -h localhost -p 5433 -u root -d ny_taxi