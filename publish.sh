#!/bin/bash
git add data0-24/*.csv
git add data24-48/*.csv

git commit -m "$(date)"
git push
