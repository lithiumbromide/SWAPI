---
title: "GetCoords Method (ISketchPoint)"
project: "SOLIDWORKS API Help"
interface: "ISketchPoint"
member: "GetCoords"
kind: "method"
source: "sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISketchPoint~GetCoords.html"
---

# GetCoords Method (ISketchPoint)

Gets the x coordinate of the sketch point.

## Syntax

### Visual Basic (Declaration)

```vb
Function GetCoords() As System.Double
```

### Visual Basic (Usage)

```vb
Dim instance As ISketchPoint
Dim value As System.Double

value = instance.GetCoords()
```

### C#

```csharp
System.double GetCoords()
```

### C++/CLI

```cpp
System.double GetCoords();
```

**NOTE:** See [Differences Between Unmanaged C++ and C++/CLI Code](DifferencesBetweenUnManagedAndCPPCLI.htm).

### Return Value

x coordinate of the sketch point

## VBA Syntax

See [SketchPoint::GetCoords](ms-its:sldworksapivb6.chm::/sldworks~SketchPoint~GetCoords.html).

## Examples

[Get Sketch Points (VBA)](Get_Sketch_Points_Example_VB.htm)

## See Also

[ISketchPoint Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISketchPoint.html)
[ISketchPoint Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISketchPoint_members.html)
[ISketchPoint::X Property](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISketchPoint~X.html)
[ISketchPoint::Y Property](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISketchPoint~Y.html)
[ISketchPoint::Z Property](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISketchPoint~Z.html)
[ISketchPoint::SetCoords Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISketchPoint~SetCoords.html)

## Availability

SOLIDWORKS 99, datecode 1999207
