---
title: "AccessSelections Method (ILoftFeatureData)"
project: "SOLIDWORKS API Help"
interface: "ILoftFeatureData"
member: "AccessSelections"
kind: "method"
source: "sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ILoftFeatureData~AccessSelections.html"
---

# AccessSelections Method (ILoftFeatureData)

Accesses the selections used to define the loft feature.

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
Dim instance As ILoftFeatureData
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

- `TopDoc`: Top-level document (see **Remarks**)
- `Component`: Component in which the feature is to be modified (see **Remarks**)

### Return Value

True if the selections were accessed successfully, false if not

## VBA Syntax

See [LoftFeatureData::AccessSelections](ms-its:sldworksapivb6.chm::/sldworks~LoftFeatureData~AccessSelections.html).

## Examples

[Get Guide Curves in Loft Feature (C#)](Get_Guide_Curves_in_Loft_Feature_Example_CSharp.htm)
[Get Guide Curves in Loft Feature (VB.NET)](Get_Guide_Curves_in_Loft_Feature_Example_VBNET.htm)
[Get Guide Curves in Loft Feature (VBA)](Get_Guide_Curves_in_Loft_Feature_Example_VB.htm)

## Remarks

| To modify a feature in a... | Then... |
| --- | --- |
| Part | TopDoc argument is the IModelDoc2 for the part Component argument is NULL |
| Assembly | TopDoc is the IModelDoc2 object for the assembly Component argument is the IComponent2 object in which the feature is to be modified |

This method puts the model into a rollback state to allow access to the selections that define this feature. You must use either of the following methods to restore the rollback state:

- [IFeature::ModifyDefinition](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.IFeature~ModifyDefinition.html) if you modified the feature
- [ILoftFeatureData::ReleaseSelectionAccess](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.ILoftFeatureData~ReleaseSelectionAccess.html) if you did not

## See Also

[ILoftFeatureData Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ILoftFeatureData.html)
[ILoftFeatureData Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ILoftFeatureData_members.html)
[ILoftFeatureData::IAccessSelections Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ILoftedBendsFeatureData~IAccessSelections.html)

## Availability

SOLIDWORKS 2001Plus FCS, Revision Number 10.0
