import skrf as rf
from matplotlib import pyplot as plt
import numpy as np
import math as math
import statistics
import random
import toolz
import ttg
import itertools
import pickle
import pathlib
import os
#returns the names of the files in the directory data as a list





##### Подготовильтельный блок
list_of_files = os.listdir("dsa_almaz_s2p_file"); # директория
CellPath = os.listdir("dsa_almaz_s2p_file");
Num_Of_Bits=int(len(list_of_files)/2); # Определили число битов в комбинации;
#Создаем таблицу истинности
# Лист битов ['Bit0', 'Bit1', 'Bit2', 'Bit3', 'Bit4', 'Bit5']
BitList = [];
for i in range(0,Num_Of_Bits,1):
    BitList.append(str('Bit'+str(i)));
#Таблица истинности
Bit = ttg.Truths(BitList, ascending=True) # развенутная , младший  - бит последний
###### Таблица Истиности готова;
print(Bit);
number_of_states = 2**Num_Of_Bits;  ## число состояний
#Надо разобрать еще все файлы, 
Cell_Name_List = [];
Cell_P1dB_List = [];
Cell_Truth_List = [];

for i in range(len(list_of_files)):
    Split_String =  list_of_files[i].split("_");
    Cell_Name_List.append(Split_String[0]);
    Cell_P1dB_List.append(Split_String[1]);
    Cell_Truth_List.append(Split_String[2][:1]);

class Cell:  # классс ячеек - 2* число бит
    def __init__(self, CellValue, P1dB, ON_OFF, Network):
            self.CellValue = CellValue;
            self.P1dB = P1dB;              
            self.ON_OFF = ON_OFF; 
            self.Network = Network;
   
def GetCells(CellPath):  # Создание всех ячееек
 
    Cell_Name_List = [];
    Cell_P1dB_List = [];
    Cell_Truth_List = [];
    list_of_files = CellPath;

    for i in range(len(list_of_files)):
        Split_String =  list_of_files[i].split("_");
        Cell_Name_List.append(Split_String[0]);
        Cell_P1dB_List.append(Split_String[1]);
        Cell_Truth_List.append(Split_String[2][:1]);
    CellList = [];

    for i in range(len(list_of_files)):
        CellValue = Cell_Name_List[i];
        P1dB = Cell_P1dB_List[i];
        ON_OFF = Cell_Truth_List[i];
        Network = rf.Network('dsa_almaz_s2p_file/'+str(CellValue)+'_'+str(P1dB)+'_'+str(ON_OFF)+'.S2P');
        Temp_Cell = Cell(CellValue, P1dB, ON_OFF, Network);
        CellList.append(Temp_Cell);
    return CellList;

#Лист всех ячеек
List_Cells = GetCells(CellPath);
############
UniqueNames = list(set(Cell_Name_List));
UniqueNames.sort(key=float); ## отсортироваали
UniqueNames.reverse(); ## развернули, младший бит последний
print(UniqueNames)
#########################################




def GetStateData(StateNumber):
    ##### Надо это обернуть в функцию
    CellList = []; # лист обьектов ячейки Сell для состояния StateString
    CascadeList =  []; # лист 2 полюсников rf.Network для состояния, в дальнейшем создания системы и перестановокж
    # Надо заполнить CascadeList по порядку в соотвествиие с таблицей истинност
    # Значит по порядку, это перебор по именам UniqueNames
    StateString =  State; # 000 000
    #StateString = 1; # 000 001 / младший бит последний
    #....
    #StateString = 63; # 111 111
    for i in range(len(UniqueNames)):
#    # теперь идем по списку ячеек и выбираем нужные
        for cell in range(len(List_Cells)):
            SelectCell = List_Cells[cell];
            if (SelectCell.CellValue==UniqueNames[i] and SelectCell.ON_OFF==str(int(Bit.base_conditions[StateString][i])) and SelectCell not in CellList):
                CellList.append(SelectCell)
                CascadeList.append(SelectCell.Network);
            else:
                continue;
##################### Return состояние - лист каскадов
    return CellList, CascadeList;

###########################   Проверка вроде работает
CellList, CascadeList= GetStateData(13);
for states in range(len(CellList)):
    print(CellList[states].CellValue+' '+CellList[states].ON_OFF);
##############################################




class State(self, Number, CellList, CascadeList, 
                  P1dB,  # точка сжатия для данного состояния при каскадном включении
                  
                  S11_dB,  # лист значений
                  S22_dB,  # /-/-/-/-/-/-/-
                  S21_dB,  # /-/-/-/-/-/-/-
                  S21_deg, # /-/-/-/-/-/-/-

                  S11_dB_Max, # максимальное значение из списка частот
                  S22_dB_Max, # максимальное значение из списка частот
                  S21_dB_MF, # дБ на центральной частоте
                  S21_deg_MF): # Градус на центральной частоте
            
            self.Number = Number;
            self.CellList = CellList;
            self.CascadeList = CascadeList;
            self.P1dB = P1dB;
            self.S11_dB = S11_dB;
            self.S22_dB = S22_dB;
            self.S21_dB = S21_dB;
            self.S11_dB_Max = S11_dB_Max;
            self.S22_dB_Max = S22_dB_Max;
            self.S21_dB_MF = S21_dB_MF;
            self.S21_deg_MF = S21_deg_MF;


print('шовашыовшаоышвоа   ышоа');
#####################




































#for cell in range(len(UniqueNames)):

#    SelectCell = rf.Network('dsa_almaz_s2p_file/'+str(UniqueNames[cell])+'_'+List_Cells[]+'_'+str(Bit0)+'.S2P');

#    CascadeList.append(SelectCell);







#for Bits_Num in range(0,Num_Of_Bits,2):
    
#    Bit0 = int(Bit.base_conditions[State][0]);     

#    Cascade.append(rf.Network('dsa_almaz_s2p_file/'+str(Cell_Name_List[Bits_Num])+'_'+Cell_P1dB_List[Bits_Num]+'_'+str(Bit0)+'.S2P'))


#print(Num_Of_Bits);



#def GetState(State, Permutaion):  # На вход номер состояния, допустим состояние 0 - s - состояние, p - перестановка

#    Bit0 = int(Bit.base_conditions[State][0]); 
#    Bit1 = int(Bit.base_conditions[State][1]); 
#    Bit2 = int(Bit.base_conditions[State][2]); 
#    Bit3 = int(Bit.base_conditions[State][3]); 
#    Bit4 = int(Bit.base_conditions[State][4]); 
#    Bit5 = int(Bit.base_conditions[State][5]); 

#    Cascade = ([rf.Network('dsa_almaz_s2p_file/0.5_'+str(Bit0)+'.S2P'),
#                                   rf.Network('dsa_almaz_s2p_file/1_'+str(Bit1)+'.S2P'),
#                                     rf.Network('dsa_almaz_s2p_file/2_'+str(Bit2)+'.S2P'),
#                                      rf.Network('dsa_almaz_s2p_file/4_'+str(Bit3)+'.S2P'),
#                                       rf.Network('dsa_almaz_s2p_file/8_'+str(Bit4)+'.S2P'),
#                                        rf.Network('dsa_almaz_s2p_file/16_'+str(Bit5)+'.S2P')]);

#    List_permutations = list(itertools.permutations(Cascade, 6)); ##720 лист этих каскадов  - 1 обьект листа это лист с 6 ячейками он же будет одинаково выдавать если состояние не менял??

#    OrderName = List_permutations[p][0].name+' '+List_permutations[p][1].name+' '+List_permutations[p][2].name+' '+List_permutations[p][3].name+' '+List_permutations[p][4].name+' '+List_permutations[p][5].name;

#    CombinationName = OrderName.replace("_1","");
#    CombinationName = CombinationName.replace("_0","");

#    StateNumber = s; # номер состояния
#    Network = rf.cascade_list(List_permutations[p]);

#    Frequency = Network.f.tolist();
#    print('waiting '+str(p));

#    State_S11_dB = [];   ### точки в соотвествии с  List_Frequencies
#    State_S12_dB = [];
#    State_S21_dB = [];
#    State_S22_dB = [];
#    State_S11_deg = [];
#    State_S12_deg = [];
#    State_S21_deg = [];
#    State_S22_deg = [];

#    for f in range(len(Frequency)):

#        State_S11_dB.append(float(Network.s11[str(Frequency[f])+'hz'].s_db[...]));
#        State_S12_dB.append(float(Network.s12[str(Frequency[f])+'hz'].s_db[...]));
#        State_S21_dB.append(float(Network.s21[str(Frequency[f])+'hz'].s_db[...]));
#        State_S22_dB.append(float(Network.s22[str(Frequency[f])+'hz'].s_db[...]));

#        State_S11_deg.append(float(Network.s11[str(Frequency[f])+'hz'].s_deg[...]))
#        State_S12_deg.append(float(Network.s12[str(Frequency[f])+'hz'].s_deg[...]))
#        State_S21_deg.append(float(Network.s21[str(Frequency[f])+'hz'].s_deg[...]))
#        State_S22_deg.append(float(Network.s22[str(Frequency[f])+'hz'].s_deg[...]))
#        print('waiting');

#    Diff_S11_S22 = [];

#    for d in range(len(State_S11_dB)):
#        Diff_S11_S22.append(abs(abs(State_S11_dB[d])-abs(State_S22_dB[d])));



    
#    return BitOrder(CombinationName, OrderName, Network, StateNumber, State_S11_dB , State_S12_dB, State_S21_dB, State_S22_dB, State_S11_deg, State_S12_deg, State_S21_deg, State_S22_deg, Frequency , Diff_S11_S22)        #, MeanValue_S11, MeanValue_S22









#file_name = 'dsa_almaz_s2p_file/0.5_10_0.s2p';
#path = pathlib.Path(file_name);
#file = path.name;
#File_z =path.stem  # 0.5_10_0
#print('next');
#print(File_z);
#File_z = File_z.replace("_0","");
#print(File_z);


#Cascade = rf.Network('dsa_almaz_s2p_file/0.5_'+str(P1dB)+'_'++str(Bit0)+'.S2P');








#def FitnessFunction(StateSystem):

#    S11_Fit = Get_S11_Fit(); # Функция расчета Fitness S11
                               
#    S22_Fit = Get_S22_Fit(); #

#    RMS_deg_Fit = Get_RMS_deg_Fit();
  
#    RMS_dB_Fit = Get_RMS_dB_Fit();

#    P1dB_Fit = Get_P1dB_Fit();

#    FitnessValue = S11_Fit + S22_Fit + RMS_deg_Fit + RMS_dB_Fit + RMS_deg_Fit + P1dB_Fit;

#    return FitnessValue;












#class BitOrder:  # 720 штук обьектов
#    def __init__(self, CombinationName, OrderName, Network, 
#                 StateNumber, State_S11_dB , State_S12_dB, 
#                 State_S21_dB, State_S22_dB, State_S11_deg, 
#                 State_S12_deg, State_S21_deg, 
#                 State_S22_deg, Frequency, Diff_S11_S22):  # OrderNetwork,
#            #,
#                # MeanValue_S11, MeanValue_S22
#            self.CombinationName = CombinationName;
#            self.OrderName = OrderName;              # Имя порядка например и вкл или выкл состояние  ('05(0)_1(1)_2(0)_4(1)_8(0)_16(1)')
#            self.StateNumber = StateNumber;          # номер состояния, шоб не терять на всякий случай
#            self.Network = Network;       # Матрица S Параметров для этого порядка для данного состояния, матрица состояния #Матрица S параметров     
                
#            self.State_S11_dB = State_S11_dB;   ### точки в соотвествии с  List_Frequencies
#            self.State_S12_dB = State_S12_dB;
#            self.State_S21_dB = State_S21_dB;
#            self.State_S22_dB = State_S22_dB;

#            self.State_S11_deg = State_S11_deg;
#            self.State_S12_deg = State_S12_deg;
#            self.State_S21_deg = State_S21_deg;
#            self.State_S22_deg = State_S22_deg;
#            self.Frequency = Frequency;
#            self.Diff_S11_S22 = Diff_S11_S22;

## таблица истинности;
#Bit = ttg.Truths(['Bit0', 'Bit1', 'Bit2', 'Bit3', 'Bit4', 'Bit5'])

#print(Bit);

# сама функция в цикле по перестановкам и по состояниям



#class PrimaryState:  # 64 штуки
#    def __init__(self,BitOrderList, StateNumber, PrimaryNetwork, Best_Network_List, Solution_Order_List):  # OrderNetwork,
            
#            self.BitOrderList = BitOrderList;  #720 порядков; обьектов BitOrder // ТОП по условию
#            self.StateNumber = StateNumber;          # номер состояния, обязательно;
#            self.PrimaryNetwork = PrimaryNetwork;
#            self.Best_Network_List = Best_Network_List;
#            self.Solution_Order_List = Solution_Order_List;
       




#def GetPrimaryState(State): # получаю состояние

#    num = 720;

#    #pickle.dump(BitOrderList, open('BitOrderList_State_'+str(State)+'.pkl', 'wb'), protocol=pickle.HIGHEST_PROTOCOL);

#    BitOrderList =  pickle.load(open('BitOrderList_State_'+str(State)+'.pkl', 'rb'));

#    Temp_List = [];

#    Limit = -9.4;

#    for i in range(len(BitOrderList)):
#        if ((BitOrderList[i].State_S11_dB[8]<Limit) and (BitOrderList[i].State_S22_dB[8]<Limit)):
#            Temp_List.append(BitOrderList[i]);
#            print('add good');
#        else:
#            print('delete bad');
#            continue;

#    Best_Network_List = Temp_List;

#    #Best_Network_List = sorted(BitOrderList, key = lambda BitOrder: BitOrder.Diff_S11_S22);

#    Best_Network_List = sorted(Best_Network_List, key = lambda BitOrder: BitOrder.CombinationName);

#    PrimaryNetwork = Best_Network_List[0].Network; # это наверное зря

#    StateNumber = State;

#    Solution_Order_List = [];

#    for i in range(len(Best_Network_List)):
#        Solution_Order_List.append(Best_Network_List[i].CombinationName);


#    return PrimaryState(BitOrderList, StateNumber, PrimaryNetwork, Best_Network_List, Solution_Order_List)



#StateSystem_List = [];
#for State in range(0,64,1):
#    StateSystem_List.append(GetPrimaryState(State));
#    print(State);




#pickle.dump(StateSystem_List, open('StateSystem_List_ALL_11.pkl', 'wb'), protocol=pickle.HIGHEST_PROTOCOL);


#Solution  = [];







#Solution = (list(set(StateSystem_List[0].Solution_Order_List)   ####))))))))))))))))))))))))))))))))
#                 & set(StateSystem_List[1].Solution_Order_List) 
#                 & set(StateSystem_List[2].Solution_Order_List) 
#                 & set(StateSystem_List[3].Solution_Order_List) 
#                 & set(StateSystem_List[4].Solution_Order_List) 
#                 & set(StateSystem_List[5].Solution_Order_List) 
#                 & set(StateSystem_List[6].Solution_Order_List) 
#                 & set(StateSystem_List[7].Solution_Order_List) 
#          & set(StateSystem_List[8].Solution_Order_List) 
#          & set(StateSystem_List[9].Solution_Order_List) 
#          & set(StateSystem_List[10].Solution_Order_List) 
#          & set(StateSystem_List[11].Solution_Order_List) 
#          & set(StateSystem_List[12].Solution_Order_List) 
#          & set(StateSystem_List[13].Solution_Order_List) 
#          & set(StateSystem_List[14].Solution_Order_List) 
#          & set(StateSystem_List[15].Solution_Order_List) 
#          & set(StateSystem_List[16].Solution_Order_List) 
#          & set(StateSystem_List[17].Solution_Order_List)
#          & set(StateSystem_List[18].Solution_Order_List) 
#          & set(StateSystem_List[19].Solution_Order_List) 
#          & set(StateSystem_List[20].Solution_Order_List)
#          & set(StateSystem_List[21].Solution_Order_List)
#           & set(StateSystem_List[22].Solution_Order_List)
#            & set(StateSystem_List[23].Solution_Order_List)
#             & set(StateSystem_List[24].Solution_Order_List)
#             & set(StateSystem_List[25].Solution_Order_List)
#              & set(StateSystem_List[26].Solution_Order_List)
#               & set(StateSystem_List[27].Solution_Order_List)
#                & set(StateSystem_List[28].Solution_Order_List)
#                 & set(StateSystem_List[29].Solution_Order_List)
#                  & set(StateSystem_List[30].Solution_Order_List)
#                   & set(StateSystem_List[31].Solution_Order_List)
#                    & set(StateSystem_List[32].Solution_Order_List)
#                     & set(StateSystem_List[33].Solution_Order_List)
#                      & set(StateSystem_List[34].Solution_Order_List)
#                       & set(StateSystem_List[35].Solution_Order_List) 
#                        & set(StateSystem_List[36].Solution_Order_List) 
#                         & set(StateSystem_List[37].Solution_Order_List) 
#                          & set(StateSystem_List[38].Solution_Order_List) 
#                           & set(StateSystem_List[39].Solution_Order_List) 
#                            & set(StateSystem_List[40].Solution_Order_List) 
#                             & set(StateSystem_List[41].Solution_Order_List) 
#                              & set(StateSystem_List[42].Solution_Order_List) 
#                               & set(StateSystem_List[43].Solution_Order_List) 
#                                & set(StateSystem_List[44].Solution_Order_List) 
#                                 & set(StateSystem_List[45].Solution_Order_List) 
#                                  & set(StateSystem_List[46].Solution_Order_List) 
#                                   & set(StateSystem_List[47].Solution_Order_List)
#                                    & set(StateSystem_List[48].Solution_Order_List)
#                                     & set(StateSystem_List[49].Solution_Order_List)
#                                      & set(StateSystem_List[50].Solution_Order_List)
#                                       & set(StateSystem_List[51].Solution_Order_List)
#                                        & set(StateSystem_List[52].Solution_Order_List)
#                                         & set(StateSystem_List[53].Solution_Order_List)
#                                          & set(StateSystem_List[54].Solution_Order_List)
#                                           & set(StateSystem_List[55].Solution_Order_List)
#                                            & set(StateSystem_List[56].Solution_Order_List)
#                                             & set(StateSystem_List[57].Solution_Order_List)
#                                             & set(StateSystem_List[58].Solution_Order_List)
#                                             & set(StateSystem_List[59].Solution_Order_List)
#                                             & set(StateSystem_List[60].Solution_Order_List)
#                                             & set(StateSystem_List[61].Solution_Order_List)
#                                             & set(StateSystem_List[62].Solution_Order_List)
#                                             & set(StateSystem_List[63].Solution_Order_List)
                       
#                       ));
#print(Solution);








##Yt = GetBitOrder(0,0);

#print('sss');

#num = 720;
############################ Сортировка списка
#ListBitOrder=[];
#for i in range(0,num,1):
#    ListBitOrder.append(GetBitOrder(0,i))
#for k in range(0,num,1):
#    print(ListBitOrder[k].State_S11_dB)
#for k in range(0,num,1):
#    print(ListBitOrder[k].OrderName)

#import operator

#print('********C111 и С22*****************')


#pickle.dump(ListBitOrder, open('ListBitOrder.pkl', 'wb'), protocol=pickle.HIGHEST_PROTOCOL);


#ListBitOrder =  pickle.load(open('ListBitOrder.pkl', 'rb'));

#Temp_List = [];

#for i in range(len(ListBitOrder)):
#    if ((ListBitOrder[i].State_S11_dB[0]<-12) and (ListBitOrder[i].State_S22_dB[0]<-12)):
#        Temp_List.append(ListBitOrder[i]);
#    else:
#        continue;


#ListBitOrder = Temp_List;

#num = len(ListBitOrder);

#ListBitOrder = sorted(ListBitOrder, key = lambda BitOrder: BitOrder.Diff_S11_S22);
##ListBitOrder = sorted(ListBitOrder, key = lambda BitOrder: BitOrder.State_S22_dB);
#X = np.arange(0,num,1);
#Y_S11 = [];
#Y_S22 = [];
#Y_S21 = [];
#Y_Dif = [];
#Level_10 = [];

#for i in range(0,num,1):
#    Y_S11.append(ListBitOrder[i].State_S11_dB);
#    Y_S22.append(ListBitOrder[i].State_S22_dB);
#    Y_Dif.append(ListBitOrder[i].Diff_S11_S22);
#    Y_S21.append(ListBitOrder[i].State_S21_dB);
#    Level_10.append(-12);

#plt.plot(X,Y_S11, 'rP-', markersize = 3.5, linewidth = 1, markeredgewidth = 1, markerFacecolor = 'k', label ='S11' ,markevery=1);
#plt.plot(X,Y_S22, 'kd-', markersize = 3.5, linewidth = 1, markeredgewidth = 1, markerFacecolor = 'y', label ='S22' ,markevery=1);
#plt.plot(X,Y_Dif, 'yd-', markersize = 3.5, linewidth = 1, markeredgewidth = 1, markerFacecolor = 'r', label ='Diff' ,markevery=1);
#plt.plot(X,Y_S21, 'bd-', markersize = 3.5, linewidth = 1, markeredgewidth = 1, markerFacecolor = 'r', label ='S21' ,markevery=1);
#plt.plot(X,Level_10, 'mh-', markersize = 3.5, linewidth = 1, markeredgewidth = 1, markerFacecolor = 'r', label ='-12 level' ,markevery=1);

#plt.ylim(-36,5);  
#plt.yticks(np.arange(-36,5,0.5))

#plt.grid(color='k', linestyle='--', linewidth=0.3);
#plt.legend();
#plt.show();





#a = [-5, -2, -5];


#b = [-3, -2, -5]

#c = [];

#for i in range(0,3,1):
#    c.append(abs(a[i] - abs(b[i])))
#    c.append(abs(a[i])-abs(b[i]))
#print(abs(a[0])-abs(b[0]))
#print(c);
##ListBitOrder = sorted(ListBitOrder, key=lambda BitOrder: operator.itemgetter(0,1));

#for k in range(0,num,1):
#    print(ListBitOrder[k].OrderName);

#print('**********VCEEEE*********************');
#for k in range(130,145,1):
#    print('**********VCEEEE******------------------------------------------------------------***************')
#    print(' S11---*'+str(ListBitOrder[k].State_S11_dB[0])+' S22---*'+str(ListBitOrder[k].State_S22_dB[0])+'\n');
#    print(' S11---*'+str(ListBitOrder[k].State_S11_dB[1])+' S22---*'+str(ListBitOrder[k].State_S22_dB[1])+'\n');
#    print(' S11---*'+str(ListBitOrder[k].State_S11_dB[2])+' S22---*'+str(ListBitOrder[k].State_S22_dB[2])+'\n');
#    print(' S11---*'+str(ListBitOrder[k].State_S11_dB[3])+' S22---*'+str(ListBitOrder[k].State_S22_dB[3])+'\n');
#    print(' S11---*'+str(ListBitOrder[k].State_S11_dB[4])+' S22---*'+str(ListBitOrder[k].State_S22_dB[4])+'\n');
#    print(' S11---*'+str(ListBitOrder[k].State_S11_dB[5])+' S22---*'+str(ListBitOrder[k].State_S22_dB[5])+'\n');
#    print(' S11---*'+str(ListBitOrder[k].State_S11_dB[6])+' S22---*'+str(ListBitOrder[k].State_S22_dB[6])+'\n');
#    print('**********VCEEEE*********************************************************************************')
#print('**********VCEEEE*********************');

#print('**********VCEEEE*********************');
#for k in range(180,190,1):
#    print('**********VCEEEE******------------------------------------------------------------***************')
#    print(' S11---*'+str(ListBitOrder[k].State_S11_dB[0])+' S22---*'+str(ListBitOrder[k].State_S22_dB[0])+'\n');
#    print(' S11---*'+str(ListBitOrder[k].State_S11_dB[1])+' S22---*'+str(ListBitOrder[k].State_S22_dB[1])+'\n');
#    print(' S11---*'+str(ListBitOrder[k].State_S11_dB[2])+' S22---*'+str(ListBitOrder[k].State_S22_dB[2])+'\n');
#    print(' S11---*'+str(ListBitOrder[k].State_S11_dB[3])+' S22---*'+str(ListBitOrder[k].State_S22_dB[3])+'\n');
#    print(' S11---*'+str(ListBitOrder[k].State_S11_dB[4])+' S22---*'+str(ListBitOrder[k].State_S22_dB[4])+'\n');
#    print(' S11---*'+str(ListBitOrder[k].State_S11_dB[5])+' S22---*'+str(ListBitOrder[k].State_S22_dB[5])+'\n');
#    print(' S11---*'+str(ListBitOrder[k].State_S11_dB[6])+' S22---*'+str(ListBitOrder[k].State_S22_dB[6])+'\n');
#    print('**********VCEEEE*********************************************************************************')
#print('**********VCEEEE*********************');













#List_Mean_S11 = [];
#for j in range(0,num,1):
#    List_Mean_S11.append(ListBitOrder[j].MeanValue_S11);
#List_Mean_S22 = [];
#for j in range(0,num,1):
#    List_Mean_S22.append(ListBitOrder[j].MeanValue_S22);
#List_Mean_S11 = statistics.mean(List_Mean_S11);
#List_Mean_S22 = statistics.mean(List_Mean_S22);
#print(str(List_Mean_S11));
#print(str(List_Mean_S22));


#ListBitOrder = sorted(ListBitOrder, key = lambda BitOrder: BitOrder.State_S22_dB);
#for k in range(0,50,1):
#    print(ListBitOrder[k].OrderName)
#print('********************************')
#for k in range(0,50,1):
#    print(ListBitOrder[k].State_S22_dB)

#print('sss');


###################################################
################################
#list_1 = [1, 1.2, 1.05];
#list_2 = [1, 1.19, 1.04];
#LISTER = [list_1, list_2];
#print(LISTER);
#print(sorted(LISTER)); 
###############################









#def GetPrimaryState(State):

#    ListBitOrder=[];

#    for i in range(0,720,1):
#        ListBitOrder.append(GetBitOrder(State,i));
    
#    ListBitOrder = sorted(ListBitOrder, key = lambda BitOrder: BitOrder.State_S11_dB)
#    BitOrderList = ListBitOrder;
    

#    StateNumber = State;



#    return PrimaryState(BitOrderList, StateNumber, PrimaryNetwork, Best_Network_List);






#ListBitOrder=[];


#Bit0 = int(Bit.base_conditions[0][0]); 
#Bit1 = int(Bit.base_conditions[0][1]); 
#Bit2 = int(Bit.base_conditions[0][2]); 
#Bit3 = int(Bit.base_conditions[0][3]); 
#Bit4 = int(Bit.base_conditions[0][4]); 
#Bit5 = int(Bit.base_conditions[0][5]); 

#Cascade = ([rf.Network('dsa_almaz_s2p_file/0.5_'+str(Bit0)+'.S2P'),
#                                   rf.Network('dsa_almaz_s2p_file/1_'+str(Bit1)+'.S2P'),
#                                     rf.Network('dsa_almaz_s2p_file/2_'+str(Bit2)+'.S2P'),
#                                      rf.Network('dsa_almaz_s2p_file/4_'+str(Bit3)+'.S2P'),
#                                       rf.Network('dsa_almaz_s2p_file/8_'+str(Bit4)+'.S2P'),
#                                        rf.Network('dsa_almaz_s2p_file/16_'+str(Bit5)+'.S2P')]);

#List_permutations = list(itertools.permutations(Cascade, 6)); ##720 лист этих каскадов  - 1 обьект листа это лист с 6 ячейками он же будет одинаково выдавать если состояние не менял??

#print(List_permutations[0][0].name)

#print(Bit);



#Cascade = ([rf.Network('dsa_almaz_s2p_file/0.5_'+str(Bit0)+'.S2P'),
#                                   rf.Network('dsa_almaz_s2p_file/1_'+str(Bit1)+'.S2P'),
#                                     rf.Network('dsa_almaz_s2p_file/2_'+str(Bit2)+'.S2P'),
#                                      rf.Network('dsa_almaz_s2p_file/4_'+str(Bit3)+'.S2P'),
#                                       rf.Network('dsa_almaz_s2p_file/8_'+str(Bit4)+'.S2P'),
#                                        rf.Network('dsa_almaz_s2p_file/16_'+str(Bit5)+'.S2P')]);



#for k in range(len(List_permutations)):
#    Network = rf.cascade_list(List_permutations[k]);
#    Frequency = Network.f.tolist();

#    State_S11_dB = [];   ### точки в соотвествии с  List_Frequencies
#    State_S12_dB = [];
#    State_S21_dB = [];
#    State_S22_dB = [];

#    State_S11_deg = [];
#    State_S12_deg = [];
#    State_S21_deg = [];
#    State_S22_deg = [];

#    for f in range(len(Frequency)):

#        State_S11_dB.append(float(Network.s11[str(f)+'hz'].s_db[...]));
#        State_S12_dB.append(float(Network.s12[str(f)+'hz'].s_db[...]));
#        State_S21_dB.append(float(Network.s21[str(f)+'hz'].s_db[...]));
#        State_S22_dB.append(float(Network.s22[str(f)+'hz'].s_db[...]));

#        State_S11_deg.append(float(Network.s11[str(f)+'hz'].s_deg[...]))
#        State_S12_deg.append(float(Network.s12[str(f)+'hz'].s_deg[...]))
#        State_S21_deg.append(float(Network.s21[str(f)+'hz'].s_deg[...]))
#        State_S22_deg.append(float(Network.s22[str(f)+'hz'].s_deg[...]))

#print('Ishoooo');
















##Bit0 = int(Bit.base_conditions[0][0]); 
##Bit1 = int(Bit.base_conditions[0][1]); 
##Bit2 = int(Bit.base_conditions[0][2]); 
##Bit3 = int(Bit.base_conditions[0][3]); 
##Bit4 = int(Bit.base_conditions[0][4]); 
##Bit5 = int(Bit.base_conditions[0][5]); 

##print('не торопись....  ')

##Cascade = ([rf.Network('6_bit/de_L2L_att_Xband_0.5dB_cell_InputPower_0dBm_'+str(Bit0)+'.S2P'),
##                                   rf.Network('6_bit/de_L2L_att_Xband_1dB_cell_InputPower_0dBm_'+str(Bit1)+'.S2P'),
##                                     rf.Network('6_bit/de_L2L_att_Xband_2dB_cell_InputPower_0dBm_'+str(Bit2)+'.S2P'),
##                                      rf.Network('6_bit/de_L2L_att_Xband_4dB_cell_InputPower_0dBm_'+str(Bit3)+'.S2P'),
##                                       rf.Network('6_bit/de_L2L_att_Xband_8dB_cell_InputPower_0dBm_'+str(Bit4)+'.S2P'),
##                                        rf.Network('6_bit/de_L2L_att_Xband_16dB_cell_InputPower_0dBm_'+str(Bit5)+'.S2P')  ]);


##List_permutations = list(itertools.permutations(Cascade, 6));

##List_Cascade = [];

##for j in range(len(List_permutations)):
##    List_Cascade.append(rf.cascade_list(List_permutations[j]))
##    print('делаю каскады.... '+str(j))


##State0_S11_dB = [];
##State0_S12_dB = [];
##State0_S21_dB = [];
##State0_S22_dB = [];

##State0_S11_deg = [];
##State0_S12_deg = [];
##State0_S21_deg = [];
##State0_S22_deg = [];


##List_Frequency = [8, 9, 10, 11, 12];

##for i in range(len(List_Cascade)):

##    for f in range(len(List_Frequency)):
##        State0_S11_dB.append(float(List_Cascade[i].s11[str(List_Frequency[f])+'ghz'].s_db[...]));
##        State0_S12_dB.append(float(List_Cascade[i].s12[str(List_Frequency[f])+'ghz'].s_db[...]));
##        State0_S21_dB.append(float(List_Cascade[i].s21[str(List_Frequency[f])+'ghz'].s_db[...]));
##        State0_S22_dB.append(float(List_Cascade[i].s22[str(List_Frequency[f])+'ghz'].s_db[...]));


##print('делаю каскады.... ')










###Order list  720 for each in 64 Primary_List_States
##Total_Sequence_Order_List = [];
##for i in range(0,64,1):
##    print('Да погоди ты.....')
##    Total_Sequence_Order_List.append(list(itertools.permutations(Primary_List_States[i], 6)));

##############Сохраняем листы последовательностей ########################################
#####                                 0
#####                             0<< 720
#####Total_Sequence_Order_List = <    
#####                             63<< 0
#####                                  720


##pickle.dump(Total_Sequence_Order_List, open('Total_Sequence_Order_List.pkl', 'wb'), protocol=pickle.HIGHEST_PROTOCOL);
##############Загружаем все########################################

##Total_Sequence_Order_List =  pickle.load(open('Total_Sequence_Order_List.pkl', 'rb'));


##print(Total_Sequence_Order_List[5])
###print(Total_Sequence_Order_List)
##print('Ishoooo') 
##print(Total_Sequence_Order_List[0][0])

##State0 = rf.cascade_list(Total_Sequence_Order_List[0][0])


#x = np.arange(1,15,1);
#S11 = [];

#for i in np.arange(1,15,1):
#    S11.append(float(State0.s11[str(i)+'ghz'].s_db[...]));


##plt.plot(x,S11);
##plt.show();
#for i in range(len(S11)):
#    print(S11[i]);
#    #print('\n')

##print('Ishoooo') 




















## List интересующих частот
#List_Frequencies = np.arange(8,12.5,0.5).tolist();

#print('sasdasda');






#Bit = ttg.Truths(['Bit0', 'Bit1', 'Bit2', 'Bit3', 'Bit4', 'Bit5'])

#print(Bit);

#Bit0 = int(Bit.base_conditions[63][0]); 
#Bit1 = int(Bit.base_conditions[63][1]); 
#Bit2 = int(Bit.base_conditions[63][2]); 
#Bit3 = int(Bit.base_conditions[63][3]); 
#Bit4 = int(Bit.base_conditions[63][4]); 
#Bit5 = int(Bit.base_conditions[63][5]); 



#Cascade = ([rf.Network('6_bit/de_L2L_att_Xband_0.5dB_cell_InputPower_0dBm_'+str(Bit0)+'.S2P'),
#                                   rf.Network('6_bit/de_L2L_att_Xband_1dB_cell_InputPower_0dBm_'+str(Bit1)+'.S2P'),
#                                     rf.Network('6_bit/de_L2L_att_Xband_2dB_cell_InputPower_0dBm_'+str(Bit2)+'.S2P'),
#                                      rf.Network('6_bit/de_L2L_att_Xband_4dB_cell_InputPower_0dBm_'+str(Bit3)+'.S2P'),
#                                       rf.Network('6_bit/de_L2L_att_Xband_8dB_cell_InputPower_0dBm_'+str(Bit4)+'.S2P'),
#                                        rf.Network('6_bit/de_L2L_att_Xband_16dB_cell_InputPower_0dBm_'+str(Bit5)+'.S2P')  ]);

#List_permutations = list(itertools.permutations(Cascade, 6));

#List_Cascade = [];

#for j in range(len(List_permutations)):
#    List_Cascade.append(rf.cascade_list(List_permutations[j]))
#    print('делаю каскады.... '+str(j))



#Cascade = ([rf.Network('6_bit/de_L2L_att_Xband_0.5dB_cell_InputPower_0dBm_'+str(Bit0)+'.S2P'),
#                                   rf.Network('6_bit/de_L2L_att_Xband_1dB_cell_InputPower_0dBm_'+str(Bit1)+'.S2P'),
#                                     rf.Network('6_bit/de_L2L_att_Xband_2dB_cell_InputPower_0dBm_'+str(Bit2)+'.S2P'),
#                                      rf.Network('6_bit/de_L2L_att_Xband_4dB_cell_InputPower_0dBm_'+str(Bit3)+'.S2P'),
#                                       rf.Network('6_bit/de_L2L_att_Xband_8dB_cell_InputPower_0dBm_'+str(Bit4)+'.S2P'),
#                                        rf.Network('6_bit/de_L2L_att_Xband_16dB_cell_InputPower_0dBm_'+str(Bit5)+'.S2P')]);

 


#Cascade = ([rf.Network('6_bit/de_L2L_att_Xband_0.5dB_cell_InputPower_0dBm_'+str(Bit0)+'.S2P'),
#                                   rf.Network('6_bit/de_L2L_att_Xband_1dB_cell_InputPower_0dBm_'+str(Bit1)+'.S2P'),
#                                     rf.Network('6_bit/de_L2L_att_Xband_2dB_cell_InputPower_0dBm_'+str(Bit2)+'.S2P'),
#                                      rf.Network('6_bit/de_L2L_att_Xband_4dB_cell_InputPower_0dBm_'+str(Bit3)+'.S2P'),
#                                       rf.Network('6_bit/de_L2L_att_Xband_8dB_cell_InputPower_0dBm_'+str(Bit4)+'.S2P'),
#                                        rf.Network('6_bit/de_L2L_att_Xband_16dB_cell_InputPower_0dBm_'+str(Bit5)+'.S2P')]);


    





##Bit0 = int(Bit.base_conditions[i][0]); 
##    Bit1 = int(Bit.base_conditions[i][1]); 
##    Bit2 = int(Bit.base_conditions[i][2]); 
##    Bit3 = int(Bit.base_conditions[i][3]); 
##    Bit4 = int(Bit.base_conditions[i][4]); 
##    Bit5 = int(Bit.base_conditions[i][5]); 
##    print('не торопись....  '+str(i))
##    Cascade = ([rf.Network('6_bit/de_L2L_att_Xband_0.5dB_cell_InputPower_0dBm_'+str(Bit0)+'.S2P'),
##                                   rf.Network('6_bit/de_L2L_att_Xband_1dB_cell_InputPower_0dBm_'+str(Bit1)+'.S2P'),
##                                     rf.Network('6_bit/de_L2L_att_Xband_2dB_cell_InputPower_0dBm_'+str(Bit2)+'.S2P'),
##                                      rf.Network('6_bit/de_L2L_att_Xband_4dB_cell_InputPower_0dBm_'+str(Bit3)+'.S2P'),
##                                       rf.Network('6_bit/de_L2L_att_Xband_8dB_cell_InputPower_0dBm_'+str(Bit4)+'.S2P'),
##                                        rf.Network('6_bit/de_L2L_att_Xband_16dB_cell_InputPower_0dBm_'+str(Bit5)+'.S2P')  ]);
##    List_permutations = list(itertools.permutations(Cascade, 6));



















##################################################################################




################*********Load Cels OFF**************
#Bit_05_ON = rf.Network('6_bit/de_L2L_att_Xband_0.5dB_cell_InputPower_0dBm_ON.S2P');
#Bit_1_ON = rf.Network('6_bit/de_L2L_att_Xband_1dB_cell_InputPower_0dBm_ON.S2P');
#Bit_2_ON = rf.Network('6_bit/de_L2L_att_Xband_2dB_cell_InputPower_0dBm_ON.S2P');
#Bit_4_ON = rf.Network('6_bit/de_L2L_att_Xband_4dB_cell_InputPower_0dBm_ON.S2P');
#Bit_8_ON = rf.Network('6_bit/de_L2L_att_Xband_8dB_cell_InputPower_0dBm_ON.S2P');
#Bit_16_ON = rf.Network('6_bit/de_L2L_att_Xband_16dB_cell_InputPower_0dBm_ON.S2P');
################*********Load Cels ON****************

################*********Load Cels OFF**************
#Bit_05_OFF = rf.Network('6_bit/de_L2L_att_Xband_0.5dB_cell_InputPower_0dBm_OFF.S2P');
#Bit_1_OFF = rf.Network('6_bit/de_L2L_att_Xband_1dB_cell_InputPower_0dBm_OFF.S2P');
#Bit_2_OFF = rf.Network('6_bit/de_L2L_att_Xband_2dB_cell_InputPower_0dBm_OFF.S2P');
#Bit_4_OFF = rf.Network('6_bit/de_L2L_att_Xband_4dB_cell_InputPower_0dBm_OFF.S2P');
#Bit_8_OFF= rf.Network('6_bit/de_L2L_att_Xband_8dB_cell_InputPower_0dBm_OFF.S2P');
#Bit_16_OFF = rf.Network('6_bit/de_L2L_att_Xband_16dB_cell_InputPower_0dBm_OFF.S2P');
################*********Load Cels ON****************

#################Off Sequence
#OFF_Sequence = [Bit_05_OFF, Bit_1_OFF, Bit_2_OFF, Bit_4_OFF, Bit_8_OFF, Bit_16_OFF]
#Available_OFF_Sequence_List = list(itertools.permutations(OFF_Sequence, 6));
#for i in range(len(Available_OFF_Sequence_List)):
#    for j in range(len(OFF_Sequence)):
#        print(Available_OFF_Sequence_List[i][j].name);
#    print('******************************** '+str(i+1))
##print('sho');

#vIn = True;
#vOut = int(vIn);

#print(vOut);

