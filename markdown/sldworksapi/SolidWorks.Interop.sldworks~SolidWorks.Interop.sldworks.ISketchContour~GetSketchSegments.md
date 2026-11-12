---
title: "GetSketchSegments Method (ISketchContour)"
project: "SOLIDWORKS API Help"
interface: "ISketchContour"
member: "GetSketchSegments"
kind: "method"
source: "sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISketchContour~GetSketchSegments.html"
---

# GetSketchSegments Method (ISketchContour)

Gets the sketch segments for this sketch contour.

## Syntax

### Visual Basic (Declaration)

```vb
Function GetSketchSegments() As System.Object
```

### Visual Basic (Usage)

```vb
Dim instance As ISketchContour
Dim value As System.Object

value = instance.GetSketchSegments()
```

### C#

```csharp
System.object GetSketchSegments()
```

### C++/CLI

```cpp
System.Object^ GetSketchSegments();
```

**NOTE:** See [Differences Between Unmanaged C++ and C++/CLI Code](DifferencesBetweenUnManagedAndCPPCLI.htm).

### Return Value

Array of [sketch segments](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.ISketchSegment.html)

## VBA Syntax

See [SketchContour::GetSketchSegments](ms-its:sldworksapivb6.chm::/sldworks~SketchContour~GetSketchSegments.html).

## Examples

[Get Sketch Contours (VBA)](Get_Sketch_Contours_Example_VB.htm)
[Get Corresponding Objects in Assembly Component (C#)](Get_Corresponding_Objects_in_Assembly_Component_Example_CSharp.htm)
[Get Corresponding Objects in Assembly Component (VB.NET)](Get_Corresponding_Objects_in_Assembly_Component_Example_VBNET.htm)
[Get Corresponding Objects in Assembly Component (VBA)](Get_Corresponding_Objects_in_Assembly_Component_Example_VB.htm)

## See Also

[ISketchContour Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISketchContour.html)
[ISketchContour Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISketchContour_members.html)
[ISketchContour::GetSketchSegmentsCount Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISketchContour~GetSketchSegmentsCount.html)
[ISketchContour::IGetSketchSegments Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISketchContour~IGetSketchSegments.html)

## Availability

SOLIDWORKS 2003 FCS, Revision Number 11.0
