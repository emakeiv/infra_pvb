up:
	docker-compose \
		-f ./.docker/docker-compose.yaml \
		-f ./.docker/docker-compose.database.yaml \
		-f ./.docker/docker-compose.pgadmin.yaml \
		-f ./.docker/docker-compose.mlflow.yaml \
		-f ./.docker/docker-compose.minio.yaml \
		-f ./.docker/docker-compose.redis.yaml \
		-f ./.docker/docker-compose.nginx.yaml up --build -d

down:
	docker-compose \
		-f ./.docker/docker-compose.yaml \
		-f ./.docker/docker-compose.database.yaml \
		-f ./.docker/docker-compose.pgadmin.yaml \
		-f ./.docker/docker-compose.mlflow.yaml \
		-f ./.docker/docker-compose.minio.yaml \
		-f ./.docker/docker-compose.redis.yaml \
		-f ./.docker/docker-compose.nginx.yaml down -v
