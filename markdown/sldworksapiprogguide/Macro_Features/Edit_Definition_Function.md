---
title: "Edit Definition Function"
project: ""
interface: ""
member: ""
kind: "topic"
source: "sldworksapiprogguide/Macro_Features/Edit_Definition_Function.htm"
---

# Edit Definition Function

The edit definition function for a macro feature:

- Obtains the [IMacroFeatureData](sldworksAPI.chm::/SolidWorks.interop.sldworks~SolidWorks.interop.sldworks.IMacroFeatureData.html) object from the input [IFeature](sldworksAPI.chm::/SolidWorks.interop.sldworks~SolidWorks.interop.sldworks.IFeature.html) object
- Obtains the selections and parameters from the IMacroFeatureData object
- Calls [IMacroFeatureData::AccessSelections](sldworksAPI.chm::/SolidWorks.interop.sldworks~SolidWorks.interop.sldworks.IMacroFeatureData~AccessSelections.html) or [IMacroFeatureData::IAccessSelections to put SOLIDWORKS in a rollback state](sldworksAPI.chm::/SolidWorks.interop.sldworks~SolidWorks.interop.sldworks.IMacroFeatureData~IAccessSelections.html)
- Provides a user interface, which:

  - allows the user to change the selections.
  - allows the user to modify the input data.
  - modifies features; possibly allows the user to change the input body.
  - creates features; ensures that IMacroFeatureData::EditBodies or IMacroFeatureData::IGetEditBodies is Nothing.
- Sets all of the selections and parameters back into the IMacroFeatureData object
- Calls [IFeature::ModifyDefinition](sldworksAPI.chm::/SolidWorks.interop.sldworks~SolidWorks.interop.sldworks.IFeature~ModifyDefinition.html) or [IFeature::IModifyDefinition2](sldworksAPI.chm::/SolidWorks.interop.sldworks~SolidWorks.interop.sldworks.IFeature~IModifyDefinition2.html) on the input feature, which flags the feature as dirty and needing a rebuild

The edit definition function is called by SOLIDWORKS whenever the user edits the definition of a macro feature. This function should handle all user-interface activity needed for acquiring and editing selections and parametric data for the macro feature. The [IPropertyManagerPage2](sldworksAPI.chm::/SolidWorks.interop.sldworks~SolidWorks.interop.sldworks.IPropertyManagerPage2.html) interface is well suited for handling the user interaction, but it is not required. Other user interface options are VBA UserForm or an external application.

The data should be stored using the macro feature’s IMacroFeatureData interface. User inputs should be validated and body operations checked before calling [IFeature::ModifyDefinition](sldworksAPI.chm::/SolidWorks.interop.sldworks~SolidWorks.interop.sldworks.IFeature~ModifyDefinition.html) or [IFeature::IModifyDefinition2](sldworksAPI.chm::/SolidWorks.interop.sldworks~SolidWorks.interop.sldworks.IFeature~IModifyDefinition2.html), which causes the macro feature [rebuild function](Rebuild_Function.htm) to be called.

The following example illustrates an VBA-based edit definition function.

```vb
Function swmEdit(app As Variant, part As Variant, feature As Variant) As Variant
msgbox "Edit definition function called."
.
.
.
swmEdit= True
End Function
```
