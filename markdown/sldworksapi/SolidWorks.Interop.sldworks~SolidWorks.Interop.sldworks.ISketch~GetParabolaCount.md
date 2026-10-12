---
title: "GetParabolaCount Method (ISketch)"
project: "SOLIDWORKS API Help"
interface: "ISketch"
member: "GetParabolaCount"
kind: "method"
source: "sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISketch~GetParabolaCount.html"
---

# GetParabolaCount Method (ISketch)

Gets the number of parabolas in the sketch.

## Syntax

### Visual Basic (Declaration)

```vb
Function GetParabolaCount() As System.Integer
```

### Visual Basic (Usage)

```vb
Dim instance As ISketch
Dim value As System.Integer

value = instance.GetParabolaCount()
```

### C#

```csharp
System.int GetParabolaCount()
```

### C++/CLI

```cpp
System.int GetParabolaCount();
```

**NOTE:** See [Differences Between Unmanaged C++ and C++/CLI Code](DifferencesBetweenUnManagedAndCPPCLI.htm).

### Return Value

Number of parabolas in the sketch

## VBA Syntax

See [Sketch::GetParabolaCount](ms-its:sldworksapivb6.chm::/sldworks~Sketch~GetParabolaCount.html).

## Examples

[Get Parabolas in Sketch (VBA)](Get_Parabolas_in_Sketch_Example_VB.htm)
[Get Polylines Information (VBA)](Get_Polylines_Information_Example_VB.htm)

## Remarks

Call this method before calling [ISketch::IGetParabolas2](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.ISketch~IGetParabolas2.html) to determine the size of the array for that method.

## See Also

[ISketch Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISketch.html)
[ISketch Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISketch_members.html)
[ISketch::GetParabolas2 Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISketch~GetParabolas2.html)
[ISketchParabola Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISketchParabola.html)
