---
title: "IGetSplineHandles Method (ISketchSpline)"
project: "SOLIDWORKS API Help"
interface: "ISketchSpline"
member: "IGetSplineHandles"
kind: "method"
source: "sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISketchSpline~IGetSplineHandles.html"
---

# IGetSplineHandles Method (ISketchSpline)

Gets the handles of this spline.

## Syntax

### Visual Basic (Declaration)

```vb
Function IGetSplineHandles( _
   ByVal Count As System.Integer _
) As SplineHandle
```

### Visual Basic (Usage)

```vb
Dim instance As ISketchSpline
Dim Count As System.Integer
Dim value As SplineHandle

value = instance.IGetSplineHandles(Count)
```

### C#

```csharp
SplineHandle IGetSplineHandles(
   System.int Count
)
```

### C++/CLI

```cpp
SplineHandle^ IGetSplineHandles(
   System.int Count
)
```

**NOTE:** See [Differences Between Unmanaged C++ and C++/CLI Code](DifferencesBetweenUnManagedAndCPPCLI.htm).

### Parameters

- `Count`: Number of spline handles

### Return Value

- in-process, unmanaged C++: Pointer to an array of [spline handles](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.ISplineHandle.html)

VBA, VB.NET, C#, and C++/CLI: Not supported

See [In-process Methods](sldworksapiprogguide.chm::/OVERVIEW/In-process_Methods.htm) for details about this type of method.

## Remarks

Before calling this method, call [ISketchSpline::GetSplineHandleCount](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.ISketchSpline~GetSplineHandleCount.html) to get the value for Count.

## See Also

[ISketchSpline Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISketchSpline.html)
[ISketchSpline Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISketchSpline_members.html)
[ISketchSpline::GetSplineHandles Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISketchSpline~GetSplineHandles.html)
[ISketchSpline::ResetAllHandles Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISketchSpline~ResetAllHandles.html)
[ISketchSpline::ShowSplineHandles Property](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISketchSpline~ShowSplineHandles.html)

## Availability

SOLIDWORKS 2007 FCS, Revision Number 15.0
