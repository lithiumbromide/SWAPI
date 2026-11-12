---
title: "ReleaseSelectionAccess Method (IMirrorPartFeatureData)"
project: "SOLIDWORKS API Help"
interface: "IMirrorPartFeatureData"
member: "ReleaseSelectionAccess"
kind: "method"
source: "sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IMirrorPartFeatureData~ReleaseSelectionAccess.html"
---

# ReleaseSelectionAccess Method (IMirrorPartFeatureData)

Releases access to the selections used to define the mirror part feature.

## Syntax

### Visual Basic (Declaration)

```vb
Sub ReleaseSelectionAccess()
```

### Visual Basic (Usage)

```vb
Dim instance As IMirrorPartFeatureData

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

See [MirrorPartFeatureData::ReleaseSelectionAccess](ms-its:sldworksapivb6.chm::/sldworks~MirrorPartFeatureData~ReleaseSelectionAccess.html).

## Examples

See the [IMirrorPartFeatureData](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.IMirrorPartFeatureData.html) examples.

## Remarks

[IMirrorPartFeatureData::AccessSelections](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.IMirrorPartFeatureData~AccessSelections.html) puts the model in a rollback state to allow access to the selections that define this feature.

Use this method to restore the rollback state if you did not modify the feature, or use [IFeature::ModifyDefinition](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.IFeature~ModifyDefinition.html) or [IFeature::IModifyDefinition2](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.IFeature~IModifyDefinition2.html) if you did.

## See Also

[IMirrorPartFeatureData Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IMirrorPartFeatureData.html)
[IMirrorPartFeatureData Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IMirrorPartFeatureData_members.html)

## Availability

SOLIDWORKS 2014 FCS, Revision Number 22.0
