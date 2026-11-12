---
title: "CreateRuledSurfaceFromEdge Method (IModeler)"
project: "SOLIDWORKS API Help"
interface: "IModeler"
member: "CreateRuledSurfaceFromEdge"
kind: "method"
source: "sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModeler~CreateRuledSurfaceFromEdge.html"
---

# CreateRuledSurfaceFromEdge Method (IModeler)

Creates a ruled surface using the specified edges and returns a surface body.

## Syntax

### Visual Basic (Declaration)

```vb
Function CreateRuledSurfaceFromEdge( _
   ByVal ModDoc As ModelDoc2, _
   ByVal Edges As System.Object, _
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
   ByVal BConnectSurface As System.Boolean, _
   ByRef RuledSurface As System.Object _
) As System.Integer
```

### Visual Basic (Usage)

```vb
Dim instance As IModeler
Dim ModDoc As ModelDoc2
Dim Edges As System.Object
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
Dim RuledSurface As System.Object
Dim value As System.Integer

value = instance.CreateRuledSurfaceFromEdge(ModDoc, Edges, Type, Length, FlipPullDir, FlipDir, TrimAndSew, Angle, CoordInput, X, Y, Z, BConnectSurface, RuledSurface)
```

### C#

```csharp
System.int CreateRuledSurfaceFromEdge(
   ModelDoc2 ModDoc,
   System.object Edges,
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
   System.bool BConnectSurface,
   out System.object RuledSurface
)
```

### C++/CLI

```cpp
System.int CreateRuledSurfaceFromEdge(
   ModelDoc2^ ModDoc,
   System.Object^ Edges,
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
   System.bool BConnectSurface,
   [Out] System.Object^ RuledSurface
)
```

**NOTE:** See [Differences Between Unmanaged C++ and C++/CLI Code](DifferencesBetweenUnManagedAndCPPCLI.htm).

### Parameters

- `ModDoc`: [Model document](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.IModelDoc2.html) in which to create surface body
- `Edges`: Array of edges on which to create ruled surface

  **NOTE:** Currently only a single edge is supported.
- `Type`: 0 = Tangent to Surface

  1 = Normal to Surface

  2 = Tapered to Vector

  3 = Perpendicular to Vector

  4 = Sweep
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
- `RuledSurface`: Ruled surface [body](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.IBody2.html)

### Return Value

0 if ruled surface body created, -1 if not

## VBA Syntax

See [Modeler::CreateRuledSurfaceFromEdge](ms-its:sldworksapivb6.chm::/sldworks~Modeler~CreateRuledSurfaceFromEdge.html).

## Examples

[Create Ruled Surface Body From Edge (VBA)](Create_Ruled_Surface_From_Edge_Example_VB.htm)

## Remarks

This method returns a surface body, unlike [IFeatureManager::InsertRuledSurfaceFromEdge2](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.IFeatureManager~InsertRuledSurfaceFromEdge2.html), which returns a feature.

If you [select](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.IModelDocExtension~SelectByID2.html) an edge with a selection mark of 4, the default face is used. If you select an edge with a selection mark of 6, the alternate face is used.

## See Also

[IModeler Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModeler.html)
[IModeler Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModeler_members.html)
[IModeler::ICreateRuledSurfaceFromEdge Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModeler~ICreateRuledSurfaceFromEdge.html)
[IModeler::ICreateRuledSurface Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModeler~ICreateRuledSurface.html)
[IModeler::CreateRuledSurface Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModeler~CreateRuledSurface.html)

## Availability

SOLIDWORKS 2009 FCS, Revision Number 17.0
