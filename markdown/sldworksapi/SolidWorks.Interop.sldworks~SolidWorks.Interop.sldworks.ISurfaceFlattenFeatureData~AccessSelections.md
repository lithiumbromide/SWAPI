---
title: "AccessSelections Method (ISurfaceFlattenFeatureData)"
project: "SOLIDWORKS API Help"
interface: "ISurfaceFlattenFeatureData"
member: "AccessSelections"
kind: "method"
source: "sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISurfaceFlattenFeatureData~AccessSelections.html"
---

# AccessSelections Method (ISurfaceFlattenFeatureData)

Accesses the selections that define this surface-flatten feature.

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
Dim instance As ISurfaceFlattenFeatureData
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

- `TopDoc`: Top-level document
- `Component`: Component in which the feature is to be modified

### Return Value

True if the selections are accessed, false if not

## VBA Syntax

See [SurfaceFlattenFeatureData::AccessSelections](ms-its:sldworksapivb6.chm::/sldworks~SurfaceFlattenFeatureData~AccessSelections.html).

## Examples

See the [ISurfaceFlattenFeatureData](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISurfaceFlattenFeatureData.html) examples.

## Remarks

| To modify a feature in a... | Then... |
| --- | --- |
| Part | TopDoc argument is the IModelDoc2 for the part Component argument is NULL |
| Assembly | TopDoc is the IModelDoc2 object for the assembly Component argument is the IComponent2 object in which the feature is to be modified |

This method puts the model into a rollback state to allow access to the selections that define this feature. You must use either of the following methods to restore the rollback state:

- [IFeature::ModifyDefinition](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.IFeature~ModifyDefinition.html) if you modified the feature
- [ISurfaceFlattenFeatureData::ReleaseSelectionAccess](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISurfaceFlattenFeatureData~ReleaseSelectionAccess.html) if you did not

## See Also

[ISurfaceFlattenFeatureData Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISurfaceFlattenFeatureData.html)
[ISurfaceFlattenFeatureData Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISurfaceFlattenFeatureData_members.html)

## Availability

SOLIDWORKS 2015 FCS, Revision Number 23.0
