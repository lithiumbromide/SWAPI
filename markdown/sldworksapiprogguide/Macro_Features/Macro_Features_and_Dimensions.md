---
title: "Macro Features and Dimensions"
project: ""
interface: ""
member: ""
kind: "topic"
source: "sldworksapiprogguide/Macro_Features/Macro_Features_and_Dimensions.htm"
---

# Macro Features and Dimensions

The following sample code shows how you might create a dimension for a macro feature.

1. In C++, create containers for the dimension types and values before inserting the macro feature:

```vb
 //Create dimension containers
 long dimType[MBossDimNum] =
 {
         swLinearDimension,
         swLinearDimension,
         swLinearDimension,
         swLinearDimension,
         swLinearDimension,
         swLinearDimension,
         swLinearDimension,
         swAngularDimension,
         swAngularDimension,
         swAngularDimension
 };
double dimValue[MBossDimNum] =
{
        pData->m_BaseRadius*2,
        pData->m_BaseHeight,
        pData->m_FinHeight,
        pData->m_FinLength,
        pData->m_FinWidth,
        pData->m_InsideRadius*2,
        pData->m_InsideHeight,
        pData->m_BaseDraft,
        pData->m_FinDraft,
        pData->m_InsideDraft
};
```

1. Insert the macro feature.

```vb
pFeatMan->IInsertMacroFeature2(_bstr_t(baseName),
        _bstr_t("SldFuncFeat.MBossFeature"),
        macroMethods, MBossParamNum, MBossParamName,
        MBossParamType, paramVal, MBossDimNum, dimType, dimValue, pEditBody,3,
        icons, swMacroFeatureIsPatternable, &pFeat);
```

1. Set the lines for the dimensions in your rebuild function:

```vb
dim->put_DimensionLineDirection(transformedVectLineDir);
dim->put_ExtensionLineDirection(transformedVectExtDir);
dim->ISetReferencePoints(2, refPoints);
```

NOTE: When regenerating a macro feature, [IDimension::ReferencePoints](sldworksAPI.chm::/SolidWorks.interop.sldworks~SolidWorks.interop.sldworks.IDimension~ReferencePoints.html) gets and sets the reference points of a display dimension ([IDisplayDimension](sldworksAPI.chm::/SolidWorks.interop.sldworks~SolidWorks.interop.sldworks.IDisplayDimension.html) object). In all other cases, this property gets and sets the reference points of a dimension ([IDimension](sldworksAPI.chm::/SolidWorks.interop.sldworks~SolidWorks.interop.sldworks.IDimension.html) object).
