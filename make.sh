#!/bin/bash

elm make src/Main.elm --output=./out/elm.js --optimize

sass src/styles.sass .tmp/temp.css

# cp src/*.css .tmp

printf '%s\n%s\n' "@tailwind base;
@tailwind components;
@tailwind utilities;" "$(cat .tmp/temp.css)" > .tmp/temp.css

npx tailwindcss -i .tmp/temp.css -o out/styles.css

elm-format --yes src