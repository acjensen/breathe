# Installation

1. Build the docker image.
`docker build -t breathe:breathe .`

2. Run the container.
`docker run -p 8080:8080 --name breathe --env PORT=8080 breathe:breathe`

3. Visit `http://localhost:8080/`.