# terminal_translater

This tool displays the solution (obtained from ChatGPT) to ERROR and WARNING messages displayed on the terminal.

## Description

We created our own command "showfix". You can create your own dictionary of favorite solutions, search history, and display solutions by adding options that suit your purpose. You can also easily customize it by adding your own options.

## Features

- Ease of use
- Ease of customization
- Original dictionaries can be used offline.

## Requirement

- Download this repository
- Addition of command "showfix"
  1. Add a path
  ```
  export PATH=$HOME/terminal_translater/command:$PATH
  ```
  2. Confirmation that the path has passed
  ```
  which showfix
  ```
- API Key Issuance for OpenAI

## Usage

1. showfix -h           (Show the help menu)
2. showfix -i "text"    (Show solution for "text")
3. showfix -o           (Add the latest history to your original search dictionary.)
4. showfix --history    (Show the command history and its results.)
5. showfix -l           (Show your original search dictionary.)
6. showfix -d "number"  (Delete a element in your original search dictionary.)
7. showfix -c           (Clear your history)

## Installation

```
$ git clone git@github.com:s1270144/terminal_translater.git
```

## Author

[@Shuto Homma](https://www.facebook.com/profile.php?id=100090890865720&sk=about)
mail to: mhomma0334@gmail.com
