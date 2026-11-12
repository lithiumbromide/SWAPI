---
title: "IGetSketchSegments Method (ISketchPath)"
project: "SOLIDWORKS API Help"
interface: "ISketchPath"
member: "IGetSketchSegments"
kind: "method"
source: "sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISketchPath~IGetSketchSegments.html"
---

# IGetSketchSegments Method (ISketchPath)

Gets the sketch segments in this sketch path.

## Syntax

### Visual Basic (Declaration)

```vb
Function IGetSketchSegments( _
   ByVal Count As System.Integer _
) As SketchSegment
```

### Visual Basic (Usage)

```vb
Dim instance As ISketchPath
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

Before calling this method, call [ISketchPath::GetSketchSegmentCount](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.ISketchPath~GetSketchSegmentCount.html) to get the value of Count.

## See Also

[ISketchPath Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISketchPath.html)
[ISketchPath Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISketchPath_members.html)
[ISketchPath::GetSketchSegments Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISketchPath~GetSketchSegments.html)

## Availability

SOLIDWORKS 2007 SP4, Revision Number 15.4
