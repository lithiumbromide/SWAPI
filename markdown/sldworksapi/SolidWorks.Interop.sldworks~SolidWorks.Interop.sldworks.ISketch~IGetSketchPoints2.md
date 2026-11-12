---
title: "IGetSketchPoints2 Method (ISketch)"
project: "SOLIDWORKS API Help"
interface: "ISketch"
member: "IGetSketchPoints2"
kind: "method"
source: "sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISketch~IGetSketchPoints2.html"
---

# IGetSketchPoints2 Method (ISketch)

Gets the sketch points in this sketch.

## Syntax

### Visual Basic (Declaration)

```vb
Function IGetSketchPoints2( _
   ByVal Count As System.Integer _
) As SketchPoint
```

### Visual Basic (Usage)

```vb
Dim instance As ISketch
Dim Count As System.Integer
Dim value As SketchPoint

value = instance.IGetSketchPoints2(Count)
```

### C#

```csharp
SketchPoint IGetSketchPoints2(
   System.int Count
)
```

### C++/CLI

```cpp
SketchPoint^ IGetSketchPoints2(
   System.int Count
)
```

**NOTE:** See [Differences Between Unmanaged C++ and C++/CLI Code](DifferencesBetweenUnManagedAndCPPCLI.htm).

### Parameters

- `Count`: Number of sketch points in this sketch

### Return Value

- in-process, unmanaged C++: Pointer to an array of [sketch points](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.ISketchPoint.html) in this sketch

VBA, VB.NET, C#, and C++/CLI: Not supported

See [In-process Methods](sldworksapiprogguide.chm::/OVERVIEW/In-process_Methods.htm) for details about this type of method.

## Remarks

Call [ISketch::GetSketchPointsCount2](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.ISketch~GetSketchPointsCount2.html) before calling this method to get the number of sketch points in this sketch.

## See Also

[ISketch Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISketch.html)
[ISketch Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISketch_members.html)
[ISketch::GetSketchPoints2 Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISketch~GetSketchPoints2.html)
[ISketch::GetUserPoints2 Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISketch~GetUserPoints2.html)
[ISketch::GetUserPointsCount Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISketch~GetUserPointsCount.html)
[ISketch::IGetUserPoints2 Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISketch~IGetUserPoints2.html)
[ISketch::IEnumSketchPoints Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISketch~IEnumSketchPoints.html)
[ISketchPoint Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISketchPoint.html)
[ISketch::MergePoints Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISketch~MergePoints.html)

## Availability

SOLIDWORKS 2006 SP2, Revision Number 14.2
