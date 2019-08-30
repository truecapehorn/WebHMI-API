import requests
import json
import time

class API:

    def __init__(self,device_adress,api_kay):
        self.device_adress=device_adress
        self.headers = {'X-WH-APIKEY': api_kay,
                        'Accept': 'application/json',
                        'Content-Type': 'application/json',
                        'X-WH-CONNS' : '',
                        'X-WH-START' : '',
                        'X-WH-END' : '',
                        'X-WH-REG-IDS' : '',
                        'X-WH-SLICES' : '',
                        'X-WH-REGS' : '',
                        }

        self.api_adress={'connectionList':{'adress':'/api/connections'},
                         'registerList':{'adress':'/api/registers/'},
                         'trendList':{'adress':'/api/trends/'},
                         'graphList':{'adress':'/api/graphs'},
                         'getCurValue':{'adress':'/api/register-values'},
                         'getLocTime':{'adress':'/api/timeinfo'},
                         'getRegLog':{'adress':'/api/register-log'},
                         'getGraphData':{'adress':'/api/graph-data/'},
                         }



    def make_api_adress(self,action_name,args):
        print(len(args))
        if len(args)==0:
            api_adress=self.api_adress[action_name]['adress']
        else:
            api_adress=self.api_adress[action_name]['adress']+'{}'.format(args[0])
        return api_adress

    def make_headers(self):
        return



    def make_req(self,action_name,head,*args):
        print(args)
        # ADRESS
        api_adress=self.make_api_adress(action_name,args)
        url = self.device_adress + api_adress
        print(url)
        #HEAD
        print(head)
        # GET
        r = requests.get(url, headers=head)
        API.clear_headers(self) # wyczyszczenie headersow
        print(r)
        return r.json()


    def clear_headers(self):
        h=['X-WH-CONNS', 'X-WH-START', 'X-WH-END', 'X-WH-REG-IDS', 'X-WH-SLICES', 'X-WH-REGS', 'X-WH-GRAPH-ID']
        for key in h:
            self.headers[key]=''
        print(self.headers)





    def response_status(self,action, r):
        '''Wydrukowanie wynikow'''
        # Response, status etc
        print('\n' + 140 * '-' + '\n')
        print('* {0} dla URL: {1}\n  Kodowanie znaków: {2}\n'.format(action, r.url, r.apparent_encoding))
        print('* ODPOWIEDZ SERWERA:\n{0}'.format(r.text))  # TEXT/HTML
        print('* KOD STATUSU I STATUS:\n[{0} --> {1}]\n'.format(r.status_code, r.reason))  # HTTP
        print('* NAGLOWEK ODPOWIEDZI:\n{0}\n'.format(r.headers))
        print('<!---------koniec-----------!>')



if __name__ == "__main__":
    from head import device_adress,APIKEY


    web = API(device_adress,APIKEY)
    headers=web.headers


    headers['X-WH-CONNS']='5'
    con1=web.make_req('getCurValue',headers)

    con2=web.make_req('graphList',headers)


    headers['X-WH-START']= '1558296000'
    headers['X-WH-END']= '1558382400'
    headers['X-WH-SLICES']= '800'
    con3=web.make_req('getGraphData',headers,'33')
    print(len(con3[0]))


