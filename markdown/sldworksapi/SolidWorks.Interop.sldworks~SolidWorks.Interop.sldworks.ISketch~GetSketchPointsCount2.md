---
title: "GetSketchPointsCount2 Method (ISketch)"
project: "SOLIDWORKS API Help"
interface: "ISketch"
member: "GetSketchPointsCount2"
kind: "method"
source: "sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISketch~GetSketchPointsCount2.html"
---

# GetSketchPointsCount2 Method (ISketch)

Gets the number of sketch points in this sketch.

## Syntax

### Visual Basic (Declaration)

```vb
Function GetSketchPointsCount2() As System.Integer
```

### Visual Basic (Usage)

```vb
Dim instance As ISketch
Dim value As System.Integer

value = instance.GetSketchPointsCount2()
```

### C#

```csharp
System.int GetSketchPointsCount2()
```

### C++/CLI

```cpp
System.int GetSketchPointsCount2();
```

**NOTE:** See [Differences Between Unmanaged C++ and C++/CLI Code](DifferencesBetweenUnManagedAndCPPCLI.htm).

### Return Value

Number of [sketch points](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.ISketchPoint.html) in this sketch

## VBA Syntax

See [Sketch::GetSketchPointsCount2](ms-its:sldworksapivb6.chm::/sldworks~Sketch~GetSketchPointsCount2.html).

## Examples

[Get Spline Points (C++)](Get_Spline_Points_Example_CPlusPlus_COM.htm)

## Remarks

Call this method before calling [ISketch::IGetSketchPoints2](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.ISketch~IGetSketchPoints2.html) to get the size of the array for that method.

## See Also

[ISketch Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISketch.html)
[ISketch Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISketch_members.html)
[ISketch::GetSketchPoints2 Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISketch~GetSketchPoints2.html)

## Availability

SOLIDWORKS 2006 SP2, Revision Number 14.2
