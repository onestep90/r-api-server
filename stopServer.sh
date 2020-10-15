#!/bin/zsh
kill $(lsof -t -i :8000); 
