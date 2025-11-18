@echo off
echo "# vac" >> README.md
echo "ddddddd"
git init
git add .
git status
git commit -m 'Added my project'
git branch -M main
git remote add origin https://github.com/zaidce/clinic.git
git remote -v
git push -f -u origin main
pause