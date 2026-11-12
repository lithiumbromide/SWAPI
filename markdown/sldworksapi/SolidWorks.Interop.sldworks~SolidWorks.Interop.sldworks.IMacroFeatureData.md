---
title: "IMacroFeatureData Interface"
project: "SOLIDWORKS API Help"
interface: "IMacroFeatureData"
member: ""
kind: "interface"
source: "sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IMacroFeatureData.html"
---

# IMacroFeatureData Interface

Allows access to the data that defines a macro feature.

**NOTE:** Click the **Members** link, located near the top of the topic, to see this interface's methods and properties.

## Syntax

### Visual Basic (Declaration)

```vb
Public Interface IMacroFeatureData
```

### Visual Basic (Usage)

```vb
Dim instance As IMacroFeatureData
```

### C#

```csharp
public interface IMacroFeatureData
```

### C++/CLI

```cpp
public interface class IMacroFeatureData
```

## VBA Syntax

See [MacroFeatureData](ms-its:sldworksapivb6.chm::/sldworks~MacroFeatureData.html).

## Examples

[Create Macro Feature Subfeature (VBA)](Create_Macro_Feature_Subfeature_Example_VB.htm)
[Cut Body in Half Using Macro Feature (VBA)](Cut_Body_in_Half_using_Macro_Feature_Example_VB.htm)
[Assign Tracking ID Using Macro Feature (VBA)](Assign_Tracking_ID_Using_Macro_Feature_VB.htm)

## Remarks

| Macro features can... | For the rebuild function only, the macro associated with a macro feature cannot: |
| --- | --- |
| be inserted into a part, assembly, or drawing document create multiple bodies edit multiple existing bodies | insert a feature from a macro feature in the same model edit definitions of other features if these features are in the same model as the macro feature rebuild, roll back, or roll forward the FeatureManager design tree NOTE: These limitations are intended to prevent nested-feature regeneration in the model that contains the macro feature. |

When the feature is creating multiple bodies, then the return value from the rebuild function should contain the array of bodies that are the result of the operation. [IMacroFeatureData::EditBodies](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.IMacroFeatureData~EditBodies.html) is not expected to contain a body when the rebuild function returns to SOLIDWORKS.

When the feature is modifying a body and the result is multiple bodies, then IMacroFeatureData::EditBodies should contain all of the resulting bodies.

Whether creating multiple bodies or modifying a body that results in multiple bodies, call [IMacroFeatureData::EnableMultiBodyConsume](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.IMacroFeatureData~EnableMultiBodyConsume.html) from the [rebuild](sldworksapiprogguide.chm::/Macro_Features/Rebuild_Function.htm) function to specify whether multiple bodies replace or append the original edit body in the FeatureManager design tree Solid Bodies folder.

If your application allows the user to decide which bodies to keep, your application must determine what it means to select the bodies and subsequently store the selected bodies with the feature.

To edit a macro feature in a drawing, do not use [IMacroFeatureData::AccessSelections](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.IMacroFeatureData~AccessSelections.html), [IMacroFeatureData::IAccessSelections](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.IMacroFeatureData~IAccessSelections.html), or [IMacroFeatureData::ReleaseSelectionAccess](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.IMacroFeatureData~ReleaseSelectionAccess.html) because the concept of a rollback bar does not exist. You can still use [IFeature::ModifyDefinition](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.IFeature~ModifyDefinition.html) or [IFeature::IModifyDefinition2](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.IFeature~IModifyDefinition2.html) to update an IMacroFeatureData object.

If the user decides to cancel the changes made to the IMacroFeatureData object, then discard the IMacroFeatureData object. This action is equivalent to using IMacroFeatureData::ReleaseSelectionAccess.

See [Overview of Macro Features](sldworksapiprogguide.chm::/Macro_Features/Overview_of_Macro_Features.htm) for more information.

## Accessors

[IFeature::GetDefinition](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IFeature~GetDefinition.html)

## Access Diagram

[MacroFeatureData](SWObjectModel.pdf#MacroFeatureData)

## See Also

[IMacroFeatureData Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IMacroFeatureData_members.html)
[SolidWorks.Interop.sldworks Namespace](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks_namespace.html)
[IFeatureManager::IInsertMacroFeature3 Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IFeatureManager~IInsertMacroFeature3.html)
[IFeatureManager::InsertMacroFeature3 Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IFeatureManager~InsertMacroFeature3.html)
