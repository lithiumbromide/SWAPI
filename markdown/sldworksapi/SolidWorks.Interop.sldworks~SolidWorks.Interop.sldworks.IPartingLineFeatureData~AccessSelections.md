---
title: "AccessSelections Method (IPartingLineFeatureData)"
project: "SOLIDWORKS API Help"
interface: "IPartingLineFeatureData"
member: "AccessSelections"
kind: "method"
source: "sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IPartingLineFeatureData~AccessSelections.html"
---

# AccessSelections Method (IPartingLineFeatureData)

Gains access to the selections that describe the parting line feature.

## Syntax

### Visual Basic (Declaration)

```vb
Function AccessSelections( _
   ByVal TopDoc As ModelDoc2, _
   ByVal Component As Component2 _
) As System.Boolean
```

### Visual Basic (Usage)

```vb
Dim instance As IPartingLineFeatureData
Dim TopDoc As ModelDoc2
Dim Component As Component2
Dim value As System.Boolean

value = instance.AccessSelections(TopDoc, Component)
```

### C#

```csharp
System.bool AccessSelections(
   ModelDoc2 TopDoc,
   Component2 Component
)
```

### C++/CLI

```cpp
System.bool AccessSelections(
   ModelDoc2^ TopDoc,
   Component2^ Component
)
```

**NOTE:** See [Differences Between Unmanaged C++ and C++/CLI Code](DifferencesBetweenUnManagedAndCPPCLI.htm).

### Parameters

- `TopDoc`: Top-level document (see **Remarks**)
- `Component`: Component in which the feature is to be modified (see **Remarks**)

### Return Value

True if the selections were successfully accessed, false if not

## VBA Syntax

See [PartingLineFeatureData::AccessSelections](ms-its:sldworksapivb6.chm::/sldworks~PartingLineFeatureData~AccessSelections.html).

## Examples

[Set Options for Parting Line (VBA)](Set_Split_Faces_Option_for_Parting_Line_Example_VB.htm)
[Get and Set Parting Line Feature Data (C#)](Get_and_Set_Parting_Line_Feature_Data_Example_CSharp.htm)
[Get and Set Parting Line Feature Data (VB.NET)](Get_and_Set_Parting_Line_Feature_Data_Example_VBNET.htm)
[Get and Set Parting Line Feature Data (VBA)](Get_and_Set_Parting_Line_Feature_Data_Example_VB.htm)

## Remarks

| To modify a feature in a... | Then... |
| --- | --- |
| Part | TopDoc argument is the IModelDoc2 for the part Component argument is Nothing or null |
| Assembly | TopDoc is the IModelDoc2 object for the assembly Component argument is the IComponent2 object in which the feature is to be modified |

This method puts the model into a rollback state to allow access to the selections that define this feature. You must use either of the following methods to restore the rollback state:

- [IFeature::ModifyDefinition](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.IFeature~ModifyDefinition.html) or [IFeature::IModifyDefinition2](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.IFeature~IModifyDefinition2.html) if you modified the feature
- [IPartingLineFeatureData::ReleaseSelectionAccess](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.IPartingLineFeatureData~ReleaseSelectionAccess.html) if you did not

## See Also

[IPartingLineFeatureData Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IPartingLineFeatureData.html)
[IPartingLineFeatureData Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IPartingLineFeatureData_members.html)

## Availability

SOLIDWORKS 2005 FCS, Revision Number 13.0
