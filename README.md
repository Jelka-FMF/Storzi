# Storži

Repository of patterns running on Jelka FMF.

> [!TIP]
> [Navodila so na voljo tudi v slovenskem jeziku.](https://github.com/Jelka-FMF/Storzi/blob/main/README.sl.md)

## About

This repository contains all patterns that are running on [Jelka FMF](https://jelka.fmf.uni-lj.si/).

The patterns can be found in the `patterns` directory. Each pattern is in a separate
directory and can be written in most programming languages that support outputting
to the standard output and can be run in a Docker container.

All patterns from the repository are automatically compiled and deployed to the
Jelkob server and will be running on the official Christmas tree at the Faculty
of Mathematics and Physics, University of Ljubljana.

## Contributing

> [!TIP]
> If you do not know how to use Git/GitHub or cannot follow these instructions
> for any other reason, you can instead check out [Jelkly](https://jelkly.fmf.uni-lj.si/docs).
> It provides Scratch-like visual programming tool for creating and submitting
> your own Jelka FMF patterns, without requiring any programming knowledge.

### General Information

All patterns are stored in the `patterns` directory.

Each pattern is contained in a separate directory that contains `config.yml` and
`main.*` files, and optionally a `Dockerfile`.

The directory name is used as a pattern ID. It should be similar to the pattern
name and should represent what the pattern does. The directory name should only
contain lowercase letters, numbers and hyphens.

The `config.yml` file contains the configuration of the pattern. It provides basic
information about the pattern, such as the name, description, author and school.

The name should be a short, descriptive and unique name of the pattern, and the
description should explain what your pattern does in a short sentence.

The `main.*` file is the main file of the pattern, which is executed when the
pattern is started.

If you are writing a pattern in one of the languages that we provide a template for,
the language will be automatically detected based on the file extension.

If you are writing a pattern in a language that we do not provide a template for,
you will also have to write a custom `Dockerfile` that will be used to compile
and run the pattern. When started, the `Dockerfile` should run the pattern and
pipe its output to `/tmp/jelka`. You can read more about developing patterns
without a library [below](#patterns-in-other-languages).

If you are writing a pattern in a language that we provide a template for, you can
still write a custom `Dockerfile` if you need additional configuration, but it is
recommended to use the default template if possible.

### Adding a Pattern

If you do not have Git and GitHub already set up, you can read the official
documentation about configuring Git [here](https://docs.github.com/en/get-started/getting-started-with-git/set-up-git).

First, fork the repository on GitHub as documented [here](https://docs.github.com/en/pull-requests/collaborating-with-pull-requests/working-with-forks/fork-a-repo).

Then, and clone it to your computer:

```bash
git clone https://github.com/YOUR-GITHUB-USERNAME/Storzi.git
cd Storzi
```

Once you are in the repository, create a Python virtual environment (venv):

```bash
python -m venv venv
```

You can then activate a virtual environment:

```bash
venv\Scripts\activate # On Windows
```

```bash
source venv/bin/activate # On Linux and macOS
```

If you are using editor like Visual Studio Code or PyCharm, you may instead
create and activate your virtual environment using editor functionalities.

Then, install the required dependencies:

```bash
pip install -r requirements.txt
```

To add a new pattern, create a new directory in the `patterns` directory, and add
the `config.yml` and `main.*` files. Check the above section for general information
about the files, and the language-specific sections below.

After you have added the pattern (and formatted it properly), commit your changes:

```bash
git add patterns/your-pattern-name
git commit -m "Your commit message"
```

You can then push your changes:

```bash
git push
```

Then, you can submit a pull request (PR) through the GitHub interface.

### Python Patterns

When writing a Python pattern, you should install the recommended libraries from
the `requirements.txt` file in the root of the repository:

```bash
pip install -r requirements.txt
```

This will install all available libraries that can be used in Python patterns, in
addition to the simulation for running the patterns locally, and development tools.

Your pattern can use the [Jelka Python API](https://github.com/Jelka-FMF/JelkaPy),
as well as other available libraries (see below).

The main pattern filename must be `main.py`.

You can check [an example Python pattern](patterns/example-python/) for a template.
You can also check existing Python patterns as an inspiration.

While developing your pattern, you can run it locally using the simulation:

```bash
jelkasim patterns/your-pattern-name/main.py
```

Before commiting your pattern, please make sure it is properly formatted:

```bash
ruff check patterns/your-pattern-name
ruff format patterns/your-pattern-name
```

### JavaScript Patterns

When writing a JavaScript pattern, you should install the recommended libraries from
the `package.json` file in the root of the repository:

```bash
npm install
```

This will install all available libraries that can be used in JavaScript patterns,
in addition to development tools.

You should still install Python dependencies as specified in the above section,
as they are used for running the simulation.

Your pattern can use the [Jelka JavaScript API](https://github.com/Jelka-FMF/JelkaJS),
as well as other available libraries (see below).

The main pattern filename must be `main.js`.

You can check [an example JavaScript pattern](patterns/example-javascript/) for a template.
You can also check existing JavaScript patterns as an inspiration.

While developing your pattern, you can run it locally using the simulation:

```bash
jelkasim node patterns/your-pattern-name/main.js
```

Before commiting your pattern, please make sure it is properly formatted:

```bash
npm run format patterns/your-pattern-name
```

### Patterns in Other Languages

If you are writing a pattern in a language that we do not provide a template for,
you will also have to write a custom `Dockerfile` that will be used to compile
and run the pattern. When started, the `Dockerfile` should run your pattern.

To develop the pattern and run the simulation, you will still have to install
Python dependencies as specified in the above section.

Docker containers automatically mount the `/tmp/jelka` pipe. Your pattern should
either write data directly to the pipe, or write it to the standard output and
redirect it to the `/tmp/jelka` pipe.

The first line should be a header that specifies the pattern properties:

```
#{"version": 0, "led_count": 1000, "fps": 60}\n
```

Then, for each frame, the pattern should write color data in the following format:

```
#<color in hex><next color in hex> ... <last color in hex>\n
```

Key guidelines for color representation:

* Each frame is represented by a separate line.
* Colors must be written using HEX digits only (for example, white is `ffffff`, not `#ffffff`).
* The line must start with `#` and end with a newline character, and must not contain `#` elsewhere.
* Lines not starting with `#` are treated as comments and are ignored.

Important notes:

* Hardware-limited framerate is 66 frames per second, so do not expect more than 60 frames per second.
* Many languages will not flush output automatically, so you may need to implement manual flushing.

The runner and the simulation set the `JELKA_POSITIONS` environment variable to
a path to a CSV file with light positions. Each line contains a light ID, and
the XYZ position of a light. If you are not using an official library, you will
need to manually load the correct file and parse its positions if you need them.
If you are using an official library, this will be handled automatically.

An example CSV file with positions is provided in the [`data/positions.csv`](data/positions.csv)
in this repository.

### Guidelines

* Patterns should be written in a way that they can be run in a Docker container.
* Patterns should output to the standard output (which is piped into `/tmp/jelka`).
* Patterns should not display inappropriate content.

## Templates

### Python

* Base image: [`images/python`](images/python)
* Default template: [`defaults/python`](defaults/python)
* Available libraries: [`requirements.in`](images/python/requirements.in)
* Pattern filename: `main.py`

### JavaScript

* Base image: [`images/javascript`](images/javascript)
* Default template: [`defaults/javascript`](defaults/javascript)
* Available libraries: [`package.json`](images/javascript/package.json)
* Pattern filename: `main.js`

# OCaml

* Base image: [`images/ocaml`](images/ocaml)
* Default template: [`defaults/ocaml`](defaults/ocaml)
* Available libraries: *None*
* Pattern filename: `main.ml`

## Structure

* `patterns/` - Directory containing all patterns
  * `pattern-name/`
    * `config.yml` - Configuration file for the pattern
    * `main.*` - Main file of the pattern

* `defaults/` - Default Docker templates for patterns
  * `javascript/` - Default Docker template for JavaScript patterns
  * `python/` - Default Docker template for Python patterns

* `images/` - Base Docker images for patterns
  * `javascript/` - Base Docker image for JavaScript patterns
  * `python/` - Base Docker image for Python patterns

## License

By contributing to this repository, you agree to license your work under the MIT license.
