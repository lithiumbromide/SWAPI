---
title: "InsertRuledSurfaceFromEdge Method (IFeatureManager)"
project: "SOLIDWORKS API Help"
interface: "IFeatureManager"
member: "InsertRuledSurfaceFromEdge"
kind: "method"
source: "sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IFeatureManager~InsertRuledSurfaceFromEdge.html"
---

# InsertRuledSurfaceFromEdge Method (IFeatureManager)

Obsolete. Superseded by [IFeatureManager::InsertRuledSurfaceFromEdge2](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.IFeatureManager~InsertRuledSurfaceFromEdge2.html).

## Syntax

### Visual Basic (Declaration)

```vb
Function InsertRuledSurfaceFromEdge( _
   ByVal Type As System.Integer, _
   ByVal Length As System.Double, _
   ByVal FlipPullDir As System.Boolean, _
   ByVal FlipDir As System.Boolean, _
   ByVal TrimAndSew As System.Boolean, _
   ByVal Angle As System.Double, _
   ByVal CoordInput As System.Boolean, _
   ByVal X As System.Double, _
   ByVal Y As System.Double, _
   ByVal Z As System.Double _
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
Dim value As Feature

value = instance.InsertRuledSurfaceFromEdge(Type, Length, FlipPullDir, FlipDir, TrimAndSew, Angle, CoordInput, X, Y, Z)
```

### C#

```csharp
Feature InsertRuledSurfaceFromEdge(
   System.int Type,
   System.double Length,
   System.bool FlipPullDir,
   System.bool FlipDir,
   System.bool TrimAndSew,
   System.double Angle,
   System.bool CoordInput,
   System.double X,
   System.double Y,
   System.double Z
)
```

### C++/CLI

```cpp
Feature^ InsertRuledSurfaceFromEdge(
   System.int Type,
   System.double Length,
   System.bool FlipPullDir,
   System.bool FlipDir,
   System.bool TrimAndSew,
   System.double Angle,
   System.bool CoordInput,
   System.double X,
   System.double Y,
   System.double Z
)
```

**NOTE:** See [Differences Between Unmanaged C++ and C++/CLI Code](DifferencesBetweenUnManagedAndCPPCLI.htm).

### Parameters

- `Type`:
- `Length`:
- `FlipPullDir`:
- `FlipDir`:
- `TrimAndSew`:
- `Angle`:
- `CoordInput`:
- `X`:
- `Y`:
- `Z`:

## VBA Syntax

See [FeatureManager::InsertRuledSurfaceFromEdge](ms-its:sldworksapivb6.chm::/sldworks~FeatureManager~InsertRuledSurfaceFromEdge.html).

## See Also

[IFeatureManager Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IFeatureManager.html)
[IFeatureManager Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IFeatureManager_members.html)
