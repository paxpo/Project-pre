import sys
import os

INfile = "Aqi_Beijing_Holi.txt"
BIN_Num = 20

sys.path.append("../../func")
from d1_remake_txt import MakeTXT
Infile = MakeTXT(INfile)
#Infile = INfile

sys.path.append("../../func")
from RAW_to_HIST_txt import Converting
from RAW_to_HIST_txt_largeBin import Converting_largeBin
TXT_FILE_LIST = Converting(Infile,NBINS=BIN_Num)
TXT_FILE_LIST_largeBin =  Converting_largeBin(Infile)

#sys.path.append("/Users/leejunho/Desktop/git/python3Env/group_study/project_pre/func")
sys.path.append("../../func")
from c1_basic_statistic import *
from c2_basic_histo_plotting import Basic_histo
#from c2_basic_histo_plotting import Basic_histo
from c4_Fit_Poisson_histo_plotting import Fit_Poisson_histo
from c5_single_sample_mean_Zdistribution import Fit_Sample_Gaus_histo
from c5_single_sample_mean_Tdistribution import t_distribution
from c7_single_sample_variance_distribution import Sample_Variance
#for Input_file in TXT_FILE_LIST:
for ij in range(len(TXT_FILE_LIST)):
    print("The file Name is :",TXT_FILE_LIST[ij])
#    MODE = most_frequent_bin(TXT_FILE_LIST[ij]);      print("MODE :",MODE)
#    DATA_RANGE = c1_data_range(TXT_FILE_LIST[ij]);    print("DATA_RANGE :",DATA_RANGE)
#    MEDIAN = c1_median(TXT_FILE_LIST[ij]);            print("MEDIAN :",MEDIAN)
#    Total_ENTRY = c1_total_ENTRY(TXT_FILE_LIST[ij]);  print("Total_ENTRY :",Total_ENTRY)
#    MEAN = c1_mean(TXT_FILE_LIST[ij]);                print("MEAN :",MEAN)
#    VARIANCE = c1_variance(TXT_FILE_LIST[ij]);        print("VARIANCE :",VARIANCE)
#    STD = c1_standard_deviation(TXT_FILE_LIST[ij]);   print("STD :",STD)
#    print("\n")
    Basic_histo(TXT_FILE_LIST[ij], TXT_FILE_LIST_largeBin[ij])
    Fit_Poisson_histo(TXT_FILE_LIST[ij], TXT_FILE_LIST_largeBin[ij])
    Fit_Sample_Gaus_histo(TXT_FILE_LIST[ij], TXT_FILE_LIST_largeBin[ij], exp_Mean_error=10)
#    t_distribution(TXT_FILE_LIST[ij], TXT_FILE_LIST_largeBin[ij], Show_T=True, Show_sample=True, Show_Gaus=False)
    t_distribution(TXT_FILE_LIST[ij],TXT_FILE_LIST_largeBin[ij], Show_T=True, Show_sample=True, Show_Gaus=True)
    Sample_Variance(TXT_FILE_LIST[ij], TXT_FILE_LIST_largeBin[ij])
