---
title: "ReleaseSelectionAccess Method (ISimpleHoleFeatureData2)"
project: "SOLIDWORKS API Help"
interface: "ISimpleHoleFeatureData2"
member: "ReleaseSelectionAccess"
kind: "method"
source: "sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISimpleHoleFeatureData2~ReleaseSelectionAccess.html"
---

# ReleaseSelectionAccess Method (ISimpleHoleFeatureData2)

Releases access to the selections that define the simple hole feature.

## Syntax

### Visual Basic (Declaration)

```vb
Sub ReleaseSelectionAccess()
```

### Visual Basic (Usage)

```vb
Dim instance As ISimpleHoleFeatureData2

instance.ReleaseSelectionAccess()
```

### C#

```csharp
void ReleaseSelectionAccess()
```

### C++/CLI

```cpp
void ReleaseSelectionAccess();
```

**NOTE:** See [Differences Between Unmanaged C++ and C++/CLI Code](DifferencesBetweenUnManagedAndCPPCLI.htm).

## VBA Syntax

See [SimpleHoleFeatureData2::ReleaseSelectionAccess](ms-its:sldworksapivb6.chm::/sldworks~SimpleHoleFeatureData2~ReleaseSelectionAccess.html).

## Examples

See [ISimpleHoleFeatureData2](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.ISimpleHoleFeatureData2.html) examples.

## Remarks

[ISimpleHoleFeatureData2::AccessSelections](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.ISimpleHoleFeatureData2~AccessSelections.html) and [ISimpleHoleFeatureData2::IAccessSelections](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.ISimpleHoleFeatureData2~IAccessSelections.html) put the model in a rollback state to allow access to the selections that define the feature.

Use this method to restore the rollback state if you did not modify the feature, or use [IFeature::ModifyDefinition](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.IFeature~ModifyDefinition.html) or [IFeature::IModifyDefinition2](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.IFeature~IModifyDefinition2.html) if you did modify the feature.

## See Also

[ISimpleHoleFeatureData2 Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISimpleHoleFeatureData2.html)
[ISimpleHoleFeatureData2 Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISimpleHoleFeatureData2_members.html)

## Availability

SOLIDWORKS 2001Plus FCS, Revision Number 10.0
