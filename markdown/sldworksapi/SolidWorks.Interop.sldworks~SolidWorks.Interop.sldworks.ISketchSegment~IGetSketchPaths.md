---
title: "IGetSketchPaths Method (ISketchSegment)"
project: "SOLIDWORKS API Help"
interface: "ISketchSegment"
member: "IGetSketchPaths"
kind: "method"
source: "sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISketchSegment~IGetSketchPaths.html"
---

# IGetSketchPaths Method (ISketchSegment)

Gets the sketch paths in this sketch segment.

## Syntax

### Visual Basic (Declaration)

```vb
Function IGetSketchPaths( _
   ByVal Count As System.Integer _
) As SketchPath
```

### Visual Basic (Usage)

```vb
Dim instance As ISketchSegment
Dim Count As System.Integer
Dim value As SketchPath

value = instance.IGetSketchPaths(Count)
```

### C#

```csharp
SketchPath IGetSketchPaths(
   System.int Count
)
```

### C++/CLI

```cpp
SketchPath^ IGetSketchPaths(
   System.int Count
)
```

**NOTE:** See [Differences Between Unmanaged C++ and C++/CLI Code](DifferencesBetweenUnManagedAndCPPCLI.htm).

### Parameters

- `Count`: Number of sketch paths

### Return Value

- in-process, unmanaged C++: Pointer to an array of [sketch paths](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.ISketchPath.html)

VBA, VB.NET, C#, and C++/CLI: Not supported

See [In-process Methods](sldworksapiprogguide.chm::/OVERVIEW/In-process_Methods.htm) for details about this type of method.

## Remarks

Before calling this method, call [ISketchSegment::GetSketchPathCount](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.ISketchSegment~GetSketchPathCount.html) to get the value of Count.

## See Also

[ISketchSegment Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISketchSegment.html)
[ISketchSegment Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISketchSegment_members.html)
[ISketchSegment::GetSketchPaths Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISketchSegment~GetSketchPaths.html)

## Availability

SOLIDWORKS 2008 FCS, Revision Number 16.0
