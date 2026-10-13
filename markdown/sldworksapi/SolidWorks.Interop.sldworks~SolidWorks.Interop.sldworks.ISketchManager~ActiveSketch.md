---
title: "ActiveSketch Property (ISketchManager)"
project: "SOLIDWORKS API Help"
interface: "ISketchManager"
member: "ActiveSketch"
kind: "property"
source: "sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISketchManager~ActiveSketch.html"
---

# ActiveSketch Property (ISketchManager)

Gets the active sketch.

## Syntax

### Visual Basic (Declaration)

```vb
ReadOnly Property ActiveSketch As Sketch
```

### Visual Basic (Usage)

```vb
Dim instance As ISketchManager
Dim value As Sketch

value = instance.ActiveSketch
```

### C#

```csharp
Sketch ActiveSketch {get;}
```

### C++/CLI

```cpp
property Sketch^ ActiveSketch {
   Sketch^ get();
}
```

**NOTE:** See [Differences Between Unmanaged C++ and C++/CLI Code](DifferencesBetweenUnManagedAndCPPCLI.htm).

### Property Value

Active [sketch](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.ISketch.html)

## VBA Syntax

See [SketchManager::ActiveSketch](ms-its:sldworksapivb6.chm::/Sldworks~SketchManager~ActiveSketch.html).

## Examples

[Constrain Sketch (VBA)](Constrain_Sketch_Example_VB.htm)
[Create 3D Sketch Plane (C#)](Create_3D_Sketch_Plane_Example_CSharp.htm)
[Create 3D Sketch Plane (VB.NET)](Create_3D_Sketch_Plane_Example_VBNET.htm)
[Create 3D Sketch Plane (VBA)](Create_3D_Sketch_Plane_Example_VB.htm)
[Rotate and Copy 3D Sketch About Coordinates (C#)](Rotate_and_Copy_3D_Sketch_About_Coordinates_Example_CSharp.htm)
[Rotate and Copy 3D Sketch About Coordinates (VB.NET)](Rotate_and_Copy_3D_Sketch_About_Coordinates_Example_VBNET.htm)
[Rotate and Copy 3D Sketch About Coordinates (VBA)](Rotate_and_Copy_3D_Sketch_About_Coordinates_Example_VB.htm)

## See Also

[ISketchManager Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISketchManager.html)
[ISketchManager Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISketchManager_members.html)

## Availability

SOLIDWORKS 2008 FCS, Revision Number 16.0
