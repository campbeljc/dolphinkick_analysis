#!/usr/bin/env python

from os import getcwd
import pandas as pd

def import_library():
    Library = pd.DataFrame([
        ['Coughlin', 'Female', 'Back', 'Fast', 0.4, 1.73, pd.DataFrame([
            [0.0, 0.023472963005780344, -0.12640190462427744, 0.0, 0.07323564393063584, -0.09818740346820809, -0.16670498150289018, 0.133333333],
            [0.033333333, 0.05267332832369943, -0.061780838150289015, 1.2832369942196533e-16, 0.1372464132947977, 0.04319025144508671, -0.01837933005780347, 0.033333333],
            [0.166666667, 0.016947479190751447, 0.06490274219653179, 0.0, 0.09926715953757226, 0.2186506479768786, 0.28651098323699425, 0.133333334],
            [0.266666667, -0.0037791468208092484, 0.016313709248554915, 0.0, -0.0010797560693641618, -0.011243549132947978, 0.032838675144508674, 0.10000000000000003]],
            columns = ['t','Finger','Shoulder','Hip','Knee','Ankle','Toe','Time']
            )
        ],
        ['NT2', 'Male', 'Front', 'Slow', 0.49999999999999967, 1.8, pd.DataFrame([
            [0.0333333333333333, -0.021147562639894663, -0.07168401747787778, 0.0, 0.05271340981561972, -0.13745915715931556, -0.17384540464266388, 0.2],
            [0.166666666666666, 0.04400558990507483, -0.0017104646252857278, -1.2335811384723945e-16, 0.1217539819635111, 0.05815579725971, 0.03669724105158183, 0.1333333333333327],
            [0.233333333333333, 0.04742651915564611, 0.021769549776362168, -1.2335811384723945e-16, 0.05971076510087889, 0.11460112989413498, 0.18208673420085777, 0.06666666666666701],
            [0.333333333333333, 0.011195768456414667, -0.019126104446375386, 0.0, -0.021769549776362335, -0.0062198713646749995, 0.04447208025742561, 0.09999999999999998]],
            columns = ['t','Finger','Shoulder','Hip','Knee','Ankle','Toe','Time']
            )
        ],
        ['Sutton', 'Female', 'Front', 'Slow', 0.5, 1.73, pd.DataFrame([
            [0.0, 0.11897715269235434, 0.06015698731635896, 0.12165079657308152, 0.14303994761889768, -0.038767836270542484, -0.07352520671999421, 0.09999999999999998],
            [0.0666666666666666, 0.12432444045380867, 0.06283063119708612, 0.0949143577658104, 0.18849189359125781, 0.05748334343563191, -0.03609419238981549, 0.0666666666666666],
            [0.166666666666666, 0.0949143577658104, 0.08154613836217514, 0.05748334343563191, 0.12699808433453527, 0.18047096194907689, 0.21255468851780174, 0.0999999999999994],
            [0.4, 0.07887249448144798, 0.07619885060072139, 0.08689342612362949, 0.07085156283926705, -0.0013368219403635665, 0.030746904628361216, 0.23333333333333403]],
            columns = ['t','Finger','Shoulder','Hip','Knee','Ankle','Toe','Time']
            )
        ],
        ['Lochte', 'Male', 'Back', 'Fast', 0.333333333, 1.88, pd.DataFrame([
            [0.0, 0.10175362872340427, -0.0510378170212766, 0.0, 0.1270954345744681, -0.002576041489361702, -0.04343849521276596, 0.1],
            [0.033333333, 0.08784300638297873, -0.003638658510638298, 5.904255319148937e-17, 0.12461599468085108, 0.12155694574468086, 0.11064097127659575, 0.033333333],
            [0.1, 0.04092685531914894, 0.018676298936170215, 5.904255319148937e-17, 0.09437971063829788, 0.16580045425531914, 0.21278100638297873, 0.06666666700000001],
            [0.233333333, 0.06620425957446809, -0.04311649042553192, 0.0, -0.007663722872340426, -0.04820417180851064, -0.023248772340425532, 0.133333333]],
            columns = ['t','Finger','Shoulder','Hip','Knee','Ankle','Toe','Time']
            )
        ],
        ['Schlesinger', 'Male', 'Front', 'Fast', 0.666666666666666, 1.88, pd.DataFrame([
            [0.0, 0.016588014010633034, -0.055594980290180854, 0.0, 0.10530875561295691, -0.0946019465697298, -0.15879253411996702, 0.16666666666666596],
            [0.0666666666666666, 0.04916084152242085, -0.01322014449938319, 0.0, 0.1531626626981766, 0.037096831332869576, -0.03865509931568697, 0.0666666666666666],
            [0.233333333333333, 0.07846633294120532, 0.03895669957042548, 0.0, 0.10435368813961703, 0.19156642846824734, 0.23982246922645162, 0.1666666666666664],
            [0.5, 0.007942140041454788, 0.016537747301509947, 0.0, -0.002111201783171404, -0.027093756217366864, 0.023273486324009312, 0.266666666666667]],
            columns = ['t','Finger','Shoulder','Hip','Knee','Ankle','Toe','Time']
            )
        ],
        ['Phelps', 'Male', 'Back', 'Slow', 0.6, 1.88, pd.DataFrame([
            [0.0, -0.009846928383711597, -0.10858234542038776, 0.0, 0.06671072202298352, -0.13726559026183033, -0.17931463579227502, 0.16666666666666696],
            [0.1, 0.05674551221724522, -0.05328578062296809, -1.181088324069314e-16, 0.1496555692191133, 0.06718384771108936, 0.06138805803178777, 0.1],
            [0.233333333333333, 0.09832143205958298, 0.03169942110311979, -1.181088324069314e-16, 0.09773002494945054, 0.1738145496680394, 0.21556789164341755, 0.133333333333333],
            [0.433333333333333, 0.008900677007498938, -0.04337971152824341, -1.181088324069314e-16, -0.01990084925597, -0.06058965843310851, -0.01851104254715777, 0.2]],
            columns = ['t','Finger','Shoulder','Hip','Knee','Ankle','Toe','Time']
            )
        ],
        ['Dressel', 'Male', 'Front', 'Fast', 0.466666666666666, 1.88, pd.DataFrame([
            [0.0, -0.010638297872340427, -0.0957446808510633, 0.0, 0.0, -0.15425531914893564, -0.17021276595744628, 0.13333333333333303],
            [0.0666666666666666, 0.015957446808510745, -0.07978723404255267, 0.0, 0.16489361702127608, 0.031914893617021274, -0.037234042553191384, 0.0666666666666666],
            [0.233333333333333, 0.021276595744680854, 0.02659574468085117, 0.0, 0.06382978723404255, 0.18085106382978672, 0.2712765957446803, 0.1666666666666664],
            [0.333333333333333, -0.07978723404255267, -0.04255319148936149, 2.362176648138628e-16, -0.026595744680850693, -0.058510638297871814, -0.01063829787234016, 0.09999999999999998]],
            columns = ['t','Finger','Shoulder','Hip','Knee','Ankle','Toe','Time']
            )
        ]
            ], 
        columns = ['Swimmer', 'Gender', 'Side', 'Speed', 'Time', 'Height', 'Data Frame']
    )
    return Library

    