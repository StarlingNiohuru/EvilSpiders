import re

def get_DMMbango(s,wanz=False,avop=False):
    b=str(bango(s))
    dic={'hodv':'41','mdb':'84','mxgs':'h_068','sma':'83','mds':'61','t28':'55',
         'star':'1','(?<![a-z])dv(?![a-z])':'53','sama':'h_244','mild':'84',
         '(?<![a-z])xv(?![a-z])':'60','tmem':'h_452','sdmt':'1','dvaj':'53',
         'natr':'h_067','nass':'h_067','onez':'118','(?<![a-z])id(?![a-z])':'55',
         'gxaz':'29','djsk':'29','dje':'2','ekdv':'49','ovg':'13','bgn':'118',
         'dkyh':'30','sdde':'1','ysch':'24','abp':'118','xvsr':'60','aka':'118',
         'vgq':'13','iene':'1','dfda':'434','gvg':'13','urps':'h_593','send':'15',
         'bazx':'84','hxak':'29','rct':'1','gkd':'24','bokd':'84','zizg':'h_826',
         'xrw':'84','djsg':'29','vdd':'24','mxbd':'h_068','bdsr':'57','dly':'118',
         'dmbj':'30','mkmp':'84','real':'84','apol':'h_838','sdsi':'1','sero':'h_422',
         'flav':'434','abs':'118','auks':'23','bndv':'58','crc':'h_093','dvdes':'1',
         'gon':'12','inf':'118','gg':'13','jak':'33','okad':'84','ols':'118',
         'prp':'118','sb':'h_113','tmdi':'h_452','tmhp':'h_452','upsm':'h_150',
         'vspds':'42','iesp':'1','axbc':'29','svdvd':'1','sflbk':'n_662'}
    if wanz==True:
        dic['wanz']='3'
    if avop==True:
        dic['avop']='118'
    for i in dic.keys():
        p=re.compile(i)
        r=p.findall(b)
        if len(r)==0:
            continue
        else:
            return dic[i]+b
    return b
