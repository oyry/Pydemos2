from Template.Maindemo import *
import random
def Hfmobile():
    q3w = ["130", "131", "132", "133", "134", "135", "136", "137", "138", "139", "147", "150", "151", "152",
           "153", "155", "156", "157", "158", "159", "166", "185", "186", "187", "188", "198", "199"]
    randomq3w = random.choice(q3w)
    h8w = "".join(random.choice("0123456789") for i in range(8))
    mobile = randomq3w + h8w
    return mobile
mobile=Hfmobile()
if __name__ == '__main__':
    TestMain(url='/amp-auth-service/rest',querystring={'method':'amp.auth.authentication.signInNoEnt'},
             payload={"code": "1582944742277124566","password":"j8ptrt","tag":"mss"})
    token= Token()
    TestMain(url='/ocm-wallet-webin/rest',
             querystring={'method': 'efuture.ocm.wallet.rebate.save', 'ent_id': 1582944742277124600, 'token': token},
             payload={'inputer_name': '[admin]惠Go MSS 管理员', 'rebate_target': '1', 'edate': '2019-3-13',
                      'inputer': 'admin', 'czk_rebate_det': [
                     {'flag': 'I', 'rebate_condition': '88', 'rebate_discount_money': '99', '_state': 'added',
                      '_id': 66, '_uid': 66}], 'billmoduleid': '✒', 'flag': 'I', 'totallimit': '0',
                      'singlelimit': '11', 'billstatus': 'N', 'inputdate': '2019-02-26 14:34:48', 'summary': 'C',
                      'rebate_type': '1', 'sdate': '2019-2-26'})
    # TestMain(url='/omw-service-wxproxy/captcha',querystring={'token': token},
    #          payload={"mobile":mobile,"state":"gh_f79e23f74622"})
    # captcha = Captcha()
    # TestMain(method='get',url='/omw-service-wxproxy/captcha/'+mobile, querystring={'token': token})
    # captcha=Captcha()
    # print(captcha)
    # TestMain(url='/omw-service-member/rest', querystring={'method':'omw.customer.register','token': token},
    #          payload={"UserAgreement": "免责声明", "corp": "0", "market": "6206", "wxid": mobile,
    #                   "mobile": mobile, "captcha": captcha, "nickname": mobile,
    #                   "name": mobile})
