docker run --name my_postgres -e POSTGRES_PASSWORD=114514 -e POSTGRES_DB=fs -p 5432:5432 -v postgresql_data:/var/lib/postgresql/data --memory="2gb"  -d postgres
