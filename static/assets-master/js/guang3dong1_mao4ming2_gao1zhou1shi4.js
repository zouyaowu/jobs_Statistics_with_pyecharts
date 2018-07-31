(function (root, factory) {if (typeof define === 'function' && define.amd) {define(['exports', 'echarts'], factory);} else if (typeof exports === 'object' && typeof exports.nodeName !== 'string') {factory(exports, require('echarts'));} else {factory({}, root.echarts);}}(this, function (exports, echarts) {var log = function (msg) {if (typeof console !== 'undefined') {console && console.error && console.error(msg);}};if (!echarts) {log('ECharts is not Loaded');return;}if (!echarts.registerMap) {log('ECharts Map is not loaded');return;}echarts.registerMap('高州市', {"type":"FeatureCollection","features":[{"type":"Feature","id":"440981","properties":{"name":"高州市","cp":[110.853299,21.918203],"childNum":1},"geometry":{"type":"Polygon","coordinates":["@@AA@A@ABABC@C@A@IGB@@GBA@@BB@@@@@@B@@@@@@@@A@@@@@A@@@@@@@@@A@@@A@@@AB@@@@A@@@@A@@@@@@@@@@A@@@@@@@@@@@@@CBABCAADAA@A@@@@A@@@@@ABAD@@@B@@@@B@BB@@@@@B@@@@@@@@@@@@@@@@@@B@@@@@@@@@B@ABCD@@@@@@AA@@@@@@AB@B@@@@@@@@@B@@@@@@@@@@@@@@AD@AA@@@A@@@A@@@@@@@BB@@B@@@@B@@ABA@@A@@@@@@AB@BA@@@@@@@@@A@@BB@@B@@BBCFA@EH@BAB@BA@@B@@A@AA@@ACACA@@AC@CACBC@ABCA@AAACC@AAC@AA@A@A@GBABCBCDE@@B@@@@A@@@BB@@@@@@@@@@BA@@@BBA@@@@@B@@B@A@@@@@A@@B@@@@@@@BA@@@AD@@@@AB@@@B@@@@@@A@@@@@BBB@@B@B@@@@@@AB@@@BA@@@@@@B@@B@@B@@@@@@@B@@BB@BA@@@@@AA@B@@BD@@@@B@@@@B@@@@@@@@BBAD@B@@A@A@@@A@@@A@A@@@@@A@@@ABA@@@@@@@BA@@C@AC@@AB@@@@CB@@A@@@@@AAA@A@@@AB@@@BAA@@AA@@@BA@@@@@@@AA@@@@AB@@AACAA@A@@B@B@@@BA@@@@@C@@@@B@@@B@F@B@BA@A@@@@BD@@@BB@@BBBBB@@@@@@@B@@@B@@D@@@B@B@DA@@B@BBB@B@@@@@A@AB@@@@@@B@BBAB@B@@D@@BB@@B@@@@@@B@D@BB@@B@@@@A@A@AA@@@@@B@@@DBB@D@BA@@@@B@@@BA@A@@@BBBBB@@B@B@@@@AD@@@@@B@@@@@@@B@@@@@@@B@BD@@BA@@@BBB@@@B@B@@ABDB@A@@B@BAB@B@@@@@@@@@@B@@@@@B@@A@@@A@@B@FB@@@B@D@BCBBB@@@@@@@@@@@@B@@@@BBB@BB@@@BBB@@@@B@@AB@@@@A@A@@@FFBFCB@BAAA@AAC@@@A@ABAB@@@@@@@@@BBB@@@B@@A@CDBB@@@@AB@B@B@@@@ABC@@B@@@@A@@@@@@@AB@@@@@@@@A@@BA@@B@@B@@B@BBD@B@B@@@@@@@@@@@@@@@@@@@B@@@@@@@@@@@BBBA@@AA@@@BBB@@@@B@B@@@@AB@B@@@B@@B@@@@@@A@@@@@BBB@@AB@@@AA@@@@@B@@@@@B@@@A@@AA@@@@@@@@@@BAB@@@@@@B@@@@@@@@BB@@@B@B@@A@@@A@@@@@@@B@B@@@DA@@A@@@A@@AB@@@@A@B@@A@@A@@@@B@@AD@B@@@@@@@@@@@@@@@@@@@@@@@B@@@@B@@@BA@@@AA@B@@@@B@@B@@@@A@@BBA@B@@@B@@@@@@BA@AAABA@@@BB@@@@B@BAB@@@@@B@@@@D@@@@@A@@A@@@@@@@@B@B@@@CA@@@@@A@@@A@@B@@@D@@B@@@@@ABA@@@@B@B@@@@@@@BB@B@B@BB@@@@B@@@D@B@@@@A@@BAD@@@@@@B@@ABA@@@@@CB@@@B@@AAAB@@@@B@@@B@@BA@@@A@A@BD@@@BA@@@A@B@AB@@AD@@@BBB@B@@AB@@A@@B@@AB@B@@E@@@@@@@@@A@@@@@AF@@@B@@@@@@@@B@@B@@@@@@@@@@@@@@A@@@@@BB@@BA@@@B@@BB@@BB@@AD@@A@B@@B@@BBA@B@BB@@B@@@@@@B@@@@@@@@@@@@B@@D@@CBA@BA@@@@BAA@@@AB@B@B@@@@@@@@@@@@BB@@@@@@A@@D@@@B@@@@@B@D@@@B@@BB@@@B@@AB@@AB@@BD@@A@@DBBAB@@@@@@@@@B@@BB@BAD@@@B@@@B@@A@A@A@@B@B@BAD@@ABABCBC@A@A@C@@@AB@B@D@B@@@BA@AB@@@@@BAB@@C@AA@@C@@BA@@@C@A@A@C@@@@@A@@@@@@@A@@@@@@@@@@@@@@@@@@@@@@@@@@@@@A@@@@B@@@@@@@@@@A@@@@@@@@@@@@@@@@@@@@@@@A@@@@@@@@@@@@@@@@@@@@@@@AB@@@@@@@@@@@@@B@@@@@@@@@B@@@@@@@B@@@@A@AB@@@@@@@@@@@@@@@B@@@@@@@A@@@@@@@@A@@@@@@@@@@@@@@@A@@@@@@@@@@@@@@@@@@@@@CB@@@@@@@@@@@@@@@@@B@@@D@@@B@@@@@@@@@@@@@B@B@@@@B@@@@@@@@@@@@@@@@B@@@@@@@@B@@@@@@@@@@@BB@@@@@@@@@B@@@@@@@@@@@@@@@@@@@@@@@@@B@@@@@@@@@@@@@@@@@B@@@B@@@@@@@@B@@@@B@@@@@@@@@@@B@@@B@@@@@@B@@B@@@@@@@B@@B@@@@@@@@@@@@@@@@@@B@@@@@@@@@@@@@@@@@B@@@@@@@@@@@@@@@@@@@@@@@@@@@B@@@@@@@@@@@@@@@@@@@@@@@@B@@@@@@@@@@@@B@@@@B@@@@@B@@@@@@@@@@@@B@@@@@@@@@@A@@@@@@@@@@@@@@@@@@@@@@@@B@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@BB@@@@@@@@@@@@@@@B@@@B@@@@@@@@@@@B@@@@@@@@@@@@B@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@BB@@@B@@B@@@@@@B@@@@@@@B@@@@A@@@@@@@@@@@@@@B@@@@@@@@@@@@@@@@@BB@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@BAB@B@DBB@@@BAB@BAD@@@B@BA@@@A@@B@@@B@@@@@B@@AB@BB@@@B@DBB@@@B@B@BBBB@@BB@@ABBA@@BA@@B@BBABAB@@A@@B@@@@B@@@BA@A@@@A@@BB@ABAA@BA@C@@BB@AB@A@@A@@@BDDJ@@@HBD@BFBDD@D@@@BDDDDBB@@@BCB@BAB@@A@@@CBC@@@CBAD@BA@@B@@BB@B@@BB@BB@@BB@BBH@DD@BAB@F@DAD@BDBD@DBDB@ABABC@ABABADBDDBDDDD@D@B@DBBBDBBB@BBB@B@DABAB@DBDBFBFADADC@A@EDCFC@E@CBCDC@A@CBE@C@EBG@CB@B@B@BBD@D@BAB@D@BBBBBBB@@@B@BB@B@@@B@@B@@AB@DA@BB@@BBHF@@@B@@AB@B@BDD@B@DD@F@F@B@DBB@BBABB@BDBBDBBBD@F@D@FCB@D@FCBCBCBAFAB@B@B@BBBBBBDFDDBB@B@DAB@B@DABABABCB@BAB@DABCB@BAHEDABEJADCB@@CBEF@@CBCDBB@DAD@B@B@DA@A@AAETAH@B@BCBA@@B@HEFCHA@@BCDC@K@ABEF@@@BADAB@DAB@BCFAF@B@BBD@FBFDDDD@B@BBBBD@@@@FDDBJFFAF@HBLDB@D@FBDBHLFF@DCFCB@@BJHFNFDAD@FBDB@BBB@B@B@BBDBBDB@BBB@BBB@B@BBD@@DDDBD@BABA@A@AD@BADAB@DEDCDC@AF@J@@AFAHC@@BCDAD@@@B@DBFBDAF@BBB@BBF@JDD@BBD@DCFCDEDEDAD@FAD@BA@AAACAACAEAA@AAA@ACCCCAAAACGCEAACACCEECEBGBE@OHCPGBCBCHCF@B@DDFFFDFBD@D@FCFE@ABABAD@F@B@HD@DBFFDH@DAFABA@ABAAAAACC@ADAD@NELGB@D@DAFA@@DCBADC@@B@@A@@B@@@@@BA@@@@BAJGB@H@FF@@BBEP@BBBDBJ@D@FAHIHCHDDJBLBF@BBBBBB@D@DADAHAHBBBDBFBDBFFDJ@@DFDDBDFDHDHAHAP@D@FBDDBDDBDBFAHCDCDANAH@B@B@@@B@BA@@D@BBB@BBBB@@BDBBBB@BBBBBDBB@D@BB@BBB@@BBBB@@BBB@B@@@B@B@@BB@B@B@BBBB@@@B@BABBBB@DBB@BB@BBB@B@@B@BB@BB@BB@@@BBB@DA@@BBB@@@BAB@@B@@B@@BABABABA@@D@@@BA@BB@BA@ABA@A@A@AB@DBB@@@BA@@BA@ABA@A@@BA@@@C@A@A@@B@DAB@B@@AB@@AB@B@@AB@A@@AB@BC@@BC@AAA@ABAB@@BB@BBBBB@D@BBB@B@B@B@BB@@B@BABABB@BBB@B@BB@B@@@B@@AB@BB@@BAB@DBBBB@DBB@BBB@B@DBB@B@B@@@@BAB@@@BBBB@@B@@B@B@@A@@BA@@BAB@@ABA@@B@@ABAB@B@@BB@B@BBBABBB@@BBBBBB@@@B@DF@BB@B@BAB@B@B@B@@@B@B@@@D@BBBDBBB@@@@BD@@@@ABAB@D@BABBHBB@DBB@BBB@B@B@BBB@B@@@BB@@@BBBBB@BBBB@BCDA@C@A@A@A@@B@BAB@BBB@B@@@B@B@B@B@BABBBB@@B@BBBBD@@@B@@BB@BAD@@@DAB@BB@BDB@@B@B@@BB@@BBB@BDB@@@@@BB@B@AB@B@BA@@@@BBDBB@BDDB@BBBBB@@BBB@@BB@@BA@A@AB@@ABAD@BAB@DB@@@B@BBBB@@D@BBB@BBAB@D@B@D@B@B@@@BAAA@@BA@C@ABCB@@ADADABC@@B@@ABA@@@E@@@AB@BADBD@@BD@B@B@BA@A@AB@BBBB@BABA@@BBB@B@@BBBBBAB@B@B@BDB@D@B@B@B@B@@BBBB@@BAB@BBBBBBB@B@DAB@BBBDBBB@@@BBB@@D@@@@BBBBBBB@DBBBBDBFDDBD@D@DBB@BBDABBD@D@B@D@B@B@BBBBBBB@D@BADCB@BC@AB@BADC@C@@@AB@BA@ABAB@B@@@BABABAB@DA@@BA@@B@BABBDAB@B@B@B@@@D@@@BAB@B@@ABABABA@A@A@@@ABABABA@ABA@C@@BA@@@AA@A@A@AA@@BAB@DA@A@ABABA@AAC@A@@@@@AAAA@AA@@@AA@@A@A@A@AB@B@BABAB@@@@ADABABABAB@@ABAB@B@@@AA@@BA@AAAAA@@A@@B@@ABC@@BCAA@AA@@@AAA@@AB@AAAAA@@A@A@A@C@CCCCA@@@AAA@@C@AAAAA@A@@AC@C@@ACAAAAAB@ACAA@@@@A@AAAAAAC@A@AB@@ABCB@@CBCBA@A@AA@CA@A@CBADADA@@BABA@@@CA@CCA@AC@AB@@A@AAAAAAAA@CACBA@A@A@@@AA@AA@CAA@C@@A@A@@A@A@A@@@CCAA@A@A@ABA@A@CBA@ABAB@D@@ABA@ABC@E@C@AAECC@@BC@AA@AA@A@A@ADCBA@A@@DC@@FABA@C@A@A@A@@BAA@@AB@@AAA@A@AAACA@A@@A@ABAB@@A@@A@@@ABAAAAAEACAA@C@AA@AB@@A@A@@@C@AAABAB@BAB@@ACAAAA@@AAAA@C@A@AA@@@@@AAA@A@AAAA@AEAC@A@AB@BAD@B@BA@AAAA@AB@@A@A@C@CBA@A@A@A@@@A@A@@AB@BA@C@AAC@@AAA@BA@AA@AA@A@@CAA@@A@@AA@A@@BAB@AA@AB@@A@A@@A@@AAAAAAAAAABAAC@C@AAAABA@@A@@AA@AAB@@AB@AA@@@@@A@AAA@A@@@A@AB@BADA@A@A@AAEB@BABABAB@@A@ABABADAF@BAD@B@BA@AB@BABA@@AC@@CAAC@ABC@A@A@A@C@AB@AC@@IE@AAAAAC@CAAACAA@EA@AACACA@AC@A@A@A@C@CGDEAKIEKA@GAKFGECGA@EDCEOG@AEAA@@@EBILAAAG@CDADBAEBAECKIGMAGGCBEBA@OCEBICMAEGMECJECUBG@@@AMCBEACE@ABA@@@@@@@@A@@BADA@@AA@@ABABGCEBGB@@KEBCFCBC@GEIC@CAFCDCBCEGCAEA@CD@BCDBJFBABAAADCAGF@DFD@JEDA@@@GI@@CEA@@@@@@C@ABCGABBJCBAB@@@@A@E@BDGDAACA@HCFEBACKB@CCACFE@ADABCBCCC@EF@DDH@BCAKFDNEBEFKBEASDCCIDADEBA@IGGGCGOKCK@CGMBCD@HKDGJ@BABQD@LOBIDCFCDCBAAG@AKK@IMGE@CAG@ABEJ@@IBEFMCGMMK@BG@@IBCCC@BEHEGAACAEBIHA@CCDKGCCBAACGAECECAAAAA@@C@A@A@@BAB@B@H@B@BABADABCB@BCBABCFCBABCBA@ABA@C@A@C@@@C@A@E@C@AAGCCAAAAAA@EEEEECAA@AA@@A@AE@E@I@K@C@C@ABA@ABAB@@AB@D@@@B@D@BBB@BBB@@AB@@A@@@@BE@A@CAC@CAC@CAC@CBCBABABAB@B@BAF@FAFADADABABABA@ABA@A@A@E@EAE@EAEAE@G@A@A@C@@@@BA@AB@BADAD@BABADABABABE@EBC@C@ABABA@ABABADADABADABA@CBA@ABA@@@C@@B@@A@ABABABABAB@BABA@A@A@CAA@AAACAACCCCC@CACCCCAAA@@A@CAABA@A@CBA@ABA@ABCAC@A@@CAA@AA@A@ABA@ABC@C@@@@@@@E@C@CAA@AA@CAAAA@@@@@A@C@I@C@C@C@C@CBC@CBCBCBEBCBABC@C@A@CAA@AAA@@@AA@@@A@A@@@CBA@ABABA@A@ABA@C@C@AAA@A@AAA@AAA@CAA@A@A@C@ABA@A@@BA@A@AB@BA@ABA@@BABA@@B@@AB@@A@ABA@@@ABA@ABA@A@@BABAB@@@@A@@@AA@@@@@CA@@C@A@EBC@C@C@A@AAA@AAAAA@GBA@CA@@A@"],"encodeOffsets":[[113413,22242]]}}],"UTF8Encoding":true});}));