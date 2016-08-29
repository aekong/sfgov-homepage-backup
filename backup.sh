rm -rf home || true
mkdir home
cd home
wget -r -l 2 --exclude-domains -p -k -E http://sfgov.org && echo OK || echo FAILED_SOMEWHERE_WGET_SFGOV.ORG
wget -r -l 2 --exclude-domains -p -k -E http://sfgov.org/news && echo OK || echo FAILED_SOMEWHERE_WGET_SFGOV.ORG.NEWS
cd sfgov.org/js
wget http://sfgov.org/js/sfhome_desktop.js
cd ..
mkdir -p sites/default/files/Homepage
mkdir -p sites/default/files/Homepage/Slide
mkdir -p sites/default/files/Homepage/Carousel
mkdir -p sites/default/files/Images/MainPages
mkdir -p sites/default/files/Images/Key\ Services
cd sites/default/files/Homepage
wget http://sfgov.org/sites/default/files/Homepage/slide.html
wget http://sfgov.org/sites/default/files/Homepage/most_requested.html
wget http://sfgov.org/sites/default/files/Homepage/carousel.html
cd ../../../../../
cp -r sfgov.org sfgov.org.bak
find ./sfgov.org/js -name "sfhome*" -type f -exec sed -i.sedtmp 's/\.\.\/sites\/default/sites\/default/g' {} \;
cd sfgov.org
wget -O residents_json.js "http://sfgov.org/residents_json?services_callback=services_callback"
wget -O business_json.js "http://sfgov.org/business_json?services_callback=services_callback"
wget -O opengov_json.js "http://sfgov.org/opengov_json?services_callback=services_callback"
wget -O visitors_json.js "http://sfgov.org/visitors_json?services_callback=services_callback"
wget -O onlineservices_json.js "http://sfgov.org/onlineservices_json?services_callback=services_callback"
cd ..
wget -O hpnews.js "http://sfgov.org/hpnews?news_callback=news_callback"
find ./sfgov.org/js -name "sfhome.js" -type f -exec sed -i.sedtmp 's/\.\.\/hpnews/\.\.\/hpnews.js/g' {} \;
wget -O hpservices.js "http://sfgov.org/hpservices?services_callback=services_callback"
find ./sfgov.org/js -name "sfhome_desktop.js" -type f -exec sed -i.sedtmp 's/\.\.\/hpservices/\.\.\/hpservices.js/g' {} \;
sed -i.sedtmp 's/http:\\\/\\\/sfgov.org\\\/news/news/g' hpnews.js
sed -i.sedtmp 's/"\}\}/.html"\}\}/g' hpnews.js
find ./sfgov.org/js/sfhome.js -exec sed -i.sedtmp 's/\.\.\/news/news.html/g' {} \;
cd ..
python get-images.py
python fix-refs.py
find ./home/sfgov.org/sites/default/files/Homepage/ -name "*.html" -type f -exec sed -i.sedtmp 's/src="\.\.\/sites\/default/src="sites\/default/g' {} \;
find ./home/sfgov.org/sites/default/files/css_injector/ -name "*.css*" -type f -exec sed -i.sedtmp 's/http:\/\/sfgov.org\/sites\/default\/files\/Images\/MainPages\/SFGov.*Pages/\.\.\/Images\/MainPages/g' {} \;
find . -name "*.sedtmp" -type f -delete