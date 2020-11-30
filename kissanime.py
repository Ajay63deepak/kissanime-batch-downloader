from gogo import gogo_convertor
from bs4 import BeautifulSoup
import requests

url = "https://kissanimes.tv/AnimeList?c="
web = "https://kissanimes.tv"
ser_web = ''
ep_web = ''
wat_web = ''
output = []
ser_name = input("Enter the name of the series : ").lower()
url += ser_name[0:1]
r = requests.get(url)
data = r.text
soup = BeautifulSoup(data , 'html.parser')
list = ''
for link in soup.find_all('a'): 
    if link.text[-5:-1:] == "Last":
        list += str(link.get('page'))
        print("there are almost "+str(list)+ ' pages to search')
        print("wait for a while until we get download link ready for you")
if list == "" :
    list += str(3)
    print("there are almost "+str(list)+ ' pages to search')
list = (int(list))
for i in range (1 , list+1) :
    ser_url = "https://kissanimes.tv/AnimeList?c={0}&page={1}".format(ser_name[0:1],i)
    r=requests.get(ser_url)
    data = r.text
    soup = BeautifulSoup(data , 'html.parser')
    new_list = ''
    for link in soup.find_all('a'):
        if link.text.lower() == ser_name :
            print("i got it {0}".format(ser_name))
            ser_web = web + str(link.get('href'))
            break
ep_web = ser_web.replace('category' , 'watch')
r = requests.get(ser_web)
data = r.text
soup = BeautifulSoup(data , 'html.parser')
ep_name = ''
ep_list = []
for link in soup.find_all('a'):
    watch = link.get('href')
    if watch[1:6] == "watch" :
        ep_name = link.get('href')
        ep_web = web + ep_name
        ep_list.append(ep_web)
ep_web = ep_web[:-1]
print("Number of episodes available " + str(len(ep_list)))
episode = []
for i in range(len(ep_list)+1):
    wat_web = "{0}{1}".format(ep_web , i)
    r = requests.get(wat_web)
    data = r.text
    soup = BeautifulSoup(data ,'html.parser')
    list = ''
    for link in soup.find_all('iframe'):
        list = link.get('src')
        output.append(list)
        f = open('watch list' , 'w')
        print(list , file=f)
    new_list = (list.split('/'))
    res= [sub.replace("vidstreaming.io" , "gogo-stream.com") for sub in new_list]
    new_list = res
    res = [sub.replace("streaming.php" , "download") for sub in new_list]
    new_list = res
    list = "/".join(new_list)
    list = str(list) + "&refer=" + str(url)
    # print(list)
    episode.append(list)
episode.remove(episode[0])
result = gogo_convertor(episode)
result_1 = [i for i in result.split("\n") if "360p" in i ]
result_2 = [i for i in result.split("\n") if "480p" in i ]
result_3 = [i for i in result.split("\n") if "720p" in i ]
result_4 = [i for i in result.split("\n") if "1080p" in i ]

# All quality
f = open('all.txt' , 'w')
print(result , file=f)
#360p quality
f = open('360p.txt' , 'w')
print(result_1 , file=f)
#480p quality
f = open('480p.txt' , 'w')
print(result_2 , file=f)
#720p quality
f = open('720p.txt' , 'w')
print(result_3 , file=f)
#1080p quality
f = open('1080p.txt' , 'w')
print(result_4 , file=f)
f= open('All_episode.html', 'w')
f.write("""
<html>
<head>All Episodes Watch Links</head><br>
<body>
""")
for i in range (len(output)):
    f.write("""<a href ="{}">Episode{}</a><br> """.format(output[i], i+1))
f.write("""
</body>
</head>
</html>
""")

print('All the files are availble in the same directory as the python script file')
print('All quality for all episodes may not available')