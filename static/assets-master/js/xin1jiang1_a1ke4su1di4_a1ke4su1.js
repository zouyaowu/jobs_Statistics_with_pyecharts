(function (root, factory) {if (typeof define === 'function' && define.amd) {define(['exports', 'echarts'], factory);} else if (typeof exports === 'object' && typeof exports.nodeName !== 'string') {factory(exports, require('echarts'));} else {factory({}, root.echarts);}}(this, function (exports, echarts) {var log = function (msg) {if (typeof console !== 'undefined') {console && console.error && console.error(msg);}};if (!echarts) {log('ECharts is not Loaded');return;}if (!echarts.registerMap) {log('ECharts Map is not loaded');return;}echarts.registerMap('阿克苏市', {"type":"FeatureCollection","features":[{"type":"Feature","id":"652901","properties":{"name":"阿克苏市","cp":[80.263387,41.167548],"childNum":2},"geometry":{"type":"MultiPolygon","coordinates":[["@@@|@V@®@ĎAĠ@¼^|P~NĊBRKVQJE@AHGBC@ğBÇAa@m@c@@uBq@Aw@@ǙBů@¥@ßAI@O@c@O@mK@O@@]@Ï@į@aB¹@¹A»B@u@¹@¹ABs@ŭAñA@lP˂Hž@R@F]äO WÎƔKhELMXOZJ@Ø@¦@ @@VNdT\\RFBHFHFDBVHJD@@ĆFj@Z@"],["@@ABABA@@D@B@BBDBFFFB@BBB@@D@FAHCLABCDCDEBGBEBCDEBMDEBC@A@ADCDC@ADCDGHCDCBGHCDCJADABMNAFCJCF@@@BGHIHIDABCD@BGLADGHGDIDIDGDQFIDABEDCFAHGJ@@CJCFCDEBIFAB@@@D@@@@A@EBC@K@E@G@KDCBC@ABA@@BCBIJAB@DABADA@A@C@C@CBEBC@C@CBA@A@CBADAB@D@BABA@ABCD@@CB@@EAA@C@ACAAAACCAAII@@E@AAC@CCAA@@GCA@GACACA@AAA@ABA@C@@@AAA@AA@C@AAG@CBC@A@EBABA@G@A@A@@AA@@A@AAC@EAEACCG@@@@CAA@CCAAAA@@@AFGBABAOMECMGA@A@@BABCBA@CB@@@B@BDBBD@B@DCD@D@DBHBB@BFBDBDDDFBD@B@DAD@@@BBFBD@B@@EHCD@B@F@BA@CBA@A@A@AD@B@D@BABABABCBABAB@BCBAB@@@DBBFB@B@@@@@BC@A@C@@@AB@@ABAB@DBBBBDB@B@BA@@BEBC@@B@@BBBBBBABCHADBBDD@D@@@@@@ABA@E@A@@@@BCDAB@@A@C@C@GBA@EBC@A@CBGBG@CBG@E@C@EBE@@@O@AAI@C@CAG@E@CAE@G@E@A@AAAACAAAAAA@ECGEGC@A@@@A@@@BA@@@@@@A@@A@@@@@@@A@@@@B@@@@A@@@@@@@A@@@@@@A@@@@@@@A@@A@@A@@@@@@@@@@AAAA@@AAA@A@@AA@A@A@@@A@@@A@@CA@@AA@A@GCCC@@@A@@A@@@@@@B@@@@@@@A@@@@@@AA@BA@@A@@@@@@@A@@@@@A@@@@@@A@@@@@A@AA@@@@@@@@A@@@@@B@@@@@@@@@@A@@@@@@@@AA@@AA@@A@@@@A@@@@@@@@@@@@@@@@@@@A@@@@@@@@@@@@@@@A@@AB@@@@@@@A@@@@B@@@@@@@AA@@B@@@A@@@@@@@@@A@@B@@@@AB@@@@@@@AB@@@@@@A@@@@@@@@BA@@@A@@@BA@@@@A@@B@AA@@@B@@@BA@@@@@@@@BA@@@@@BA@@@A@@@@@B@@@A@@@A@@@A@@@@@@@@@@@B@@A@@@@@@A@@@@@A@@A@AA@@@@@@@@@@A@@@@@@AA@A@A@@AA@ABA@@@A@@BA@@B@@A@@B@@AB@@@@@B@@@@A@@@@@@@@@@@@@@@@@@@@A@@@@@@@@@@@@@@@@B@@A@@@@B@@@@A@@A@@B@@@@@@@AB@@@@@BA@@@A@@@@@@@@A@@@@@@@@@@@A@B@@@@@@@@A@@@@@@@@@@A@@@@@@@@@A@B@@@@@BA@@@@@ABA@A@@@@@A@@@@@@@A@ACA@@@A@@@@@AA@@AA@@A@AA@@@@@A@AAA@@@A@EAC@AAKCA@@A@ABA@@@ABA@@BAF@BAB@B@@@BCDCB@@@@AECCCAEAAAA@CA@@CBC@AB@@ABA@A@AB@BA@@BABABEAA@@CACC@A@CAA@AA@@A@C@A@@AC@@AA@A@AB@J@BA@@BA@@@@@A@@ACA@BABA@ABC@A@A@A@@DA@@DAHAB@B@B@BAFCBCFC@AB@@CAC@@@C@A@C@A@A@ABCBA@ABABCBC@C@KBG@A@A@G@C@CCC@CAA@ABCBADE@ABA@@@CAC@@AA@@AAA@CAG@A@KBA@EBA@C@@AA@AAAC@@@CB@@ABADCJC@ADABABEBABCBC@A@A@C@G@@AE@A@E@AAA@@@E@E@AAEAI@CAA@AA@@@A@KB@@ABADADABAB@@A@G@@@CBCBA@C@A@@AAABC@@AA@CAAAAEE@A@@@A@A@A@C@AAAAEEG@AACACACAA@@AC@@A@@AC@A@@A@@B@BAB@@@BA@A@@ACEEAAA@AAA@@A@@@EBCBA@A@A@@@ABAD@B@B@D@B@@@BA@A@C@A@AA@AAAAA@A@CAIC@@@A@@@@BAD@BA@ABA@AA@@@@AB@@@B@@A@@@CBA@A@A@AAA@ACA@@@A@ABA@@B@DADCB@BA@@@@@A@@AAA@@A@@BABA@@@@FB@@@@BA@@@EAA@@@G@A@CCGEKAACE@@BG@@ACACECAACE@C@@@C@A@@@A@@AAE@M@K@A@A@C@GAA@GCEAECECCAAAAAGE@@AA@ACE@AAA@@ACEGCEACAAEGAAAC@ACCACCECCAA@@AAACA@EGA@G@ABE@CBCBA@ABA@A@A@EBA@A@A@@BA@@B@@AB@@E@@@ABEDGHABABONEDGHABEDKHKHIFGDIDCBGBC@IBA@E@Q@G@]ASABA@A@GBCBEDE@ADCDCDABAD@LCNADAB@BABADEBGBCBC@EBEBCBEDCBCDCHGHEJCFCB@NIDEDE@ABABCLIDEDCDCDAFCHAHAFCDC@@FIBCBIBCBG@C@ABOAAE@IBE@K@CBGBC@IBOBIBIBEBMDGBQDEBC@IFEBUHEBWHKDSDOFGBMBYFIBQBC@S@G@G@E@A@AB@@@B@@F@b@B@z@L@R@@@H@D@J@pJ@AR@f@L@J@VhBTD@BABGLEFOTCDDDDB@DFFBBDBBBHDDFLJFHDDBDBFBD@F@BBD@HBF@F@LAH@@@BBD@D@H@F@D@H@FAHAFCHEJEFILKJABABA@ABGFABADCB@B@BADCBADCDCBC@ADCDCDAJ@B@BAB@@@B@BADCN@DAFADBBF@B@B@BBFBDBFBDBFB@@BBFDBBBBDBB@@BB@DBB@D@@@@@@BAB@@@B@B@BBD@@BDBB@BB@B@B@B@@@BB@BBD@BBFDBBD@@DDB@BDB@DFDBDDDBDBBBHBJBB@D@HBB@D@BB@D@B@@@@ADABAB@D@BAB@B@@ADA@@DCDADADADELENADEJABKTAD@@@@BB@BB@FDHFJF@BDBFFB@FB@BDBB@B@BB@@B@BB@@@B@@BBDBB@@@B@B@B@DBBBB@BDD@BBDBB@@@DBB@BBBBDB@@DBB@DBHBFDB@DBB@D@@@BBBBDB@BB@DB@@B@B@B@B@FDBBB@F@DBB@DBB@DBB@DB@@B@B@HDD@@BD@B@@@HFF@BB@@BBDDF@B@DBB@B@HBDBBBBB@BD@DBDB@BB@DDFDB@BBB@BBDBBBB@DDDBB@DDDBNHFDDBB@BBBBB@BBDBDBB@DBDDB@DBDDB@FDDBBBDBD@BBLFHB@@DBB@@BBB@@BBDB@BD@FFFDB@BBDDB@BBDFHHHFTJBB@HCD@HFDCJEFKJONCHCLBJDJCLMJEFCJHLPLDHAFIFEHBNBJFHEH@JEH@F@FDBD@B@B@HHDBFBDDDFDDDBFBD@LFBB@D@D@BABAB@DDBHJB@@B@DBBB@BBF@FAF@D@FBDBFBJBDBDBDDDBFBHAF@HCJCHEFEB@DBJJPJBBNDND@FDHBFDBB@N@JFLHF@HBRBPBRBHBRFRB@@HDHIDCHIBCFDHFDFDDBFB@LEHIJCDBBFBD@DAD@JBFBH@TBHFFB@FB@BFDBLDHH@BBHDFD@F@HABCTFJPPFHHLCFEDQDSDKB@FAXAL@@JA`EACj@HPD@HATBJJBX@HGJQLMXWJGVCJIJOJGFODGHOHEJKZUNKJIHWAEAMCKKGIKEKEKAKIKGMAGCKCGG_@EHGBECE@I@MAEKGGKCCCYAOCCCCGCIEAAA@@ADE@A@AC@@A@CBABAAACAGKACAEACIEA@EBA@ACCEACCCAC@CBC@@@AACBADE@@BCDAPALG@ADAFCB@FIBEDEDGDQBOJMBMBODQ@UBABCBABADCDCB@DCDABAB@BA@@BAB@@ADA@@@@BA@AB@@ADA@A@AB@@A@A@@BAB@BABA@@@@B@@A@A@A@AB@@A@@@@BAA@BA@C@AB@@ABABA@ABA@A@A@@@@BA@A@A@AB@@A@@@@@CB@@AB@@A@@@AB@@@@A@@B@B@@A@ABA@@BA@@BABCBG@@@C@CBAJQPKFABAXOLGBEBAFWBO@@DO@ADM@CBG@A@CDGDK@CFQDCDC@ABC@EDEDKDEDC@@BABCB@DEHGFCHEPKFEBADAB@DALAXEF@B@tGKHUhHD@HFR@J@VC\\ApA\\@V@T@P@hDJ@ZFJBbJxTfdNbNXJNFfPXLnV^NNHXJZJNDDBLBPFTNRPVTDNH^FZĸÖDABABADAB@HBBAB@B@@A@@B@@AB@B@@@D@@AB@AA@@@A@@BABAB@BAB@@AB@@@B@@@B@B@@@DCBAB@B@BB@@B@B@@@@A@@@@B@B@@@@B@@@@B@@@BABAB@B@B@B@@@B@BAB@@@@@@@@@@BB@@@@AB@@@@@B@@A@@@AB@BABAB@BCB@B@B@DAD@BAB@B@B@@@B@@@B@B@@@BAB@@@@A@@B@DADAB@B@B@D@D@DAD@D@BAB@D@@@B@@AB@BAB@@@BBDBB@BBB@@@@A@@A@@A@@B@@@@@D@@@B@@@@A@A@@B@D@BABA@@BAB@@BB@@@B@@@BA@@B@@@BA@@B@@AB@@@@@BB@ABB@@@@BA@@B@B@B@@@B@@@@A@@@@@@@AB@@@B@BABAB@@@@BB@@@@@@@@@B@@@B@@@B@@@B@@AB@B@@@@@@@AA@@@@B@B@DA@@BA@@@A@@@@BA@@D@FAB@@@BBB@@AB@@@@@BAB@@@F@B@@@B@@@B@@@@A@@B@@@D@B@@@@@@@@A@@@AB@@@B@@@@@@@D@DADA@@B@@@@@@B@@@@B@@@BABAB@@@@@BB@@B@@@B@@A@@@@D@BBBA@@B@B@@AB@@BB@@@B@@@@A@@@@B@@@B@@@B@@C@AB@@@B@@@@A@@@A@@@@B@@@@@@@BAB@@@B@@@B@@@B@@AB@B@@@B@BAD@D@D@BAB@B@B@B@ÔXLJJnHb@ZAL@B@@@@@@@@@B@@@B@BAB@D@B@@@@@ZAŢG@IF_JSHWZgFGDKBCTYDCBEPWDCLKDCLGFCFCFADA×sWȍÛ[KµgÑh»gHÃmqOÝumOÉDéDĉqQURIHEDMLCBOPGFCBEBABEBC@CBA@ABEBEBCBA@IDGBC@A@CBE@CAE@C@A@C@G@EAA@EAGAO@I@A@GAA@A@A@E@A@A@A@E@CBGBCBA@ugCK@AC@A@AA@@OKECE@IAC@G@CAECCEAA@AGAC@A@@@A@@@KB@A@K@CkSQIACAAECACCCCAGCWE@BBBDD@@@B@@ABC@ABABA@@B@F@@BBAB@BCDABCB@B@D@D@@BBFDFDB@BB@@@D@D@BCB@B@BBD@DABABABCBCBABA@A@C@A@@@EEA@@@A@AAAAAAAAAAA@@C@@AAEAEAC@C@C@CBA@CDAD"]],"encodeOffsets":[[[83365,41410]],[[82484,41635]]]}}],"UTF8Encoding":true});}));