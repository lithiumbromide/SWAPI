---
title: "SketchOffsetOnSurface Method (IModelDocExtension)"
project: "SOLIDWORKS API Help"
interface: "IModelDocExtension"
member: "SketchOffsetOnSurface"
kind: "method"
source: "sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelDocExtension~SketchOffsetOnSurface.html"
---

# SketchOffsetOnSurface Method (IModelDocExtension)

Creates a Euclidean sketch offset from selected edges of a face or surface.

## Syntax

### Visual Basic (Declaration)

```vb
Function SketchOffsetOnSurface( _
   ByVal Offset As System.Double, _
   ByVal Reverse As System.Boolean, _
   ByVal UseFront As System.Boolean, _
   ByVal MakeConstruct As System.Boolean _
) As System.Boolean
```

### Visual Basic (Usage)

```vb
Dim instance As IModelDocExtension
Dim Offset As System.Double
Dim Reverse As System.Boolean
Dim UseFront As System.Boolean
Dim MakeConstruct As System.Boolean
Dim value As System.Boolean

value = instance.SketchOffsetOnSurface(Offset, Reverse, UseFront, MakeConstruct)
```

### C#

```csharp
System.bool SketchOffsetOnSurface(
   System.double Offset,
   System.bool Reverse,
   System.bool UseFront,
   System.bool MakeConstruct
)
```

### C++/CLI

```cpp
System.bool SketchOffsetOnSurface(
   System.double Offset,
   System.bool Reverse,
   System.bool UseFront,
   System.bool MakeConstruct
)
```

**NOTE:** See [Differences Between Unmanaged C++ and C++/CLI Code](DifferencesBetweenUnManagedAndCPPCLI.htm).

### Parameters

- `Offset`: Offset distance
- `Reverse`: True to reverse the 3D sketch, false to not
- `UseFront`: Although not currently used, must be set to true
- `MakeConstruct`: True to make the 3D sketch construction geometry after offsetting, false to not

### Return Value

True if the 3D sketch is created, false if not

## VBA Syntax

See [ModelDocExtension::SketchOffsetOnSurface](ms-its:sldworksapivb6.chm::/sldworks~ModelDocExtension~SketchOffsetOnSurface.html).

## Examples

[Offset Edges to Create 3D Sketch (C#)](Offset_Edges_to_Create_3D_Sketch_on_Surface_Example_CSharp.htm)
[Offset Edges to Create 3D Sketch (VB.NET)](Offset_Edges_to_Create_3D_Sketch_on_Surface_Example_VBNET.htm)
[Offset Edges to Create 3D Sketch (VBA)](Offset_Edges_to_Create_3D_Sketch_on_Surface_Example_VB.htm)

## Remarks

To create a geodesic sketch offset along the curvature of a surface, use [IModelDocExtension::GeodesicSketchOffset](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelDocExtension~GeodesicSketchOffset.html).

Before calling this method, call [IModelDocExtension::SelectByID2](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelDocExtension~SelectByID2.html) for each edge to offset and set Append to true and Mark to 1.

After calling this method, call [ISketchManager::InsertSketch](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.ISketchManager~InsertSketch.html) to rebuild the model with the 3D sketch.

## See Also

[IModelDocExtension Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelDocExtension.html)
[IModelDocExtension Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelDocExtension_members.html)
[ISketchManager::SketchOffset2 Method ()](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISketchManager~SketchOffset2.html)
[IModelDoc2::SketchOffsetEdges Method ()](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelDoc2~SketchOffsetEdges.html)
[IModelDoc2::SketchOffsetEntities2 Method ()](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelDoc2~SketchOffsetEntities2.html)

## Availability

SOLIDWORKS 2017 FCS, Revision Number 25.0
