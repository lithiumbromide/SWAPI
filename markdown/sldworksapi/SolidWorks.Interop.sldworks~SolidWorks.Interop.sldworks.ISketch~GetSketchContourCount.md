---
title: "GetSketchContourCount Method (ISketch)"
project: "SOLIDWORKS API Help"
interface: "ISketch"
member: "GetSketchContourCount"
kind: "method"
source: "sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISketch~GetSketchContourCount.html"
---

# GetSketchContourCount Method (ISketch)

Gets the number of sketch contours in this sketch.

## Syntax

### Visual Basic (Declaration)

```vb
Function GetSketchContourCount() As System.Integer
```

### Visual Basic (Usage)

```vb
Dim instance As ISketch
Dim value As System.Integer

value = instance.GetSketchContourCount()
```

### C#

```csharp
System.int GetSketchContourCount()
```

### C++/CLI

```cpp
System.int GetSketchContourCount();
```

**NOTE:** See [Differences Between Unmanaged C++ and C++/CLI Code](DifferencesBetweenUnManagedAndCPPCLI.htm).

### Return Value

Number of sketch contours

## VBA Syntax

See [Sketch::GetSketchContourCount](ms-its:sldworksapivb6.chm::/sldworks~Sketch~GetSketchContourCount.html).

## Remarks

Call this method before calling [ISketch::IGetSketchContours](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.ISketch~IGetSketchContours.html) to get the size of the array for that method.

This method works even if the sketch is suppressed.

## See Also

[ISketch Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISketch.html)
[ISketch Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISketch_members.html)
[ISketch::GetSketchContours Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISketch~GetSketchContours.html)

## Availability

SOLIDWORKS 2009 FCS, Revision Number 17.0
