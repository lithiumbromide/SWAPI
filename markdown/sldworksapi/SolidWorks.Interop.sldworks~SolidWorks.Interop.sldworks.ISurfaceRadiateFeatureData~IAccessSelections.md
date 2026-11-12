---
title: "IAccessSelections Method (ISurfaceRadiateFeatureData)"
project: "SOLIDWORKS API Help"
interface: "ISurfaceRadiateFeatureData"
member: "IAccessSelections"
kind: "method"
source: "sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISurfaceRadiateFeatureData~IAccessSelections.html"
---

# IAccessSelections Method (ISurfaceRadiateFeatureData)

Accesses the selections for this surface radiate feature.

## Syntax

### Visual Basic (Declaration)

```vb
Function IAccessSelections( _
   ByVal TopDoc As ModelDoc2, _
   ByVal Component As Component2 _
) As System.Boolean
```

### Visual Basic (Usage)

```vb
Dim instance As ISurfaceRadiateFeatureData
Dim TopDoc As ModelDoc2
Dim Component As Component2
Dim value As System.Boolean

value = instance.IAccessSelections(TopDoc, Component)
```

### C#

```csharp
System.bool IAccessSelections(
   ModelDoc2 TopDoc,
   Component2 Component
)
```

### C++/CLI

```cpp
System.bool IAccessSelections(
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

See [SurfaceRadiateFeatureData::IAccessSelections](ms-its:sldworksapivb6.chm::/sldworks~SurfaceRadiateFeatureData~IAccessSelections.html).

## Remarks

| To modify a feature in a... | Then... |
| --- | --- |
| Part | TopDoc argument is the IModelDoc2 for the part Component argument is NULL |
| Assembly | TopDoc is the IModelDoc2 object for the assembly Component argument is the IComponent2 object in which the feature is to be modified |

This method puts the model into a rollback state to allow access to the selections that define this feature. You must use either of the following methods to restore the rollback state:

- [IFeature::ModifyDefinition](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.IFeature~ModifyDefinition.html) or [IFeature::IModifyDefinition2](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.IFeature~IModifyDefinition2.html) if you modified the feature
- [ISurfaceRadiateFeatureData::ReleaseSelectionAccess](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.ISurfaceRadiateFeatureData~ReleaseSelectionAccess.html) if you did not

## See Also

[ISurfaceRadiateFeatureData Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISurfaceRadiateFeatureData.html)
[ISurfaceRadiateFeatureData Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISurfaceRadiateFeatureData_members.html)
[ISurfaceRadiateFeatureData::AccessSelections Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISurfaceRadiateFeatureData~AccessSelections.html)

## Availability

SOLIDWORKS 2001Plus SP2, Revision Number 10.2
