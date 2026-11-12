---
title: "GetSplineHandles Method (ISketchSpline)"
project: "SOLIDWORKS API Help"
interface: "ISketchSpline"
member: "GetSplineHandles"
kind: "method"
source: "sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISketchSpline~GetSplineHandles.html"
---

# GetSplineHandles Method (ISketchSpline)

Gets the handles of this spline.

## Syntax

### Visual Basic (Declaration)

```vb
Function GetSplineHandles() As System.Object
```

### Visual Basic (Usage)

```vb
Dim instance As ISketchSpline
Dim value As System.Object

value = instance.GetSplineHandles()
```

### C#

```csharp
System.object GetSplineHandles()
```

### C++/CLI

```cpp
System.Object^ GetSplineHandles();
```

**NOTE:** See [Differences Between Unmanaged C++ and C++/CLI Code](DifferencesBetweenUnManagedAndCPPCLI.htm).

### Return Value

Array of [spline handles](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.ISplineHandle.html)

## VBA Syntax

See [SketchSpline::GetSplineHandles](ms-its:sldworksapivb6.chm::/sldworks~SketchSpline~GetSplineHandles.html).

## Examples

[Get and Set Spline Handles (VBA)](Get_and_Set_Spline_Handles_Example_VB.htm)
[Get and Set Spline Handles (VB.NET)](Get_and_Set_Spline_Handles_Example_VBNET.htm)
[Get and Set Spline Handles (C#)](Get_and_Set_Spline_Handles_Example_CSharp.htm)

## See Also

[ISketchSpline Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISketchSpline.html)
[ISketchSpline Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISketchSpline_members.html)
[ISketchSpline::GetSplineHandleCount Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISketchSpline~GetSplineHandleCount.html)
[ISketchSpline::IGetSplineHandles Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISketchSpline~IGetSplineHandles.html)
[ISketchSpline::ResetAllHandles Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISketchSpline~ResetAllHandles.html)
[ISketchSpline::ShowSplineHandles Property](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISketchSpline~ShowSplineHandles.html)

## Availability

SOLIDWORKS 2007 FCS, Revision Number 15.0
