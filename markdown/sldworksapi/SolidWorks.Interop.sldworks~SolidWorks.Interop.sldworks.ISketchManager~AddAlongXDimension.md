---
title: "AddAlongXDimension Method (ISketchManager)"
project: "SOLIDWORKS API Help"
interface: "ISketchManager"
member: "AddAlongXDimension"
kind: "method"
source: "sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISketchManager~AddAlongXDimension.html"
---

# AddAlongXDimension Method (ISketchManager)

Projects and displays along the x axis a dimension between selected points in a 3D sketch.

## Syntax

### Visual Basic (Declaration)

```vb
Function AddAlongXDimension( _
   ByVal X As System.Double, _
   ByVal Y As System.Double, _
   ByVal Z As System.Double _
) As DisplayDimension
```

### Visual Basic (Usage)

```vb
Dim instance As ISketchManager
Dim X As System.Double
Dim Y As System.Double
Dim Z As System.Double
Dim value As DisplayDimension

value = instance.AddAlongXDimension(X, Y, Z)
```

### C#

```csharp
DisplayDimension AddAlongXDimension(
   System.double X,
   System.double Y,
   System.double Z
)
```

### C++/CLI

```cpp
DisplayDimension^ AddAlongXDimension(
   System.double X,
   System.double Y,
   System.double Z
)
```

**NOTE:** See [Differences Between Unmanaged C++ and C++/CLI Code](DifferencesBetweenUnManagedAndCPPCLI.htm).

### Parameters

- `X`: X coordinate of dimension text placement
- `Y`: Y coordinate of dimension text placement
- `Z`: Z coordinate of dimension text placement

### Return Value

[IDisplayDimension](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.IDisplayDimension.html)

## VBA Syntax

See [SketchManager::AddAlongXDimension](ms-its:sldworksapivb6.chm::/Sldworks~SketchManager~AddAlongXDimension.html).

## Examples

[Add Along X Dimension to 3D Sketch (VBA)](Add_Along_X_Dimension_To_3D_Sketch_Example_VB.htm)
[Add Along X Dimension to 3D Sketch (VB.NET)](Add_Along_X_Dimension_To_3D_Sketch_Example_VBNET.htm)
[Add Along X Dimension to 3D Sketch (C#)](Add_Along_X_Dimension_To_3D_Sketch_Example_CSharp.htm)

## Remarks

This method works only for 3D sketches in edit mode, and the display dimension is visible only when the sketch is in edit mode.

## See Also

[ISketchManager Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISketchManager.html)
[ISketchManager Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISketchManager_members.html)
[ISketchManager::FullyDefineSketch Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISketchManager~FullyDefineSketch.html)
[ISketchManager::AddAlongYDimension Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISketchManager~AddAlongYDimension.html)
[ISketchManager::AddAlongZDimension Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISketchManager~AddAlongZDimension.html)

## Availability

SOLIDWORKS 2010 FCS, Revision Number 18.0
