---
title: "ReleaseSelectionAccess Method (ISurfRevolveFeatureData)"
project: "SOLIDWORKS API Help"
interface: "ISurfRevolveFeatureData"
member: "ReleaseSelectionAccess"
kind: "method"
source: "sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISurfRevolveFeatureData~ReleaseSelectionAccess.html"
---

# ReleaseSelectionAccess Method (ISurfRevolveFeatureData)

Releases access to the selections for this surface revolve feature.

## Syntax

### Visual Basic (Declaration)

```vb
Sub ReleaseSelectionAccess()
```

### Visual Basic (Usage)

```vb
Dim instance As ISurfRevolveFeatureData

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

See [SurfRevolveFeatureData::ReleaseSelectionAccess](ms-its:sldworksapivb6.chm::/sldworks~SurfRevolveFeatureData~ReleaseSelectionAccess.html).

## Remarks

[ISurfRevolveFeatureData::AccessSelections](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.ISurfRevolveFeatureData~AccessSelections.html) and [ISurfRevolveFeatureData::IAccessSelections](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.ISurfRevolveFeatureData~IAccessSelections.html) put the model in a rollback state to allow access to the selections that define the feature.

Use this method to restore the rollback state if you did not modify the feature, or use [IFeature::ModifyDefinition](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.IFeature~ModifyDefinition.html) or [IFeature::IModifyDefinition2](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.IFeature~IModifyDefinition2.html) if you did modify the feature.

## See Also

[ISurfRevolveFeatureData Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISurfRevolveFeatureData.html)
[ISurfRevolveFeatureData Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISurfRevolveFeatureData_members.html)

## Availability

SOLIDWORKS 2001Plus SP1, Revision Number 10.1
