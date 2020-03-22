# -*- coding: UTF-8 -*-
# Code automatically generated by pycrate_asn1c

from pycrate_asn1rt.utils            import *
from pycrate_asn1rt.err              import *
from pycrate_asn1rt.glob             import make_GLOBAL, GLOBAL
from pycrate_asn1rt.dictobj          import ASN1Dict
from pycrate_asn1rt.refobj           import *
from pycrate_asn1rt.setobj           import *
from pycrate_asn1rt.asnobj_basic     import *
from pycrate_asn1rt.asnobj_str       import *
from pycrate_asn1rt.asnobj_construct import *
from pycrate_asn1rt.asnobj_class     import *
from pycrate_asn1rt.asnobj_ext       import *
from pycrate_asn1rt.init             import init_modules

class ModuleTestConstraint1:

    _name_  = 'ModuleTestConstraint1'
    _oid_   = [1, 3, 6, 1, 4, 1, 9363, 1, 5, 1, 16, 1]
    
    _obj_ = [
        'Type0',
        'Type6',
        ]
    _type_ = [
        'Type0',
        'Type6',
        ]
    _set_ = [
        ]
    _val_ = [
        ]
    _class_ = [
        ]
    _param_ = [
        ]
    
    #-----< Type0 >-----#
    Type0 = STR_IA5(name='Type0', mode=MODE_TYPE)
    Type0._const_val = ASN1Set(rv=[], rr=[], ev=None, er=[])
    
    #-----< Type6 >-----#
    Type6 = STR_IA5(name='Type6', mode=MODE_TYPE)
    Type6._const_val = ASN1Set(rv=[], rr=[], ev=None, er=[])
    
    _all_ = [
        Type0,
        Type6,
    ]

class ModuleTestConstraint2:

    _name_  = 'ModuleTestConstraint2'
    _oid_   = [1, 3, 6, 1, 4, 1, 9363, 1, 5, 1, 16, 2]
    
    _obj_ = [
        'Type1',
        'Type2',
        'Type3',
        'Type4',
        'Type5',
        'ten',
        'v1',
        ]
    _type_ = [
        'Type1',
        'Type2',
        'Type3',
        'Type4',
        'Type5',
        ]
    _set_ = [
        ]
    _val_ = [
        'ten',
        'v1',
        ]
    _class_ = [
        ]
    _param_ = [
        ]
    
    #-----< Type1 >-----#
    Type1 = STR_IA5(name='Type1', mode=MODE_TYPE)
    Type1._const_sz = ASN1Set(rv=[], rr=[ASN1RangeInt(lb=1, ub=10)], ev=[], er=[])
    Type1._const_alpha = ASN1Set(rv=['#'], rr=[ASN1RangeStr(lb='a', ub='z')], ev=[], er=[])
    
    #-----< Type2 >-----#
    Type2 = STR_IA5(name='Type2', mode=MODE_TYPE)
    Type2._const_sz = ASN1Set(rv=[], rr=[ASN1RangeInt(lb=0, ub=4)], ev=None, er=[])
    
    #-----< Type3 >-----#
    Type3 = STR_BMP(name='Type3', mode=MODE_TYPE)
    Type3._const_sz = ASN1Set(rv=[1], rr=[], ev=None, er=[])
    
    #-----< Type4 >-----#
    Type4 = INT(name='Type4', mode=MODE_TYPE)
    Type4._const_val = ASN1Set(rv=[], rr=[ASN1RangeInt(lb=1, ub=None)], ev=None, er=[])
    
    #-----< Type5 >-----#
    Type5 = BOOL(name='Type5', mode=MODE_TYPE)
    Type5._const_val = ASN1Set(rv=[True, False], rr=[], ev=None, er=[])
    
    #-----< ten >-----#
    ten = INT(name='ten', mode=MODE_VALUE)
    ten._val = 10
    
    #-----< v1 >-----#
    v1 = STR_IA5(name='v1', mode=MODE_VALUE, typeref=ASN1RefType(('ModuleTestConstraint2', 'Type1')))
    v1._const_alpha = ASN1Set(rv=['#'], rr=[ASN1RangeStr(lb='a', ub='z')], ev=[], er=[])
    v1._val = '#value wi th ""double quotes""'
    
    _all_ = [
        Type1,
        Type2,
        Type3,
        Type4,
        Type5,
        ten,
        v1,
    ]

init_modules(ModuleTestConstraint1, ModuleTestConstraint2)