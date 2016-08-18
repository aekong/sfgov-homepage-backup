rm -rf sfgov.org*
rm *.js
wget -r -l 2 --exclude-domains -p -k -E http://sfgov.org
wget -r -l 2 --exclude-domains -p -k -E http://sfgov.org/news
cd sfgov.org/js
wget http://sfgov.org/js/sfhome_desktop.js
cd ..
mkdir -p sites/default/files/Homepage
mkdir -p sites/default/files/Homepage/Slide
mkdir -p sites/default/files/Homepage/Carousel
mkdir -p sites/default/files/Images/MainPages
cd sites/default/files/Homepage
wget http://sfgov.org/sites/default/files/Homepage/slide.html
wget http://sfgov.org/sites/default/files/Homepage/most_requested.html
wget http://sfgov.org/sites/default/files/Homepage/carousel.html
cd ../../../../../
cp -r sfgov.org sfgov.org.bak
find ./sfgov.org/js -name "sfhome*" -type f -exec sed -i "" 's/\.\.\/sites\/default/sites\/default/g' {} \;
python get-images.py
find ./sfgov.org/sites/default/files/Homepage/ -name "*.html" -type f -exec sed -i "" 's/src="\.\.\/sites\/default/src="sites\/default/g' {} \;
find ./sfgov.org/sites/default/files/css_injector/ -name "*.css*" -type f -exec sed -i "" 's/http:\/\/sfgov.org\/sites\/default\/files\/Images\/MainPages\/SFGov.*Pages/\.\.\/Images\/MainPages/g' {} \;
wget -O hpnews.js "http://sfgov.org/hpnews?news_callback=news_callback"
find ./sfgov.org/js -name "sfhome.js" -type f -exec sed -i "" 's/\.\.\/hpnews/\.\.\/hpnews.js/g' {} \;
wget -O hpservices.js "http://sfgov.org/hpservices?services_callback=services_callback"
find ./sfgov.org/js -name "sfhome_desktop.js" -type f -exec sed -i "" 's/\.\.\/hpservices/\.\.\/hpservices.js/g' {} \;
cd sfgov.org
wget -O residents_json.js "http://sfgov.org/residents_json?services_callback=services_callback"
find ./sites/default/files/js_injector/ -name "*.js*" -type f -exec sed -i "" 's/residents_json/residents_json.js/g' {} \;
wget -O business_json.js "http://sfgov.org/business_json?services_callback=services_callback"
find ./sites/default/files/js_injector/ -name "*.js*" -type f -exec sed -i "" 's/business_json/business_json.js/g' {} \;
wget -O opengov_json.js "http://sfgov.org/opengov_json?services_callback=services_callback"
find ./sites/default/files/js_injector/ -name "*.js*" -type f -exec sed -i "" 's/opengov_json/opengov_json.js/g' {} \;
wget -O visitors_json.js "http://sfgov.org/visitors_json?services_callback=services_callback"
find ./sites/default/files/js_injector/ -name "*.js*" -type f -exec sed -i "" 's/visitors_json/visitors_json.js/g' {} \;
wget -O onlineservices_json.js "http://sfgov.org/onlineservices_json?services_callback=services_callback"
find ./sites/default/files/js_injector/ -name "*.js*" -type f -exec sed -i "" 's/onlineservices_json/onlineservices_json.js/g' {} \;
cd ..
sed -i "" 's/http:\\\/\\\/sfgov.org\\\/news/news/g' hpnews.js
sed -i "" 's/"\}\}/.html"\}\}/g' hpnews.js
find ./sfgov.org/js/sfhome.js -exec sed -i "" 's/\.\.\/news/news.html/g' {} \;