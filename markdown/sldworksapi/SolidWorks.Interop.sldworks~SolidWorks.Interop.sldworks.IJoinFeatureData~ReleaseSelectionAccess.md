---
title: "ReleaseSelectionAccess Method (IJoinFeatureData)"
project: "SOLIDWORKS API Help"
interface: "IJoinFeatureData"
member: "ReleaseSelectionAccess"
kind: "method"
source: "sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IJoinFeatureData~ReleaseSelectionAccess.html"
---

# ReleaseSelectionAccess Method (IJoinFeatureData)

Releases access to the selections that define this join feature.

## Syntax

### Visual Basic (Declaration)

```vb
Sub ReleaseSelectionAccess()
```

### Visual Basic (Usage)

```vb
Dim instance As IJoinFeatureData

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

See [JoinFeatureData::ReleaseSelectionAccess](ms-its:sldworksapivb6.chm::/sldworks~JoinFeatureData~ReleaseSelectionAccess.html).

## Examples

[Insert Join Feature (C#)](Insert_Join_Feature_Example_CSharp.htm)
[Insert Join Feature (VB.NET)](Insert_Join_Feature_Example_VBNET.htm)
[Insert Join Feature (VBA)](Insert_Join_Feature_Example_VB.htm)

## Remarks

[IJoinFeatureData::AccessSelections](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.IJoinFeatureData~AccessSelections.html) puts the model into a rollback state to allow access to the selections that define this feature.

Use this method to restore the rollback state if you did not modify the feature or use [IFeature::ModifyDefinition](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.IFeature~ModifyDefinition.html) or [IFeature::IModifyDefintion2](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.IFeature~IModifyDefinition2.html) if you did.

## See Also

[IJoinFeatureData Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IJoinFeatureData.html)
[IJoinFeatureData Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IJoinFeatureData_members.html)

## Availability

SOLIDWORKS 2005 FCS, Revision Number 13.0
