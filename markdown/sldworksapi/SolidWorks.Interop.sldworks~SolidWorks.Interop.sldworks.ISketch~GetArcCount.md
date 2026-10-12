---
title: "GetArcCount Method (ISketch)"
project: "SOLIDWORKS API Help"
interface: "ISketch"
member: "GetArcCount"
kind: "method"
source: "sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISketch~GetArcCount.html"
---

# GetArcCount Method (ISketch)

Gets the number of arcs in the sketch.

## Syntax

### Visual Basic (Declaration)

```vb
Function GetArcCount() As System.Integer
```

### Visual Basic (Usage)

```vb
Dim instance As ISketch
Dim value As System.Integer

value = instance.GetArcCount()
```

### C#

```csharp
System.int GetArcCount()
```

### C++/CLI

```cpp
System.int GetArcCount();
```

**NOTE:** See [Differences Between Unmanaged C++ and C++/CLI Code](DifferencesBetweenUnManagedAndCPPCLI.htm).

### Return Value

Number of arcs in the sketch

## VBA Syntax

See [Sketch::GetArcCount](ms-its:sldworksapivb6.chm::/sldworks~Sketch~GetArcCount.html).

## Examples

[Get Arcs in Sketch (VBA)](Get_Arcs_in_Sketch_Example_VB.htm)
[Get Polylines Information (VBA)](Get_Polylines_Information_Example_VB.htm)

## Remarks

Call this method before [ISketch::IGetArcs2](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.ISketch~IGetArcs2.html) to determine the size of the array for that method.

## See Also

[ISketch Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISketch.html)
[ISketch Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISketch_members.html)
[ISketch::GetArcs2 Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISketch~GetArcs2.html)
[ISketchArc Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISketchArc.html)
