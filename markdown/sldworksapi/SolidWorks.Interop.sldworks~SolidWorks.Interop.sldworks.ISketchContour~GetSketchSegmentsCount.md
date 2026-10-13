---
title: "GetSketchSegmentsCount Method (ISketchContour)"
project: "SOLIDWORKS API Help"
interface: "ISketchContour"
member: "GetSketchSegmentsCount"
kind: "method"
source: "sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISketchContour~GetSketchSegmentsCount.html"
---

# GetSketchSegmentsCount Method (ISketchContour)

Gets the number of sketch segments for this sketch contour.

## Syntax

### Visual Basic (Declaration)

```vb
Function GetSketchSegmentsCount() As System.Integer
```

### Visual Basic (Usage)

```vb
Dim instance As ISketchContour
Dim value As System.Integer

value = instance.GetSketchSegmentsCount()
```

### C#

```csharp
System.int GetSketchSegmentsCount()
```

### C++/CLI

```cpp
System.int GetSketchSegmentsCount();
```

**NOTE:** See [Differences Between Unmanaged C++ and C++/CLI Code](DifferencesBetweenUnManagedAndCPPCLI.htm).

### Return Value

Number of sketch segments

## VBA Syntax

See [SketchContour::GetSketchSegmentsCount](ms-its:sldworksapivb6.chm::/sldworks~SketchContour~GetSketchSegmentsCount.html).

## Remarks

Call this method before calling [ISketchContour::IGetSketchSegments](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.ISketchContour~IGetSketchSegments.html) to get the size of the array for that method.

## See Also

[ISketchContour Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISketchContour.html)
[ISketchContour Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISketchContour_members.html)
[ISketchContour::GetSketchSegments Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISketchContour~GetSketchSegments.html)

## Availability

SOLIDWORKS 2003 FCS, Revision Number 11.0
