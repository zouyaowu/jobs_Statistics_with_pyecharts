(function (root, factory) {if (typeof define === 'function' && define.amd) {define(['exports', 'echarts'], factory);} else if (typeof exports === 'object' && typeof exports.nodeName !== 'string') {factory(exports, require('echarts'));} else {factory({}, root.echarts);}}(this, function (exports, echarts) {var log = function (msg) {if (typeof console !== 'undefined') {console && console.error && console.error(msg);}};if (!echarts) {log('ECharts is not Loaded');return;}if (!echarts.registerMap) {log('ECharts Map is not loaded');return;}echarts.registerMap('马关县', {"type":"FeatureCollection","features":[{"type":"Feature","id":"532625","properties":{"name":"马关县","cp":[104.394157,23.012915],"childNum":1},"geometry":{"type":"Polygon","coordinates":["@@BG@C@C@C@@@@@@CCCCAECECEEECCECCAMQGCGGIQEB@FBHAHBF@BBHCBGHCDEBC@C@GBGAEAC@IECEAEBE@GAEGAUBQHMLIRCJBB@B@B@D@B@BAB@BAB@@@B@@@@B@B@@@@BBD@@BBB@BB@@BBBB@BDB@BBBBBBB@BB@BBB@@@BB@B@@@B@B@B@@AFABADAB@BAB@BAD@DAD@B@BAB@@ADADABA@@B@B@B@B@B@BAB@B@@AD@B@B@B@B@B@BAB@@@BBB@@@D@@@BBDBB@BBB@B@BBD@@BB@D@B@@@B@B@@@B@@@BABABABA@@BA@ABCBA@ABA@@B@@ABAB@BA@@@@@@BBB@@BBBB@@DBD@B@B@DADADAD@B@B@B@B@BBB@B@BB@BB@DFBB@@B@@B@BBFBB@B@@@DBB@B@BBBBB@BAB@B@D@@BB@B@B@@@BBB@B@@@B@B@B@B@@B@@BA@@@@B@BAD@B@@@BAB@B@BBB@@@B@BAB@B@B@@BB@@BB@@@B@@AB@BA@@B@F@BAD@BAB@B@BAB@B@B@@BDB@@BDD@@@B@B@BAD@BAB@B@DAB@BAB@B@B@@BB@B@BA@@@@@CBA@@BABADA@@B@DBBB@@DDB@BBB@B@@FJ@BDBBBD@DB@@B@BBDD@B@BBB@B@@@BBDDD@@@DB@BDB@BBBBBB@@BBBBB@B@BBD@B@B@@@B@@@B@B@@@@@BB@BB@@B@B@B@D@B@@@B@B@B@@BB@BBBABAB@@@BB@@B@@@D@B@BB@@B@BAB@B@@@DBD@B@D@BBB@@@BBBFJ@B@B@B@@@D@@BD@B@D@BBBA@AB@B@BABABAB@BAB@BABABA@AB@B@B@BA@@BA@@@@B@@@@@BA@@@ABABAB@B@B@@@@ABAFAB@B@B@B@@ABABABABA@@BA@@D@B@D@B@D@B@DAB@B@BBB@B@BB@@BB@DBBBBBDFBB@B@B@B@BABCBAB@B@B@B@BDDBFBDDDBFB@@BABBBB@DBDBB@B@D@NDNBVBNFPDPPNLHHDDHDFFBBPLNLRLLHLDPARIRINETIPETCBAL@RGHAL@HDJHBBRHH@NDLDPBRDP@PANAREHAJ@LDNHNJHBD@DCBEAKBKBEFGJCPDFBLB@@@@BBPFFBB@@@@@NHRJPLLJHLRRRFPFRFPFJHJHJPFNDJFLHJHHDDDHHJHJFHFDDAHMNKPED@LCNIJS@K@EBQAQEWGOEOEQ@@@@CG^IN@N@B@P@VBJJJMBMBKRGNECSCMPKHELEFALEV@@KEMFM\\CJAGMAMCCCABEAC@EACBCFKDCHG@C@AECCAGCEAEAMBCACCAABC@EAE@GDA@EBI@E@CAEDEDCHEDADEJ@DAFBBGBEBI@EEICG@CBCDC@@DGHILAPERARCDBL@L@JGBCJCB@FAFAF@LFJFF@FABIS[IIBCBABCDE@A@@@G@I@MGEOEKOKOGQAGIB@A@@@@B@@@@A@@@@@A@@A@@@@@@@A@@@@@@A@@@@@@@@BA@@@@@@@@B@@@@@@@B@@@B@@@@A@@@@@A@@@@@@BA@@@@@@@@@@B@@@@@@@B@@@@A@@A@@@AA@@@@@@@@@@@@BA@@@@@@@@A@@A@@@@A@@@@A@@@A@@@@@@@@A@@@@A@@@@@@@@@AB@@@@A@@@@A@@@@@@@AB@@AB@BA@@@A@@@@@@@@@@A@@BA@@@@@AAA@A@@@AA@AA@@AAAA@@@@@B@@AB@@@@A@@@@B@@@@@@@BA@@@@AAA@@A@@@@A@@AB@@A@@@A@@@A@A@A@@@@AA@@A@@A@@@A@AB@@@@@@A@@BB@@B@@@@@B@@@B@@@@B@@@AB@@@B@@@B@@@@@@B@BB@@B@@@B@@@@@@@@@@@AB@@A@BB@@@@@@@@@@@@B@B@@@B@@@@@B@@@@@@@@@AB@@@@@@B@@@@B@@@@@@@@@@@@@@AB@@@@B@@B@@@BAB@@@@A@@@@BA@@@@B@@@@AB@@@B@@@@AB@@@@@B@@@@@@@@A@@@@B@B@@@@@BA@@@B@@B@@@@@@@B@@@@@@@@A@@@@@@@@BB@@B@@@@@@@B@@A@@@@@@@@@@@A@@@AB@@@@@BA@@@@@A@@@@@@@@@@B@@@@@@A@I@E@E@I@KEGIEIOIQCKCEAMGMKAMAGGOOKAAQCCEAMEEYIMISMIIOIOCSGOEQGGIMOEOCKGKU@MEEIKIMAMDIHOLKH@B@B@B@B@B@B@B@DABAD@BABAB@BA@A@A@ABABABC@ABA@ABABAB@@C@ABABA@C@C@C@C@CAEAE@E@EBA@CBABABABCBCBABEBEBABA@ABA@A@AAC@A@A@C@AB@@AB@B@BBD@B@B@B@B@BAB@BADABA@@BABABAB@@ABABABABAB@BA@@B@B@B@B@B@@@B@@AB@B@B@BABA@@BB@@BB@@B@D@@BB@BBB@B@B@B@BBB@@@BBB@BBB@B@B@BBD@DBB@DBB@@BBABB@@BBBB@@B@@@BAB@BB@BB@B@@@B@@@BA@@B@BA@@BBB@BBB@BDBBD@@@D@@BFBA@B@@@BDBDHDDBB@@@B@@@D@BBB@BAD@B@DAD@BCF@@@DAB@H@B@@CDCDA@EB@@CD@@A@ABCBCDABA@C@C@CAAAECC@AAEAA@AAA@A@@AA@G@CB@@ABCFGFC@CAE@CAIGEEIKACGCEACEACIGCAA@I@GDCD@HBFDBBJ@F@H@HAF@@@@A@@@IIEE@AA@CACBEAAACAE@CBIFCJALAFAFABGBCD@DBF@D@@@F@DCBEAACIAMBEACGAG@EAGAAABEAIGI@IO@C@CAECEACCECCEEAECEAC@A@EI@CACAEACACCLCFACAGEM@CDC@EBC@G@@FCHAHCDIBEAECCACGBCAECCECACDE@EDE@EH@DBFDDA@EEGEC@EBADAHFBC@COOEG@CAABE@ABIBAAA@A@@A@AC@C@A@@@@EGAEAAEAEEEKAC@B@BCFCBEAICAG@A@AB@@A@A@CAC@E"],"encodeOffsets":[[106497,23281]]}}],"UTF8Encoding":true});}));