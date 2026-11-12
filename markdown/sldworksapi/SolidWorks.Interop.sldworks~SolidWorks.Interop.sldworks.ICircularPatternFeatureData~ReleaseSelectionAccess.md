---
title: "ReleaseSelectionAccess Method (ICircularPatternFeatureData)"
project: "SOLIDWORKS API Help"
interface: "ICircularPatternFeatureData"
member: "ReleaseSelectionAccess"
kind: "method"
source: "sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ICircularPatternFeatureData~ReleaseSelectionAccess.html"
---

# ReleaseSelectionAccess Method (ICircularPatternFeatureData)

Releases access to the selections that define this circular pattern.

## Syntax

### Visual Basic (Declaration)

```vb
Sub ReleaseSelectionAccess()
```

### Visual Basic (Usage)

```vb
Dim instance As ICircularPatternFeatureData

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

See [CircularPatternFeatureData::ReleaseSelectionAccess](ms-its:sldworksapivb6.chm::/sldworks~CircularPatternFeatureData~ReleaseSelectionAccess.html).

## Remarks

[ICircularPatternFeatureData::AccessSelections](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.ICircularPatternFeatureData~AccessSelections.html) or [ICircularPatternFeatureData::IAccessSelections2](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.ICircularPatternFeatureData~IAccessSelections2.html) puts the model into a rollback state to allow access to the selections that define this feature.

Use this method to restore the rollback state if you did not modify the feature or use [IFeature::ModifyDefinition](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.IFeature~ModifyDefinition.html) or [IFeature::IModifyDefinition2](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.IFeature~IModifyDefinition2.html) if you did.

## See Also

[ICircularPatternFeatureData Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ICircularPatternFeatureData.html)
[ICircularPatternFeatureData Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ICircularPatternFeatureData_members.html)
