---
title: "IGetSketchSegments Method (ISketchContour)"
project: "SOLIDWORKS API Help"
interface: "ISketchContour"
member: "IGetSketchSegments"
kind: "method"
source: "sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISketchContour~IGetSketchSegments.html"
---

# IGetSketchSegments Method (ISketchContour)

Gets the sketch segments for this sketch contour.

## Syntax

### Visual Basic (Declaration)

```vb
Function IGetSketchSegments( _
   ByVal Count As System.Integer _
) As SketchSegment
```

### Visual Basic (Usage)

```vb
Dim instance As ISketchContour
Dim Count As System.Integer
Dim value As SketchSegment

value = instance.IGetSketchSegments(Count)
```

### C#

```csharp
SketchSegment IGetSketchSegments(
   System.int Count
)
```

### C++/CLI

```cpp
SketchSegment^ IGetSketchSegments(
   System.int Count
)
```

**NOTE:** See [Differences Between Unmanaged C++ and C++/CLI Code](DifferencesBetweenUnManagedAndCPPCLI.htm).

### Parameters

- `Count`: Number of sketch segments

### Return Value

- in-process, unmanaged C++: Pointer to an array of [sketch segments](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.ISketchSegment.html)

VBA, VB.NET, C#, and C++/CLI: Not supported

See [In-process Methods](sldworksapiprogguide.chm::/OVERVIEW/In-process_Methods.htm) for details about this type of method.

## Remarks

Before calling this method, call [ISketchContour::GetSketchSegmentsCount](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.ISketchContour~GetSketchSegmentsCount.html) to get the value for Count.

## See Also

[ISketchContour Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISketchContour.html)
[ISketchContour Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISketchContour_members.html)
[ISketchContour::GetSketchSegments Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISketchContour~GetSketchSegments.html)

## Availability

SOLIDWORKS 2003 FCS, Revision Number 11.0
