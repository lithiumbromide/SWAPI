---
title: "AccessSelections Method (IDomeFeatureData2)"
project: "SOLIDWORKS API Help"
interface: "IDomeFeatureData2"
member: "AccessSelections"
kind: "method"
source: "sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IDomeFeatureData2~AccessSelections.html"
---

# AccessSelections Method (IDomeFeatureData2)

Gains access to selections used to define the dome.

## Syntax

### Visual Basic (Declaration)

```vb
Function AccessSelections( _
   ByVal TopDoc As System.Object, _
   ByVal Component As System.Object _
) As System.Boolean
```

### Visual Basic (Usage)

```vb
Dim instance As IDomeFeatureData2
Dim TopDoc As System.Object
Dim Component As System.Object
Dim value As System.Boolean

value = instance.AccessSelections(TopDoc, Component)
```

### C#

```csharp
System.bool AccessSelections(
   System.object TopDoc,
   System.object Component
)
```

### C++/CLI

```cpp
System.bool AccessSelections(
   System.Object^ TopDoc,
   System.Object^ Component
)
```

**NOTE:** See [Differences Between Unmanaged C++ and C++/CLI Code](DifferencesBetweenUnManagedAndCPPCLI.htm).

### Parameters

- `TopDoc`: Top level document (see **Remarks**)
- `Component`: Component for the feature (see Remarks)

### Return Value

True if the selections where successfully accessed, false if not

## VBA Syntax

See [DomeFeatureData2::AccessSelections](ms-its:sldworksapivb6.chm::/sldworks~DomeFeatureData2~AccessSelections.html).

## Examples

[Change Height of Dome Feature (VBA)](Change_Height_of_Dome_Feature_Example_VB.htm)
[Get and Set Constraint for Dome Feature (VBA)](Get_and_Set_Constraint_for_Dome_Feature_Example_VB.htm)
[Create and Modify Dome Feature (C#)](Create_and_Modify_Dome_Feature_Example_CSharp.htm)
[Create and Modify Dome Feature (VB.NET)](Create_and_Modify_Dome_Feature_Example_VBNET.htm)
[Create and Modify Dome Feature (VBA)](Create_and_Modify_Dome_Feature_Example_VB.htm)

## Remarks

| To modify a feature in a... | Then... |
| --- | --- |
| Part | TopDoc argument is the IModelDoc2 for the part Component argument is NULL |
| Assembly | TopDoc is the IModelDoc2 object for the assembly Component argument is the IComponent2 object in which the feature is to be modified |

This method puts the model into a rollback state to allow access to the selections that define this feature. You must use either of the following methods to restore the rollback state:

- [IFeature::ModifyDefinition](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.IFeature~ModifyDefinition.html) or [IFeature::IModifyDefinition2](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.IFeature~IModifyDefinition2.html) if you modified the feature
- [IDomeFeatureData2::ReleaseSelectionAccess](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.IDomeFeatureData2~ReleaseSelectionAccess.html) if you did not

## See Also

[IDomeFeatureData2 Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IDomeFeatureData2.html)
[IDomeFeatureData2 Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IDomeFeatureData2_members.html)
[IDomeFeatureData2::IAccessSelections Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IDomeFeatureData2~IAccessSelections.html)
