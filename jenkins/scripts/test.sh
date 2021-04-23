#!/bin/bash
#!/usr/bin/env sh

echo 'This command is for a devDependency'
set -x
npm install --save-dev cross-env
set +x

echo 'the following "npm" command tests that our application is rendering'
echo 'this command invokes: runner Jest (https://facebook.github.io/jest/)'
set -x
npm test