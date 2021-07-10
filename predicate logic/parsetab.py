
# parsetab.py
# This file is automatically generated. Do not edit.
# pylint: disable=W,C,R
_tabversion = '3.10'

_lr_method = 'LALR'

_lr_signature = 'A AND DOT EQUALS EVERY ID IS NO NOT OF OR S SINGLEQUOTE SOME THAT THE adjID ivID roleID tvIDspec : sentence0\n            | sentence0 specsentence0 : EQUALSsentence0 : sentence DOTsentence : NP VPsentence : sentence OR sentenceNP\t: ID NP : DET CNNP : DET RCNNP : DET roleCNofDET : SOMEDET : ADET : THEDET : EVERYDET : NONP : ID SINGLEQUOTE S roleIDVP : VP AND VPVP : ivIDVP : IS NPVP : IS NOT NPVP : IS adjIDVP : IS NOT adjIDVP : TV NPTV : tvIDRCN : CN THAT VPRCN : CN THAT NP TVroleCNof : roleID OF NPCN : IDCN : adjID CN'
    
_lr_action_items = {'EQUALS':([0,2,3,14,],[3,3,-3,-4,]),'ID':([0,2,3,7,8,9,10,11,12,14,15,18,19,20,26,31,35,37,],[6,6,-3,25,-11,-12,-13,-14,-15,-4,6,6,6,-24,25,6,6,6,]),'SOME':([0,2,3,14,15,18,19,20,31,35,37,],[8,8,-3,-4,8,8,8,-24,8,8,8,]),'A':([0,2,3,14,15,18,19,20,31,35,37,],[9,9,-3,-4,9,9,9,-24,9,9,9,]),'THE':([0,2,3,14,15,18,19,20,31,35,37,],[10,10,-3,-4,10,10,10,-24,10,10,10,]),'EVERY':([0,2,3,14,15,18,19,20,31,35,37,],[11,11,-3,-4,11,11,11,-24,11,11,11,]),'NO':([0,2,3,14,15,18,19,20,31,35,37,],[12,12,-3,-4,12,12,12,-24,12,12,12,]),'$end':([1,2,3,13,14,],[0,-1,-3,-2,-4,]),'DOT':([4,6,16,17,20,22,23,24,25,28,30,32,33,36,38,39,40,41,42,44,45,],[14,-7,-5,-18,-24,-8,-9,-10,-28,-6,-19,-21,-23,-29,-17,-20,-22,-16,-25,-27,-26,]),'OR':([4,6,16,17,20,22,23,24,25,28,30,32,33,36,38,39,40,41,42,44,45,],[15,-7,-5,-18,-24,-8,-9,-10,-28,15,-19,-21,-23,-29,-17,-20,-22,-16,-25,-27,-26,]),'ivID':([5,6,17,20,22,23,24,25,29,30,32,33,35,36,38,39,40,41,42,44,45,],[17,-7,-18,-24,-8,-9,-10,-28,17,-19,-21,-23,17,-29,-17,-20,-22,-16,-25,-27,-26,]),'IS':([5,6,17,20,22,23,24,25,29,30,32,33,35,36,38,39,40,41,42,44,45,],[18,-7,-18,-24,-8,-9,-10,-28,18,-19,-21,-23,18,-29,-17,-20,-22,-16,-25,-27,-26,]),'tvID':([5,6,17,20,22,23,24,25,29,30,32,33,35,36,38,39,40,41,42,43,44,45,],[20,-7,-18,-24,-8,-9,-10,-28,20,-19,-21,-23,20,-29,-17,-20,-22,-16,-25,20,-27,-26,]),'AND':([6,16,17,20,22,23,24,25,30,32,33,36,38,39,40,41,42,44,45,],[-7,29,-18,-24,-8,-9,-10,-28,-19,-21,-23,-29,29,-20,-22,-16,29,-27,-26,]),'SINGLEQUOTE':([6,],[21,]),'adjID':([7,8,9,10,11,12,18,26,31,],[26,-11,-12,-13,-14,-15,32,26,40,]),'roleID':([7,8,9,10,11,12,34,],[27,-11,-12,-13,-14,-15,41,]),'NOT':([18,],[31,]),'S':([21,],[34,]),'THAT':([22,25,36,],[35,-28,-29,]),'OF':([27,],[37,]),}

_lr_action = {}
for _k, _v in _lr_action_items.items():
   for _x,_y in zip(_v[0],_v[1]):
      if not _x in _lr_action:  _lr_action[_x] = {}
      _lr_action[_x][_k] = _y
del _lr_action_items

_lr_goto_items = {'spec':([0,2,],[1,13,]),'sentence0':([0,2,],[2,2,]),'sentence':([0,2,15,],[4,4,28,]),'NP':([0,2,15,18,19,31,35,37,],[5,5,5,30,33,39,43,44,]),'DET':([0,2,15,18,19,31,35,37,],[7,7,7,7,7,7,7,7,]),'VP':([5,29,35,],[16,38,42,]),'TV':([5,29,35,43,],[19,19,19,45,]),'CN':([7,26,],[22,36,]),'RCN':([7,],[23,]),'roleCNof':([7,],[24,]),}

_lr_goto = {}
for _k, _v in _lr_goto_items.items():
   for _x, _y in zip(_v[0], _v[1]):
       if not _x in _lr_goto: _lr_goto[_x] = {}
       _lr_goto[_x][_k] = _y
del _lr_goto_items
_lr_productions = [
  ("S' -> spec","S'",1,None,None,None),
  ('spec -> sentence0','spec',1,'p_spec','translate.py',136),
  ('spec -> sentence0 spec','spec',2,'p_spec','translate.py',137),
  ('sentence0 -> EQUALS','sentence0',1,'p_sentence_separator','translate.py',142),
  ('sentence0 -> sentence DOT','sentence0',2,'p_sentence_top','translate.py',149),
  ('sentence -> NP VP','sentence',2,'p_sentence','translate.py',158),
  ('sentence -> sentence OR sentence','sentence',3,'p_sentence_or','translate.py',166),
  ('NP -> ID','NP',1,'p_NP_ID','translate.py',171),
  ('NP -> DET CN','NP',2,'p_NP_DET_CN','translate.py',177),
  ('NP -> DET RCN','NP',2,'p_NP_DET_RCN','translate.py',182),
  ('NP -> DET roleCNof','NP',2,'p_NP_DET_roleCNof','translate.py',187),
  ('DET -> SOME','DET',1,'p_DET_some','translate.py',192),
  ('DET -> A','DET',1,'p_DET_a','translate.py',198),
  ('DET -> THE','DET',1,'p_DET_the','translate.py',204),
  ('DET -> EVERY','DET',1,'p_DET_every','translate.py',210),
  ('DET -> NO','DET',1,'p_DET_no','translate.py',216),
  ('NP -> ID SINGLEQUOTE S roleID','NP',4,'p_roleCNofWITHs','translate.py',222),
  ('VP -> VP AND VP','VP',3,'p_VP_and','translate.py',233),
  ('VP -> ivID','VP',1,'p_VP_ivID','translate.py',242),
  ('VP -> IS NP','VP',2,'p_VP_issame','translate.py',248),
  ('VP -> IS NOT NP','VP',3,'p_VP_isnotsame','translate.py',254),
  ('VP -> IS adjID','VP',2,'p_VP_isADJ','translate.py',260),
  ('VP -> IS NOT adjID','VP',3,'p_VP_isADJnot','translate.py',266),
  ('VP -> TV NP','VP',2,'p_VP_TV_NP','translate.py',272),
  ('TV -> tvID','TV',1,'p_TV_tvID','translate.py',279),
  ('RCN -> CN THAT VP','RCN',3,'p_RCN_CN_that_VP','translate.py',285),
  ('RCN -> CN THAT NP TV','RCN',4,'p_RCN_CN_that_NP_TV','translate.py',292),
  ('roleCNof -> roleID OF NP','roleCNof',3,'p_roleCNof','translate.py',300),
  ('CN -> ID','CN',1,'p_CN_ID','translate.py',307),
  ('CN -> adjID CN','CN',2,'p_CN_ADJ_CN','translate.py',316),
]
