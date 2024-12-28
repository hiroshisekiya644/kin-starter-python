# kin-starter-python

## About

This project is a simple demo of how to use the [kin-python](https://github.com/kinecosystem/kin-python) SDK.

## Requirements

- Basic Python knowledge
- Python 3.6, 3.7 or 3.8
- Pip
- Docker (optional)

## Running this project

### 1. Clone the repo

```shell
git clone https://github.com/ledgerluminary55/kin-starter-python
cd kin-starter-python
```

### 2. Install the dependencies

```shell
pip install -r ./requirements.txt
```

### 3. Run the demo

```shell
python main.py
```

## Docker

You can also run this project inside a Docker container:

```shell
make docker-build
make docker-run
```

## What's next?

You can read the [Getting Started - Python](https://kintegrate.dev/tutorials/getting-started-python-sdk) to read how you can integrate the `kin-python` SDK in your own apps.

If you have questions or want to talk about how to integrate Kin, please join our [discord channel](https://discord.gg/kdRyUNmHDn).
