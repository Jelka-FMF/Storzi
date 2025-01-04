FROM ocaml/opam:alpine-ocaml-5.2

# Set working directory
WORKDIR /app

# Copy the entrypoint script
COPY entrypoint.sh .

# Run the entrypoint script
CMD ["/bin/sh", "entrypoint.sh"]
