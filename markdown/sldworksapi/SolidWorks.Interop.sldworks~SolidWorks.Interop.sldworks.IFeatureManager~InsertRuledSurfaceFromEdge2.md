---
title: "InsertRuledSurfaceFromEdge2 Method (IFeatureManager)"
project: "SOLIDWORKS API Help"
interface: "IFeatureManager"
member: "InsertRuledSurfaceFromEdge2"
kind: "method"
source: "sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IFeatureManager~InsertRuledSurfaceFromEdge2.html"
---

# InsertRuledSurfaceFromEdge2 Method (IFeatureManager)

Inserts a ruled surface from the selected edge on this feature.

## Syntax

### Visual Basic (Declaration)

```vb
Function InsertRuledSurfaceFromEdge2( _
   ByVal Type As System.Integer, _
   ByVal Length As System.Double, _
   ByVal FlipPullDir As System.Boolean, _
   ByVal FlipDir As System.Boolean, _
   ByVal TrimAndSew As System.Boolean, _
   ByVal Angle As System.Double, _
   ByVal CoordInput As System.Boolean, _
   ByVal X As System.Double, _
   ByVal Y As System.Double, _
   ByVal Z As System.Double, _
   ByVal BConnectSurface As System.Boolean _
) As Feature
```

### Visual Basic (Usage)

```vb
Dim instance As IFeatureManager
Dim Type As System.Integer
Dim Length As System.Double
Dim FlipPullDir As System.Boolean
Dim FlipDir As System.Boolean
Dim TrimAndSew As System.Boolean
Dim Angle As System.Double
Dim CoordInput As System.Boolean
Dim X As System.Double
Dim Y As System.Double
Dim Z As System.Double
Dim BConnectSurface As System.Boolean
Dim value As Feature

value = instance.InsertRuledSurfaceFromEdge2(Type, Length, FlipPullDir, FlipDir, TrimAndSew, Angle, CoordInput, X, Y, Z, BConnectSurface)
```

### C#

```csharp
Feature InsertRuledSurfaceFromEdge2(
   System.int Type,
   System.double Length,
   System.bool FlipPullDir,
   System.bool FlipDir,
   System.bool TrimAndSew,
   System.double Angle,
   System.bool CoordInput,
   System.double X,
   System.double Y,
   System.double Z,
   System.bool BConnectSurface
)
```

### C++/CLI

```cpp
Feature^ InsertRuledSurfaceFromEdge2(
   System.int Type,
   System.double Length,
   System.bool FlipPullDir,
   System.bool FlipDir,
   System.bool TrimAndSew,
   System.double Angle,
   System.bool CoordInput,
   System.double X,
   System.double Y,
   System.double Z,
   System.bool BConnectSurface
)
```

**NOTE:** See [Differences Between Unmanaged C++ and C++/CLI Code](DifferencesBetweenUnManagedAndCPPCLI.htm).

### Parameters

- `Type`: - 0 = Tangent to Surface
  - 1 = Normal to Surface
  - 2 = Tapered to Vector
  - 3 = Perpendicular to Vector
  - 4 = Sweep
- `Length`: Distance at which to create the surface; valid for Tangent to Surface, Tapered to Vector, Perpendicular to Vector, and Sweep types only
- `FlipPullDir`: True to flip the pull direction, false to not; valid for Normal to Surface and Tapered to Vector types only
- `FlipDir`: True to flip the direction, false to not; valid for Perpendicular to Vector type only
- `TrimAndSew`: True to trim and knit the surface, false to not
- `Angle`: Angle for Tapered to Vector type only
- `CoordInput`: True to enable coordinate input, false if not; for Sweep type only
- `X`: x coordinate
- `Y`: y coordinate
- `Z`: z coordinate
- `BConnectSurface`: True to remove any connecting surfaces, false to not

### Return Value

Pointer to the [IFeature](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.IFeature.html) object

## VBA Syntax

See [FeatureManager::InsertRuledSurfaceFromEdge2](ms-its:sldworksapivb6.chm::/sldworks~FeatureManager~InsertRuledSurfaceFromEdge2.html).

## Remarks

If you [select](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.IModelDocExtension~SelectByID2.html) an edge with a selection mark of 4, the default face is used. If you select an edge with a selection mark of 6, the alternate face is used.

## See Also

[IFeatureManager Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IFeatureManager.html)
[IFeatureManager Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IFeatureManager_members.html)
[IRuledSurfaceFeatureData Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IRuledSurfaceFeatureData.html)
[IModeler::CreateRuledSurface Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModeler~CreateRuledSurface.html)
[IModeler::CreateRuledSurfaceFromEdge Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModeler~CreateRuledSurfaceFromEdge.html)
[IModeler::ICreateRuledSurface Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModeler~ICreateRuledSurface.html)
[IModeler::ICreateRuledSurfaceFromEdge Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModeler~ICreateRuledSurfaceFromEdge.html)

## Availability

SOLIDWORKS 2004 SP3, Revision Number 12.3
