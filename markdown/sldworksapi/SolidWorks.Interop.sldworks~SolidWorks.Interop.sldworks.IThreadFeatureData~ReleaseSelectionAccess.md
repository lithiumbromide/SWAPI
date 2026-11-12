---
title: "ReleaseSelectionAccess Method (IThreadFeatureData)"
project: "SOLIDWORKS API Help"
interface: "IThreadFeatureData"
member: "ReleaseSelectionAccess"
kind: "method"
source: "sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IThreadFeatureData~ReleaseSelectionAccess.html"
---

# ReleaseSelectionAccess Method (IThreadFeatureData)

Releases the selections that created this thread feature.

## Syntax

### Visual Basic (Declaration)

```vb
Sub ReleaseSelectionAccess()
```

### Visual Basic (Usage)

```vb
Dim instance As IThreadFeatureData

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

See [ThreadFeatureData::ReleaseSelectionAccess](ms-its:sldworksapivb6.chm::/sldworks~ThreadFeatureData~ReleaseSelectionAccess.html).

## Remarks

[IThreadFeatureData::AccessSelections](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IThreadFeatureData~AccessSelections.html) puts the model in a rollback state to allow access to the selections that define the feature.

Use this method to restore the rollback state if you did not modify the feature, or use [IFeature::ModifyDefinition](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.IFeature~ModifyDefinition.html) if you did modify the feature.

## See Also

[IThreadFeatureData Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IThreadFeatureData.html)
[IThreadFeatureData Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IThreadFeatureData_members.html)

## Availability

SOLIDWORKS 2018 FCS, Revision Number 26.0
