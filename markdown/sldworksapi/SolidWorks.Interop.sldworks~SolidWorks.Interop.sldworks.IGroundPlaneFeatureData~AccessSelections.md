---
title: "AccessSelections Method (IGroundPlaneFeatureData)"
project: "SOLIDWORKS API Help"
interface: "IGroundPlaneFeatureData"
member: "AccessSelections"
kind: "method"
source: "sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IGroundPlaneFeatureData~AccessSelections.html"
---

# AccessSelections Method (IGroundPlaneFeatureData)

Gains access to the selections that define this ground plane feature.

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
Dim instance As IGroundPlaneFeatureData
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

## VBA Syntax

See [GroundPlaneFeatureData::AccessSelections](ms-its:sldworksapivb6.chm::/sldworks~GroundPlaneFeatureData~AccessSelections.html).

## Examples

See the [IGroundPlaneFeatureData](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IGroundPlaneFeatureData.html) example.

## Remarks

| To modify a feature in a... | Then... |
| --- | --- |
| Part | TopDoc argument is the IModelDoc2 for the part Component argument is Nothing or null |
| Assembly | TopDoc is the IModelDoc2 object for the assembly Component argument is the IComponent2 object in which the feature is to be modified |

This method puts the model into a rollback state to allow access to the selections that define this feature. You must use either of the following methods to restore the rollback state:

- [IFeature::ModifyDefinition](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.IFeature~ModifyDefinition.html) or [IFeature::IModifyDefinition2](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.IFeature~IModifyDefinition2.html) if you modified the feature
- [IGroundPlaneFeatureData::ReleaseSelectionAccess](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IGroundPlaneFeatureData~ReleaseSelectionAccess.html) if you did not

## See Also

[IGroundPlaneFeatureData Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IGroundPlaneFeatureData.html)
[IGroundPlaneFeatureData Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IGroundPlaneFeatureData_members.html)

## Availability

SOLIDWORKS 2019 FCS, Revision Number 27.0
