# howawrs-apitest
pyproject.toml
    [tool.poetry]
    name = "hogwart-apitest"
    version = "0.1.0"
    description = "API test framework with pytest and requests."
    
    [tool.poetry.dependencies]
    python = "^3.5"
    pytest = "5.0"
    requests = "^2.22"
    
    [tool.poetry.dev-dependencies]
    
    [build-system]
    requires = ["poetry>=0.12"]
    build-backend = "poetry.masonry.api"