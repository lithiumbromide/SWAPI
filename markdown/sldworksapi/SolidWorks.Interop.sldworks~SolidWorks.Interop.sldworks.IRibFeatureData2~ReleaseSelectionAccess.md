---
title: "ReleaseSelectionAccess Method (IRibFeatureData2)"
project: "SOLIDWORKS API Help"
interface: "IRibFeatureData2"
member: "ReleaseSelectionAccess"
kind: "method"
source: "sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IRibFeatureData2~ReleaseSelectionAccess.html"
---

# ReleaseSelectionAccess Method (IRibFeatureData2)

Releases access to the selections that define this rib feature.

## Syntax

### Visual Basic (Declaration)

```vb
Sub ReleaseSelectionAccess()
```

### Visual Basic (Usage)

```vb
Dim instance As IRibFeatureData2

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

See [RibFeatureData2::ReleaseSelectionAccess](ms-its:sldworksapivb6.chm::/sldworks~RibFeatureData2~ReleaseSelectionAccess.html).

## Remarks

[IRibFeatureData2::AccessSelections](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.IRibFeatureData2~AccessSelections.html) and [IRibFeatureData2::IAccessSelections](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.IRibFeatureData2~IAccessSelections.html) put the model in a rollback state to allow access to the selections that define the feature.

Use this method to restore the rollback state if you did not modify the feature, or use [IFeature::ModifyDefinition](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.IFeature~ModifyDefinition.html) or [IFeature::IModifyDefinition2](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.IFeature~IModifyDefinition2.html) if you did modify the feature.

## See Also

[IRibFeatureData2 Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IRibFeatureData2.html)
[IRibFeatureData2 Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IRibFeatureData2_members.html)

## Availability

SOLIDWORKS 2004 FCS, Revision Number 12.0
