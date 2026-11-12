---
title: "IAccessSelections Method (ISurfaceExtendFeatureData)"
project: "SOLIDWORKS API Help"
interface: "ISurfaceExtendFeatureData"
member: "IAccessSelections"
kind: "method"
source: "sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISurfaceExtendFeatureData~IAccessSelections.html"
---

# IAccessSelections Method (ISurfaceExtendFeatureData)

Accesses the selections that define this surface-extend feature.

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
Dim instance As ISurfaceExtendFeatureData
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

See [SurfaceExtendFeatureData::IAccessSelections](ms-its:sldworksapivb6.chm::/sldworks~SurfaceExtendFeatureData~IAccessSelections.html).

## Remarks

| To modify a feature in a... | Then... |
| --- | --- |
| Part | TopDoc argument is the IModelDoc2 for the part Component argument is NULL |
| Assembly | TopDoc is the IModelDoc2 object for the assembly Component argument is the IComponent2 object in which the feature is to be modified |

This method puts the model into a rollback state to allow access to the selections that define this feature. You must use either of the following methods to restore the rollback state:

- [IFeature::ModifyDefinition](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.IFeature~ModifyDefinition.html) or [IFeature::IModifyDefinition2](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.IFeature~IModifyDefinition2.html) if you modified the feature
- [ISurfaceExtendFeatureData::ReleaseSelectionAccess](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.ISurfaceExtendFeatureData~ReleaseSelectionAccess.html) if you did not

## See Also

[ISurfaceExtendFeatureData Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISurfaceExtendFeatureData.html)
[ISurfaceExtendFeatureData Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISurfaceExtendFeatureData_members.html)
[ISurfaceExtendFeatureData::AccessSelections Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISurfaceExtendFeatureData~AccessSelections.html)

## Availability

SOLIDWORKS 2001Plus SP1, Revision Number 10.1
