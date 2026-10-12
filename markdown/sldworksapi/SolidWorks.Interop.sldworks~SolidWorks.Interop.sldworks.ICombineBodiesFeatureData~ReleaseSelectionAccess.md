---
title: "ReleaseSelectionAccess Method (ICombineBodiesFeatureData)"
project: "SOLIDWORKS API Help"
interface: "ICombineBodiesFeatureData"
member: "ReleaseSelectionAccess"
kind: "method"
source: "sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ICombineBodiesFeatureData~ReleaseSelectionAccess.html"
---

# ReleaseSelectionAccess Method (ICombineBodiesFeatureData)

Releases access to the selections that define this combine feature.

## Syntax

### Visual Basic (Declaration)

```vb
Sub ReleaseSelectionAccess()
```

### Visual Basic (Usage)

```vb
Dim instance As ICombineBodiesFeatureData

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

See [CombineBodiesFeatureData::ReleaseSelectionAccess](ms-its:sldworksapivb6.chm::/sldworks~CombineBodiesFeatureData~ReleaseSelectionAccess.html).

## Examples

[Combine Bodies (C#)](Combine_Bodies_Example_CSharp.htm)
[Combine Bodies (VB.NET)](Combine_Bodies_Example_VBNET.htm)
[Combine Bodies (VBA)](Combine_Bodies_Example_VB.htm)

## Remarks

[ICombineBodiesFeatureData::AccessSelections](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.ICombineBodiesFeatureData~AccessSelections.html) puts the model into a rollback state to allow access to the selections that define this feature.

Use this method to restore the rollback state if you did not modify the feature or use [IFeature::ModifyDefinition](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.IFeature~ModifyDefinition.html) if you did.

## See Also

[ICombineBodiesFeatureData Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ICombineBodiesFeatureData.html)
[ICombineBodiesFeatureData Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ICombineBodiesFeatureData_members.html)

## Availability

SOLIDWORKS 2005 FCS, Revision Number 13
