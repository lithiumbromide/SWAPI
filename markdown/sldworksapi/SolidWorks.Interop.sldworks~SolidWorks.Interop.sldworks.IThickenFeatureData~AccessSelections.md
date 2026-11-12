---
title: "AccessSelections Method (IThickenFeatureData)"
project: "SOLIDWORKS API Help"
interface: "IThickenFeatureData"
member: "AccessSelections"
kind: "method"
source: "sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IThickenFeatureData~AccessSelections.html"
---

# AccessSelections Method (IThickenFeatureData)

Gains access to the selections that define this thicken feature.

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
Dim instance As IThickenFeatureData
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
- `Component`: Component to which this feature is to be applied

### Return Value

True if access is successful, false if not

## VBA Syntax

See [ThickenFeatureData::AccessSelections](ms-its:sldworksapivb6.chm::/sldworks~ThickenFeatureData~AccessSelections.html).

## Examples

[Create Thicken Feature (VBA)](Create_Thicken_Feature_Example_VB.htm)

## Remarks

| To modify a feature in a... | Then... |
| --- | --- |
| Part | TopDoc argument is the IModelDoc2 for the part Component argument is NULL |
| Assembly | TopDoc is the IModelDoc2 object for the assembly Component argument is the IComponent2 object in which the feature is to be modified |

This method puts the model into a rollback state to allow access to the selections that define this feature. You must use either of the following methods to restore the rollback state:

- [IFeature::ModifyDefinition](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.IFeature~ModifyDefinition.html) or [IFeature::IModifyDefinition2](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.IFeature~IModifyDefinition2.html) if you modified the feature
- [IThickenFeatureData::ReleaseSelectionAccess](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.IThickenFeatureData~ReleaseSelectionAccess.html) if you did not

## See Also

[IThickenFeatureData Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IThickenFeatureData.html)
[IThickenFeatureData Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IThickenFeatureData_members.html)
[IThickenFeatureData::IAccessSelections Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IThickenFeatureData~IAccessSelections.html)

## Availability

SOLIDWORKS 2001Plus FCS, Revision Number 10.0
