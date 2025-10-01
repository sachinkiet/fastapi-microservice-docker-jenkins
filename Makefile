PY_SERVICES = user_service task_service

.PHONY: lint format test

lint:
	@for srv in $(PY_SERVICES); do \
	  echo "🔍 Linting $$srv..."; \
	  docker run --rm -v $(PWD):/app -w /app python:3.11 bash -c "\
	    pip install pylint && \
	    pylint --disable=duplicate-code,R0903,C0114,C0115,C0116 $$srv \
	  "; \
	done

format:
	@for srv in $(PY_SERVICES); do \
	  echo "✨ Checking code format in $$srv..."; \
	  docker run --rm -v $(PWD):/app -w /app python:3.11 bash -c "\
	    pip install black && \
	    black --check $$srv \
	  "; \
	done

test:
	@for srv in $(PY_SERVICES); do \
	  echo "🧪 Running tests for $$srv..."; \
	  docker run --rm -v $(PWD):/app -w /app python:3.11 bash -c "\
	    pip install -r $$srv/requirements.txt && \
	    pytest $$srv/tests -v \
	  "; \
	done