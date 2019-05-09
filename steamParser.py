from collections import OrderedDict
import pandas as pd
import requests
from datetime import datetime
from tqdm import tqdm

def getReviews(appid):
    '''
    Request reviews from the Steam Web API and return them as a list. This is a blocking call that may take some time, depending on how many reviews there are.\n
    **appid** -- The Steam App ID as a string obtained from the game's store page URL\n
    **progress** -- Set to true to print the progress of each request.
    '''
    def _makeRequest(appid, params):
        '''
        Helper function that sends a request to the Steam Web API and returns the response object.\n
        **appid** -- The Steam App ID obtained from the game's Store page URL\n
        **params** -- An object used to build the Steam API query. (https://partner.steamgames.com/doc/store/getreviews)
        '''
        response = requests.get(url=ENDPOINT+str(appid), params=para) # get the data from the endpoint
        try:
            return response.json() # return data extracted from the json response
        except ValueError:
            print('Decoding JSON has failed')
            return {"success": 0}
    
    def _extractReview(data, savelist):
        for reviews in data['reviews']:
            if reviews['review'] not in savelist:
                savelist.append(reviews['review'])
        return savelist

    ENDPOINT = 'https://store.steampowered.com/appreviews/' # https://partner.steamgames.com/doc/store/getreviews
    para = {
        'json': 1,
        'language': 'english',# languages at https://partner.steamgames.com/doc/store/localization
        'filter': 'all', # sort by: recent, update
        'start_offset': 0, # for pagination
        'review_type': 'all', # all, positive, negative
        'purchase_type': 'all', # all, non_steam_purchase, steam
        'num_per_page': 100,                                         
        #'day_range': 120,
    }

    savelist = []
    all_dict = OrderedDict()
    data = _makeRequest(appid, para)
    
    if data['success'] == 1:
        if data['query_summary']['num_reviews'] > 20:
            all_dict['appid'] = appid
            all_dict['ReviewNum'] = data['query_summary']['num_reviews']
            all_dict['totalReviews'] = data['query_summary']['total_reviews']
            all_dict['PosReviews'] = data['query_summary']['total_positive']
            all_dict['NegReviews'] = data['query_summary']['total_negative']
            all_dict['reviewScore'] = data['query_summary']['review_score_desc']
            
            savelist = _extractReview(data, savelist)
            
            all_dict['allReviewsCount'] = len(savelist)
            all_dict['allReviews'] = savelist
    
    return all_dict



if __name__ == "__main__":
    url = 'http://api.steampowered.com/ISteamApps/GetAppList/v2'
        
    idlist = []
    response1 = requests.get(url)
    data1 = response1.json()
    for idx, value in enumerate(data1['applist']['apps']): 
        id_dict = OrderedDict()
        id_dict['appid'] = value['appid']
        id_dict['appname'] = value['name']
        idlist.append(id_dict)
    
    idname = pd.DataFrame(idlist)
    appid_list = idname['appid'].unique().tolist()
    print('all appid_list finished.')
    
    idname.to_csv('applist_name.csv', encoding='utf-8', index=None)


    all_list = []
    for idx in range(0, len(appid_list) // 5000):
        print(idx, 'start...')
        now = datetime.now()    

        target_list = appid_list[idx*5000: (idx+1)*5000]
        
        n = 0
        for each in tqdm(target_list):
            all_dict = getReviews(each)
            if len(all_dict):
                all_list.append(all_dict)
                n += 1
        
        later = datetime.now()
        diff = later - now
        
        print('總共爬取', n, '，花費', str(round(diff.seconds/60.0, 2)), '分鐘')
            
        data = pd.DataFrame(all_list)
        data.to_csv('allreviews.csv', index=None)
