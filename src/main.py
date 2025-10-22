
from spider2Database import getConfigFromYaml,start_with_config

if __name__=="__main__":
    config=getConfigFromYaml("config.yaml")
    start_with_config(config)


    '''
    co=r"_m_h5_tk_enc=ec7dc22e8b5e5124123d89381bb7821f;sdkSilent=1754801600652;xlly_s=1;tfstk=gSLsGK6-OR21Pi-RfZlUPBtk5p_jUXuzlS1vZIUaMNQTH-dRLdWN7j0fHdXe7ORNW5xHUQUw7cb4lNbckYkrz4lMsZbxlc2HxOAptshF6OhjVPQckYkEz4RMsZvTVDRpBBhCgszT6KI99wCAp1BADKBdv_CzBZQvHXGCi9ImsIvv9X1cptQAkKdKOscEF71jfOAsNegmh3jceCBQkrNl1GB-r9aYke1_UTdsqrUvR1s6owejwjswDQjk7Qgb-NRWvwC6H4HOJQKBaGTsFPWDIEs2-GFxZMAdBg5HKREONN612FIaibbGDHTC7FH0qBRCBg_eYDDN0N96qTjtxvvXOOJv5MesLt-yTFIBevzBnit9C6QR4x4PFpAUcWsul66rOXZ0morMfFW3w7NcX6f1YXGQBnjOt66rOXZ0mGCh19lIORKc.;havana_lgc2_77=eyJoaWQiOjIyMDU4NjU1MTc1NTIsInNnIjoiYzkyNDllNjQwZjQ1NDYxODk0MjAwN2RkMzJjZWZmMmQiLCJzaXRlIjo3NywidG9rZW4iOiIxbHJQT0poNC1FaXVJOXl4dENKbjdRQSJ9;sgcookie=E100Q08HRlUV7FeKQOO9JqeWQdvOZeNFpVbawVd1LNNRCLj80otL6l8xTmofQbqcb%2BHWFPLBMokKuAgKExzHNriTjYLV8owUCGVvmDha6xifJ8WmM8euq%2B8ayey%2FRvD280nk;_tb_token_=e073537ae93e3;havana_lgc_exp=1757227924979;t=630549d4a3155233f811f79174530aa0;_hvn_lgc_=77;_m_h5_tk=b51d1934419477a2f1db90a531e67979_1754732975740;_samesite_flag_=true;cna=dLr7H+iY8R8CAbf3CTLIDAhh;cookie2=26a0eca1202ced5a2df4401f1c3a1182;csg=a97b503d;isg=BPLyLl1xziUXUv1FIEMKssQ8QzjUg_YdjZ5pqLzLr6WQT5NJpBAAL7fsO-tzP261;tracknick=tb454737635;unb=2205865517552"
    #co=get_cookies.get_cookies("https://www.goofish.com/")
    print(co)
    a=getGoods(30,co,"RTX5070",price_range=(4000,5000),is_save=True)
    #print(a)
    #data2db(a)
    k="11"  '''