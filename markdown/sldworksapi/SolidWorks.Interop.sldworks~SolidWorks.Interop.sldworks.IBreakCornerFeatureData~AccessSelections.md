---
title: "AccessSelections Method (IBreakCornerFeatureData)"
project: "SOLIDWORKS API Help"
interface: "IBreakCornerFeatureData"
member: "AccessSelections"
kind: "method"
source: "sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IBreakCornerFeatureData~AccessSelections.html"
---

# AccessSelections Method (IBreakCornerFeatureData)

Gains access to the selections that describe this break corner feature.

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
Dim instance As IBreakCornerFeatureData
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

- `TopDoc`: Top-level document
- `Component`: Component in which the feature is to be modified

### Return Value

True if the selections were successfully accessed, false if not

## VBA Syntax

See [BreakCornerFeatureData::AccessSelections](ms-its:sldworksapivb6.chm::/sldworks~BreakCornerFeatureData~AccessSelections.html).

## Examples

[Modify Break Corner Feature (C#)](Modify_Break_Corner_Feature_Example_CSharp.htm)
[Modify Break Corner Feature (VB.NET)](Modify_Break_Corner_Feature_Example_VBNET.htm)
[Modify Break Corner Feature (VBA)](Modify_Break_Corner_Feature_Example_VB.htm)

## Remarks

| To modify a feature in a... | Then... |
| --- | --- |
| Part | TopDoc argument is the IModelDoc2 for the part Component argument is NULL |
| Assembly | TopDoc argument is the IModelDoc2 object for the assembly Component argument is the IComponent2 object in which the feature is to be modified |

This method puts the model into a rollback state to allow access to the selections that define this feature. You must use either of the following methods to restore the rollback state:

- [IFeature::ModifyDefinition](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.IFeature~ModifyDefinition.html) if you modified the feature
- [IBreakCornerFeatureData::ReleaseSelectionAccess](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.IBreakCornerFeatureData~ReleaseSelectionAccess.html) if you did not

## See Also

[IBreakCornerFeatureData Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IBreakCornerFeatureData.html)
[IBreakCornerFeatureData Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IBreakCornerFeatureData_members.html)
[IBreakCornerFeatureData::IAccessSelections Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IBreakCornerFeatureData~IAccessSelections.html)

## Availability

SOLIDWORKS 2001Plus SP1, Revision Number 10.1
