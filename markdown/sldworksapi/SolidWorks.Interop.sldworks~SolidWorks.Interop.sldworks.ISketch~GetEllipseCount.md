---
title: "GetEllipseCount Method (ISketch)"
project: "SOLIDWORKS API Help"
interface: "ISketch"
member: "GetEllipseCount"
kind: "method"
source: "sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISketch~GetEllipseCount.html"
---

# GetEllipseCount Method (ISketch)

Gets the number of ellipses in the sketch.

## Syntax

### Visual Basic (Declaration)

```vb
Function GetEllipseCount() As System.Integer
```

### Visual Basic (Usage)

```vb
Dim instance As ISketch
Dim value As System.Integer

value = instance.GetEllipseCount()
```

### C#

```csharp
System.int GetEllipseCount()
```

### C++/CLI

```cpp
System.int GetEllipseCount();
```

**NOTE:** See [Differences Between Unmanaged C++ and C++/CLI Code](DifferencesBetweenUnManagedAndCPPCLI.htm).

### Return Value

Number of ellipses in the sketch

## VBA Syntax

See [Sketch::GetEllipseCount](ms-its:sldworksapivb6.chm::/sldworks~Sketch~GetEllipseCount.html).

## Examples

[Get Polylines Information (VBA)](Get_Polylines_Information_Example_VB.htm)

## Remarks

Call this method before calling [ISketch::GetEllipses3](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.ISketch~GetEllipses3.html) to determine the size of the array for that method.

## See Also

[ISketch Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISketch.html)
[ISketch Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISketch_members.html)
[ISketch::GetEllipses3 Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISketch~GetEllipses3.html)
