# diffnote

## Overview
diffnote is a CLI tool designed to generate commit messages automatically based on Git diffs. using a gpt assistant it analyzes your code changes and suggests relevant commit messages, that adhere to the conventional commit spec

## Installation

To install diffnote, ensure you have Python installed on your system. Then, run the following command:

```shell 
pip install diffnote
```

## Configuration

Before using diffnote, set your OpenAI API key in your environment variables:
```shell 
export OPENAI_API_KEY='your_api_key_here'
```


## Usage

To use diffnote, simply run the following command in your Git repository: ```diffnote```


diffnote will generate a commit message based on the current Git diff and automatically commit the changes.

## Features

- **Automatic Commit Messages**: Generates commit messages based on Git diffs.
- **Conventional Commits Standard**: Follows the guidelines of Conventional Commits for message formatting.
- **Easy Integration**: Seamlessly integrates into your existing Git workflow.



