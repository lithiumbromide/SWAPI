---
title: "ReleaseSelectionAccess Method (IFillPatternFeatureData)"
project: "SOLIDWORKS API Help"
interface: "IFillPatternFeatureData"
member: "ReleaseSelectionAccess"
kind: "method"
source: "sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IFillPatternFeatureData~ReleaseSelectionAccess.html"
---

# ReleaseSelectionAccess Method (IFillPatternFeatureData)

Releases access to selections that define this fill pattern feature.

## Syntax

### Visual Basic (Declaration)

```vb
Sub ReleaseSelectionAccess()
```

### Visual Basic (Usage)

```vb
Dim instance As IFillPatternFeatureData

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

See [FillPatternFeatureData::ReleaseSelectionAccess](ms-its:sldworksapivb6.chm::/sldworks~FillPatternFeatureData~ReleaseSelectionAccess.html).

## Remarks

[IFillPatternFeatureData::AccessSelections](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.IFillPatternFeatureData~AccessSelections.html) puts the model into a rollback state to allow access to the selections that define the fill pattern feature.

Use this method to restore the rollback state if you did not modify the fill pattern feature, or use [IFeature::ModifyDefinition](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.IFeature~ModifyDefinition.html) or [IFeature::IModifyDefinition2](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.IFeature~IModifyDefinition2.html) if you did modify the fill pattern feature.

## See Also

[IFillPatternFeatureData Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IFillPatternFeatureData.html)
[IFillPatternFeatureData Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IFillPatternFeatureData_members.html)

## Availability

SOLIDWORKS 2014 FCS, Revision Number 22.0
