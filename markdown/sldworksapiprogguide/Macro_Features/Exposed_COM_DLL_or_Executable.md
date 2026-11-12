---
title: "Exposed COM DLL or Executable and Macro Features"
project: ""
interface: ""
member: ""
kind: "topic"
source: "sldworksapiprogguide/Macro_Features/Exposed_COM_DLL_or_Executable.htm"
---

# Exposed COM DLL or Executable and Macro Features

For macro features that define their behavior using COM, a COM server needs to implement the [ISwComFeature](swpublishedAPI.chm::/SolidWorks.interop.swpublished~SolidWorks.interop.swpublished.ISwComFeature.html) interface. This interface has three methods that must be implemented in the appropriate [macro feature function](Overview_of_Macro_Features.htm):

- [ISwComFeature::Edit](swpublishedAPI.chm::/SolidWorks.interop.swpublished~SolidWorks.interop.swpublished.ISwComFeature~Edit.html) in the edit definition function
- [ISwComFeature::Regenerate](swpublishedAPI.chm::/SolidWorks.interop.swpublished~SolidWorks.interop.swpublished.ISwComFeature~Regenerate.html) in the rebuild function
- [ISwComFeature::Security](swpublishedAPI.chm::/SolidWorks.interop.swpublished~SolidWorks.interop.swpublished.ISwComFeature~Security.html) in the security function

To associate the COM server with the macro feature, supply the program ID of the COM server as an argument to [IFeatureManager::InsertMacroFeature3](sldworksAPI.chm::/SolidWorks.interop.sldworks~SolidWorks.interop.sldworks.IFeatureManager~InsertMacroFeature3.html) or [IFeatureManager::IInsertMacroFeature3](sldworksAPI.chm::/SolidWorks.interop.sldworks~SolidWorks.interop.sldworks.IFeatureManager~IInsertMacroFeature3.html).
