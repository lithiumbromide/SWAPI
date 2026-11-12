---
title: "IAccessSelections2 Method (IClosedCornerFeatureData)"
project: "SOLIDWORKS API Help"
interface: "IClosedCornerFeatureData"
member: "IAccessSelections2"
kind: "method"
source: "sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IClosedCornerFeatureData~IAccessSelections2.html"
---

# IAccessSelections2 Method (IClosedCornerFeatureData)

Gains access to the selections that describe this closed corner feature.

## Syntax

### Visual Basic (Declaration)

```vb
Function IAccessSelections2( _
   ByVal TopDoc As ModelDoc2, _
   ByVal Component As Component2 _
) As System.Boolean
```

### Visual Basic (Usage)

```vb
Dim instance As IClosedCornerFeatureData
Dim TopDoc As ModelDoc2
Dim Component As Component2
Dim value As System.Boolean

value = instance.IAccessSelections2(TopDoc, Component)
```

### C#

```csharp
System.bool IAccessSelections2(
   ModelDoc2 TopDoc,
   Component2 Component
)
```

### C++/CLI

```cpp
System.bool IAccessSelections2(
   ModelDoc2^ TopDoc,
   Component2^ Component
)
```

**NOTE:** See [Differences Between Unmanaged C++ and C++/CLI Code](DifferencesBetweenUnManagedAndCPPCLI.htm).

### Parameters

- `TopDoc`: Top-level document
- `Component`: Component in which the feature is to be modified

### Return Value

True if the selections were successfully accessed

## VBA Syntax

See [ClosedCornerFeatureData::IAccessSelections2](ms-its:sldworksapivb6.chm::/sldworks~ClosedCornerFeatureData~IAccessSelections2.html).

## Remarks

Remarks

| To modify a feature in a... | Then... |
| --- | --- |
| Part | TopDoc argument is the IModelDoc2 for the part Component argument is NULL |
| Assembly | TopDoc is the IModelDoc2 object for the assembly Component argument is the IComponent2 object in which the feature is to be modified |

This method puts the model into a rollback state to allow access to the selections that define this feature. You must use either of the following methods to restore the rollback state:

- [IFeature::IModifyDefinition2](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.IFeature~IModifyDefinition2.html) if you modified the feature
- [IClosedCornerFeatureData::ReleaseSelectionAccess](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.IClosedCornerFeatureData~ReleaseSelectionAccess.html) if you did not

## See Also

[IClosedCornerFeatureData Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IClosedCornerFeatureData.html)
[IClosedCornerFeatureData Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IClosedCornerFeatureData_members.html)
[AccessSelections Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IClosedCornerFeatureData~AccessSelections.html)

## Availability

SOLIDWORKS 2001Plus FCS, Revision Number 10.0
