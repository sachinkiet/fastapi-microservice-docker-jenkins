# Variables
DOCKER_REGISTRY ?= sachinkiet
DOCKER_TAG ?= latest

PY_SERVICES = user_service task_service

.PHONY: lint format test docker-build docker-push docker-deploy all ci

# Install dependencies
install:
	pip install -r requirements.txt

# Lint using the prebuilt Docker image
lint:
	@for srv in $(PY_SERVICES); do \
		docker run --rm -v $$PWD:/app -w /app/$$srv $(DOCKER_REGISTRY)/$$srv:$(DOCKER_TAG) sh -c "pip install pylint && pylint --disable=duplicate-code,R0903,C0114,C0115,C0116 ."; \
	done

# Check formatting using black
format:
	@for srv in $(PY_SERVICES); do \
		docker run --rm -v $$PWD:/app -w /app/$$srv $(DOCKER_REGISTRY)/$$srv:$(DOCKER_TAG) sh -c "pip install black && black --check ."; \
	done

# Run pytest
test:
	@for srv in $(PY_SERVICES); do \
		docker run --rm -v $$PWD:/app -w /app/$$srv $(DOCKER_REGISTRY)/$$srv:$(DOCKER_TAG) sh -c "pytest tests -v"; \
	done

# Build Docker images
docker-build:
	@for srv in $(PY_SERVICES); do \
		docker build -t $(DOCKER_REGISTRY)/$$srv:$(DOCKER_TAG) ./$$srv ; \
	done

# Push Docker images
docker-push:
	@for srv in $(PY_SERVICES); do \
		docker push $(DOCKER_REGISTRY)/$$srv:$(DOCKER_TAG) ; \
	done

# Deploy with docker-compose
docker-deploy:
	@docker compose down || true
	@docker compose up -d --pull always

# Run all checks
all: lint format test

# Full CI pipeline
# ci: lint format test docker-build docker-push