kkmanual Readme.md -t .thumb.jpg
mdpp Readme.md
mdpp base/* -q
git add .
git commit -m "updating"
git push origin master

# #copy missing or changed files
cd ..
cp arcade/Readme.md moodle

# #updating
kkmirror arcade moodle qxcodeed moodle

cd moodle
kkmanual --root Readme.md
# # pushing moodle
git add .
git commit -m "updating"
git push origin master