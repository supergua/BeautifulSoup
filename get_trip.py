from bs4 import BeautifulSoup
import requests
import time

urls = ['http://www.tripadvisor.cn/Hotels-g293920-oa{}-Phuket-Hotels.html'.format(str(i)) for i in range(30, 780, 30)]
url_saves = 'https://www.tripadvisor.cn/Saves/634825'

headers = {
    'User-Agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/56.0.2924.87 Safari/537.36',
    'Cookie':'TAUnique=%1%enc%3Aplp4ZR4gFVWFU1luDKjsMvAV5vylgpdzHo9jp%2Fw1gAcbC1YwqgTFtA%3D%3D; TASSK=enc%3AANLRLy6246yaTpXN7HSDg1IH9HrZ8YUzq0grHLPW263AYT%2Fx81U7MLuDlCeWMbNgFD75bGyAF35WEVYtO0BAfMS6LgDc%2BAnbS5ikfXKiC5tpk%2BwUV4ogqsZ5fpO3Bm4PLQ%3D%3D; VRMCID=%1%V1*id.12082*llp.%2F-m12082*e.1488771930973; TAPD=tripadvisor.cn; ServerPool=A; _smt_uid=58b3a0de.24e7661c; SecureLogin2=3.4%3AAJ%2FteOBNn4bme2a2VXK0c%2B2%2B7lPT7xdGkkvFJ4Wx7XnGG2vTkeu2FkoXpu6jpCm6X2UA0GxSlgIGhNuJsMxvG%2B76zatfa9LW5w%2Bq0o1zasiOhDYzKk4nkkh8ee3aiUU8TcF3ZDSQwdFFQpGbRUtGz2IJAK71HQcb2rdk1XB1%2FbkNQ6mbb%2Bwgi7Hg98EqxJ9yeoRdJLLe39QG0lB5C540i6c%3D; TAAuth2=%1%3%3Ac8964931d2a48db535ecc4115efcb636%3AAEYCd8KjaDfpmGcMdkn3Ze104r%2FQgvzBf9fF5P2BpgvUDnDgAlr%2FqlATHRmMmSlL2rfNg7m1KuuYGZ0OprcM117Ysq0gyGE4xaUoUs9%2Bks1jNTmOeMzftBkievFkP9qdkk4ZLDR0uwp4jlxjNFXkbxqmqa9yTrrG4xi5qLCuFXSW8PRLBTOZCocQbvRjUlbF4g%3D%3D; CM=%1%HanaPersist%2C%2C-1%7CPremiumMobSess%2C%2C-1%7Ct4b-pc%2C%2C-1%7CHanaSession%2C%2C-1%7CRCPers%2C%2C-1%7CWShadeSeen%2C%2C-1%7CFtrPers%2C%2C-1%7CTheForkMCCPers%2C%2C-1%7CHomeASess%2C2%2C-1%7CPremiumSURPers%2C%2C-1%7CPremiumMCSess%2C%2C-1%7Csesscoestorem%2C%2C-1%7CCCSess%2C%2C-1%7CViatorMCPers%2C%2C-1%7Csesssticker%2C%2C-1%7CPremiumORSess%2C%2C-1%7Ct4b-sc%2C%2C-1%7CMC_IB_UPSELL_IB_LOGOS2%2C%2C-1%7Cb2bmcpers%2C%2C-1%7CMC_IB_UPSELL_IB_LOGOS%2C%2C-1%7CPremMCBtmSess%2C%2C-1%7CPremiumSURSess%2C%2C-1%7CLaFourchette+Banners%2C%2C-1%7Csess_rev%2C%2C-1%7Csessamex%2C%2C-1%7Cperscoestorem%2C%2C-1%7CPremiumRRSess%2C%2C-1%7CSaveFtrPers%2C%2C-1%7CTheForkRRSess%2C%2C-1%7Cpers_rev%2C%2C-1%7CMetaFtrSess%2C%2C-1%7CRBAPers%2C%2C-1%7CWAR_RESTAURANT_FOOTER_PERSISTANT%2C%2C-1%7CFtrSess%2C%2C-1%7CHomeAPers%2C%2C-1%7CPremiumMobPers%2C%2C-1%7CRCSess%2C%2C-1%7CLaFourchette+MC+Banners%2C%2C-1%7Cbookstickcook%2C%2C-1%7Csh%2C%2C-1%7Cpssamex%2C%2C-1%7CTheForkMCCSess%2C%2C-1%7CCCPers%2C%2C-1%7CWAR_RESTAURANT_FOOTER_SESSION%2C%2C-1%7Cb2bmcsess%2C%2C-1%7CViatorMCSess%2C%2C-1%7CPremiumMCPers%2C%2C-1%7CPremiumRRPers%2C%2C-1%7CPremMCBtmPers%2C%2C-1%7CTheForkRRPers%2C%2C-1%7CSaveFtrSess%2C%2C-1%7CPremiumORPers%2C%2C-1%7CRBASess%2C%2C-1%7Cbookstickpers%2C%2C-1%7Cperssticker%2C%2C-1%7CMetaFtrPers%2C%2C-1%7C; TATravelInfo=V2*A.2*MG.-1*HP.2*FL.3*RVL.1830576_57l298566_58l678584_58l297470_58l2699311_58l8047053_58l297407_58l5037699_58*RS.1; TAReturnTo=%1%%2FHotel_Review-g297407-d5037699-Reviews-Langham_Place_Xiamen-Xiamen_Fujian.html; CommercePopunder=SuppressAll*1488253557908; roybatty=TNI1625!AB8CqU%2B%2BEvATdnz%2FL0habgEpxbowtOoAJNMruj3fOhJMKdvsbHsJt292GbwwpGnFF3hc0A%2FiIbJLWNm2iVQswKw8mbuuIVdPydxDW6%2FU2tIPhU9x%2B%2FQ9EHRFpVuEcZVqXF%2FrZWygWvzQKDCfHGQgSLfW%2FV5v%2BOKhB2X6vXzkZmTE%2C1; TASession=%1%V2ID.3C88AE1A2FB5CFD73297DA09F675EB90*SQ.116*LP.%2FHotels-g298566-Osaka_Osaka_Prefecture_Kinki-Hotels%5C.html*PR.427%7C*LS.ActionRecord*GR.44*TCPAR.5*TBR.47*EXEX.50*ABTR.1*PPRP.55*PHTB.36*FS.59*CPU.86*HS.popularity*ES.popularity*AS.popularity*DS.5*SAS.popularity*FPS.oldFirst*TS.1939170E2BF56B74217C8728B35E1A4F*LF.zhCN*FA.1*DF.0*MS.-1*RMS.-1*TRA.true*LD.5037699*BG.297407*BT.hr7f5a; TAUD=LA-1488244429389-1*LG-13772022-2.1.F.*LD-13772023-.....; ki_t=1488167242961%3B1488243109127%3B1488258202268%3B2%3B35; ki_r=; Hm_lvt_2947ca2c006be346c7a024ce1ad9c24a=1488167135,1488243107; Hm_lpvt_2947ca2c006be346c7a024ce1ad9c24a=1488258203'
}

def get_jiudian(url,data=None):
    wb_data = requests.get(url)
    time.sleep(5)
    soup = BeautifulSoup(wb_data.text, 'lxml')
    titles = soup.select('div.listing_title > a')
    imgs = soup.select('img[width="180"]')
    cates = soup.select('div.clickable_tags')
    for title, img, cate in zip(titles, imgs, cates):
        data = {
            'title': title.get_text(),
            'img': img.get('src'),
            'cate': list(cate.stripped_strings),
        }
        print(data)

for single_url in urls:
    get_jiudian(single_url)

