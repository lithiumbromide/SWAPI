---
title: "GetRotationDir Method (ISketchArc)"
project: "SOLIDWORKS API Help"
interface: "ISketchArc"
member: "GetRotationDir"
kind: "method"
source: "sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISketchArc~GetRotationDir.html"
---

# GetRotationDir Method (ISketchArc)

Gets the rotation direction of this sketch arc.

## Syntax

### Visual Basic (Declaration)

```vb
Function GetRotationDir() As System.Integer
```

### Visual Basic (Usage)

```vb
Dim instance As ISketchArc
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

Rotation direction with respect to the normal of the arc's sketch plane (counterclockwise = 1, clockwise = -1) (see **Remarks**)

## VBA Syntax

See [SketchArc::GetRotationDir](ms-its:sldworksapivb6.chm::/sldworks~SketchArc~GetRotationDir.html).

## Examples

See the [ISketchArc](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISketchArc.html) examples.

## Examples

[Get All Elements in Sketch (VBA)](Get_All_Elements_of_Sketch_Example_VB.htm)

## Remarks

This method determines the direction that the sketch proceeds around this arc, beginning at the arc's start point and ending at the arc's end point. The direction is with respect to the normal of the arc's sketch plane and not with respect to the viewer.

| If the normal to the arc's sketch plane is... | And the normal to the arc is... | And this method returns... | It means that... |
| --- | --- | --- | --- |
| (0, 0, -1) | (0, 0, 1) | 1 (counterclockwise) | With respect to its sketch plane's normal (from behind the screen), the arc travels counterclockwise from its start point to its end point. Note that from the perspective of the viewer (in front of the screen), the arc travels clockwise from its start point to its end point. |

## See Also

[ISketchArc Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISketchArc.html)
[ISketchArc Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISketchArc_members.html)

## Availability

SOLIDWORKS 99, datecode 1999207
