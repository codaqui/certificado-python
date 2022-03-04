#!/bin/sh

#Créditos pekman
#email: fervelinux@openboxmail.com
#Licença: BSD

clear

echo -e "\e[32;5;1m entre com o texto a ser exibido na imagem \e[m"
echo ""
read texto

echo -e "\e[35;5;1m entre a altura do texto \e[m"
echo ""
read altura

width=`identify -format %w in $( ls *.jpg )`; \
  convert -background '#000000d0' -fill gray74 -gravity center -font Titillium-Web-Regular -size ${width}x$altura \
          caption:"$texto" \
          $( ls *.jpg *.png *.JPG *.jpeg ) +swap -gravity south -composite up.jpg;
