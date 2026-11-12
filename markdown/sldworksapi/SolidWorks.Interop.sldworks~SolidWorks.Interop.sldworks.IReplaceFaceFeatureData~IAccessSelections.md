---
title: "IAccessSelections Method (IReplaceFaceFeatureData)"
project: "SOLIDWORKS API Help"
interface: "IReplaceFaceFeatureData"
member: "IAccessSelections"
kind: "method"
source: "sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IReplaceFaceFeatureData~IAccessSelections.html"
---

# IAccessSelections Method (IReplaceFaceFeatureData)

Accesses the selections that define this Replace Face feature.

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
Dim instance As IReplaceFaceFeatureData
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

- `TopDoc`: Top-level document (see **Remarks**)
- `Component`: Component in which the feature is to be modified (see **Remarks**)

### Return Value

True if the selections were successfully accessed, false if not

## VBA Syntax

See [ReplaceFaceFeatureData::IAccessSelections](ms-its:sldworksapivb6.chm::/sldworks~ReplaceFaceFeatureData~IAccessSelections.html).

## Remarks

| To modify a feature in a... | Then... |
| --- | --- |
| Part | TopDoc argument is the IModelDoc2 for the part Component argument is NULL |
| Assembly | TopDoc is the IModelDoc2 object for the assembly Component argument is the IComponent2 object in which the feature is to be modified |

This method puts the model into a rollback state to allow access to the selections that define this feature. You must use either of the following methods to restore the rollback state:

- [IFeature::ModifyDefinition](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.IFeature~ModifyDefinition.html) or [IFeature::IModifyDefinition2](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.IFeature~IModifyDefinition2.html) if you modified the feature
- [IReplaceFaceFeatureData::ReleaseSelectionAccess](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.IReplaceFaceFeatureData~AccessSelections.html) if you did not

## See Also

[IReplaceFaceFeatureData Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IReplaceFaceFeatureData.html)
[IReplaceFaceFeatureData Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IReplaceFaceFeatureData_members.html)
[IReplaceFaceFeatureData::AccessSelections Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IReplaceFaceFeatureData~AccessSelections.html)

## Availability

SOLIDWORKS 2001Plus FCS, Revision Number 10.0
