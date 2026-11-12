---
title: "GetRotationDir Method (ISketchEllipse)"
project: "SOLIDWORKS API Help"
interface: "ISketchEllipse"
member: "GetRotationDir"
kind: "method"
source: "sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISketchEllipse~GetRotationDir.html"
---

# GetRotationDir Method (ISketchEllipse)

Gets the rotation direction for this sketch ellipse segment.

## Syntax

### Visual Basic (Declaration)

```vb
Function GetRotationDir() As System.Integer
```

### Visual Basic (Usage)

```vb
Dim instance As ISketchEllipse
Dim value As System.Integer

value = instance.GetRotationDir()
```

### C#

```csharp
System.int GetRotationDir()
```

### C++/CLI

```cpp
System.int GetRotationDir();
```

**NOTE:** See [Differences Between Unmanaged C++ and C++/CLI Code](DifferencesBetweenUnManagedAndCPPCLI.htm).

### Return Value

Rotation direction (counterclockwise = 1, clockwise = -1)

## VBA Syntax

See [SketchEllipse::GetRotationDir](ms-its:sldworksapivb6.chm::/sldworks~SketchEllipse~GetRotationDir.html).

## Remarks

This method determines the direction (counterclockwise or clockwise) that the sketch entity proceeds around the ellipse, beginning at its start point and ending at its ending point if the sketch entity is not a complete ellipse.

## See Also

[ISketchEllipse Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISketchEllipse.html)
[ISketchEllipse Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISketchEllipse_members.html)

## Availability

SOLIDWORKS 2007 FCS, Revision Number 15.0
