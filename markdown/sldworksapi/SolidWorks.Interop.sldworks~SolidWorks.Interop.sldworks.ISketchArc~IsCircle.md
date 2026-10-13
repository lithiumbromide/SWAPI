---
title: "IsCircle Method (ISketchArc)"
project: "SOLIDWORKS API Help"
interface: "ISketchArc"
member: "IsCircle"
kind: "method"
source: "sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISketchArc~IsCircle.html"
---

# IsCircle Method (ISketchArc)

Gets whether the sketch arc is a complete circle or a partial arc.

## Syntax

### Visual Basic (Declaration)

```vb
Function IsCircle() As System.Integer
```

### Visual Basic (Usage)

```vb
Dim instance As ISketchArc
Dim value As System.Integer

value = instance.IsCircle()
```

### C#

```csharp
System.int IsCircle()
```

### C++/CLI

```cpp
System.int IsCircle();
```

**NOTE:** See [Differences Between Unmanaged C++ and C++/CLI Code](DifferencesBetweenUnManagedAndCPPCLI.htm).

### Return Value

1 if a complete circle, 0 if a partial arc

## VBA Syntax

See [SketchArc::IsCircle](ms-its:sldworksapivb6.chm::/sldworks~SketchArc~IsCircle.html).

## Examples

See the [ISketchArc](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISketchArc.html) examples.

## Examples

[Get All Elements of Sketch (VBA)](Get_All_Elements_of_Sketch_Example_VB.htm)

## See Also

[ISketchArc Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISketchArc.html)
[ISketchArc Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISketchArc_members.html)

## Availability

SOLIDWORKS 99, datecode 1999207
