---
title: "AccessSelections Method (IAdvancedHoleFeatureData)"
project: "SOLIDWORKS API Help"
interface: "IAdvancedHoleFeatureData"
member: "AccessSelections"
kind: "method"
source: "sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IAdvancedHoleFeatureData~AccessSelections.html"
---

# AccessSelections Method (IAdvancedHoleFeatureData)

Gains access to the selections used to define the Advanced Hole feature.

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
Dim instance As IAdvancedHoleFeatureData
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

- `TopDoc`: [IModelDoc2](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.IModelDoc2.html) for the part
- `Component`: Null or Nothing

### Return Value

True if the selections are successfully accessed, false if not

## VBA Syntax

See [AdvancedHoleFeatureData::AccessSelections](ms-its:sldworksapivb6.chm::/sldworks~AdvancedHoleFeatureData~AccessSelections.html).

## Examples

See the [IAdvancedHoleFeatureData](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IAdvancedHoleFeatureData.html) examples.

## Remarks

This method puts the model into a rollback state to allow access to the selections that define this feature.

You must use either of the following methods to restore the original state of the model:

- [IFeature::ModifyDefinition](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.IFeature~ModifyDefinition.html) or [IFeature::IModifyDefinition2](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.IFeature~IModifyDefinition2.html), if you modified the feature
- [IAdvancedHoleFeatureData::ReleaseSelectionAccess](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IAdvancedHoleFeatureData~ReleaseSelectionAccess.html), if you did not modify the feature

## See Also

[IAdvancedHoleFeatureData Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IAdvancedHoleFeatureData.html)
[IAdvancedHoleFeatureData Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IAdvancedHoleFeatureData_members.html)

## Availability

SOLIDWORKS 2018 FCS, Revision Number 26.0
