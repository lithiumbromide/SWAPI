---
title: "FeatureSketchDrivenPattern Method (IFeatureManager)"
project: "SOLIDWORKS API Help"
interface: "IFeatureManager"
member: "FeatureSketchDrivenPattern"
kind: "method"
source: "sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IFeatureManager~FeatureSketchDrivenPattern.html"
---

# FeatureSketchDrivenPattern Method (IFeatureManager)

Obsolete. See [IFeatureManager::CreateFeature](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IFeatureManager~CreateFeature.html) and the Remarks in [ISketchPatternFeatureData](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISketchPatternFeatureData.html).

## Syntax

### Visual Basic (Declaration)

```vb
Function FeatureSketchDrivenPattern( _
   ByVal UseCentroid As System.Boolean, _
   ByVal BGeomPatt As System.Boolean _
) As Feature
```

### Visual Basic (Usage)

```vb
Dim instance As IFeatureManager
Dim UseCentroid As System.Boolean
Dim BGeomPatt As System.Boolean
Dim value As Feature

value = instance.FeatureSketchDrivenPattern(UseCentroid, BGeomPatt)
```

### C#

```csharp
Feature FeatureSketchDrivenPattern(
   System.bool UseCentroid,
   System.bool BGeomPatt
)
```

### C++/CLI

```cpp
Feature^ FeatureSketchDrivenPattern(
   System.bool UseCentroid,
   System.bool BGeomPatt
)
```

**NOTE:** See [Differences Between Unmanaged C++ and C++/CLI Code](DifferencesBetweenUnManagedAndCPPCLI.htm).

### Parameters

- `UseCentroid`: True to use a centroid as the reference point, false to not
- `BGeomPatt`: True to pattern using only the feature geometry, false to pattern each instance

### Return Value

Pointer to the [IFeature](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.IFeature.html) object

## VBA Syntax

See [FeatureManager::FeatureSketchDrivenPattern](ms-its:sldworksapivb6.chm::/sldworks~FeatureManager~FeatureSketchDrivenPattern.html).

## Remarks

Before calling this method, select the required entities using the proper selection marks:

- features = 4
- points = 32
- sketches = 64
- faces = 128
- bodies = 256

See [IModelDocExtension::SelectByID2](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.IModelDocExtension~SelectByID2.html) for details about selecting input entities. See the SOLIDWORKS Help for more information about sketch-driven patterns.

## See Also

[IFeatureManager Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IFeatureManager.html)
[IFeatureManager Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IFeatureManager_members.html)

## Availability

SOLIDWORKS 2003 SP4, Revision Number 11.4
