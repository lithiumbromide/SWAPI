---
title: "IsClosed Method (ISketchContour)"
project: "SOLIDWORKS API Help"
interface: "ISketchContour"
member: "IsClosed"
kind: "method"
source: "sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISketchContour~IsClosed.html"
---

# IsClosed Method (ISketchContour)

Gets whether this sketch contour is open or closed.

## Syntax

### Visual Basic (Declaration)

```vb
Function IsClosed() As System.Boolean
```

### Visual Basic (Usage)

```vb
Dim instance As ISketchContour
Dim value As System.Boolean

value = instance.IsClosed()
```

### C#

```csharp
System.bool IsClosed()
```

### C++/CLI

```cpp
System.bool IsClosed();
```

**NOTE:** See [Differences Between Unmanaged C++ and C++/CLI Code](DifferencesBetweenUnManagedAndCPPCLI.htm).

### Return Value

True if the sketch contour is open, false if closed

## VBA Syntax

See [SketchContour::IsClosed](ms-its:sldworksapivb6.chm::/sldworks~SketchContour~IsClosed.html).

## Examples

[Get Sketch Contours (VBA)](Get_Sketch_Contours_Example_VB.htm)
[Create Extrude Feature Using Sketch Contours (C#)](Create_Extrude_Feature_Using_Sketch_Contours_Example_CSharp.htm)
[Create Extrude Feature Using Sketch Contours (VB.NET)](Create_Extrude_Feature_Using_Sketch_Contours_Example_VBNET.htm)
[Create Extrude Feature Using Sketch Contours (VBA)](Create_Extrude_Feature_Using_Sketch_Contours_Example_VB.htm)

## Remarks

This method works even if the sketch is suppressed.

## See Also

[ISketchContour Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISketchContour.html)
[ISketchContour Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISketchContour_members.html)

## Availability

SOLIDWORKS 2009 FCS, Revision Number 17.0
