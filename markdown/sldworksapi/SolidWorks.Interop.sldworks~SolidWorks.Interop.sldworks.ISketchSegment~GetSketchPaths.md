---
title: "GetSketchPaths Method (ISketchSegment)"
project: "SOLIDWORKS API Help"
interface: "ISketchSegment"
member: "GetSketchPaths"
kind: "method"
source: "sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISketchSegment~GetSketchPaths.html"
---

# GetSketchPaths Method (ISketchSegment)

Gets the sketch paths for this sketch segment.

## Syntax

### Visual Basic (Declaration)

```vb
Function GetSketchPaths() As System.Object
```

### Visual Basic (Usage)

```vb
Dim instance As ISketchSegment
Dim value As System.Object

value = instance.GetSketchPaths()
```

### C#

```csharp
System.object GetSketchPaths()
```

### C++/CLI

```cpp
System.Object^ GetSketchPaths();
```

**NOTE:** See [Differences Between Unmanaged C++ and C++/CLI Code](DifferencesBetweenUnManagedAndCPPCLI.htm).

### Return Value

Array of [sketch paths](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.ISketchPath.html)

## VBA Syntax

See [SketchSegment::GetSketchPaths](ms-its:sldworksapivb6.chm::/Sldworks~SketchSegment~GetSketchPaths.html).

## See Also

[ISketchSegment Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISketchSegment.html)
[ISketchSegment Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISketchSegment_members.html)
[ISketchSegment::GetSketchSegmentCount Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISketchPath~GetSketchSegmentCount.html)
[ISketchSegment::IGetSketchSegments Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISketchPath~IGetSketchSegments.html)

## Availability

SOLIDWORKS 2008 FCS, Revision Number 16.0
