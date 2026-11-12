---
title: "IAccessSelections Method (IHoleSeriesFeatureData2)"
project: "SOLIDWORKS API Help"
interface: "IHoleSeriesFeatureData2"
member: "IAccessSelections"
kind: "method"
source: "sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IHoleSeriesFeatureData2~IAccessSelections.html"
---

# IAccessSelections Method (IHoleSeriesFeatureData2)

Gains access to the selections that define this hole series feature.

## Syntax

### Visual Basic (Declaration)

```vb
Function IAccessSelections( _
   ByVal TopDoc As ModelDoc, _
   ByVal Component As Component _
) As System.Boolean
```

### Visual Basic (Usage)

```vb
Dim instance As IHoleSeriesFeatureData2
Dim TopDoc As ModelDoc
Dim Component As Component
Dim value As System.Boolean

value = instance.IAccessSelections(TopDoc, Component)
```

### C#

```csharp
System.bool IAccessSelections(
   ModelDoc TopDoc,
   Component Component
)
```

### C++/CLI

```cpp
System.bool IAccessSelections(
   ModelDoc^ TopDoc,
   Component^ Component
)
```

**NOTE:** See [Differences Between Unmanaged C++ and C++/CLI Code](DifferencesBetweenUnManagedAndCPPCLI.htm).

### Parameters

- `TopDoc`: Top-level document (see **Remarks**)
- `Component`: Component in which the feature is to be modified (see **Remarks**)

### Return Value

True if the selections are successfully accessed, false if not

## Remarks

| To modify a feature in a... | Then... |
| --- | --- |
| Part | TopDoc argument is the IModelDoc2 for the part Component argument is NULL |
| Assembly | TopDoc is the IModelDoc2 object for the assembly Component argument is the IComponent2 object in which the feature is to be modified |

This method puts the model into a rollback state to allow access to the selections that define this feature. You must use either of the following methods to restore the rollback state:

- [IFeature::IModifyDefinition2](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.IFeature~IModifyDefinition2.html) if you modified the feature
- [IHoleSeriesFeatureData2::ReleaseSelectionAccess](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.IHoleSeriesFeatureData2~ReleaseSelectionAccess.html) if you did not

## See Also

[IHoleSeriesFeatureData2 Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IHoleSeriesFeatureData2.html)
[IHoleSeriesFeatureData2 Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IHoleSeriesFeatureData2_members.html)
[IHoleSeriesFeatureData2::AccessSelections Method ()](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IHoleSeriesFeatureData2~AccessSelections.html)

## Availability

SOLIDWORKS 2014 FCS, Revision Number 22.0
