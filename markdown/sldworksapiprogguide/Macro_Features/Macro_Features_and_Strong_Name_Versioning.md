---
title: "Macro Features and Strong Name Versioning"
project: ""
interface: ""
member: ""
kind: "topic"
source: "sldworksapiprogguide/Macro_Features/Macro_Features_and_Strong_Name_Versioning.htm"
---

# Macro Features and Strong Name Versioning

If you run different major versions of SOLIDWORKS (e.g., SOLIDWORKS 2008 and SOLIDWORKS 2009) on the same system, then you should strongly name macro features that are COM features (i.e., implemented within a DLL file) and their servers beginning with SOLIDWORKS 2009. Otherwise, SOLIDWORKS cannot distinguish between macro features created in different major versions of SOLIDWORKS and may invoke the wrong macro feature if you run a different major version of SOLIDWORKS than the version just run.

Strongly naming macro features ensures that the macro features are unaffected when installing or uninstalling different major versions of SOLIDWORKS. SOLIDWORKS has implemented strong naming to be compatible with your applications that use macro features.

Strong name versioning of a macro feature allows your application to choose to use either the version of the macro feature server used to create the feature or to use the version of the running SOLIDWORKS, if different.

To implement strong name versioning, you must perform the following steps at each SOLIDWORKS major version release beginning with SOLIDWORKS 2009:

1. Increment the version number of the type library in the macro feature server’s IDL file; for example:

```vb
...
[
      uuid(A0BFC86A-8107-4ACD-886E-398DC76BBC80),
      version(17.0),
      helpstring("sldFuncFeat 17.0 Type Library")
]
library SLDFUNCFEATLib
...
```

1. Increment the version number of the macro feature server’s type library in your macro feature server’s .h file; for example:

```vb
public IDispatchImpl<IFuncFeatApp, &IID_IFuncFeatApp, &LIBID_SLDFUNCFEATLib, 17, 0>
```

1. Replace the CLSID with a new UUID and increment the version number of ProgID in all macro feature and macro feature server files, including the macro feature’s .rgs file.

1. Increment ProgID in [IFeatureManager::IInsertMacroFeature3](sldworksAPI.chm::/SolidWorks.interop.sldworks~SolidWorks.interop.sldworks.IFeatureManager~IInsertMacroFeature3.html) in the macro feature’s .cpp file; for example:

```vb
FeatMan->IInsertMacroFeature3(_bstr_t(baseName),
```

```vb
_bstr_t("SldFuncFeat.LipGrooveFeature.17"),
macroMethods, LipGrooveParamNum, LipGrooveParamName,
LipGrooveParamType, paramVal, LipGrooveDimNum, dimType,
dimValue, bodyCount, pEditBodies, 3, icons,
swMacroFeatureIsPatternable | swMacroFeatureNoCachedBody,
&pFeat);
```

1. Register the version of the macro feature to use with SOLIDWORKS by including a line of code similar to the following in your macro feature’s .rgs file:

```vb
CurVer = s ‘SldFuncFeat.LipGrooveFeature.17’ //Substitute your macro feature name and version
```

which creates the following registry key:

```vb
HCLM/SOFTWARE/SOLIDWORKS/SOLIDWORKS 2009/MacroFeatures/SldFuncFeat.LipGrooveFeature/CurVer=SldFuncFeat.LipGrooveFeature.17
```
