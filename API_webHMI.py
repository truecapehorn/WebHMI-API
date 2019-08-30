import requests
import json
import time

class API:

    def __init__(self,device_adress,headers):
        self.device_adress=device_adress
        self.headers=headers
        self.api_adress={'connectionList':'/api/connections',
                         'registerList':'/api/registers/',
                         'trendList':'/api/trends/',
                         'graphList':'/api/trends/',
                         'getCurValue':'/api/register-values',
                         'getLocTime':'/api/timeinfo',
                         'getRegLog':'/api/register-log',
                         'getGraphData':'/api/graph-data/',
                         'getGraph':'/api/graph-data/{}'.format(self.headers['X-WH-GRAPH']),

                         }


    def make_req(self,action_name,head):
        # ADRESS
        api_adress=self.api_adress[action_name]
        url = self.device_adress + api_adress
        # GET
        r = requests.get(url, headers=head)
        return r.json()




    def response_status(self,action, r):
        '''Wydrukowanie wynikow'''
        # Response, status etc
        print('\n' + 140 * '-' + '\n')
        print('* {0} dla URL: {1}\n  Kodowanie znaków: {2}\n'.format(action, r.url, r.apparent_encoding))
        print('* ODPOWIEDZ SERWERA:\n{0}'.format(r.text))  # TEXT/HTML
        print('* KOD STATUSU I STATUS:\n[{0} --> {1}]\n'.format(r.status_code, r.reason))  # HTTP
        print('* NAGLOWEK ODPOWIEDZI:\n{0}\n'.format(r.headers))
        print('<!---------koniec-----------!>')








    def connectionList(self):
        '''Zczytanie listy połaczen webHMI'''
        # ADRESS
        url = self.device_adress + self.api_adress['connectionList']
        # GET
        r = requests.get(url, headers=self.headers)
        return r.json()


    def registerList(self):
        '''Zczytanie listy rejestrow webHMI'''
        # ADRESS
        url = self.device_adress + self.api_adress['registerList']
        # GET
        r = requests.get(url, headers=headers)
        return r.json()


    def trendList(self):
        '''Zczytanie listy trendow webHMI'''
        # ADRESS
        api_adress = '/api/trends/'
        url = self.device_adress + self.api_adress
        # GET
        r = requests.get(url, headers=headers)
        return r.json()


    def graphList(self):
        '''Zczytanie listy grafow webHMI'''
        # ADRESS
        api_adress = '/api/graphs/'
        url = self.device_adress + self.api_adress
        # GET
        r = requests.get(url, headers=headers)
        return r.json()


    def getCurValue(self):
        '''Zczytanie wartosci z rejestru'''
        # ADRESS
        api_adress = '/api/register-values'
        url = self.device_adress + self.api_adress
        # GET
        r = requests.get(url, headers=headers)
        return r.json()


    def getLocTime(self):
        '''Zczytanie daty UNIX time'''
        # ADRESS
        api_adress = '/api/timeinfo'
        url = self.device_adress + self.api_adress
        # GET
        r = requests.get(url, headers=headers)
        return r.json()


    def getRegLog(self):
        '''Zczytanie wartosci logow'''
        # ADRESS
        api_adress = '/api/register-log'
        url = self.device_adress + self.api_adress
        # GET
        r = requests.get(url, headers=headers)
        return r.json()


    def getGraphData(self):
        '''Zczytanie wartosc i wykresow'''
        # ADRESS
        api_adress = '/api/graph-data/'
        url = self.device_adress + self.api_adress
        # GET
        r = requests.get(url, headers=headers)
        action = 'pobranie wykresow'
        return r.json()


    def getGraph(self, graphID):
        '''Zczytanie wartosc i wykresow ale dla konkretnego'''
        # ADRESS
        url = self.device_adress + self.api_adress['getGraph']+graphID
        # GET
        r = requests.get(url, headers=headers)
        action = 'pobranie wykresow'
        return r.json()


if __name__ == "__main__":
    from head import headers,device_adress


    web = API(device_adress,headers)

    print(web.headers)
    head=web.headers
    print(web.api_adress)
    head = web.headers
    head['X-WH-CONNS']='5'
    con=web.make_req('getCurValue',head)
    print(con)