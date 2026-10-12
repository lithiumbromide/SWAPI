---
title: "FeatureLocalSketchDrivenPattern Method (IFeatureManager)"
project: "SOLIDWORKS API Help"
interface: "IFeatureManager"
member: "FeatureLocalSketchDrivenPattern"
kind: "method"
source: "sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IFeatureManager~FeatureLocalSketchDrivenPattern.html"
---

# FeatureLocalSketchDrivenPattern Method (IFeatureManager)

Obsolete. See [IFeatureManager::CreateFeature](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IFeatureManager~CreateFeature.html) and the Remarks in [ILocalSketchPatternFeatureData](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ILocalSketchPatternFeatureData.html).

## Syntax

### Visual Basic (Declaration)

```vb
Function FeatureLocalSketchDrivenPattern( _
   ByVal ReferencePoint As System.Integer _
) As Feature
```

### Visual Basic (Usage)

```vb
Dim instance As IFeatureManager
Dim ReferencePoint As System.Integer
Dim value As Feature

value = instance.FeatureLocalSketchDrivenPattern(ReferencePoint)
```

### C#

```csharp
Feature FeatureLocalSketchDrivenPattern(
   System.int ReferencePoint
)
```

### C++/CLI

```cpp
Feature^ FeatureLocalSketchDrivenPattern(
   System.int ReferencePoint
)
```

**NOTE:** See [Differences Between Unmanaged C++ and C++/CLI Code](DifferencesBetweenUnManagedAndCPPCLI.htm).

### Parameters

- `ReferencePoint`: Type of selected reference point as defined in [swLocalSketchPatternReferencePoint_e](ms-its:swconst.chm::/SOLIDWORKS.Interop.swconst~SOLIDWORKS.Interop.swconst.swLocalSketchPatternReferencePoint_e.html) (see **Remarks**)

### Return Value

Local sketch pattern [feature](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.IFeature.html)

## VBA Syntax

See [FeatureManager::FeatureLocalSketchDrivenPattern](ms-its:sldworksapivb6.chm::/sldworks~FeatureManager~FeatureLocalSketchDrivenPattern.html).

## Remarks

| To select ... | Use a mark of... |
| --- | --- |
| Components to pattern | 1 |
| Sketch to define the pattern | 16 |
| Reference point for ReferencePoint NOTE: If ReferencePoint is set to swLocalSketchPatternReferencePoint_e.swLocalSketchPatternSelectedPoint, then the selected reference point must be a vertex. | 32 |

## See Also

[IFeatureManager Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IFeatureManager.html)
[IFeatureManager Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IFeatureManager_members.html)

## Availability

SOLIDWORKS 2015 FCS, Revision Number 23.0
