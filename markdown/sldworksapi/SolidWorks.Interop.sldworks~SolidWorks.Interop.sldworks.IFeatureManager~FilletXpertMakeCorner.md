---
title: "FilletXpertMakeCorner Method (IFeatureManager)"
project: "SOLIDWORKS API Help"
interface: "IFeatureManager"
member: "FilletXpertMakeCorner"
kind: "method"
source: "sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IFeatureManager~FilletXpertMakeCorner.html"
---

# FilletXpertMakeCorner Method (IFeatureManager)

Creates or changes a fillet corner feature.

## Syntax

### Visual Basic (Declaration)

```vb
Function FilletXpertMakeCorner( _
   ByVal CornerType As System.Integer _
) As Feature
```

### Visual Basic (Usage)

```vb
Dim instance As IFeatureManager
Dim CornerType As System.Integer
Dim value As Feature

value = instance.FilletXpertMakeCorner(CornerType)
```

### C#

```csharp
Feature FilletXpertMakeCorner(
   System.int CornerType
)
```

### C++/CLI

```cpp
Feature^ FilletXpertMakeCorner(
   System.int CornerType
)
```

**NOTE:** See [Differences Between Unmanaged C++ and C++/CLI Code](DifferencesBetweenUnManagedAndCPPCLI.htm).

### Parameters

- `CornerType`: See **Remarks**

### Return Value

[Feature](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.IFeature.html)

## VBA Syntax

See [FeatureManager::FilletXpertMakeCorner](ms-its:sldworksapivb6.chm::/sldworks~FeatureManager~FilletXpertMakeCorner.html).

## Remarks

For the fillet corner, everything is dependent on the convexity of the three filleted edges adjacent.

If all three edges have the same convexity, then no corner substitution is possible. Otherwise, there will be two edges of one convexity, and one of the other. It does not matter if the two same edges are both convex or both concave, as long as the edges are the same.

The valid values for the CornerType argument are:

- 1 = if the two edges with the same convexity have the same radius, make a triangular corner patch.
- 2 = if the two edges with the same convexity have the same radius, make a quadrilateral corner patch.
- 3 = if the two edges with the same convexity have different radii, make a triangular corner patch.
- 4 = if the two edges with the same convexity have different radii, make two triangular corner patches (which together look like a split quadrilateral patch).
- 5 = if the two edges with the same convexity have different radii, make a quadrilateral corner patch.

NOTE: Types 1 and 3 relate to one another, as do types 2 and 5. This means that if the corner type is not consistent with the convexity/radius requirements, then the appropriate type will be mapped and substituted. Thus, specifying type 1 on a corner with two edges of the same convexity, but different radii, results in a type 3, automatically.

## See Also

[IFeatureManager Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IFeatureManager.html)
[IFeatureManager Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IFeatureManager_members.html)
[IFeatureManager::FeatureFillet Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IFeatureManager~FeatureFillet.html)
[IFeatureManager::IFeatureFillet Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IFeatureManager~IFeatureFillet.html)
[IFeatureManager::FilletXpertChange Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IFeatureManager~FilletXpertChange.html)
[IFeatureManager::FilletXpertRemove Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IFeatureManager~FilletXpertRemove.html)

## Availability

SOLIDWORKS 2008 FCS, Revision Number 16.0
