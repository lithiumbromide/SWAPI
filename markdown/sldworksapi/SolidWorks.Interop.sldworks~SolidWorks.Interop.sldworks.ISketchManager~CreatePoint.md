---
title: "CreatePoint Method (ISketchManager)"
project: "SOLIDWORKS API Help"
interface: "ISketchManager"
member: "CreatePoint"
kind: "method"
source: "sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISketchManager~CreatePoint.html"
---

# CreatePoint Method (ISketchManager)

Creates a sketch point in the active 2D or 3D sketch.

## Syntax

### Visual Basic (Declaration)

```vb
Function CreatePoint( _
   ByVal X As System.Double, _
   ByVal Y As System.Double, _
   ByVal Z As System.Double _
) As SketchPoint
```

### Visual Basic (Usage)

```vb
Dim instance As ISketchManager
Dim X As System.Double
Dim Y As System.Double
Dim Z As System.Double
Dim value As SketchPoint

value = instance.CreatePoint(X, Y, Z)
```

### C#

```csharp
SketchPoint CreatePoint(
   System.double X,
   System.double Y,
   System.double Z
)
```

### C++/CLI

```cpp
SketchPoint^ CreatePoint(
   System.double X,
   System.double Y,
   System.double Z
)
```

**NOTE:** See [Differences Between Unmanaged C++ and C++/CLI Code](DifferencesBetweenUnManagedAndCPPCLI.htm).

### Parameters

- `X`: X location of the point
- `Y`: Y location of the point
- `Z`: Z location of the point; ignored for 2D sketches

### Return Value

Newly created [sketch point](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.ISketchPoint.html)

## VBA Syntax

See [SketchManager::CreatePoint](ms-its:sldworksapivb6.chm::/Sldworks~SketchManager~CreatePoint.html).

## Examples

[Create Sketch Point (VBA)](Create_Sketch_Point_Example_VB.htm)
[Create Sketch Point (VB.NET)](Create_Sketch_Point_Example_VBNET.htm)
[Create Sketch Point (C#)](Create_Sketch_Point_Example_CSharp.htm)

## Remarks

This method creates a point in the active 2D or 3D sketch. If a sketch is not active, the point is not created and NULL is returned. Use [ISketchManager::ActiveSketch](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.ISketchManager~ActiveSketch.html) to check to see if the sketch is active.

[ISketchManager::AddToDB](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.ISketchManager~AddToDB.html) and [ISketchManager::DisplayWhenAdded](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.ISketchManager~DisplayWhenAdded.html) increase performance during entity creation by adding entities directly to the SOLIDWORKS database. ISketchManager::AddToDB also avoids inferencing.

## See Also

[ISketchManager Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISketchManager.html)
[ISketchManager Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISketchManager_members.html)

## Availability

SOLIDWORKS 2008 FCS, Revision Number 16.0
