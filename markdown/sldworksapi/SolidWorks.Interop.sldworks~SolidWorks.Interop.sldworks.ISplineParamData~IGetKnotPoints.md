---
title: "IGetKnotPoints Method (ISplineParamData)"
project: "SOLIDWORKS API Help"
interface: "ISplineParamData"
member: "IGetKnotPoints"
kind: "method"
source: "sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISplineParamData~IGetKnotPoints.html"
---

# IGetKnotPoints Method (ISplineParamData)

Gets all of the knot points of the spline.

## Syntax

### Visual Basic (Declaration)

```vb
Function IGetKnotPoints( _
   ByVal Count As System.Integer, _
   ByRef KnotPoints As System.Double _
) As System.Boolean
```

### Visual Basic (Usage)

```vb
Dim instance As ISplineParamData
Dim Count As System.Integer
Dim KnotPoints As System.Double
Dim value As System.Boolean

value = instance.IGetKnotPoints(Count, KnotPoints)
```

### C#

```csharp
System.bool IGetKnotPoints(
   System.int Count,
   out System.double KnotPoints
)
```

### C++/CLI

```cpp
System.bool IGetKnotPoints(
   System.int Count,
   [Out] System.double KnotPoints
)
```

**NOTE:** See [Differences Between Unmanaged C++ and C++/CLI Code](DifferencesBetweenUnManagedAndCPPCLI.htm).

### Parameters

- `Count`: Size of KnotPoints array
- `KnotPoints`: - in-process, unmanaged C++: Pointer to an array of double values between 0 and 1, inclusive

  VBA, VB.NET, C#, and C++/CLI: Not supported

  See [In-process Methods](sldworksapiprogguide.chm::/OVERVIEW/In-process_Methods.htm) for details about this type of method.

### Return Value

True if successful, false if not

## Remarks

Before calling this method, call [ISplineParamData::KnotPointsCount](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.ISplineParamData~KnotPointsCount.html) to populate the Count parameter.

Together with [control points](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.ISplineParamData~GetControlPoints.html), knots determine the shape and smoothness of a spline. The knot vector divides the parametric space into intervals or knot spans. These intervals may be uniform or non-uniform. Each interval governs a different control point.

## See Also

[ISplineParamData Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISplineParamData.html)
[ISplineParamData Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISplineParamData_members.html)
[ISplineParamData::GetKnotPoints Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISplineParamData~GetKnotPoints.html)

## Availability

SOLIDWORKS 2011 FCS, Revision Number 19.0
