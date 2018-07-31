(function (root, factory) {if (typeof define === 'function' && define.amd) {define(['exports', 'echarts'], factory);} else if (typeof exports === 'object' && typeof exports.nodeName !== 'string') {factory(exports, require('echarts'));} else {factory({}, root.echarts);}}(this, function (exports, echarts) {var log = function (msg) {if (typeof console !== 'undefined') {console && console.error && console.error(msg);}};if (!echarts) {log('ECharts is not Loaded');return;}if (!echarts.registerMap) {log('ECharts Map is not loaded');return;}echarts.registerMap('西盟佤族自治县', {"type":"FeatureCollection","features":[{"type":"Feature","id":"530829","properties":{"name":"西盟佤族自治县","cp":[99.590123,22.644508],"childNum":1},"geometry":{"type":"Polygon","coordinates":["@@@GCICCECGECGCAIACAEKWCCCMC@AQU@I@KIGGECAAEAAAABEBEBA@CAAIGCA@CDABABACCAAAG@CACAA@CDAGAM@C@CBABCFC@ADAB@F@@AD@FADC@C@EBEBCBEFABCFABC@AACA@@A@AAMCECA@E@ABCDEDEFABC@@@MEGCC@EAEAA@CB@@KNEFCBIFABGHAB@@B@@B@@@B@B@B@B@D@BAFADABA@EDEBGDA@ABAB@DA@ABCD@@AD@@AB@@@BAD@B@BBB@B@B@B@D@D@D@@BB@BBBBBBBBBBBBBBD@BBB@DBB@BBBBB@BB@BBDFBDD@@BBD@BDD@BBBDBBB@BB@@B@DADAF@B@BA@BB@B@B@B@B@BABABCDCFCDAB@DABCBAB@B@@@@@DBBBBBB@DABABEBAB@@@B@D@D@BAB@@AB@D@D@DBDA@@@A@A@@B@D@DAB@D@B@B@@@B@B@B@BCBAD@BBBAD@@AB@B@B@B@D@B@BB@B@AD@@BD@BA@ABA@@BABCB@B@BA@CAAB@B@D@B@@A@AAAB@@@@ABBD@D@BA@AD@D@B@D@DADADAF@D@@CDAB@D@@@FAB@F@@AD@BA@@@@@@BA@@@@@AB@@@@A@@@AB@@A@@@@@A@@@A@@@AB@@@@@@@@A@@B@@@B@@@@@B@@A@@@AB@@@@@BA@@B@@@B@BA@@B@@@@@B@@@@@@ABA@@@A@@@AB@@@@@@AB@@@@A@@B@@@B@@A@@B@@A@@B@@@@A@@B@@@@@B@@@@AB@B@@@@@B@@@BA@@@@B@@@@@@@B@@@@B@@@@@B@@BB@@@@@@@B@@@@@B@@@@@B@@@B@@@@B@@@@@@@@BB@@@@@@BB@@@@BB@@@@@@@B@B@@@@@@@BB@@@@B@@@@@@@BA@@@@@@@@BB@@@@@@@@@@BB@@B@@@@@@@B@@@@@@@@@@B@@@@@@@B@@A@@B@@@@@@@@@B@@@@@B@@@@A@@@@B@@B@@@@@@B@@@@@@@@B@@@@B@@@@@@@@@@AB@@@@B@@@@@@B@@@@@@@@@B@@B@@@@@@@@B@@@@@@@@A@@B@@@@@@@@@@B@@@@B@@@@@@@@@B@@@@A@@@B@@@@B@@@@@@@@B@@@@@@@@@@@@@@B@A@@@@B@@A@@B@@@@@@@@@@@@@@B@@@@@@@@@B@@@@B@@@@@@@@@@B@@@@@@@@@@B@@@@@@@B@@@@@@B@@@@AB@@@@@@@B@@A@@@@@@@@B@@BB@@@B@@@B@@BB@@@@@B@@@@@@A@@@@@@@@BA@@B@@@B@BB@@@@B@@@@@@@B@@@@@@@@@@B@@B@@@@@@@@@@A@@@@BB@@@@@@@@@@B@@B@@@@@@@B@@B@@B@@@@B@@@@@@@@@@@@@@@B@@@@@@B@@@@BB@@@@@@BB@@@@B@@@@@@@@@@@B@@@B@@A@@B@B@@@B@@@@@@@B@@@@@@@B@@@B@@@@@BA@@B@@@@@B@@@@@B@@@BB@AB@@@@@B@@@B@@@B@@@@@B@@@B@@@@B@B@@BB@@@B@@@B@B@@BB@@@B@@@B@B@@@B@B@@@@@B@@@@B@@B@@@B@@@@BB@@@B@@@@@@@B@@A@@B@@@@AB@@@@@@@B@@AB@@@@@B@@@@@B@@@@@B@@@@@B@@@@@B@@@@@B@@@@@@@B@@B@@@@@@B@@B@@BA@B@@B@@@@BB@@@@@B@@@@@BB@@@@B@@@@@@@B@@@@@B@B@@@@@@@BB@@@@@@@@@AB@@@@@@@@BB@@@@@@@B@@@B@@@@@B@@@@@@@@@B@@@@@B@@@@@@AB@B@@EDRH@B@B@@@@@@@B@@@@@B@@@BB@@@@@@B@@@@@@B@@@@@@@@B@@@@@@@@@@@B@@@@B@@@@B@@@@@@BB@@@@@@B@@B@@B@@@@@B@@@@@@@@@@@B@A@@BB@@@@@@@@@@@@A@@B@@@B@@@B@@@@@@@@AB@@@@@B@@@@@B@@@@@B@@@@@@@B@@@@@B@@@B@@@@@@@@@BB@@B@@@@@@@B@@@@A@@@@@@@A@@B@@@@@@@@B@@@@@@@@@@B@@A@@@@@@@A@@B@@@@@@@@B@@@@@@@@@@A@@B@@@@@B@@@@BB@@@@@@@B@@@@B@@B@@BB@@@@@B@@B@@B@@@BB@@@@@@B@@B@@@@@@@B@@@B@@@B@B@@@@@B@@@@BB@@@@@@@BB@@@@BB@@@@@BB@@@@@B@@@@@@B@@BB@@@@@B@@@@BB@@@@B@@@@BB@@@@@B@@@@BB@@@B@@@@@B@@@@@@@B@@@@@B@@@B@@@@@B@@@@@@@B@@BB@@@B@@@@@@@@@B@@@@@@@B@@@@@@@@@@@@@B@@@@@@@@@B@@@@B@@B@@@@@@@@@B@@@@@@@B@@@B@@@@@@@B@@@@A@@B@@@B@@@B@@@B@@@B@A@@@@B@@@@@B@@@B@B@@@@A@@B@@A@@@@BA@@@@@@B@@@@@@@B@@A@@B@@@@@B@@A@@@AB@@A@@@AB@@@@A@@@@@@B@@@@@@A@@@@@@B@@@@@B@@@@@@@@@BA@@@@B@@@@@@@B@@@@B@@@@@@@@B@@@@@@@@@B@@@@@@@B@@@B@@A@@@@@BB@@@@@@@@@@@@AB@@@@@@@B@@@@@@A@B@@B@@@@A@@@@B@@B@@B@@A@@B@@B@@B@@@B@@@@AB@@@@@@A@@B@@@@@B@@@@@@AB@@@@@B@@A@@B@@AB@@@@@B@@@@AB@@@@A@@@@B@B@@@@@B@@@B@@@@@B@@A@@B@@@B@@@B@@@@@B@B@@@B@@@B@@@B@@A@@B@@@@@B@@A@@B@@@@A@@B@@@@@@@B@@A@@@@@BB@@@B@@@@@@@B@@@B@@@@@B@@A@@B@@A@@@@B@@@@@B@@@@AB@@@@@@A@@@@B@@@B@@@@@@@B@@@@@@@B@@@@B@@@@B@@B@@@@@@B@@B@@@@B@@@B@@@@@@@@@B@@@@@B@@@@@@@B@@@@@@@@@BA@@@@@@B@@A@@@@@BB@@@@@B@@A@@@@BB@@@@B@@@@@B@@@@@@@@BB@@@@@@@B@@@@@@@@BB@@@@B@@B@@B@@@@@@@@B@@HDLAHAXMPGRKHGNGVK^GVCHBDBD@^P@@PGFAHAF@@@\\CL@JAFCFAB@DBFFFFFDL@DBJBD@HFFDDADEB]GKSOEICK@aFOBEHCFAHCFEDQFEF@F@RLP\\BBNAFCBAAG@EDGDGDEBEDIDGBA@CACCEAAEIAECACC@AECICIAGAGCA@KHKDMDKAECC@I@A@AABE@E@EBC@EJAJAHADCDCDGDIBCDC@@BCBC@EA@CACAAAC@@AQBCAA@ACCE@ABADAAMBIAIB@@@T@NATAXBFAHID@@KBKDMDKFIFILILEPKFCPSCWGOIIGEMIECGGEGMKIEGCOACCACACCECCCECAICCAE@GEKECAEACC@E@WACCAC@AHGJIHIFGDC@GAG@G@BH@JC@CBC@CAAACGBI@GCCCACCAE@A"],"encodeOffsets":[[101961,23095]]}}],"UTF8Encoding":true});}));