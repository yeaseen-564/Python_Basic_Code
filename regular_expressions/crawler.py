import re
import requests
text_html = """<div class="book-cover">
    <a href="http://dimik.pub/book/155/learn-programming-with-python-by-tamim-shahriar-subeen"><img
            src="http://dimik.pub/wp-content/uploads/2017/05/leanr.programming.with_.python.front_.cover_small_.png"></a>
</div> <!-- end .book-cover -->
<div class="slide-description">
    <div class="inner-sd">
        <div class="top-sd-head clearfix">
            <div class="tsh-left">

                <h2 class="sd-title"><a
                        href="http://dimik.pub/book/155/learn-programming-with-python-by-tamim-shahriar-subeen"></a>
                </h2>"""

text_plain = re.sub("\s+", " ", text_html)
# print(text_plain)
result = re.findall('<div class="book-cover">\s*<a href="(.*?)">\s*<img src="(.*?)">\s*.*?<h2 class="sd-title">\s*<a href="(.*?)"><', text_plain)  # Crawler for Links
# print(match)
for item in result:
    print("Book-Link: ", item[0])
    print("Picture-link: ", item[1])

