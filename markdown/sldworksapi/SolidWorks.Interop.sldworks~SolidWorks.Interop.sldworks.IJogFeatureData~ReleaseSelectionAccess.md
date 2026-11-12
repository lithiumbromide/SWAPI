---
title: "ReleaseSelectionAccess Method (IJogFeatureData)"
project: "SOLIDWORKS API Help"
interface: "IJogFeatureData"
member: "ReleaseSelectionAccess"
kind: "method"
source: "sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IJogFeatureData~ReleaseSelectionAccess.html"
---

# ReleaseSelectionAccess Method (IJogFeatureData)

Releases access to the selections for this jog feature.

## Syntax

### Visual Basic (Declaration)

```vb
Sub ReleaseSelectionAccess()
```

### Visual Basic (Usage)

```vb
Dim instance As IJogFeatureData

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

See [JogFeatureData::ReleaseSelectionAccess](ms-its:sldworksapivb6.chm::/sldworks~JogFeatureData~ReleaseSelectionAccess.html).

## Remarks

[IJogFeatureData::AccessSelections](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.IJogFeatureData~AccessSelections.html) and [IJogFeatureData::IAccessSelections](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.IJogFeatureData~IAccessSelections.html) put the model into a rollback state to allow access to the selections that define this feature.

Use this method to restore the rollback state if you did not modify the feature or use [IFeature::ModifyDefinition](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.IFeature~ModifyDefinition.html) or [IFeature::IModifyDefintion2](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.IFeature~IModifyDefinition2.html) if you did.

## See Also

[IJogFeatureData Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IJogFeatureData.html)
[IJogFeatureData Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IJogFeatureData_members.html)

## Availability

SOLIDWORKS 2001Plus SP1, Revision Number 10.1
