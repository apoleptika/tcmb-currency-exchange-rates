
git init
git status
git add -A
git status
git commit -m "initial commit"
git status
git remote add origin https://github.com/apoleptika/tcmb-currency-exchange-rates.git
// git push -u origin master
// *** artık main kullanılıyor ***

//git push -u origin main
// git pushh hata verdi ve aşağıdaki 2 komut bunu çözdü 
git pull origin main
git push -f origin main


*******************************
dosyayı güncelle, status ie kontrol et, add ile ekle, commit, push -f ile Githuba gönder
git status 
# git add -A   add all files
git add README.md 
git commit -m "commit 6"
git push -f origin main
**********************************


//git push ... Use web browser for Github authentication 
// dosyaları resetlemek için 
//git checkout .
//git restore .

// About renaming your branch from master to main
git branch -m master main \
git push -u origin main \
git remote set-head origin main

-----------------------------
A clear guide for changing from master to main. 
git fetch --all                # update all remotes
git checkout main              # checkout the new main
# update local HEAD
git symbolic-ref refs/remotes/origin/HEAD refs/remotes/origin/main
    
git branch -d master           # delete local master
git branch -rd origin/master   # delete remote master ref