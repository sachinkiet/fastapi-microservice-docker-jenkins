PY_SERVICES = user_service task_service

.PHONY: lint format test

lint:
	@for srv in $(PY_SERVICES); do \
		echo "🔍 Linting $$srv..."; \
		docker run --rm -v $$PWD:/app -w /app/$$srv python:3.11 bash -c "\
			pip install --no-cache-dir -r requirements.txt && \
			pip install pylint && \
			pylint $$(find . -name '*.py')"; \
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