#!/bin/bash


function add_commit_push (){

    echo "tu veux lancer le commit_push workflow ?"
    read -r answer
    
    if [ "$answer" = 'oui' ]; then
        git commit -m "$V1"
        git push origin Leandre
    
    git add .
    git commit -m "V1"
    git push origin Leandre
    else
        echo "ne fais pas le commit_push"
    fi
}


function init {
    if [[ ! -e '.git' ]]; then
        echo "no .git repository"
        echo "--------"
        git init # initialiser un dépot local git
        git remote add origin git@github.com:laysrt/chip8.git
    else
        echo "c'est déjà un dépot git"
    fi
}

init
add_commit_push "$V1"