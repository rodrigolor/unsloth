# Copyright 2023-present, the unsloth authors.
# Licensed under the Apache License, Version 2.0

from setuptools import setup, find_packages
import os

# Read the README for the long description
def read_readme():
    readme_path = os.path.join(os.path.dirname(__file__), "README.md")
    if os.path.exists(readme_path):
        with open(readme_path, "r", encoding="utf-8") as f:
            return f.read()
    return ""

# Core dependencies
INSTALL_REQUIRES = [
    "torch>=2.1.0",
    "transformers>=4.38.0",
    "datasets>=2.16.0",
    "sentencepiece>=0.1.99",
    "tqdm>=4.66.1",
    "psutil",
    "wheel>=0.42.0",
    "packaging>=23.1",
    "tyro>=0.7.2",
]

# Optional dependencies
EXTRAS_REQUIRE = {
    "huggingface": [
        "hf_transfer>=0.1.4",
        "huggingface_hub>=0.20.1",
    ],
    "training": [
        "trl>=0.7.9",
        "peft>=0.8.0",
        "accelerate>=0.26.1",
        "bitsandbytes>=0.42.0",
        "xformers>=0.0.23.post1",
    ],
    "dev": [
        "pytest>=7.4.0",
        "pytest-cov>=4.1.0",
        "black>=23.12.0",
        "isort>=5.13.0",
        "flake8>=6.1.0",
    ],
}

# Combine all optional deps under 'all'
EXTRAS_REQUIRE["all"] = [
    dep
    for group in ["huggingface", "training"]
    for dep in EXTRAS_REQUIRE[group]
]

setup(
    name="unsloth",
    version="2024.1.0",
    author="unsloth contributors",
    author_email="",
    description="2x faster, 60% less memory LLM finetuning",
    long_description=read_readme(),
    long_description_content_type="text/markdown",
    url="https://github.com/unslothai/unsloth",
    project_urls={
        "Bug Tracker": "https://github.com/unslothai/unsloth/issues",
        "Documentation": "https://github.com/unslothai/unsloth#readme",
    },
    packages=find_packages(exclude=["tests*", "docs*", "examples*"]),
    python_requires=">=3.8",
    install_requires=INSTALL_REQUIRES,
    extras_require=EXTRAS_REQUIRE,
    classifiers=[
        "Development Status :: 4 - Beta",
        "Intended Audience :: Developers",
        "Intended Audience :: Science/Research",
        "License :: OSI Approved :: Apache Software License",
        "Programming Language :: Python :: 3",
        "Programming Language :: Python :: 3.8",
        "Programming Language :: Python :: 3.9",
        "Programming Language :: Python :: 3.10",
        "Programming Language :: Python :: "Topic",
        "Operating=[
        "llora",
        "ers",
        "huggingface",
        "efficient training",
    ],
    include_package_data=True,
    zip_safe=False,
)
