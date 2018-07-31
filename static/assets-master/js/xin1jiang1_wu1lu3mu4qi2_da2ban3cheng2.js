(function (root, factory) {if (typeof define === 'function' && define.amd) {define(['exports', 'echarts'], factory);} else if (typeof exports === 'object' && typeof exports.nodeName !== 'string') {factory(exports, require('echarts'));} else {factory({}, root.echarts);}}(this, function (exports, echarts) {var log = function (msg) {if (typeof console !== 'undefined') {console && console.error && console.error(msg);}};if (!echarts) {log('ECharts is not Loaded');return;}if (!echarts.registerMap) {log('ECharts Map is not loaded');return;}echarts.registerMap('达坂城区', {"type":"FeatureCollection","features":[{"type":"Feature","id":"650107","properties":{"name":"达坂城区","cp":[88.311099,43.363668],"childNum":2},"geometry":{"type":"MultiPolygon","coordinates":[["@@@EGBAECB@BB@@BMDFLOBDJIBA@YDDN@@C@ABA@EBA@EDA@C@A@@BEBA@A@CBC@ED@@BBDL@@DLBNDJFF@@@@DAFADAFAD@FADAD@FAFABAH@DALCJAB@@@@@@B@@@B@B@@@B@B@@@B@@BBB@@@BB@B@B@B@@@@@@A@@B@@A@@B@@A@@@@BA@@@@@@BA@@@@B@@A@@@@B@@A@@@@B@@@@@@AB@@@@@@BB@BB@@@BBBB@B@@@B@B@@@@AB@B@BABA@@@@B@@@BB@AB@@@B@@A@@@@BA@@BBB@D@BB@@B@@@BB@@BB@@@@B@@AB@@ABA@AB@@AB@@@@AB@@A@A@@AA@A@AA@@AAA@@@@@A@@@@@A@@BA@@@A@@@@@@@AB@@A@@B@@@BA@@@@@@BA@A@@BA@@@@@@B@@@BB@@B@@@B@@@B@@@B@B@@A@@B@B@@@B@@BB@BBB@B@@@@@@@B@B@@@B@B@@@@@@B@@BB@@@BB@@@@@@@@@@@BA@A@A@@@A@AAA@A@A@C@@@AB@@A@@@@@AB@@A@@@@@A@A@@BA@A@@BA@A@A@@@@@A@A@A@@AA@@@AB@@A@@@ABC@@@A@A@A@A@A@A@@@A@A@@@A@CBA@@@A@@@CBA@C@@@A@ABA@A@A@CB@@AB@@A@BB@BD@D@@@D@B@B@D@BA@@B@@A@@BAB@B@@@D@D@B@B@@@B@@@B@@@B@B@B@B@B@B@B@B@B@@@BB@@@@@@B@@@@@@BB@@@@B@@@@@@@B@@@@A@@B@@@@@@@B@@A@@@@BA@@@A@@@A@@B@@@@@@@@@B@@@@@@@@@B@@A@@B@@@@@BA@@@@BA@@@@@@@@B@@@B@BBBFHFF@@BDBB@@FHDDBBBBBBBBBBBB@@ABA@@@A@AB@B@@@BB@DDDDDBBB@@B@@@B@@A@@@@BA@@@@B@@B@@B@@@@BB@@@@BB@@BB@@@BB@@BB@@BBBBBBBBB@@B@BBBB@DF@BBBB@@@BBBBBBBB@BB@@@@B@A@@B@@@@@@A@@@@@AB@B@B@@@B@@AB@@@@@B@@BB@@@B@@@B@@BB@@@@@B@@@BB@@@@BB@@@@BB@@BB@@BB@@@@BB@@@@@@BBB@@@@@F@@@B@@@D@@@BA@@@@B@@@@@@AB@@@@@@A@@A@@@@A@@@@B@@@B@@@@AB@@@@B@@B@@@@@@@B@@@B@B@@@@@@@B@@B@@B@@@B@@@B@@@BB@@@@B@@BB@@@@@B@@@B@@@F@B@DAFA@@B@@AB@@@B@@BB@@BB@B@@BB@B@@@B@B@B@@@B@B@@A@@B@@AB@@@B@@AB@@A@@@@BA@@A@@A@@@@@A@@AA@@@@@@BA@@B@B@@@B@@BA@@B@B@@B@B@@@B@BAD@@@B@B@D@B@DBBAB@B@B@D@BBB@@@B@B@BB@B@@@B@D@@BB@DBDBBBBBBFB@@DBFBB@B@@BFBB@@@B@B@@@B@@@BA@@B@@@B@@@B@@BB@BBB@FDB@BBB@@@@@B@@@B@@@BA@@BA@@@@@AB@@@@AB@@@@@F@B@@@F@D@B@@@BBB@B@BB@@@@B@@@BB@@DB@BB@@@B@BA@@B@@AB@@B@@B@@@@@BA@@@@B@@@B@B@@@@@B@B@BBB@@@@@B@@@B@@@@BB@@@B@B@B@B@B@@@B@B@@@@@@AB@@@@A@@B@@@@@@@@@@@@@@@@B@@B@@@@@@A@@B@@@@@BA@@@@B@B@@@@@B@@@B@BAB@@@B@@@B@@@BA@@B@B@@@@@@@B@@@@@@@B@@B@@@@B@@@@@@@B@@@@@@ABA@@@@@A@@@@@@B@@@@A@@B@@@@@@@@@@@@@BA@@@A@@@A@@@@BA@@@A@@@@@@FCD@@@DAD@DB@@BB@@@@B@B@@@B@@@D@@@BBB@BBB@B@B@@@@@B@@A@@@@BA@@BA@@@@@@AAAA@@@A@ABADEDABA@@B@@@@AB@B@F@JAJAH@B@B@D@DAB@F@DBDBDBDBBBB@BBD@HBH@D@@@DADABADAD@BADCDABA@@BA@@B@@@@@B@@@B@@@B@@BB@BBB@@BB@@BBB@B@BBD@BBB@BBB@@@BB@@@B@B@DBD@@@@@BBJB@@B@B@@@BBB@B@B@B@@AB@@@B@B@@@BBB@B@B@DB@@B@B@B@BB@@B@@@HBFBB@@@BBB@B@BB@@B@@@B@BA@BH@J@H@H@DADEBADCD@FAF@HBD@D@BADAFG@EBABGAEACDEDCFCHBDBDAF@BAD@DFDDDDDBDBDABBD@BBFBDBB@B@@@JBJAHAH@FB@DADAF@DBBBBBBB@D@DCFAFAHAHAF@FAD@DADCDCBADAFAFD@F@D@F@DB@B@B@D@D@B@BAHAF@DADBB@DABABADDDDBD@@BBB@@BDBDBFDBBBDDDBBDDDDDB@DAFADEHEF@BEBABADBBDB@BBDAFBBBFBBB@B@D@D@B@DCDCB@B@B@B@BBDDFHFHDHBBBBF@D@FABADCDAFAFANEFCDE@GAAAA@@AAAA@A@EBCB@B@BAB@B@BA@AAC@C@A@ABCB@@AD@DBD@DDB@DB@@DB@BD@FDDBDBB@BB@@B@B@B@BAHANCN@LBF@H@FAN@@@D@D@F@D@D@BAD@D@DABADABABAHAF@FBDBDFBBHHDBB@@@FDFBDDDFFD@@BB@AB@DADADAD@DAD@H@B@B@B@BBB@@@B@B@BB@@D@BBDBBBDBB@BBDBDFBBB@@BBD@D@BBF@B@BBB@B@@DDDDDBBD@@BHBFDFLFHFF@B@BB@@BBB@@BB@@@DB@@@AB@@@BA@AB@@AB@@A@@@A@C@AAC@A@C@@BA@ABC@CBCBADAFAFAD@DABABABE@AAEAA@A@C@A@@@@AAAAA@@AAA@@AAAA@A@@@A@ABABA@@BA@ABA@ABABA@@@@B@B@B@@@B@B@B@B@B@@@@@B@@@@@@@BB@BBB@@B@@@B@D@B@B@B@@@B@B@@@B@B@@A@@B@BA@AB@BAB@B@B@BAB@B@B@B@B@B@BBD@BBB@BB@BB@@BB@@@B@@@@@@@BA@AB@B@DAB@B@B@B@B@F@@@B@D@BBDBD@BBB@B@B@@@@A@@@C@A@AA@@A@@@A@@@C@AB@@A@AB@@ADAB@BABAB@BA@@@AB@@ABA@ABABABAB@@@@AB@@A@AB@@@B@@AB@BA@@@@@A@@AA@A@A@A@@@A@A@@@@@@BA@@D@B@B@BABAB@B@DAD@F@B@BB@@B@BBB@DBB@BBD@@@B@@@@@B@BABABAB@B@BAB@B@BA@@@@BA@A@AB@@AB@B@B@B@@@B@BBDBB@@BBBB@@BBBD@@@B@B@@@BA@@BAB@@ABADA@@BAD@BAB@D@B@@@B@BB@@B@B@@@@@B@@@BAB@@@B@@@@@@@@@@@@@BC@AB@@A@ABA@@@@BA@@BAB@BAB@B@@AB@@@@ABAB@BAB@@@BAD@D@F@@@B@B@DAB@B@B@BA@@@@@AAAAA@AA@@A@@@A@@@A@A@ABA@@@A@@@A@@AACA@AA@@AA@AA@@AA@@@A@@@@A@AAC@AAC@A@A@A@A@AA@@@@@A@@@@@A@@@AB@@A@AB@@A@A@@@AA@@A@@@A@A@ABA@AB@@@@@@@B@@AB@@@BBB@B@D@B@D@@@B@DBD@B@BBB@@@B@@@B@@@@BBBB@BDB@B@B@DAD@BAD@B@@AB@B@@AD@@@F@BBBAB@@@B@B@B@B@BAB@@@B@@@B@BA@@@@@AB@@@@A@@@@B@@@@@B@B@DBB@B@DBBBD@@@B@@@D@@@B@BB@@BBD@@@B@D@DAB@B@B@@BB@BB@@B@@BB@@BB@B@@BB@@@BB@@B@@BB@@@D@B@D@@@B@B@@@B@@@@BB@@@BB@B@@BBB@@@B@B@BA@@B@BAB@B@B@B@@@@@B@BAB@B@@@B@B@B@@@B@B@BBDB@@B@BBD@D@B@@@@@B@@AB@@A@AB@@A@A@@AA@C@A@@@@B@@AB@B@B@BBB@B@FBB@B@@@@@B@@@@@@@BA@@@@@@BA@@BAB@BAB@@@@@BA@@@A@@@@@A@@AA@@AA@A@@@@@@B@@@BA@@B@@@BAB@BAB@@@@@@A@@BA@@@@@@BA@@B@@AB@B@@@B@D@@@B@BA@@@@@A@A@@@A@@@AB@@AB@BADABABABABA@@BADA@AB@BA@@BAB@BA@@B@B@BBB@D@BBDBD@B@B@B@@@BA@@@@BA@A@@@ABC@@@A@A@@@AAA@AAA@A@@@A@@@A@@@ABA@@@CBA@ABA@@BCBA@ABC@A@A@@@A@@@A@@@@@A@A@@@@BA@@B@B@B@B@@@@AB@@@BA@AB@@@BAB@B@B@B@B@D@D@BAB@B@B@B@@AB@@@B@@A@AA@@A@A@A@@@A@A@@@AB@DAB@B@@@@@@A@AA@AA@ABECEAADC@ABAD@BABGDCBABA@ADCB@HGHEBADG@C@A@EEKAG@A@AD@@AB@@ABA@@@A@@BA@A@@@ABABA@@@@@@BABAB@B@@ADA@@DAB@B@BC@@@A@A@@BA@AB@BA@@@A@@@ABABAAA@A@@@@@AA@@A@AAAAA@A@@@AAAAA@@A@A@@A@CAA@A@@AAA@AA@AA@B@@C@@@A@A@@AAAA@ACCAGA@@AA@@@AA@A@@BA@A@@@AAA@ACE@ACC@A@AA@@A@@A@@AA@@@@AA@@@AA@@A@@@@A@@A@AC@@@AA@@A@@@@AA@@@@@@A@AA@A@@A@@@@A@@AAAA@AAA@@@ABA@A@A@A@@@A@A@A@@@ABA@@@@@A@AAC@@@A@@BA@A@AAG@AAA@A@A@@@CBC@A@@@@AA@ACACA@@A@@A@@@@DC@A@A@A@@@A@@ACACAA@A@A@A@A@CBC@@@A@@AAA@AA@@A@@C@@AAA@AAA@AA@@E@A@C@A@A@AAA@CAC@C@@@@@CACAAAA@A@A@CA@@A@@@AA@@AAC@A@AAA@A@CAA@@@C@@@@@AAA@@AA@@@AAA@A@AAAAC@A@A@@@A@AAAAA@@@@AA@@@AA@@@@@AA@AAAA@@A@@@AA@@A@@@A@@@@@BAAA@A@@@@AAAA@@@AAAA@@@A@AA@@A@AA@@@@AA@@AAA@AA@A@@@AA@@AA@@@AAA@@A@@A@@A@@CBA@A@CBC@C@@@A@ABC@@@A@C@C@CB@@C@A@C@C@CBC@E@A@@@A@A@A@A@A@@@A@@@A@@@@@A@@@ABA@A@A@A@A@A@A@A@A@@@@@A@@BA@@@A@A@ABA@A@@@A@C@ABAAA@@@A@@@A@@@A@@@A@A@C@A@@@@@AA@@@@@@A@A@A@A@A@A@A@A@A@@BA@@@@@@@@@A@A@@@A@@B@@A@@@@@@@A@@A@@@@@@@A@@A@@@A@@@@AA@@@@AB@@@@A@@AA@@@@@AA@@@@@A@@@@AAA@@@@AA@@@@@@A@@AA@@@A@@A@AA@@@AA@@@@A@@A@@A@@A@@@AA@@@A@@@@@A@@@@@@B@@@@@@AB@@@A@@@@A@@@A@A@@@A@@@A@ABA@AAA@@@A@@A@@@@A@A@A@@@A@@@A@A@@@@@@@AB@@A@@@A@@@@@A@A@A@C@A@A@A@A@C@A@A@@@AA@@A@@@@A@@@@A@@A@@@@AA@@@@A@@A@@A@@@AA@@@@@A@@A@@@AA@@A@@@A@@@AA@@@@AA@@@@A@A@A@AAA@A@@@AAA@@@A@A@AAA@C@@@A@@@ABA@@@A@@@A@A@A@A@A@@AA@A@@@@@@A@@@A@A@@B@@AA@@@@@A@@@AAA@CAA@A@AA@@@@AA@@A@A@AA@@A@A@@@@@@@AA@@A@@@@@@AA@@@@@AAA@@AA@A@CA@@A@A@@@AA@@@@@@@AB@@@@A@@@ABA@@@@@A@@@A@@@@@A@@A@@@@@A@@@A@@@A@A@ABA@A@A@A@A@@@A@@@A@A@A@@@A@A@A@A@@@A@AB@@@@A@A@@@A@A@A@@BA@@@AB@@@@AA@@@@AA@@@@A@@@A@C@C@ABA@@@AB@@@B@@A@A@@AA@A@A@@@@@@BB@@B@@AB@@@@ABA@A@A@A@CAA@AAC@A@AAA@AA@@AA@@AC@@A@@@A@AACA@@A@A@@@A@@@A@@BC@@@@@ABA@@@A@AB@@A@@B@@@@A@@@@@@A@@@@@@@@@@@@BA@@@@BA@@@A@@@A@@@@@A@@A@@@@@A@A@A@@@A@@AA@@@A@@A@@C@C@@@A@A@A@A@ABA@@@A@@@@B@@@B@@@@AB@@A@A@@@@@A@@@@@@@@BAB@@@B@@A@@BA@@@@@A@@@A@@@@@CB@@A@A@@@@@A@@@@AA@@@@@AB@@A@A@@@A@@BA@@@@@A@@@@A@@@@A@AA@@CA@@AAA@AA@@@A@@B@@AB@@@BA@@@@@A@@@@@@AA@@@@@A@@@@@A@AA@@A@@A@@@@@@AA@@@B@@A@@@@@@BA@@@@@@@A@A@@@@@A@A@A@ABA@AB@@AB@@CB@@C@@@@BA@@@@@A@@@@A@AA@@AA@A@@@@@A@@@@@AA@@@@A@@@@@A@@@@BA@@@@@A@A@@@@@A@@@@@A@@@@@@@@AA@@B@@A@@@A@@B@@@B@@@@A@@@@@@@A@@@@@@A@@@@A@@@@AA@@BA@A@A@A@A@@@@A@@A@@A@@A@@AA@@@@@A@@@@@@@A@@@@@@@A@@@A@@@@@@B@@@@@@@@A@@@@@@@@AA@A@A@@@AB@DABAB@@CBC@C@A@CAA@C@@AAAAAC@AA@@AA@AA@@@AA@@AAA@@@@A@@A@@A@AA@@AAAA@@A@AA@@CA@AA@AAA@AA@@A@A@@@AA@AA@@@AAA@@@@@CA_IGCGGECAGAIAGEGIGCEACECGAMCMEOGECEAE@I@ODWJSDOF]RSLMHIBKBGACCAEC@IBGBI@CACAAG@GACEAE@S@KFKDI@IBODG@E@C@C@EBMFGRCHQ^[hCL@PDPHNJHBNBJEF@BHBBBCDIDQ@GAI@E@I@C@CDIJA@CCEAE@QDIBC@C@GAEAE@EAEAG@KFEDEBAAAICA@@@@AB@@A@@@A@@@@@@@AB@B@@@B@@A@@@A@@@AB@@C@A@AB@@A@A@@BA@@B@B@@@@A@@@@B@@@@@@@B@@@@@@@@A@A@A@A@C@C@CBA@A@GBGBEBA@GBMHE@IDGDGDKD@@ABCB@b@Z@XBV@P@@@@CDAFCDAB@@SFoL[HaHCBA@CBCBA@CBKBABA@IDE@ABA@EBCBE@MFIBIDIBCBCBA@GDIBIDA@GBYHIBaJSHMDCBA@A@A@ABC@@@ABEDCBA@A@AB@B@@EFCDAB@DAB@B@B@@AB@@@@CD@@@BAB@@@BADCDAB@DABCDABADABABADCDCDABABCDADEFAFEFILGLABEDINABEFABCB@@ABABABCD@@@@@BA@ADAB@BABEHCDCFADABCDABCFABA@AB@@CBCBCBA@CDEDGBE@I@C@E@ABC@CBED@@@AAA@C@A@A@@AA@ABARAbEAI@@AEAC@CAG@A@@@C@@@@ZH@A@A@@JDB@AKFAEECCIBKBE@@@H@DNOCA@KBCKG@_F"],["@@J@DAFCFCD@D@HBBADAJEBBDBB@DBBBB@@BB@B@BABIB@BCLAF@H@FBD@@ABADCFABADCBAB@LA@@@@@AA@@@AA@@A@B@B@@@BB@@B@B@BA@@B@@BB@DC@ABA@ABEFC@E@@@AT@@@@AB@@A@@BA@ABEB@B@BA@A@AACAAA@@ABA@@B@@@DC@A@@@@AA@@A@@A@@BABABC@O@KACKCA@C@AAGA@ACAA@CAAAACQMYSGEGGKMEBMHCFABIDMDQFIBC@I@GAC@KFA@IDIBMBQBGDEBGDEDABGH@@A@E@C@A@@@SLC@A@MAG@IFYNEFEF@@CDEBIBCBMFIBA@KP@BEDABCBA@IBEBmT@@EBG@GBE@GB@@GHKLEDKDEBEF@@EBC@ODMDOBIBGDE@aJGBC@ECE@EDIHC@@B@D@H@@@BB@DBB@BBBBBB@@@BBBBBBDBBBB@B@B@B@BB@DBDBDBBDB@BBBBBBB@BBABA@@BCD@@@B@D@D@DBB@B@B@B@BA@ABAB@B@@@B@B@B@@BBB@B@B@B@DBFBB@@@AD@B@D@D@B@BBB@@@B@@@@@@BAB@D@D@B@BAB@B@D@B@D@DBD@DBD@B@BBB@@BA@@B@BB@DBB@B@BB@@@@BB@@@@@@@BB@@@@B@@@@FF@@@B@@DH@@B@@BB@@B@B@@@@B@@@DADCBABC@ABA@ABA@A@ABABCAA@A@A@@@A@A@A@@@A@@@A@ABC@@BA@@@ABCBAAAAA@@@A@ABA@CBA@AAA@A@CBA@C@@@A@A@A@A@A@@DAB@B@B@D@BAB@D@D@DADADA@ABA@A@ADAB@D@@@@A@AB@D@B@DABAB@B@BBB@D@D@BAB@B@@@B@BABAB@BAB@@AD@F@B@DAB@BBDA@@@@BA@AB@B@BA@AB@@A@AB@BA@@B@@@BA@AB@B@@@@@BAB@@A@@B@DA@@DAB@B@DCB@B@B@@@BA@@DA@ABA@@@ABAB@B@B@B@B@B@@@BAD@@ADABB@@D@B@@@BA@@B@@@B@B@BA@AB@@A@ABABAB@BBB@@@@AB@@AD@B@@@B@BAD@B@B@@AB@D@BABBD@D@B@BAD@D@BABBB@B@B@B@@AB@DAB@B@B@BBBAD@D@D@DABBB@@BD@@@BA@@N@F@J@J@D@PDNBHBJD"]],"encodeOffsets":[[[89814,44621]],[[89586,44072]]]}}],"UTF8Encoding":true});}));