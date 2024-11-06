import argparse #line:1
import http .client #line:2
class Hilal :#line:4
    def __init__ (OOO0000OO00000OOO ,O0000000000000OO0 ,O0O0O0OO000OO00O0 ,O0OO00O0OOOOOO0O0 ):#line:5
        OOO0000OO00000OOO .server =O0000000000000OO0 #line:6
        OOO0000OO00000OOO .port =O0O0O0OO000OO00O0 #line:7
        OOO0000OO00000OOO .turbo =O0OO00O0OOOOOO0O0 #line:8
    def test_connection (OO0O000O000OOO00O ):#line:10
        print (f"Test ediliyor = {OO0O000O000OOO00O.server}:{OO0O000O000OOO00O.port} bu turbo seviyesi ile = {OO0O000O000OOO00O.turbo}")#line:11
        try :#line:12
            O00O0OOO0OOOO00O0 =http .client .HTTPConnection (OO0O000O000OOO00O .server ,OO0O000O000OOO00O .port ,timeout =5 )#line:14
            O00O0OOO0OOOO00O0 .request ("GET","/")#line:15
            O0O00O0O000OO000O =O00O0OOO0OOOO00O0 .getresponse ()#line:16
            if O0O00O0O000OO000O .status ==200 :#line:19
                print ("Sunucu erişilebilir!")#line:20
            else :#line:21
                print (f"Sunucu erişilebilir, fakat bir hata oluştu: {O0O00O0O000OO000O.status} {O0O00O0O000OO000O.reason}")#line:22
            O00O0OOO0OOOO00O0 .close ()#line:24
        except (http .client .HTTPException ,OSError )as OO0OO00O0OOO0O0O0 :#line:26
            print (f"Sunucuya bağlanma başarısız oldu: {OO0OO00O0OOO0O0O0}")#line:27
def display_banner ():#line:29
    print ("""
 #     #  #  #         # #   #       
 #     #  #  #        #   #  #       
 #######  #  #       #     # #       
 #     #  #  #       ####### #       
 #     #  #  #       #     # #       
 #     # ### ####### #     # ####### 
    """)#line:37
def main ():#line:39
    display_banner ()#line:40
    print ("Türkiye'nin Port tarama programı")#line:41
    print ("Bir sunucuyu, portu, test etmek için izniniz olmalı. Sorumluluk alarak kullanın.\n")#line:42
    O0O0000O0OO0O0O0O =argparse .ArgumentParser (description ="HİLAL")#line:44
    O0O0000O0OO0O0O0O .add_argument ("-s","--server",type =str ,required =True ,help ="Server IP veya URL")#line:45
    O0O0000O0OO0O0O0O .add_argument ("-p","--port",type =int ,default =80 ,help ="Port, normal 80")#line:46
    O0O0000O0OO0O0O0O .add_argument ("-t","--turbo",type =int ,default =10 ,help ="Turbo seviyesi, normal 10")#line:47
    O0O0000O0OO0O0O0O .add_argument ("-q","--sessiz",action ="store_true",help ="Sessiz mod")#line:48
    OO00O0OOOO0OO0O00 =O0O0000O0OO0O0O0O .parse_args ()#line:50
    if not OO00O0OOOO0OO0O00 .sessiz :#line:52
        print (f"\n[Server IP/URL: {OO00O0OOOO0OO0O00.server}]  [Port: {OO00O0OOOO0OO0O00.port}]  [Turbo: {OO00O0OOOO0OO0O00.turbo}]")#line:53
    O0OOO0OOOO0OO00O0 =Hilal (OO00O0OOOO0OO0O00 .server ,OO00O0OOOO0OO0O00 .port ,OO00O0OOOO0OO0O00 .turbo )#line:56
    O0OOO0OOOO0OO00O0 .test_connection ()#line:57
    input ("Çıkmak için enter tuşuna basın...")#line:60
if __name__ =="__main__":#line:62
    main ()#line:63
