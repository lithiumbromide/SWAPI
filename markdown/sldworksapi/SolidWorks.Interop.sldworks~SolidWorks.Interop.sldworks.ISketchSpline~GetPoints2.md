---
title: "GetPoints2 Method (ISketchSpline)"
project: "SOLIDWORKS API Help"
interface: "ISketchSpline"
member: "GetPoints2"
kind: "method"
source: "sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISketchSpline~GetPoints2.html"
---

# GetPoints2 Method (ISketchSpline)

Gets an array of sketch points for the spline.

## Syntax

### Visual Basic (Declaration)

```vb
Function GetPoints2() As System.Object
```

### Visual Basic (Usage)

```vb
Dim instance As ISketchSpline
Dim value As System.Object

value = instance.GetPoints2()
```

### C#

```csharp
System.object GetPoints2()
```

### C++/CLI

```cpp
System.Object^ GetPoints2();
```

**NOTE:** See [Differences Between Unmanaged C++ and C++/CLI Code](DifferencesBetweenUnManagedAndCPPCLI.htm).

### Return Value

Array of [sketch points](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.ISketchPoint.html) or NULL if the operation fails

## VBA Syntax

See [SketchSpline::GetPoints2](ms-its:sldworksapivb6.chm::/sldworks~SketchSpline~GetPoints2.html).

## Examples

[Get All Elements of Sketch (VBA)](Get_All_Elements_of_Sketch_Example_VB.htm)
[Simplify Spline (VBA)](Simplify_Spline_Example_VB.htm)
[Get Spline's Parameters (C#)](Get_Spline's_Parameters_Example_CSharp.htm)
[Get Spline's Parameters (VB.NET)](Get_Spline's_Parameters_Example_VBNET.htm)
[Get Spline's Parameters (VBA)](Get_Spline's_Parameters_Example_VB.htm)

## See Also

[ISketchSpline Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISketchSpline.html)
[ISketchSpline Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISketchSpline_members.html)
[ISketchSpline::DeletePoint Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISketchSpline~DeletePoint.html)
[ISketchSpline::GetPointCount Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISketchSpline~GetPointCount.html)
[ISketchSpline::IEnumPoints Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISketchSpline~IEnumPoints.html)
[ISketchSpline::InsertPoint Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISketchSpline~InsertPoint.html)
[ISplineHandle::SplinePointNumber Property](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISplineHandle~SplinePointNumber.html)
[ISketchSpline::ShowInflectionPoints Property](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISketchSpline~ShowInflectionPoints.html)

## Availability

SOLIDWORKS 2000 FCS, Revision Number 8.0
