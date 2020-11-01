from unittest import TestCase
from utils import Enigma, Settings, EnigmaMachineData


class Test_Enigma(TestCase):

    def setUp(self):
        self.data_obj = EnigmaMachineData()
        self.data_obj.set_machine("example_machine")
        self.settings = Settings()
        self.I = self.data_obj.get_rotor("i")
        self.II = self.data_obj.get_rotor("ii")
        self.III = self.data_obj.get_rotor("iii")
        self.IV = self.data_obj.get_rotor("iv")
        self.V = self.data_obj.get_rotor("v")
        self.Beta = self.data_obj.get_rotor("beta")
        self.Gamma = self.data_obj.get_rotor("gamma")
        self.A = self.data_obj.get_reflector("a")
        self.B = self.data_obj.get_reflector("b")
        self.C = self.data_obj.get_reflector("c")
        self.etw = self.data_obj.get_entry_wheel("etw")
        self.settings.add_reflector(self.B)
        self.settings.add_entry_wheel(self.etw)

    def test_AAZ(self):
        self.I.update({"start_position": "A", "position": 1})
        self.II.update({"start_position": "A", "position": 2})
        self.III.update({"start_position": "Z", "position": 3})
        self.settings.add_rotors([self.I, self.II, self.III])
        self.assertEqual("U", Enigma(settings=self.settings).press_key("A"))

    def test_AAA(self):
        self.I.update({"start_position": "A", "position": 1})
        self.II.update({"start_position": "A", "position": 2})
        self.III.update({"start_position": "A", "position": 3})
        self.settings.add_rotors([self.I, self.II, self.III])
        self.assertEqual("B", Enigma(settings=self.settings).press_key("A"))

    def test_QEV(self):
        self.I.update({"start_position": "Q", "position": 1})
        self.II.update({"start_position": "E", "position": 2})
        self.III.update({"start_position": "V", "position": 3})
        self.settings.add_rotors([self.I, self.II, self.III])
        self.assertEqual("L", Enigma(settings=self.settings).press_key("A"))

    def test_MCK(self):
        self.I.update({"start_position": "M", "position": 1})
        self.II.update({"start_position": "C", "position": 2})
        self.III.update({"start_position": "K", "position": 3})
        self.settings.add_rotors([self.I, self.II, self.III])
        self.assertEqual("APZMT", Enigma(settings=self.settings).parse("THEQU"))

    def test_MEU(self):
        self.I.update({"start_position": "M", "position": 1})
        self.II.update({"start_position": "E", "position": 2})
        self.III.update({"start_position": "U", "position": 3})
        self.settings.add_rotors([self.I, self.II, self.III])
        self.assertEqual("GDXTZ", Enigma(settings=self.settings).parse("AAAAA"))

    def test_IV_V_Beta_B_AAA_ring_settings_14_09_24(self):
        self.IV.update({"start_position": "A", "ring_setting": 14, "position": 1})
        self.V.update({"start_position": "A", "ring_setting": 9, "position": 2})
        self.Beta.update({"start_position": "A", "ring_setting": 24, "position": 3})
        self.settings.add_rotors([self.IV, self.V, self.Beta])
        self.assertEqual("Y", Enigma(settings=self.settings).press_key("H"))

    def test_I_II_III_IV_C_QEVZ_ring_settings_07_11_15_19(self):
        self.I.update({"start_position": "Q", "ring_setting": 7, "position": 1})
        self.II.update({"start_position": "E", "ring_setting": 11, "position": 2})
        self.III.update({"start_position": "V", "ring_setting": 15, "position": 3})
        self.IV.update({"start_position": "Z", "ring_setting": 19, "position": 4})
        self.settings.add_reflector(self.C)
        self.settings.add_rotors([self.I, self.II, self.III, self.IV])
        self.assertEqual("V", Enigma(settings=self.settings).press_key("Z"))

    def test_I_II_III_B_AAA_ring_settings_01_01_02(self):
        self.I.update({"start_position": "A", "position": 1})
        self.II.update({"start_position": "A",  "position": 2})
        self.III.update({"start_position": "A", "ring_setting": 2, "position": 3})
        self.settings.add_rotors([self.I, self.II, self.III])
        self.assertEqual("U", Enigma(settings=self.settings).press_key("A"))

    def test_parse(self):
        self.I.update({"start_position": "A", "position": 1})
        self.II.update({"start_position": "A", "position": 2})
        self.III.update({"start_position": "Z", "position": 3})
        self.settings.add_rotors([self.I, self.II, self.III])
        self.settings.set_switchboard_pairs(["HL", "MO", "AJ", "CX", "BZ",
                                             "SR", "NI", "YW", "DG", "PK"])
        self.assertEqual("RFKTMBXVVW", Enigma(settings=self.settings).parse("HELLOWORLD"))

    def test_m4_Beta_I_II_III_B_Thin_AQEU(self):
        settings = Settings()
        data = EnigmaMachineData()
        data.set_machine("m4")
        beta = data.get_rotor("beta")
        i = data.get_rotor("i")
        ii = data.get_rotor("ii")
        iii = data.get_rotor("iii")
        beta.update({"start_position": "A", "position": 1})
        i.update({"start_position": "Q", "position": 2})
        ii.update({"start_position": "E", "position": 3})
        iii.update({"start_position": "U", "position": 4})
        settings.add_entry_wheel(data.get_entry_wheel("etw"))
        settings.add_rotors([beta, i, ii, iii])
        settings.add_reflector(data.get_reflector("b-thin"))
        self.assertEqual("HRWFU", Enigma(settings=settings).parse("AAAAA"))

    def test_m4_Beta_I_II_III_B_Thin_AQEV(self):
        settings = Settings()
        data = EnigmaMachineData()
        data.set_machine("m4")
        beta = data.get_rotor("beta")
        i = data.get_rotor("i")
        ii = data.get_rotor("ii")
        iii = data.get_rotor("iii")
        beta.update({"start_position": "A", "position": 1})
        i.update({"start_position": "Q", "position": 2})
        ii.update({"start_position": "E", "position": 3})
        iii.update({"start_position": "V", "position": 4})
        settings.add_entry_wheel(data.get_entry_wheel("etw"))
        settings.add_rotors([beta, i, ii, iii])
        settings.add_reflector(data.get_reflector("b-thin"))
        self.assertEqual("LNPJG", Enigma(settings=settings).parse("AAAAA"))

    def test_IV_V_Beta_I_A_EZGP_18_24_03_05(self):
        settings = Settings()
        data = EnigmaMachineData()
        data.set_machine("example_machine")
        iv = data.get_rotor("iv")
        v = data.get_rotor("v")
        beta = data.get_rotor("beta")
        i = data.get_rotor("i")
        iv.update({"start_position": "E", "ring_setting": 18, "position": 1})
        v.update({"start_position": "Z", "ring_setting": 24, "position": 2})
        beta.update({"start_position": "G", "ring_setting": 3, "position": 3})
        i.update({"start_position": "P", "ring_setting": 5, "position": 4})
        settings.add_entry_wheel(data.get_entry_wheel("etw"))
        settings.add_rotors([iv, v, beta, i])
        settings.add_reflector(data.get_reflector("a"))
        settings.set_switchboard_pairs(["PC", "XZ", "FM", "QA", "ST",
                                        "NB", "HY", "OR", "EV", "IU"])
        enigma = Enigma(settings=settings)
        self.assertEqual("CONGRATULATIONSONPRODUCINGYOURWORKINGENIGMAMACHINESIMULATOR",
                         enigma.parse("BUPXWJCDPFASXBDHLBBIBSRNWCSZXQOLBNXYAXVHOGCUUIBCVMPUZYUUKHI"))

    def test_B_II_IV_Beta_Gamma_4_24_17_7(self):
        settings = Settings()
        data = EnigmaMachineData()
        data.set_machine("example_machine")
        ii = data.get_rotor("ii")
        iv = data.get_rotor("iv")
        beta = data.get_rotor("beta")
        gamma = data.get_rotor("gamma")
        ii.update({"start_position": "V", "ring_setting": 4, "position": 1})
        iv.update({"start_position": "E", "ring_setting": 24, "position": 2})
        beta.update({"start_position": "Q", "ring_setting": 17, "position": 3})
        gamma.update({"start_position": "J", "ring_setting": 7, "position": 4})
        settings.add_entry_wheel(data.get_entry_wheel("etw"))
        settings.add_rotors([ii, iv, beta, gamma])
        settings.add_reflector(data.get_reflector("b"))
        settings.set_switchboard_pairs(["AT", "LU", "NR", "IG"])
        enigma = Enigma(settings=settings)
        self.assertEqual("ACOMPUTERWOULDDESERVETOBECALLEDINTELLIGENTIFITCOULDDECEIVEAHUMANINTOBELIEVINGTHATITWASHUMANSOMETIMESITSTHEVERYPEOPLEWHONOONEIMAGINESANYTHINGOFWHODOTHETHINGSNOONECANIMAGINESOMETIMESITISTHEPEOPLENOONECANIMAGINEANYTHINGOFWHODOTHETHINGSNOONECANIMAGINETHOSEWHOCANIMAGINEANYTHINGCANCREATETHEIMPOSSIBLEALANTURING",
                         enigma.parse("BHCHRJCBLHJBPWXCAPXQCUAZRKBBTFEXBQWJFGVATZUJLXEMZRLOJHFWTMFUCAGFOHNNCPIOCJKAHJTWLWVHFJAQCZDXAHHMLSCRKXMJTXYFPKMBJFFLSNAOYYWCUOOPCBJGJUHFVOZOJNSNAWYMTCKBKAHQPYCUDPFZGAGIOHLKYTSXUOBDCJSGLMDCOIXJHFIUTCBVWOXKROVLBFVSYXBDJPUOIWAZEPHNUXRDVDKFFRXOXXHOVFUGZNAPNNJEOACFBSXUDDBCDWVFVIOOBISLKCDMRPDDCTZXNVWMFZDGJXUGC"))

    def test_very_long_MEU(self):
        self.I.update({"start_position": "M", "position": 1})
        self.II.update({"start_position": "E", "position": 2})
        self.III.update({"start_position": "U", "position": 3})
        self.settings.add_rotors([self.I, self.II, self.III])
        raw_encryption = "gdxtz fjebg zkljc szrlf djdil gzjvx ldong dseit voulx lyzpc dunrq qhrmg qkqxl sbbby psiio otnoz xmrfk mbbzy hcxse rzpzr xpvdg rnnom kcbrz bohdh pcdbm xvlyv oefsz snvhc nmzbr rqqre ddqxe qzkvw iqgpn mwwjt vtusx lnque bklld uzntp lvvpf mqvnb jvdyj qqyzu jfkuv wvixt ullpk mwtpw etflk ueesp svmeo shitx swegg uyjmq gswnd dliex rqdin qgpey wxhhd mvnlw qftfg fjelm vduvx lhqbu kunmo nhutg flmns mljku ktixr zhjfh vznrd vdqpx xtjef htrse tkcqi gzrop ztmxf tukmb oyuum bhluy etmjq bczwf yuvsc ezhqf hnbkl gsmoh fcgdh yvpwx fwidy nxlge lgcvj yduon diris olbky stwfe nhfch klhgf gygmw sdczz zvfip ddhof knbme rwcow fywjq fpdrq csteb vvvkz vufht ilgtj dfvsr dolse ezxmq guppx suumr lbkyp tlimm ssjvh efrtk nmmxm mfeih snxuu kmifl klvwe yqrvp ogwhc cnkep vfbhl snrqr lpeff xigpr mqdxh bbmih jnwgi jjitj kkbfz hycjd nkcdq krmox iwtov bltum npgmh ynzxc vkefx cqvku sfkli nbsbr bshtb opeeq bnges rwsqm hwbfb grslx motsg ityhm ggghb ibozg yijdi fzequ ythjq usehf scvul okllt hnbnl gsipq iuqxs dvpln lgkip tnipm ckjpn ctewu hgcvp wynxk dictd jxypw dhdtu blzrt uuuwt dmhwl fqcym crsol ssvgd bnhrp qmbem ddlbo lzwgc zyiul qsrqt lsnkg ukrrt dbtnj uhybe ztnvs hljnd zjnfu kospe qwctk kyoec mecwo pjrig jutnk shhzm gcgwm yvjwf drril drgfx fxfpk wmcqp yylns grnyk wtfpy punrw zppdr fsost csodg rbvrs oxkbm qgfvs fwscn teshq ghrbk wqczm jsuvc etiug ylkkj gtgnl sydst dsvdz xlhsw vyroq lueed zydwy ogdco nlune hdygq hpiqu vnwom vmoii dnhil ingox beykp ngrqd kthkl icjpb yzkwp otlsy wnpgu kkeyu jmnnx sbhfb nzvyb fdqnx gvisz xxmgf oqdlf hixse repqz pcedg tmcog fucvm uyzqr nqhvm tjlnd frbsd eykel rtuwr lqnke wdrdl gonqw mftsh qpfnm vuutx lqqtm cnjfz hhftg tghtu mcwzd ifild ypwrc bodxr mqory qidup tebws sxbvl rvshs dgosn wxtrk qjgei dmxws orlss bmzot uclrr jquje gdlsq joknp jymfd dwhhu sdrvd compn orgpg krnrk toqqq cgvhb oqzos htcrf jquhe lbizg rqwjc upkji expjm yxbcf njuhd hliss rrecu czgob ygklu hymev kyikq lnnnv jpjfw tmiho mxrvf obfls sgrib cqssz bqleg bgwon fckei igbhy eqlcq zcbnh poqxq xhfem hgprm qrxhs bwihg pjhit oncid cyybw bdmsn leofk ejzql dybdz tedjc lznpf yifid mniwv gciik ybcsj egwiq jlhgi hpett kdgfe tvrvv yqjnu lvwoj qjjrb jqzmn pcisj ygcoz lpfdi ejchz csjmp msmle fngxt eskpq nrwgh supkn dqbgz tdhpo iletw sofdd ugrtp jqjqp ugkji serhe comkk czocv edvrv jorob tztys cdwus nmqqn muhit gydeu fmshr cvciy pwlgw scyoq mrrvt ijyqj nufvm fjlrj doisc otluh btumr jquie udzvc jyeiw nbvzc cgbyh kuvtt osqqv wzhsj grdlx distu ckovl fozke ydwho jbnoo nqijh qpoql ptwsc eqobv mopjs udvvn ewxqp nmyvo mjyew nglkh qmgyh kdjkd ipevb iozjf vyonp josqp vmrqj qfngd vomji ftfxg rywuy xpfzs egths oqbbw xhcuf nzevb yzjeg kfimd fdmve cwpic fpydu qjytr ilulf kgvtw flspy xmoit inmiv gycvq bnyqv cgjnx zwbgo sxgsd dhjng gkhjg qgspe bhlxb yfvon xhuii rffig nnxfz feiyi nceuw ubkzg kglgk idtvt oxwhp cjvye icdid lewkk vjgob hebye hepss dqyyc gdhjr iqeve gdqid zgcwi psyii dnmiz dlpnr bkgpx nverf nbyxp vvxrz sqpnm wvtxj qwrow lismo nisib ghubt ychgg mxcsq rwyrm miktg imcet wsjjz flsqz oybgf gfbjz dohyf yixhn xkfgz pgsjk onlcd ivpqi svrbe cmoel yycdg tbvxv yjsqt fgohl vqtjc heqcn bmcrk hujsx bfzoy lzdur cjlgt knpjg fsfqp rnyku vtdoo mtzfi hrwfu hvifw cclly jxuzi jwizu joqxi omzri qptuz ksvru omgtl nihhq itckx iyjdh poile iwcgg pxngk yuxfw jsswh fnstr sicfy mxosp juhlj dtbdz exomw odnuy lpfuo nufks zzdgp szzxn ogluy gowrb ulobw boxer qpslu teshl gtqtk rlkiy cxwru cogby hbgbi jsfts oqzbj chlbv zqjgs wftws dygyl cxwzd obroo bczxf dhusi rezcm bhlyi gefir upeic kqzcl hkclt zgqhs lkuvz tgfwd vsemt qonlb vcejt xongl shcmg jyiog krtqs neidg fclkv ejoyj xdgok rqimd fsmmn dlwrs tmryb sztjf uvfdh pcnbb bcffv rknku htmnm wydmh ejhdz joukw mcjkl lspse knsnj tksjg gypoi slkuj zbtxc tiuqm rntgs mytee hyprw jbvgf svidq nsupt mjhec ehqbm upyob qznmx idejr fqwrm fulum uxegz rnvxu oxwvi mdfym dkkdc qzhip juhhd jsvtf loklj tomcv qxthc snjmk jthor qrjqu tesdl sejdl vxtiu pbezt utdxp wzbcz ycxvw kneko wfcdc rygyd xvdip upqmh pxwek ecixw ywwwd hpcyb puinm vxqqz rzurn mqtuc hkjjg zzeur tnegi eevkm tsjyk kimdf hmvum vmsrh pwoqq kjsqo jesur tfcmq mltsu cwyqp eimfs imowo clnkh fbfwp cxrwp ledxw sltxw ocljk kqinq exvey gunvr eoily lxkws tlfyn rqxgr cglcu hhyqw kimdf ymltz hlgym ohuhj hobgk qubwb dqsjl xovzt oxzoo pdbvz rqxqs nrfvm ejlso bgrgw ldwku xgxke cwowj rkkte lkrtm nqrde oshjx xoelt psrsd ooorl qbcxt cykcy dmzoz putig plgoz sooxo nqgkd bbziy ecdms dlgdq ncwpb czhgy cbgzy yxndk qdfzh dpniy vdpis tqxdp zmzdx bgmhi sckrn ylkbe zwssd tzszb gbxfy hwbug iorvc irkxo ugjhu qqmgv lyjxt zrvbs znmfm vgpem hrxeb ukihm ccdgb jzqnu kdrim dfbml vnukm durce lnurg gqkvk bvyqo vtdhr zhhib ewwbb zzrkv imdfh mvcfv cbptu onxuh vvhbv hqpnm tvssj njotm oxhmw gkktt uieyw xejiz oczyp ctfcm pmuvx yvlqh ncwvu wjpsl kfuks pwemk stupo olllw gooyp wpsuw willo txnip oclow wrqls lgwqp rpkqr wkfer qvhuc xlkbo ycwnz mrpcn wvyfu qzvpu mxlkb gtndi slkns lhstn llnnh gctys olsfe tllyc shlub nipej nfkzr ufxqv xuhcp jbezv buwcr wpcmf komxd vodhi ukmmc bezef sjxfw orpyy vycnv hvtmi vvkmg ebjpf msrch obxqf bwhzv eiosu jlrww cdqkd lmjfs zweoz xbmzr oyozu jtubh dsvpn jznjv gbizh iclqv yrxqn ilhef beltm wquon rfbuv slkkj gthqb mrpjq lvzei roqpc swcjz unfdh tfhjz hgxrw zqppd zmcgu htuqz zwclg cnmek foneq pumjd kpjgb putim vbzfr ftblz jfwzf fyixm nxbcp zdegw hkiji bvzks kqwnd ivplj yhwwv mjhmu gguhu izimd fsmin knnus sklvz lccgv pyodt psqbe pdryv bbjob xxxdi hjhzj kfjgr tsenn igohn hosgn miqgz sbryc cixuh ntqox yqosv wfmis jvsur xlhfb ihqfn klipo nmpqz tvvqu pxlnp wntkv jjeet gvbiz jkdjz fzmrv ueemq emojg ucsql ygnvl fkgkt lnrjl gsnlp jzwcs evpcn vxuwx lomyr yppnc ohxsg jgtow jimdf ymisd ijfdc klfnd mdtxy xefvi bwnxp lsciu rrdml tjrnd ftmbk bjgsq vnorp oxesb bxzxj owwfr tqsye tdcmj fjkzm zcuvh ywhrq imdfn mdrgf oqzcm qgneb szkuq nwvcb pklif ukoey jwbdx kbizm qesrr qrctq egdpu dctkf pfdqp leixd evepp jtbse dyrhv lzseq pnnpo wlduw eltgb tlied rtjco noklc cgzim fzvnd yicsg gdblz fbrmm dgzhz rqwkx zvfih cfbpx jmxen blzty sjdtw hwqyd osyco onudx ipgcn zkwfu fppgh eqify sbrzw neslc bzyof bwivh cnssn gclwv yhblh xpemo plxgt gcxtq wdrtq pbrxv mveuh xlwqx kvnbk buuht ptdwm fmctz srfjy pqlgr wcxmp kembj fiduz tzlhq zxcvi dqfkg tgrvk gwzpo plmmw looew zcdqt nddbj zdoxs neght ysjfk dnmzj erpuo milnp chnjk czzue xmdqd mtydd vklbu xyehw ckjbj rmdqj szmgs kdrdn dmxui teohl rpmrc jphgw ztjjv qowmq cnoyv rkjrt lkpie etonv vhgkg qpnmm vvujv mhxxu wwgfe xsqgi ykcvo lorqm jtshh unezh dhqpr kxxqe pjpvx trqxv zhfou blzps zhllo klhtm wwled gwrpj lsxyk ghibu ethvh omoko zenpy knqon mlibo zvybj dpfuj qtblt nwgfq pbcww yycxo yirxx xvlkw tnewm dotqw kxukt jghvx lstlk upmib qzfgs vqpoo lljwn rdzqk mmopj vtcbl zgtmd qppkb omrqy vvrsh uhgkk jjctf ewwdi jjlce gyooz dtoht vnunc rmpom bucvn nxxbt bynun qpeki vjlxk wttsf yibfl uxnkp cbmzy lqevs urxlp xfqce ucklf ipebj zqcff jiuln xpchs jwbhd yzcvh nyjiv nqgpj ybvnr qqvyd szynj lrvpo orfqg jeddv gqrzd gtobr zdomb qhgjh uzqmj slujf ryexg fwqsh wrqnk gjgyf umtms oozzo oydwl dtuxk lvnko merle thkmo pxvce wwuwj imdfy mksii yfxkl vfnih rxwve gfvib znxhh brhtm orcvn lurfl ojimd fqmub vieee gsjpu tlewg qpmln kkftk nihgz sbinn wongj tjmfp qmptx sxcvi uvmor gphfm hfbeh pdmvi xlbzb ixysr dmlll rnifg gstrs zcqvn qrhev jfmsu qpinf eljff gsrqw ebjlk neivg fdieo tuxkx vwjoe gydqt hpqdy itebn zdemc izelf bvnbw nwcdj rkonl txdqc cizew fznls cpsbx wdiky rsrjr qxser hpwqm jrswz szdin qpxrr pjnng kfywe higdw lrfdl gecbr cyljh fclrw wxevl kzlry tnyrh ftudc zzzmf bbzjr dywuu ksyhy gnrfg ultnv hpydp whtqe pjepr qhowt wnhgc fyomz yswyg dqizu klvmg tkqun tpvni jrjkf lrmtl kmwhc yedyz xzoic rzbxc ybbxb uxfyu kjtgl dkvvt tzkcf hxpjb bnxqp iemce jvfbr rtcew ubuzb pjdwp kleci dezwz kjomr wddpm ocmzd ukxgf xyebw yhjqt hrjze obmbo xxrvg mhuqb nyrvt rjdrz gfcyw gfjkx bieoe cwooj rfhbp cdsnz csllu rngou khvcd ouevu kphqz wuhyr dhtlt zblbn fsjqz oneyk limtm bizwf sshjj umzqg fjhjc nfpji pmecu yzrve uhxlo mqksi whmzs bwzcj cuyfy uxtzi gecnl gpmoy rmylb tzidc vlunx lzfls jmmgh rhcgg hyfds kviue xlibg ehiek pxvdq msrwy onvfu gxlez vcdpi rwhke vijtc olwyw xdjip llsqo oujsc zueui qlmer fqgle udert eukjz evtev iwskm tpsml gveeq coxwy yxnmv cqpiy suvtb chfft juqqr jydnt vqiri emcvz bqfwf ebwqo brupl ecbkz jfiwe chekk yokyi czexz udkee ohxyl xkwit dzyco dzucz vjydj wcolx ylxnn ieeif lgdre snmrv footu srtqs tesds zjqoh edzzs prnod rqciz eofdv nrrcz kdpjw smljw ybfzt ysbdo mcxlg eneiu hhmit oymic fzgef jglse xxjkl lcbpz ykecg prmqb xypgp ihnzp ddiqt wnrqm vmyox quwvn hzdws mjipl smwju nycez hjfnn ikqks opsmo qcnmu ftrrj quheq duxyj bnrkv ldvdb hexoi mdfnm eoxfv qnchu hpwgm jsmff doplr biycu kvptc equmd wfedv xlike fthub wmfds vcmpl umbtf ttdhp cfbqt xpvvb stvte ipvvd mhwqp nmrvc hjnxp gizxi feeox mtuyw gcilk nzhcj kfcpw tcqmg ymyid nzgzf ycqgq xuftb cuhcu qkysv btksj ggjto ybwlz zmbwx otvlm qoqrn qrvtr jukdr dgtts jpyhn kdjgh hcvqc jzixm yjljl sjses nkndb zbzbs ynmoe ssitp jegkc gcwyw ygxio iomde jcmyh ubexj vkvpf whpjm oztyo gwccc zbzuc bvzyg solpk mitdc fjhbz jhili oniej blhpx mwoxy gyjic wigmc srmuo nysig ghieq ursyh wcnwx qeviw fgdcw hijeq zhzbc bzlzy ixuon ikvph ulrkq jtfgo jqdgm ozyty cfqpl cpoll nmwbe tzyex wfcsz zujsd ozzub tyuhg tmrns bumde jctrn yukjm qophu vvnir fvezx fgfej cuotr fbiyl nxzqc lgemo qszbx zvjes gqbny pvgij rhhne nshmk gfcuh crrrq qdeid qzoox yugqu wvcfd hyilt kseth kbgoq pvmir csoiy luhcj rfqsr zggjj fgmoi qzzdi fbhmx sbryu chgbr olkgk lkqbv zbmwj kxeeh hpppx kvqfn klquc ygfyg edlzk zcthp bbwuq timtu hjckv pydlz kzctc rovxx qbtco eeuyg qjdww fcgvk mtdlt mijqr ltwpj gfopb cnzkm fybdq fnpde twtnv tdost stcso mgrjp qjqrj ndluk dtndc exluk tdtyv nbcor znumg fbfzm ffsim dfdmq yfzwd fwklo ccvey yerqu uttjh mpglq qndut rcdoe ylnxc jbfyo rzjgn bclch swtbo zslqh vrcqo merdm hcsgi tsuhh pdgxr sergq iwejd dphxu rxgqp onmfv prqds prjbh kbnqv ogghb vxyjk todkg whdhq tlomc mjmox ikrfo ovptp odlvz wnzsc wkbmo kkqpw vukmj udppm rbpok tsvxt hocxc kusye vpoel hjwus mkqsn snocx ltusj cteme ohduu smkes uxsjf jzsxp tzngf tisun xnwxg hsyzd wjztd nhlse mcoou urvng heuvh uqztl kfvpf mejwu sjhyb rejek fhyuw qpxwh zglwk dztbl hdohp cyxxe wtyxq vcwmb oyvuf zhctt puvjp pzomw lsett fsgug knibw tstrz dlmdj wrovx hjjub zweim cjjvd vssic lrnlo ehfjg szghv nyeuu peheq gglvp mwimd fkmiu rqmuc pqzgs rekon jpeen wkljl esqfn upyex wvxqv gbhhq bnynv fujfm zgpkl ouhct uhcmu lkkjg tmpkl yxreu vewif rctgk podlv owvhq mrcjm oefzw khlgb phfni kknxu rrmzp cuwvd bfzji ggfbd bvhse qcodl kdytx rexgj exifw qcpqk fjcww uvqen ygfrh tocpo hnjkj zbxls qlkbt iuhzd ibhjl ximdf umjgx yvwem ocmim uhdqf wpotl sywqt pntpw dutmb bzzwt fbzzh ycfdq jiynw mqfqs pvrmu vpzdd zpzpb gikqb vlgeh cqpwu gocjk dwpdc buldt svqgz otxcj cdywy kkevh zocsp kxfhz jqbkx qpivp qjimd fpmti eiude ocnwo dbwzq rxsdc poibr xfdtv dvwkg ikijw koebp jmusx loibi jwwho nxjbv zgkhv uptmt hssfn uzgyd wmtuk lhkft ddzpz mbqqz gcvyn rgelr ftogq kvvdu vxlvk shuzr imkgg febrz uoeng gilyl ovdlg ufebo ubdzg owcxl tksbt mcdlp bmuqo fxyhc xtgyj flinh nxshi unthe orxpq pkovh cbubt zszso ostgo tfsod bbzzl xlcyz xifgw fdzee qibmg fjbwz fckpf mgbxq civib brnco cjuvy dkmvj pfmdr mtglw fozlx gjeyy qpvpb wnckv klztc bdldc tsnrc oovpt gbvbb isgjs oyhde nctnu ukcug hrevw bdjct qxxog lebzm dbrzo sxdtz szbgd cfprb zyqgs ncchg yewoh vjbyz gkdgy nneuj iwcty cytuu mboyv unnqu kksob scors uoscn vroql heuds ukymi gibsx pihnt uvggh ifqtg zxlgy qcnvn srclv pyosv rbkce xrnlg dyweb fxivk ktugk pvmzo tuogm hhzdr ekjhl efkkp oxlwb wvbyu kdtqu hdqtr evrqj mqwnd ovwlj hccxc fxrpp xmsje zcjuf tbrzz mcssn jnylc gloyc itvyq xpdiy fgefy vxsxh kegxk mmdsw bcyrk izocg mfddt mwztl ssflj moolu uqjmi jsciq vruis tltgn clgki ktzhr xenrx jhyzt lxicw wmywx dyibl erbfl wjqyw ongiq qcuuq tpphb iehtu vgceg peymw icgkw jcufk luidm jdivp jdmpg qpwit kgvib oomtn duhqp hgsqr jrnoo vpwmd nxllv fiimk ieyiz mquwy dpoul tuwbu kvmmw rlqlq sqpeu gjrcx zwpfy iyybw loewr ouvkp oztce uwtfj zqwpb qldtt srmdf lgxbx zryqk dgjrz ezmkh jnqyp djwcj fjlfn trsnc nlgss gjcdl xujbl tfgkh jgqun cqdes txzdt uwjbr ovgjs frmrw extvh iitrf ygpdu fbmhf giicn xbkef rqpgd tvhsw nbenj grhqq qcvni xxnvc ohxyg kpdzi jelwn sjisw iuidn ighvt gyevp bmzxy wvdik yvefe kmctm ruwow ucjvf ugxlc tsixt cjnxl kwvhd ddmvp imedx yzpci qpqkl overj duowr wycxy kmppl zfewp unzqm oetyf ouxtw thsyy reomu qcmit urdsf mmsor licqt pprnw eupjq exbcz njjwj cufko mqibj lhhyn cvcqy gibez fygtd sfgqy zuqxy vudry tkixz lskrv tefls noiwp xtfqm vjmyw fuptm yhczc cxofs hffsl wrsnv mlfqi pbnxw mtrsv fqspn zosul tunrv qbuek dkppn eygnv mhmee xyrqg xhwwq exygb xlepk spqsm cxsng tqspw ggoqd jhvrr ielkt igqqk omboy ouvgd htcoe ewknh hdcov qzbvb bfspq qonxt yyhxz mrodb bbhzw ydodf lpruc bdhtc rhtuh hxwjm tosyu ujziw xyevb kgfhy csglt boblv spcqo wbtrv gsgft fsdnl tmyox fugkm zzsoh xcngf ugqpe lspsm rtxst tpiun ldfif kclvs qwlqo nlyvn wjhyk bhrih lngih dmdsh ejhrz igzku myzvy opcbm zyibt zfygi dmffl fdijk llvuq pvslw eqonl yvypj qfeuu gnkrz yorex oggyh xuqpx vwzhx neyiu twtlo iqmlu ktktn frtjk rsdjt nldlx ggexs vrbzc cnhbx zsrgn eftmb bzykm gkhjg qvxxq vyojb dlkst enmds jmioe quyvn ihifc bntrw vvjkx wfnpg myycx cxxqp czsuh ccsly tunrq qpkej drqyt verhp leewc uqhrw wcdlk klqhl ggbgz ykydb szjwx glhny qbemx bslrn nuhmj drtbo himdf dmjxv ukfor litbg zigxs qdtzs zwgcg dexpo kicym duqsw expof lgjwb tmvqs ntyrx vykjt fovyk lvnfo fblsl ghkdq oipyl pwzib imdfp mmiwl sywnl hpreh yjdxm fwwcd vkklc ywwtm obvrk kevjx wjqun tyvec jibbl lbtgs ebvzn nwuwp cmykl jfyew xprwe lpwbv zekyq rnqbv vqjts onppd zdqtq nhlrq mroqn udvnf dezcu bfqbo zwlgj ofbiy nnxci fbbld qtrzp hhxbs cctrs qbgzj hrsnt pmztq bxzqp ujbdr pqhbc etmxv jecfk mgxkc vpile ywxbj pwqez tdxgh sijpx ggkeo gwhdj qgldb qzwyt mzjhm kbiyg iehwc ejdrx gvxzn fozxm jksqq ziefw gejds mhtsz ghewb zzqde tukhc jouzr upwmt mihum dkotd lffud gpifb qypqd vrjlh lvvqp skceu kwvdj oylmb qshvz utivl sxvpf ncjzu sfcyh dxjww qkvtd qpphz xjuyt xmheo wiznb gunfj ybjzh owkfl inynx xfjjl kydzq ijclf xkrqx jeuwp hebgy jwqhh ipvrm wthtv vwudx lnlim okjyd ygszf lwniq gkdvv uolfi guhhy uowxr kyour mrkcv ovors sguih ynfzg fmoui yglnu gtdyd wkgff zstmo kldte jltxv xuwxl mrylj erluo kxukt sxhpj cnzkw fpsmi osrpr gtltb gzivg mxqep zpckf dxuvc ugqke wvfxl czwpc mwkhk btnee obsmo pbwzh flgrk qjgeq dfmsh jxlge dwwxg vpkij hfcer vkdtd ppjzo lxjyv tqkrq sprmo cysls tcecw bcvpi uhvpi sveuh xlucz ksbyi qnork ykgqx rqegw ibjmx dltni hnyry extqp ilcwy cxdkz ftpzr rccuc tsvuw vpfop bmymx uyini qduph huqgy regoy lwkdv tilvw bolqb midmr hhcde iyixe einrz bdkyw rjclr juoxc euuft gwhun sblgs qtzgp ermge tuewk cjgkl edweo ulegm bkzfl ofdok tvsko qkrze mhstr uhlfe rfwou kdvvn ojbvf uthmo qoiyl dpczc sylxn pimiw llgwd strso nwpnz iccez hffzj wkgfb nxkpc jtfyh kwoms oryuk ogzlg xydjr kppls ccmcy hxcii znmgs sskdj emvvl bwnkd vzuzx lvnxp vqsvy ixivd iwssd xtosl sgfgi xumwt mowxe dnmtu vxwcc oikrs udbyl xxdke onxni sgwts srbgp vnyfw blvpj kpytl hqdtc bzykf omrhs mrbvb hmugb kzjwt cyzxy ficom zbjvu xgnhb wzibg hsvrb sclzf cfxec ygxpw fmtvp dijdf verfk lsemp ivcyf durqp lxtvf ugxlb ttpre bvmkd itfnm rulmb dbvss wouow fwfiy wfejy sbihv wccov krfmv psgbq hssgc yxnjr qkwvd voglh eynhy dckfn ulrcg oiyqx peipt vglgv llxze ykbsz rqwvl unxld zmces zrfgt khbyz jrzjh fjgvz ckfix xoecw emcfk cybkh edwvb jvqqp utdou zrojv orsko cjofl jrzev xqqxv gyezv lehki kdgzh zsqvf zruoy zpopx qooll hhoim dfkmk srpod gmozu hekvr uqorw pcmzk jevhl gxhxf ebgzq ldekl ssrrk cvwre lgntq zhtrg eouqv rpbmy mxies hincc ywxug odblb hhljk ubtfq xevjg qgrnm nrorf loygq hptqs bvxwe vjlel pekmh ilgiw echek yuzkm eyxnv rwilx sceic yhxcd izhmu ksndj trypt citvy cmqop iuzje dsrvj qqlgf bhzcb hhyyx xpiyi fnzng rsuyt cbwzy qfojj fumrb yfhgj ocjez bdzgi dbxhb ubtfs dueom uzceh yutcw uowim lwkdc tblky ywqoy hxork fokec ipwmd exfls zifnl cqcbj zuuqk rqsur tpcui kptid repjc onfyo rrqxg eibpo mgzul ktnfz nhyhw cqvly vxbdi dwihc xzqxf nmpro ddvtl bsbrt sswpo slkyl qrkrt eojdh cmioe puzis gwpge fryyo nscfe znstr szcbb qjern mokfb czery codfz iznnx ovfuo buziz nzdid ingxd vpbub dgpqc vzzbf vzeer kmtul wtcsl kewor rdfry exvts blznn mbtbs ksfur ompoj niley wirgn owjlf ndryg vtwzb obwvo tcysk stmtt ssvge qmmys jedfd uonlc rwcll ykxbt wwqdz lkzbz ggfsn msvnz voulx lleuq ndxxl wuhwc xvilg jqtns ivjqj iyepi leoyz ynmjv rqngg iuymu ulmri xmqvb gzxjb ucfku vtpoe iceut htxsu honsx hmvnr sqrre jdhyw wczkl mkgse dqfns hfjgc zqppe tdqus fuhys nmxqn lslrn wcjwu hgpcz klbcx lbyzs istus tjgtp gxqdm upzrb qzggs ebczo ylndz edfeu nhbrs qevhu fhjvw kcjgk gbkmo qjiis gfkyo jilgf rgqij eldcv qecdx tnjmm nmbyd poslr twsju qwmmr iktwr eeost uvdop llbco svxvo lpbzs qkwen mrqhx jwrzd cydjb zpzby nrhfo dhtin vgbey bcszo btyzq vjmmd rhyoz imdfp meivg nlkhu foncs ehyvn lxveb qpmwz llgyi yixzz sivuv nrqgn iuvfg jreym ojbdo btzir ccjmy oxiuw ceizb mytvd tiqpp rzids zrzmc whwgc lkmod dzztc nrgyo mqopu uwvnr lgvve vcuij ubone uljku stuhx bvjbe mbcem euciu gwpem hlxuc qkibe jtrlg fbjzf ocsbt bsisy bfolg mlqfe fpxnm hdklv iuexl vwuqs ncsvp jmltn mgcst meohh uomuk hzehv htjbm zkcye tywxd iiclo bxlkn feysj qpunk zybqb pisbu komiv tbnvz jvbez kvvsx rwjce xyrqq idfth gfgnm hczpo jluhw ijuqj jedqt ebuzj hqokv bkbjg svjzo tnyod zpoyx ljcgd fylxn hikec jbmlz yxxsr dvonn wxxpe mypfz scfdx xjzwi vvxix rlznc gowyr eepnq whddo rseln uxmrc jzulf mvnlb jlmoo vxhwo qpsrq tysxi gestt zxiep bkdqt bczvr qmhoc bupcq qdbee yoxxu ejcho epotl slwfs qbjpe wgdog flonv pvygy hxiqm vnlzo irssn pkmmd iygjr jqute sdpig joxvu yvgpx qpmft kuvtr obyte lghre dbexx wnotu wpjmu ixtvn dijov xzpuc bqzyh dblsk rstke fxome gklpv dcfeg exknx gwfyk pyzyz nmoks imywb hmrqi mdfrm goxyv wwonc popue sidgu kived oktmd sshug bnwrf qoter qgdhv tqscs qcbnf klkmh qpjcd hfyix ehipp cxpxg rehnc mjgyo csusw rdtcs lgqhu osxiy rlpiv kxqzq snrov bgjmn cjwjo wxtxd ivpdm uctob hrsen fmmdh tkgff nmmbi hndgv nypju fcpfl xvcri xuwmx lgvsu rxluh idwhf hjoyx kfgiu turhd jvzzb semfu jbvco dwuwq pjdtv tusxl mttld mphwk bsxid pnzwj kyvxy otowi zyhhh hbexo tplzi wpwmd fxtlw qifrw jcptw ugivp eduzt zmhkt ebcup kzyij mtrjw ipfmn okqun fcmrk jbxgp vvbkz qjiie swrej kkfdt lknrp jlpmd vmyei qhnce vomjb stfmo zsvon jhgom jnkgj gygez iezyw lnvio nnmuw mruet hzhex uklgw kqcdn buzjr mmfjv fbrrw tcdwn bczbd zzxnm rgpeh njkuz wcurw bufjp jfcmy iyymg imdfv momep phixm hswcs xvyun jqwnd cvglj ieyqr uckpd umvgv xiqhn cevpt jnwzo lrwbl xlqsv psjvu utxlt qmihs mrbvn pibmz ehcdh zjztz shfwo fomoo zxcfc jylyf hdjvz zdscj uezes irugj icswc clokl qtzgq egoxe gbowp lcckm ysgth srqmc qlsbi jgolx uhdls hisgo hlkqy sryow tkbyu htsnm winmb ubtzs jfuol gcyxy emzct jgikf ssrru cvfcg yzrsq osxle ekjhe pobly lwgso bonbc jyyvg esici hnytx slibf eeeig qbddz hrqnr hqycq zpifw vnrox vjwfl neibh zgqlw vcbhk ywzdj pywuv sbizj sjoey uhtcj hghmb qsxdi tpqrx sotvj nvfug xlkjs vclko vqeop mhqpy ktxje uppvi tqsjx psnyt evtrh rodwz czmkb xvjgq rofdh osggn cbzhy txsfi ivnuk uxmoy tevfk utiiw edwvi jcfky xwmze hkdry ooose itwsd egpls bddxv dfuhj llhbk elsur tscjw zbjty wdvqs iplfn ddovi uexlh hbjem epmqi vpdoe mubxz xywpd niyjs kfrfy tcons yhizn ntgsn ycfgf xtonu cfpgu mrqlo bfkij gnxtv etemn klbzx hwrkm ooxje urptp vrujt pggoe bjzhb mdwgf hgrqm kzljm yjhjl gfjks xwibe fwgwj ynmuk ssimq edukn mguko bgbip sviuo dzmln xbexv jbkob wzhyc ddtzx cvqcx fywkm bxzui zrscr oicrf fjclk uiipk zsiqp bnhpj muuxk gtvij mchbc szkug nssbt qspug ucdqh bvowj roniv ujcec hpjmq zznkb lgszn mtsrk sonnb nzryq ddcrs jxdiw klncy qpygn cvult nthsp gukzx wpnhp qgmqp mpzun tkrhi xtxnl kutde zbozn lhkix jeuep vvnro jmfbx hgfgh wdebv zbyyo dizic pcnsd qsslt ltnel omroq pugil slgnc nsrdr jfomr dcrtq sdezd szdmf tuozx nwekj hvinj gueyd sotoj zimio tdhiv juxbq gnimv mgjle ftcmo qxdkf fjuxp okljg whsbz wlkgi gfibx zbjvp kfnik inxkx vvfwz spjuc dvrym oxlpk mrtom vpgde trvll icdpe zqyct zsffy hwwyl kqimb txrkp mzize jwumj trwvn jfdnt bcxxo yibgh kfvgd otjgj eohsf szklx nmgcz zrkqj geddu nnzzp jrckv fuifh tondg vcyub eyowq fykxt mdhxe edxjb fymrf ohwpm njvkl ddptu bdxtv iuexl yokqd irohi toeki hjqqv wjcuq kcgzh xjync dbwxy bnztu opemh fxtvn kiids yzxpl smjvp nfjhf ccrfe cjetq tncdm juesr kvupb mydxw tmdis euyix snvit nepsp nmkbx fglsi qnekl grdjd cmxxg bybxq slpqo zhfbp wedqp bhzjk bhrjq nzvqz fdoyo lrpot bgzfg cmkkv jgokb fpwuh eklys uxkcn eezeu wthjb pqbnf nlqme conyy vpken ygxvy vrgpz nuzxx tsnyo rnmop oslrr wczvc xdiwu xbkxp rugep iuntk ehtzk crznw nyqiv vrfei ioubt ydhhf bwrqw juyln zkhgg iqjcv zbufy fdibz lwsgq gfmbf zyrqu ktjgh hkbpg fbsgg qtlxd fiegg grhqm qhkbd fhnwx khkbg zdvpt oustr ohiop mecjt wjwuh ihqpv vvlck oztrn tjcxs kttiz onoqp dhipi meexn jtrik gdxtz fjebg zkljc szrlf djdil gzjvx ldong dseit voulx lyzpc dunrq qhrmg qkqxl sbbby psiio otnoz xmrfk mbbzy hcxse rzpzr"
        self.assertEqual(raw_encryption.upper().replace(" ", ""),
                         Enigma(settings=self.settings).parse("A" * 17000))

    def test_norenigma(self):
        settings = Settings()
        data = EnigmaMachineData()
        data.set_machine("norenigma")
        i = data.get_rotor("i")
        iii = data.get_rotor("iii")
        v = data.get_rotor("v")
        i.update({"start_position": "A", "position": 1})
        iii.update({"start_position": "A", "position": 2})
        v.update({"start_position": "A", "position": 3})
        settings.add_entry_wheel(data.get_entry_wheel("etw"))
        settings.add_rotors([i, iii, v])
        settings.add_reflector(data.get_reflector("ukw"))
        enigma = Enigma(settings=settings)
        self.assertEqual("DBMZX",
                         enigma.parse("AAAAA"))

    def test_sondermaschine(self):
        settings = Settings()
        data = EnigmaMachineData()
        data.set_machine("sondermaschine")
        i = data.get_rotor("i")
        ii = data.get_rotor("ii")
        iii = data.get_rotor("iii")
        i.update({"start_position": "P", "position": 1})
        ii.update({"start_position": "D", "position": 2})
        iii.update({"start_position": "U", "position": 3})
        settings.add_entry_wheel(data.get_entry_wheel("etw"))
        settings.add_rotors([i, ii, iii])
        settings.add_reflector(data.get_reflector("ukw"))
        enigma = Enigma(settings=settings)
        self.assertEqual("WEPKI",
                         enigma.parse("AAAAA"))

    def test_m3(self):
        settings = Settings()
        data = EnigmaMachineData()
        data.set_machine("m3")
        i = data.get_rotor("i")
        v = data.get_rotor("v")
        viii = data.get_rotor("viii")
        i.update({"start_position": "P", "position": 1})
        v.update({"start_position": "Y", "position": 2})
        viii.update({"start_position": "Z", "position": 3})
        settings.add_entry_wheel(data.get_entry_wheel("etw"))
        settings.add_rotors([i, v, viii])
        settings.add_reflector(data.get_reflector("b"))
        enigma = Enigma(settings=settings)
        self.assertEqual("ZMOIR",
                         enigma.parse("AAAAA"))

    def test_error_states_parser(self):
        settings = Settings()
        data = EnigmaMachineData()
        data.set_machine("m3")
        i = data.get_rotor("i")
        v = data.get_rotor("v")
        viii = data.get_rotor("viii")
        i.update({"start_position": "P", "position": 1})
        v.update({"start_position": "Y", "position": 2})
        viii.update({"start_position": "Z", "position": 3})
        settings.add_entry_wheel(data.get_entry_wheel("etw"))
        settings.add_rotors([i, v, viii])
        settings.add_reflector(data.get_reflector("b"))
        enigma = Enigma(settings=settings,
                        error_checks=True,
                        correct_case=False)

        with self.assertRaises(TypeError):
            enigma.parse(123)

        with self.assertRaises(TypeError):
            enigma.parse(['a', 23])

        with self.assertRaises(SyntaxError):
            enigma.parse("abc")

        with self.assertRaises(SyntaxError):
            enigma.parse("123")

    def test_key_states_parser(self):
        settings = Settings()
        data = EnigmaMachineData()
        data.set_machine("m3")
        i = data.get_rotor("i")
        v = data.get_rotor("v")
        viii = data.get_rotor("viii")
        i.update({"start_position": "P", "position": 1})
        v.update({"start_position": "Y", "position": 2})
        viii.update({"start_position": "Z", "position": 3})
        settings.add_entry_wheel(data.get_entry_wheel("etw"))
        settings.add_rotors([i, v, viii])
        settings.add_reflector(data.get_reflector("b"))
        enigma = Enigma(settings=settings,
                        error_checks=True,
                        correct_case=False)

        with self.assertRaises(TypeError):
            enigma.press_key(123)

        with self.assertRaises(TypeError):
            enigma.press_key(['a', 23])

        with self.assertRaises(SyntaxError):
            enigma.press_key("abc")

        with self.assertRaises(SyntaxError):
            enigma.press_key("1")
