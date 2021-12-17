import unittest
import numpy as np
import pandas as pd
from cbsyst.MyAMI_V2 import (
    MyAMI_params,
    MyAMI_K_calc,
    MyAMI_pK_calc,
    MyAMI_K_calc_multi,
)


class MyAMIConsistency(unittest.TestCase):
    """Compare MyAMI_V2 with MyAMI_V1"""

    def test_CompareToMyAMI_V1(self):
        # parameters calculated by MyAMI_V1.py
        MyAMI_orig = {
            "K0": np.array(
                [
                    -60.240900000000003,
                    93.451700000000002,
                    23.358499999999999,
                    0.023517,
                    -0.023656,
                    0.0047035999999999996,
                ]
            ),
            "K1": np.array(
                [
                    61.217199999999998,
                    -3633.8600000000001,
                    -9.6776999999999997,
                    0.011554999999999999,
                    -0.00011519999999999999,
                ]
            ),
            "K2": np.array(
                [
                    -25.928999999999998,
                    -471.77999999999997,
                    3.16967,
                    0.017809999999999999,
                    -0.0001122,
                ]
            ),
            "KB": np.array(
                [
                    148.0248,
                    137.1942,
                    1.6214200000000001,
                    -8966.8999999999996,
                    -2890.5300000000002,
                    -77.941999999999993,
                    1.728,
                    -0.099599999999999994,
                    -24.4344,
                    -25.085000000000001,
                    -0.24740000000000001,
                    0.053104999999999999,
                ]
            ),
            "KW": np.array(
                [
                    148.96520000000001,
                    -13847.26,
                    -23.652100000000001,
                    118.67,
                    -5.9770000000000003,
                    1.0495000000000001,
                    -0.016150000000000001,
                ]
            ),
            "KspC": np.array(
                [
                    -171.90649999999999,
                    -0.077993000000000007,
                    2839.319,
                    71.594999999999999,
                    -0.77712000000000003,
                    0.0028425999999999998,
                    178.34,
                    -0.077109999999999998,
                    0.0041248999999999999,
                ]
            ),
            "KspA": np.array(
                [
                    -171.94499999999999,
                    -0.077993000000000007,
                    2903.2930000000001,
                    71.594999999999999,
                    -0.068392999999999995,
                    0.0017275999999999999,
                    88.135000000000005,
                    -0.10018000000000001,
                    0.0059414999999999997,
                ]
            ),
            "KSO4": np.array(
                [
                    141.328,
                    -4276.1000000000004,
                    -23.093,
                    -13856.0,
                    324.56999999999999,
                    -47.985999999999997,
                    35474.0,
                    -771.53999999999996,
                    114.723,
                    -2698.0,
                    1776.0,
                ]
            ),
        }

        MyAMI_lowMgnormCa = {
            "K0": np.array(
                [
                    -58.835988024241153,
                    91.481812147562721,
                    22.67747869243458,
                    0.015798688488939287,
                    -0.018255877435858551,
                    0.0038003679139008897,
                ]
            ),
            "K1": np.array(
                [
                    58.062087886559837,
                    -3494.0233318473447,
                    -9.2038164315804138,
                    0.011168501289914329,
                    -0.00011365376326036976,
                ]
            ),
            "K2": np.array(
                [
                    -31.434097349400538,
                    -162.75662343373008,
                    3.9109079889323324,
                    0.017704525744139957,
                    -0.00011016412477939389,
                ]
            ),
            "KB": np.array(
                [
                    156.24940221168944,
                    128.25079663389661,
                    1.2732109192923926,
                    -9381.59308693192,
                    -2723.8280995436671,
                    -66.130468335345725,
                    2.0505262462401235,
                    -0.11549440220126056,
                    -25.63858301431771,
                    -23.400388268842654,
                    -0.19484439742973533,
                    0.04906551592740143,
                ]
            ),
            "KW": np.array(
                [
                    167.00613348978843,
                    -14400.583448847821,
                    -26.52650914480521,
                    338.16897225894417,
                    -10.913107565225641,
                    1.7768705047133142,
                    -0.018636421994989119,
                ]
            ),
            "KspC": np.array(
                [
                    -82.768891656782529,
                    -0.0510250425127734,
                    653.61741054522099,
                    35.217868927106146,
                    -0.88625140484347653,
                    0.0030161168011013243,
                    188.12909155930794,
                    -0.074743157746358937,
                    0.0040202923717078919,
                ]
            ),
            "KspA": np.array(
                [
                    -81.943776995027889,
                    -0.050733308492461167,
                    697.26556788488676,
                    34.861317352102368,
                    -0.17500557330551639,
                    0.0018967287129921546,
                    97.551225643759196,
                    -0.097813597252809872,
                    0.0058373362605226046,
                ]
            ),
            "KSO4": np.array(
                [
                    144.01723254985009,
                    -4387.5774837397103,
                    -23.495881238664886,
                    -14072.430144624854,
                    329.36367918201313,
                    -48.71841105264248,
                    35279.449308067575,
                    -770.95513413049468,
                    114.68004975234182,
                    -2574.4649294352289,
                    1744.9018046633666,
                ]
            ),
        }

        MyAMI_highMgnormCa = {
            "K0": np.array(
                [
                    -61.810571613553734,
                    95.652592105230966,
                    24.119389775679647,
                    0.031633200121371587,
                    -0.029340456577593793,
                    0.0056540258038219647,
                ]
            ),
            "K1": np.array(
                [
                    64.646362988472191,
                    -3785.8006010138361,
                    -10.192756962536393,
                    0.011991951216023209,
                    -0.00011695382574553078,
                ]
            ),
            "K2": np.array(
                [
                    -22.608853013802992,
                    -640.62695443600217,
                    2.7186241756853655,
                    0.017134698149918966,
                    -0.00010846862856783123,
                ]
            ),
            "KB": np.array(
                [
                    135.80210783355605,
                    148.02810999968719,
                    1.9073200904360372,
                    -8397.0531700794145,
                    -3102.8610734941999,
                    -91.196260901984544,
                    1.8875655121628416,
                    -0.10394558858478999,
                    -22.634895306112007,
                    -27.082927065489599,
                    -0.29068978419138441,
                    0.057501272476377069,
                ]
            ),
            "KW": np.array(
                [
                    152.35156939395085,
                    -14181.651163426186,
                    -24.014243686459675,
                    94.885045534960184,
                    -5.0639203227863989,
                    0.91026133561441924,
                    -0.017428588478068725,
                ]
            ),
            "KspC": np.array(
                [
                    -204.75418064702887,
                    -0.088662754155618279,
                    3593.6747830384475,
                    85.188432139333557,
                    -0.77303216591690571,
                    0.0028322646621595665,
                    180.47102892397942,
                    -0.077798210121014622,
                    0.0041609885276488552,
                ]
            ),
            "KspA": np.array(
                [
                    -205.27704739574395,
                    -0.088822477794205643,
                    3669.2749301858271,
                    85.387619157326156,
                    -0.065400426582049809,
                    0.0017191937785523521,
                    90.430831723766886,
                    -0.10086886021110948,
                    0.0059773450025442203,
                ]
            ),
            "KSO4": np.array(
                [
                    138.11090558191418,
                    -4143.2416843287729,
                    -22.610868816926811,
                    -13639.732449040992,
                    319.889250580885,
                    -47.26969380854311,
                    35696.914533285184,
                    -772.52584556489103,
                    114.82170476859116,
                    -2829.3346454669118,
                    1808.8923394974406,
                ]
            ),
        }

        MyAMI_normMglowCa = {
            "K0": np.array(
                [
                    -6.03548508e01,
                    9.36114752e01,
                    2.34137368e01,
                    1.94715158e-02,
                    -2.08806308e-02,
                    4.23607009e-03,
                ]
            ),
            "K1": np.array(
                [
                    6.05702335e01,
                    -3.60485464e03,
                    -9.58081876e00,
                    1.14809803e-02,
                    -1.14709385e-04,
                ]
            ),
            "K2": np.array(
                [
                    -2.77919921e01,
                    -3.79324545e02,
                    3.43382118e00,
                    1.79447289e-02,
                    -1.12751209e-04,
                ]
            ),
            "KB": np.array(
                [
                    1.49647292e02,
                    1.35549007e02,
                    1.56718807e00,
                    -9.04463876e03,
                    -2.85979178e03,
                    -7.57991009e01,
                    1.75233915e00,
                    -1.01451490e-01,
                    -2.46730649e01,
                    -2.47778376e01,
                    -2.39231676e-01,
                    5.23920566e-02,
                ]
            ),
            "KW": np.array(
                [
                    1.49576235e02,
                    -1.38635875e04,
                    -2.37505094e01,
                    1.29091623e02,
                    -6.21968885e00,
                    1.08462795e00,
                    -1.54398156e-02,
                ]
            ),
            "KspC": np.array(
                [
                    -2.11408017e02,
                    -9.01621865e-02,
                    3.85340661e03,
                    8.76362418e01,
                    -8.57175711e-01,
                    2.97591758e-03,
                    1.89300240e02,
                    -7.66468777e-02,
                    4.10487970e-03,
                ]
            ),
            "KspA": np.array(
                [
                    -2.12187806e02,
                    -9.03999985e-02,
                    3.93558943e03,
                    8.79398038e01,
                    -1.49603758e-01,
                    1.86290184e-03,
                    9.92628637e01,
                    -9.97183643e-02,
                    5.92165270e-03,
                ]
            ),
            "KSO4": np.array(
                [
                    1.41162345e02,
                    -4.27119136e03,
                    -2.30672798e01,
                    -1.38886757e04,
                    3.25460559e02,
                    -4.81245694e01,
                    3.54568237e04,
                    -7.71587320e02,
                    1.14734249e02,
                    -2.68397019e03,
                    1.77246279e03,
                ]
            ),
        }

        MyAMI_normMghighCa = {
            "K0": np.array(
                [
                    -5.85908747e01,
                    9.11381861e01,
                    2.25586439e01,
                    4.97087339e-02,
                    -4.15659267e-02,
                    7.72433484e-03,
                ]
            ),
            "K1": np.array(
                [
                    6.43284560e01,
                    -3.77425690e03,
                    -1.01428091e01,
                    1.18920079e-02,
                    -1.18008513e-04,
                ]
            ),
            "K2": np.array(
                [
                    -1.81464422e01,
                    -8.46680857e02,
                    2.05841462e00,
                    1.69653256e-02,
                    -1.07290463e-04,
                ]
            ),
            "KB": np.array(
                [
                    1.40900391e02,
                    1.44409880e02,
                    1.84931823e00,
                    -8.63149694e03,
                    -3.02381006e03,
                    -8.74468911e01,
                    1.65056596e00,
                    -9.13773676e-02,
                    -2.33844143e01,
                    -2.64301900e01,
                    -2.81647582e-01,
                    5.62137006e-02,
                ]
            ),
            "KW": np.array(
                [
                    1.45097630e02,
                    -1.36326635e04,
                    -2.31086658e01,
                    8.08676920e01,
                    -5.26774127e00,
                    9.51226062e-01,
                    -2.04932435e-02,
                ]
            ),
            "KspC": np.array(
                [
                    4.11053758e01,
                    -1.26438575e-02,
                    -2.60992410e03,
                    -1.49164849e01,
                    -4.26344372e-01,
                    2.25682999e-03,
                    1.28795617e02,
                    -7.85719757e-02,
                    4.18761611e-03,
                ]
            ),
            "KspA": np.array(
                [
                    4.49695745e01,
                    -1.13889201e-02,
                    -2.64163126e03,
                    -1.65152747e01,
                    2.88801705e-01,
                    1.13086887e-03,
                    3.76621559e01,
                    -1.01642049e-01,
                    6.00390771e-03,
                ]
            ),
            "KSO4": np.array(
                [
                    1.44315482e02,
                    -4.38452060e03,
                    -2.35474419e01,
                    -1.37127931e04,
                    3.20008438e02,
                    -4.72715939e01,
                    3.54890440e04,
                    -7.70535961e02,
                    1.14566217e02,
                    -2.74112295e03,
                    1.78717921e03,
                ]
            ),
        }

        MyAMI_lowMglowCa = {
            "K0": np.array(
                [
                    -5.90319397e01,
                    9.17565596e01,
                    2.27724665e01,
                    1.24391613e-02,
                    -1.59576406e-02,
                    3.41280775e-03,
                ]
            ),
            "K1": np.array(
                [
                    5.76448794e01,
                    -3.47522029e03,
                    -9.14143733e00,
                    1.11150018e-02,
                    -1.13242402e-04,
                ]
            ),
            "K2": np.array(
                [
                    -3.37954086e01,
                    -3.46595936e01,
                    4.24078016e00,
                    1.76509013e-02,
                    -1.09083384e-04,
                ]
            ),
            "KB": np.array(
                [
                    1.57635777e02,
                    1.27122314e02,
                    1.25371033e00,
                    -9.44500320e03,
                    -2.69984318e03,
                    -6.52280782e01,
                    2.04733321e00,
                    -1.16013074e-01,
                    -2.58437375e01,
                    -2.31951765e01,
                    -1.91902793e-01,
                    4.86397978e-02,
                ]
            ),
            "KW": np.array(
                [
                    1.67104783e02,
                    -1.44077184e04,
                    -2.65351179e01,
                    3.39503783e02,
                    -1.09367304e01,
                    1.77820861e00,
                    -1.72130700e-02,
                ]
            ),
            "KspC": np.array(
                [
                    -1.33143211e02,
                    -6.72875403e-02,
                    1.91186338e03,
                    5.58167821e01,
                    -1.05394339e00,
                    3.29112393e-03,
                    2.11295270e02,
                    -7.37559566e-02,
                    3.97954823e-03,
                ]
            ),
            "KspA": np.array(
                [
                    -1.33474910e02,
                    -6.73659373e-02,
                    1.98398576e03,
                    5.59337422e01,
                    -3.44386192e-01,
                    2.17466025e-03,
                    1.20964128e02,
                    -9.68304730e-02,
                    5.79693999e-03,
                ]
            ),
            "KSO4": np.array(
                [
                    1.43444246e02,
                    -4.36227512e03,
                    -2.34091242e01,
                    -1.41292019e04,
                    3.30493981e02,
                    -4.88918849e01,
                    3.53149195e04,
                    -7.71380180e02,
                    1.14744966e02,
                    -2.58830780e03,
                    1.74920566e03,
                ]
            ),
        }

        MyAMI_highMghighCa = {
            "K0": np.array(
                [
                    -6.02425828e01,
                    9.34540602e01,
                    2.33593155e01,
                    5.85141596e-02,
                    -4.77295195e-02,
                    8.75502995e-03,
                ]
            ),
            "K1": np.array(
                [
                    6.79888755e01,
                    -3.93646799e03,
                    -1.06925912e01,
                    1.23494824e-02,
                    -1.19840962e-04,
                ]
            ),
            "K2": np.array(
                [
                    -1.70362926e01,
                    -9.01669948e02,
                    1.92175902e00,
                    1.61037168e-02,
                    -1.01676990e-04,
                ]
            ),
            "KB": np.array(
                [
                    1.29522254e02,
                    1.55382699e02,
                    2.20070106e00,
                    -8.08694346e03,
                    -3.23198975e03,
                    -1.01880510e02,
                    1.62155185e00,
                    -8.75521170e-02,
                    -2.17129119e01,
                    -2.84732629e01,
                    -3.34760145e-01,
                    6.08933621e-02,
                ]
            ),
            "KW": np.array(
                [
                    1.48590714e02,
                    -1.39952958e04,
                    -2.34644673e01,
                    5.44315222e01,
                    -4.23762669e00,
                    7.90919098e-01,
                    -2.00690949e-02,
                ]
            ),
            "KspC": np.array(
                [
                    -3.25067958e01,
                    -3.60455866e-02,
                    -8.14801019e02,
                    1.52645053e01,
                    -5.31234464e-01,
                    2.42410927e-03,
                    1.45756113e02,
                    -7.84765220e-02,
                    4.19289172e-03,
                ]
            ),
            "KspA": np.array(
                [
                    -2.98860875e01,
                    -3.51988299e-02,
                    -8.16536597e02,
                    1.41766901e01,
                    1.81328644e-01,
                    1.30281645e-03,
                    5.50191697e01,
                    -1.01568084e-01,
                    6.01026695e-03,
                ]
            ),
            "KSO4": np.array(
                [
                    1.41126393e02,
                    -4.25101378e03,
                    -2.30696231e01,
                    -1.34717641e04,
                    3.14539498e02,
                    -4.64358728e01,
                    3.57305062e04,
                    -7.71293348e02,
                    1.14627567e02,
                    -2.89408279e03,
                    1.82606015e03,
                ]
            ),
        }

        # Compare to MyAMI_V2

        def pcomp(par, opar):
            diffs = []
            Ks = MyAMI_K_calc(param_dict=par)
            oKs = MyAMI_K_calc(param_dict=opar)

            for k in Ks:
                diffs.append(Ks[k] - oKs[k])
            return all(abs(np.array(diffs)) < 1e-6)

        self.assertTrue(pcomp(MyAMI_params(), MyAMI_orig), msg="Ambient params")

        self.assertTrue(
            pcomp(MyAMI_params(0.01, 0.01), MyAMI_lowMgnormCa),
            msg="Low Mg, Norm Ca params",
        )

        self.assertTrue(
            pcomp(MyAMI_params(0.01, 0.1), MyAMI_highMgnormCa),
            msg="High Mg, Norm Ca params",
        )

        self.assertTrue(
            pcomp(MyAMI_params(0.005, 0.05), MyAMI_normMglowCa),
            msg="Normal Mg, Low Ca params",
        )

        self.assertTrue(
            pcomp(MyAMI_params(0.05, 0.05), MyAMI_normMghighCa),
            msg="Normal Mg, High Ca params",
        )

        self.assertTrue(
            pcomp(MyAMI_params(0.05, 0.1), MyAMI_highMghighCa),
            msg="High Mg, High Ca params",
        )

        self.assertTrue(
            pcomp(MyAMI_params(0.005, 0.01), MyAMI_lowMglowCa),
            msg="Low Mg, Low Ca params",
        )
        return

    def test_CompareToDickson2007(self):
        # Check params @ 25ºC and 35 PSU

        # Parameters are from Dickson, Sabine & Christian
        # (Guide to best practises for ocean CO2 measurements,
        # PICES Special Publication, 2007), Chapter 5.7.2 (seawater).

        # Except KspC and KspA, which are from from Zeebe &
        # Wolf-Gladrow, 2001, Appendix A.10

        K_ckeck = {
            "K0": np.exp(-3.5617),
            "K1": 10 ** (-5.8472),
            "K2": 10 ** (-8.9660),
            "KB": np.exp(-19.7964),
            # 'KW': np.exp(-30.434),
            "KSO4": np.exp(-2.30),
            "KspC": 10 ** -6.3693,
            "KspA": 10 ** -6.1883,
        }

        Ks = MyAMI_K_calc()

        for k, p in K_ckeck.items():
            self.assertAlmostEqual(Ks[k] / p, 1, places=3, msg="failed on " + k)
        return

    def test_CompareToMehrbachData(self):
        """
        Compares pK1 and pK2 calcualted by MyAMI_V2 to data from
        Mehrbach et al (1973), as per Lueker et al (2000).

        Test data on Total pH scale taken from Table 2 of Lueker et al (2000)
        """
        # read data
        lk = pd.read_csv(
            "cbsyst/test_data/Lueker2000/Lueker2000_Table2.csv", comment="#"
        )

        # calculate MyAMI Ks
        mKs = MyAMI_K_calc(lk.TempC, lk.Sal)

        # calculate pK1 and pK2 2 residuals
        rpK1 = lk.pK1 - -np.log10(mKs.K1)
        rpK2 = lk.pK2 - -np.log10(mKs.K2)

        # calculate median and 95% CI of residuals
        rpK1_median = rpK1.median()
        rpK1_95ci = np.percentile(rpK1[~np.isnan(rpK1)], (2.5, 97.5))
        self.assertLessEqual(
            abs(rpK1_median), 0.005, msg="Median offset from Mehrbach (1973) pK1."
        )
        self.assertTrue(
            all(abs(rpK1_95ci) <= 0.02),
            msg="95% CI of difference from Mehrbach pK1 <= 0.02",
        )

        rpK2_median = rpK1.median()
        rpK2_95ci = np.percentile(rpK2[~np.isnan(rpK2)], (2.5, 97.5))
        self.assertLessEqual(
            abs(rpK2_median), 0.005, msg="Median offset from Mehrbach (1973) pK2."
        )
        self.assertTrue(
            all(abs(rpK2_95ci) <= 0.02),
            msg="95% CI of difference from Mehrbach pK2 <= 0.02",
        )

        return


if __name__ == "__main__":
    unittest.main()
