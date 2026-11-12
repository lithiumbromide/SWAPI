---
title: "IMacroFeatureData Interface"
project: ""
interface: "IMacroFeatureData"
member: ""
kind: "interface"
source: "sldworksapiprogguide/Macro_Features/MacroFeatureData_Interface.htm"
---

# IMacroFeatureData Interface

The [IMacroFeatureData](sldworksAPI.chm::/SolidWorks.interop.sldworks~SolidWorks.interop.sldworks.IMacroFeatureData.html) allows access to the data that defines a macro feature. The IMacroFeature interface supports:

- Typical feature data methods such as [IMacroFeatureData::AccessSelections](sldworksAPI.chm::/SolidWorks.interop.sldworks~SolidWorks.interop.sldworks.IMacroFeatureData~AccessSelections.html) or [IMacroFeatureData::IAccessSelections](sldworksAPI.chm::/SolidWorks.interop.sldworks~SolidWorks.interop.sldworks.IMacroFeatureData~IAccessSelections.html) and [IMacroFeatureData::ReleaseSelectionAccess](sldworksAPI.chm::/SolidWorks.interop.sldworks~SolidWorks.interop.sldworks.IMacroFeatureData~ReleaseSelectionAccess.html)
- An input body, which you can get or set using [IMacroFeatureData::EditBodies](sldworksAPI.chm::/SolidWorks.interop.sldworks~SolidWorks.interop.sldworks.IMacroFeatureData~EditBodies.html) or [IMacroFeatureData::IGetEditBodies](sldworksAPI.chm::/SolidWorks.interop.sldworks~SolidWorks.interop.sldworks.IMacroFeatureData~IGetEditBodies.html)
- Methods for feature parameters. For example:
