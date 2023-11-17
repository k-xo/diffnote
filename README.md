# DiffNote

## Overview
DiffNote is a CLI tool designed to generate commit messages automatically based on Git diffs. Utilizing the power of OpenAI's GPT-4, it analyzes your code changes and suggests relevant commit messages, adhering to the Conventional Commits standard.

## Installation

To install DiffNote, ensure you have Python installed on your system. Then, run the following command:

```shell 
pip install diffnote
```

## Configuration

Before using DiffNote, set your OpenAI API key in your environment variables:
```shell 
export OPENAI_API_KEY='your_api_key_here'
```


## Usage

To use DiffNote, simply run the following command in your Git repository: ```diffnote```


DiffNote will generate a commit message based on the current Git diff and automatically commit the changes.

## Features

- **Automatic Commit Messages**: Generates commit messages based on Git diffs.
- **Conventional Commits Standard**: Follows the guidelines of Conventional Commits for message formatting.
- **Easy Integration**: Seamlessly integrates into your existing Git workflow.



