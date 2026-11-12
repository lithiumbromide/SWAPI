---
title: "AccessSelections Method (IMoveCopyBodyFeatureData)"
project: "SOLIDWORKS API Help"
interface: "IMoveCopyBodyFeatureData"
member: "AccessSelections"
kind: "method"
source: "sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IMoveCopyBodyFeatureData~AccessSelections.html"
---

# AccessSelections Method (IMoveCopyBodyFeatureData)

Gains access to selections that define this feature.

## Syntax

### Visual Basic (Declaration)

```vb
Function AccessSelections( _
   ByVal PTopDoc As ModelDoc2, _
   ByVal PComponent As Component2 _
) As System.Boolean
```

### Visual Basic (Usage)

```vb
Dim instance As IMoveCopyBodyFeatureData
Dim PTopDoc As ModelDoc2
Dim PComponent As Component2
Dim value As System.Boolean

value = instance.AccessSelections(PTopDoc, PComponent)
```

### C#

```csharp
System.bool AccessSelections(
   ModelDoc2 PTopDoc,
   Component2 PComponent
)
```

### C++/CLI

```cpp
System.bool AccessSelections(
   ModelDoc2^ PTopDoc,
   Component2^ PComponent
)
```

**NOTE:** See [Differences Between Unmanaged C++ and C++/CLI Code](DifferencesBetweenUnManagedAndCPPCLI.htm).

### Parameters

- `PTopDoc`: Top-level document (see **Remarks**)
- `PComponent`: Component in which the feature is to be modified (see **Remarks**)

### Return Value

True if the selections were successfully accessed, false if not

## VBA Syntax

See [MoveCopyBodyFeatureData::AccessSelections](ms-its:sldworksapivb6.chm::/sldworks~MoveCopyBodyFeatureData~AccessSelections.html).

## Examples

[Copy and Rotate Body Using Edge (VBA)](Copy_and_Rotate_Body_using_Edge_Example_VB.htm)
[Move and Copy Body By Setting Transforms (VBA)](Move_and_Copy_Body_by_Setting_Transforms_Example_VB.htm)
[Modify Move/Copy Body Using Vertex (C#)](Move_and_Copy_Body_Using_Vertex_Example_CSharp.htm)
[Modify Move/Copy Body Using Vertex (VB.NET)](Move_and_Copy_Body_Using_Vertex_Example_VBNET.htm)
[Modify Move/Copy Body Using Vertex (VBA)](Move_and_Copy_Body_using_Vertex_Example_VB.htm)
[Set Bodies for Move/Copy (C#)](Set_Bodies_for_Move_Copy_Example_CSharp.htm)
[Set Bodies for Move/Copy (VB.NET)](Set_Bodies_for_Move_Copy_Example_VBNET.htm)
[Set Bodies for Move/Copy (VBA)](Set_Bodies_for_Move_Copy_Example_VB.htm)

## Remarks

| To modify a feature in a... | Then... |
| --- | --- |
| Part | PTopDoc argument is the IModelDoc2 for the part PComponent argument is Nothing or null |
| Assembly | PTopDoc is the IModelDoc2 object for the assembly PComponent argument is the IComponent2 object in which the feature is to be modified |

This method puts the model into a rollback state to allow access to the selections that define this feature. You must use either of the following methods to restore the rollback state:

- [IFeature::ModifyDefinition](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.IFeature~ModifyDefinition.html) or [IFeature::IModifyDefinition2](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.IFeature~IModifyDefinition2.html) if you modified the feature
- [IMoveCopyBodyFeatureData::ReleaseSelectionAccess](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.IMoveCopyBodyFeatureData~ReleaseSelectionAccess.html) if you did not

## See Also

[IMoveCopyBodyFeatureData Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IMoveCopyBodyFeatureData.html)
[IMoveCopyBodyFeatureData Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IMoveCopyBodyFeatureData_members.html)

## Availability

SOLIDWORKS 2005 FCS, Revision Number 13.0
