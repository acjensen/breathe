# Installation

1. Build the docker image.
`docker build .`

2. Run the container.
`docker run -p 8080:8080 --name breathe --env PORT=8080 2b75e2568928`

3. Visit `http://localhost:8080/`.