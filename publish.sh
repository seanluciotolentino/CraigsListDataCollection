#!/bin/bash
git add data0-24/*.csv
git add data24-48/*.csv

d=date
git commit -m $d
git push
