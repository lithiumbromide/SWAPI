---
title: "IGetSketchContours Method (ISketch)"
project: "SOLIDWORKS API Help"
interface: "ISketch"
member: "IGetSketchContours"
kind: "method"
source: "sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISketch~IGetSketchContours.html"
---

# IGetSketchContours Method (ISketch)

Gets the sketch contours in this sketch.

## Syntax

### Visual Basic (Declaration)

```vb
Function IGetSketchContours( _
   ByVal Count As System.Integer _
) As SketchContour
```

### Visual Basic (Usage)

```vb
Dim instance As ISketch
Dim Count As System.Integer
Dim value As SketchContour

value = instance.IGetSketchContours(Count)
```

### C#

```csharp
SketchContour IGetSketchContours(
   System.int Count
)
```

### C++/CLI

```cpp
SketchContour^ IGetSketchContours(
   System.int Count
)
```

**NOTE:** See [Differences Between Unmanaged C++ and C++/CLI Code](DifferencesBetweenUnManagedAndCPPCLI.htm).

### Parameters

- `Count`: Number of sketch contours

### Return Value

- in-process, unmanaged C++: Pointer to an array of [sketch contours](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.ISketchContour.html)

VBA, VB.NET, C#, and C++/CLI: Not supported

See [In-process Methods](sldworksapiprogguide.chm::/OVERVIEW/In-process_Methods.htm) for details about this type of method.

## Remarks

Call [ISketch::GetSketchContourCount](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.ISketch~GetSketchContourCount.html) before calling this method to get Count.

This method works even if the sketch is suppressed.

## See Also

[ISketch Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISketch.html)
[ISketch Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISketch_members.html)
[ISketch::GetSketchContours Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISketch~GetSketchContours.html)

## Availability

SOLIDWORKS 2009 FCS, Revision Number 17.0
