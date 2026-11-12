---
title: "InsertSplitLineIntersect Method (IFeatureManager)"
project: "SOLIDWORKS API Help"
interface: "IFeatureManager"
member: "InsertSplitLineIntersect"
kind: "method"
source: "sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IFeatureManager~InsertSplitLineIntersect.html"
---

# InsertSplitLineIntersect Method (IFeatureManager)

Creates split lines using the selected intersecting tool and target entities.

## Syntax

### Visual Basic (Declaration)

```vb
Function InsertSplitLineIntersect( _
   ByVal CompleteOption As System.Integer _
) As Feature
```

### Visual Basic (Usage)

```vb
Dim instance As IFeatureManager
Dim CompleteOption As System.Integer
Dim value As Feature

value = instance.InsertSplitLineIntersect(CompleteOption)
```

### C#

```csharp
Feature InsertSplitLineIntersect(
   System.int CompleteOption
)
```

### C++/CLI

```cpp
Feature^ InsertSplitLineIntersect(
   System.int CompleteOption
)
```

**NOTE:** See [Differences Between Unmanaged C++ and C++/CLI Code](DifferencesBetweenUnManagedAndCPPCLI.htm).

### Parameters

- `CompleteOption`: - 1 = Linear
  - 7 = Natural
  - 9 = Split all and linear
  - 15 = Split all and natural

### Return Value

Pointer to the [IFeature](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.IFeature.html) object

## VBA Syntax

See [FeatureManager::InsertSplitLineIntersect](ms-its:sldworksapivb6.chm::/sldworks~FeatureManager~InsertSplitLineIntersect.html).

## See Also

[IFeatureManager Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IFeatureManager.html)
[IFeatureManager Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IFeatureManager_members.html)
[ISplitLineFeatureData Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISplitLineFeatureData.html)
[IModelDoc2::InsertSplitLineProject Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelDoc2~InsertSplitLineProject.html)
[IModelDoc2::InsertSplitLineSil Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelDoc2~InsertSplitLineSil.html)

## Availability

SOLIDWORKS 2005 FCS, Revision Number 13.0
