---
title: "GetSplineHandleCount Method (ISketchSpline)"
project: "SOLIDWORKS API Help"
interface: "ISketchSpline"
member: "GetSplineHandleCount"
kind: "method"
source: "sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISketchSpline~GetSplineHandleCount.html"
---

# GetSplineHandleCount Method (ISketchSpline)

Gets the number of [handles](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.ISplineHandle.html) in this spline.

## Syntax

### Visual Basic (Declaration)

```vb
Function GetSplineHandleCount() As System.Integer
```

### Visual Basic (Usage)

```vb
Dim instance As ISketchSpline
Dim value As System.Integer

value = instance.GetSplineHandleCount()
```

### C#

```csharp
System.int GetSplineHandleCount()
```

### C++/CLI

```cpp
System.int GetSplineHandleCount();
```

**NOTE:** See [Differences Between Unmanaged C++ and C++/CLI Code](DifferencesBetweenUnManagedAndCPPCLI.htm).

### Return Value

Number of handles

## VBA Syntax

See [SketchSpline::GetSplineHandleCount](ms-its:sldworksapivb6.chm::/sldworks~SketchSpline~GetSplineHandleCount.html).

## Remarks

Call this method before calling [ISketchSpline::IGetSplineHandles](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.ISketchSpline~IGetSplineHandles.html) to get the size of the array for that method.

## See Also

[ISketchSpline Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISketchSpline.html)
[ISketchSpline Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISketchSpline_members.html)
[ISketchSpline::GetSplineHandles Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISketchSpline~GetSplineHandles.html)
[ISketchSpline::ResetAllHandles Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISketchSpline~ResetAllHandles.html)
[ISketchSpline::ShowSplineHandles Property](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISketchSpline~ShowSplineHandles.html)

## Availability

SOLIDWORKS 2007 FCS, Revision Number 15.0
