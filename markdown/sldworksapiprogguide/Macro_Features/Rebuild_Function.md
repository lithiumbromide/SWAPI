---
title: "Rebuild Function"
project: ""
interface: ""
member: ""
kind: "topic"
source: "sldworksapiprogguide/Macro_Features/Rebuild_Function.htm"
---

# Rebuild Function

The rebuild function for a macro feature performs the real work. No new features can be introduced and no user interaction can occur during a rebuild of a model containing a macro feature.

There are three types of rebuild functions:

| Type | Definition | Actions |
| --- | --- | --- |
| Independent | Interacts with the model, but does not modify existing geometry or create new geometry | Obtains the IMacroFeatureData object from the input IFeature object Obtains the selections and parameters from the IMacroFeatureData object Processes the inputs according to the design of the feature Validates data based on the model Updates external databases Return values can be: True, which indicates success False, which indicates failure with no additional information String, which is displayed in an error message to the user; for example: VBA s wmRebuild = "Macro feature output error message" C++ COM CComBSTR bMsg = _T("Macro feature output error message"); _variant_t vBSTRRet = bMsg; *retval = vBSTRRet; C# functionReturnValue = "Macro feature output error message"; return functionReturnValue; VB.NET Regenerate = "Macro feature output error message" |
| Modify | Modifies one or more input bodies | Obtains the IMacroFeatureData from the input feature Obtains the bodies to modify from IMacroFeatureData::EditBodies or IMacroFeatureData::IGetEditBodies Obtains the selections and parameters from the IMacroFeatureData object Processes the inputs according to the design of the feature Copies any selected object for use with the input body Creates any new geometry based on the input data Modifies the input bodies Calls IMacroFeatureData::GetEntitiesNeedUserId on the input body Gets any faces or edges that need IDs Places IDs using IMacroFeatureData::SetFaceUserId and IMacroFeatureData::SetEdgeUserId , respectively NOTE : The numbering scheme should be consistent and reproducible. Return values can be: True, which indicates success False, which indicates failure and no additional information is provided String, which is displayed in an error message to the user; for example: VBA swmRebuild = "Macro feature output error message" C++ COM CComBSTR bMsg = _T("Macro feature output error message"); _variant_t vBSTRRet = bMsg; *retval = vBSTRRet; C# functionReturnValue = "Macro feature output error message"; return functionReturnValue; VB.NET Regenerate = "Macro feature output error message" NOTE: A macro feature rebuild function can output more than one body, in a VARIANT SafeArray containing multiple IBody2 objects, by either modifying one or more edit bodies or by creating one or more new bodies. For multibody macro features only, call IMacroFeatureData::EnableMultiBodyConsume from within the rebuild function to specify whether the original edit body is appended (default) or replaced with multiple bodies in the FeatureManager design tree's Solid Bodies folder. |
| Create | Creates one or more output bodies | Obtains the IMacroFeatureData object from the input Feature object Obtains the selections and parameters from the IMacroFeatureData object Processes the inputs according to the design of the feature Copies any new selected object Creates any new geometry based on the input data Creates the new bodies Calls IMacroFeatureData::GetEntitiesNeedUserId on the new body Gets any faces or edges that need IDs Places IDs using IMacroFeatureData::SetFaceUserId and IMacroFeatureData::SetEdgeUserId , respectively NOTE : The numbering scheme should be consistent and reproducible. Return values can be: IBody2 , the newly created body, or a VARIANT SafeArray containign multiple IBody2 objects False, which indicates failure and provides no additional information String, which is displayed in an error message to the user; for example: VBA swmRebuild = "Macro feature output error message" C++ COM CComBSTR bMsg = _T("Macro feature output error message"); _variant_t vBSTRRet = bMsg; *retval = vBSTRRet; C# functionReturnValue = "Macro feature output error message"; return functionReturnValue; VB.NET Regenerate = "Macro feature output error message" NOTE: A macro feature rebuild function can output more than one body, in a VARIANT SafeArray containing multiple IBody2 objects, by either modifying one or more edit bodies or by creating one or more new bodies. For multibody macro features only, call IMacroFeatureData::EnableMultiBodyConsume from within the rebuild function to specify whether the original edit body is appended (default) or replaced with multiple bodies in the FeatureManager design tree's Solid Bodies folder. |

The rebuild function is called by SOLIDWORKS whenever the macro feature is regenerated. The parametric information needed to regenerate the feature should be stored in the feature’s parameter and selection lists. These lists are created when the feature is inserted into the model and are available for reading and editing from the feature’s IMacroFeatureData interface. For example, the data stored in the parameters and selection lists can be used to perform low-level Boolean body operations to affect geometric features.

Because IBody2 objects created using the API do not always automatically assign IDs to their faces and edges, you should always check that there are no entity IDs that need to be assigned. Otherwise, any Boolean body operations involving that Body2 object will cause regeneration to fail. Use IMacroFeatureData::GetEntitiesNeedUserId to check for the IDs. If the faces and edges arrays returned are both empty, then no user IDs are required. Otherwise, use IMacroFeatureData::SetFaceUserId and IMacroFeatureData::SetEdgeUserId to set the IDs of those entities.

The macro feature’s rebuild function is responsible for ensuring that the same IDs are always placed on the same entities each time the regeneration function is called. The order in which the entities are returned cannot be used. Instead, there should be some algorithm used that relies on the geometry of the body to determine entity IDs. Of course, features with no impact on the geometry of the model can also be created.

The following example illustrates a VBA-based rebuild function. When called, it returns true to indicate to SOLIDWORKS that it was successful.

```vb
Function swmRegen(app As Variant, part As Variant, feature As Variant) As Variant
msgbox "Regeneration function called."
.
.
.
swmRegen = True
End Function
```

NOTES:

- When regenerating a macro feature, [IDimension::ReferencePoints](sldworksAPI.chm::/SolidWorks.interop.sldworks~SolidWorks.interop.sldworks.IDimension~ReferencePoints.html) gets and sets the reference points of a display dimension ([IDisplayDimension](sldworksAPI.chm::/SolidWorks.interop.sldworks~SolidWorks.interop.sldworks.IDisplayDimension.html) object). In all other cases, this property gets and sets the reference points of a dimension ([IDimension](sldworksAPI.chm::/SolidWorks.interop.sldworks~SolidWorks.interop.sldworks.IDimension.html) object).
-

  ```
  If your macro feature is crashing while regenerating, then force garbage collection and wait for all finalizers to complete before continuing. For example, include the following code at the end of your rebuild function in a VB.NET application:
  ```

  ‘Wait for all finalizers to complete before continuing

  GC.Collect()
  GC.WaitforPendingFinalizers()
  GC.Collect()
  GC.WaitforPendingFinalizers()
