---
title: "GeodesicSketchOffset Method (IModelDocExtension)"
project: "SOLIDWORKS API Help"
interface: "IModelDocExtension"
member: "GeodesicSketchOffset"
kind: "method"
source: "sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelDocExtension~GeodesicSketchOffset.html"
---

# GeodesicSketchOffset Method (IModelDocExtension)

Creates a geodesic sketch offset along the curvature of a surface.

## Syntax

### Visual Basic (Declaration)

```vb
Function GeodesicSketchOffset( _
   ByVal Offset As System.Double, _
   ByVal Reverse As System.Boolean, _
   ByVal MakeConstruct As System.Boolean _
) As System.Boolean
```

### Visual Basic (Usage)

```vb
Dim instance As IModelDocExtension
Dim Offset As System.Double
Dim Reverse As System.Boolean
Dim MakeConstruct As System.Boolean
Dim value As System.Boolean

value = instance.GeodesicSketchOffset(Offset, Reverse, MakeConstruct)
```

### C#

```csharp
System.bool GeodesicSketchOffset(
   System.double Offset,
   System.bool Reverse,
   System.bool MakeConstruct
)
```

### C++/CLI

```cpp
System.bool GeodesicSketchOffset(
   System.double Offset,
   System.bool Reverse,
   System.bool MakeConstruct
)
```

**NOTE:** See [Differences Between Unmanaged C++ and C++/CLI Code](DifferencesBetweenUnManagedAndCPPCLI.htm).

### Parameters

- `Offset`: Offset distance
- `Reverse`: True to reverse the offset direction, false to not
- `MakeConstruct`: True to make sketch construction geometry after offsetting, false to not

### Return Value

True if the sketch offset is created, false if not

## VBA Syntax

See [ModelDocExtension::GeodesicSketchOffset](ms-its:sldworksapivb6.chm::/sldworks~ModelDocExtension~GeodesicSketchOffset.html).

## Remarks

To create a Euclidean sketch offset, use [IModelDocExtension::SketchOffsetOnSurface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelDocExtension~SketchOffsetOnSurface.html).

Before calling this method, call [IModelDocExtension::SelectByID2](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelDocExtension~SelectByID2.html) for each edge to offset and set Append to true and Mark to 1.

After calling this method, call [ISketchManager::InsertSketch](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.ISketchManager~InsertSketch.html) to rebuild the model with the 3D sketch.

## See Also

[IModelDocExtension Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelDocExtension.html)
[IModelDocExtension Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelDocExtension_members.html)
[ISketchManager::SketchOffset2 Method ()](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISketchManager~SketchOffset2.html)
[IModelDoc2::SketchOffsetEdges Method ()](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelDoc2~SketchOffsetEdges.html)
[IModelDoc2::SketchOffsetEntities2 Method ()](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelDoc2~SketchOffsetEntities2.html)

## Availability

SOLIDWORKS 2019 FCS, Revision Number 27.0
