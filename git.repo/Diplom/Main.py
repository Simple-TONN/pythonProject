import YaDownloader as YD
import requests
import pprint

# YD.uploader.upload()
#
# uploader = YaUploader(insert_token())
#     result = YD.uploader.upload(get_path(file_name))
#     print(result)


class MainVkApi:


    def __init__(self,token_vk):
        self.token_vk = token_vk


    def getgroups_vk(self,iduser):
        print(iduser)
        self.param = {
            'access_token': self.token_vk,
            'v': '5.130',
            'user_id':iduser,
            'extended': '1',
            'count' : '5'
        }
        self.method_name = 'groups.get'
        self.url = f"https://api.vk.com/method/{self.method_name}"
        self.resp_groups = requests.get(self.url,params=self.param)
        return  self.resp_groups.json()

    def getalbum_vk(self,iduser):
        album_list = {}
        print('getalbum', iduser)
        self.param = {
            'access_token': self.token_vk,
            'v': '5.130',
            'owner_id': iduser,
            'count': '5'
        }
        self.method_name = 'photos.getAlbums'
        self.url = f"https://api.vk.com/method/{self.method_name}"
        self.resp_album = requests.get(self.url,params=self.param)
        print(self.resp_album.json())
        for each_album in self.resp_album.json()['response']['items']:
            album_list[each_album['id']] = each_album['title']
            print(each_album['title'])
        print(self.resp_album.json()['response']['items'])
        return album_list   # {280886758: 'тест2альбом', 280882127: 'TestAlbom'}

    def getphotolist_vk(self, iduser, idalbum='profile'):
        photo_list ={}
        self.param = {
            'access_token': self.token_vk,
            'v': '5.130',
            'owner_id': iduser,
            'album_id': idalbum,
            'photo_sizes': '1',
            'count': '5',
            'extended': '1'
        }
        self.method_name = 'photos.get'
        self.url = f"https://api.vk.com/method/{self.method_name}"
        self.resp_photo = requests.get(self.url, params=self.param)
        #print(self.resp_photo.json()['response']['items'])
        for each_photo in self.resp_photo.json()['response']['items']:
            photo_list[each_photo['id']] = {'link_max_photo':each_photo['sizes'][-1]['url'],'likes': each_photo['likes']['count']}
            #photo_list[each_photo['id']] = {'liles': each_photo['likes']['count']}
        print(photo_list)
        print(photo_list.values())
        return self.resp_photo.json()



    def getiduser_vk(self,name):
        self.param = {
            'access_token': self.token_vk,
            'v': '5.130',
            'user_ids':name}
        self.method_name = 'users.get'
        self.url = f"https://api.vk.com/method/{self.method_name}"
        self.resp_user = requests.get(self.url, params=self.param)
        return self.resp_user.json()['response'][0]['id']





vas = MainVkApi(YD.insert_token('VK'))
#vas.getgroups_vk('644850263')
#vas.getalbum_vk('4613289')
#print(vas.getphotolist_vk('644850263','280882127'))

print(vas.getphotolist_vk('552934290'))
#print(vas.getphotolist_vk('fursov.anton'))
#print(vas.getiduser_vk('begemot_korovin'))
#print(vas.getiduser_vk('4613289'))
#print(vas.getiduser_vk('644850263'))









#vasa = MainVkApi(YD.insert_token('VK'))



#YD.insert_token('VK')


# #print(YD.insert_token('VK'))
# method_name = 'users.get'
# url = f"https://api.vk.com/method/{method_name}"
# param = {
#         'access_token': YD.insert_token('VK'),
#         'v': '5.130',
#         'user_id' : '644850263',
#         'extended': '1'
#
#     }
# resp= requests.get(url, params=param)
# print(resp.status_code)
# print(resp.json())

#resp = requests.get(f"https://api.vk.com/method/")