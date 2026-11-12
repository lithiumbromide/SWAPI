---
title: "SplinePointNumber Property (ISplineHandle)"
project: "SOLIDWORKS API Help"
interface: "ISplineHandle"
member: "SplinePointNumber"
kind: "property"
source: "sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISplineHandle~SplinePointNumber.html"
---

# SplinePointNumber Property (ISplineHandle)

Gets the number of the points of this spline handle.

## Syntax

### Visual Basic (Declaration)

```vb
ReadOnly Property SplinePointNumber As System.Integer
```

### Visual Basic (Usage)

```vb
Dim instance As ISplineHandle
Dim value As System.Integer

value = instance.SplinePointNumber
```

### C#

```csharp
System.int SplinePointNumber {get;}
```

### C++/CLI

```cpp
property System.int SplinePointNumber {
   System.int get();
}
```

**NOTE:** See [Differences Between Unmanaged C++ and C++/CLI Code](DifferencesBetweenUnManagedAndCPPCLI.htm).

### Property Value

Number of the point of this handle

## VBA Syntax

See [SplineHandle::SplinePointNumber](ms-its:sldworksapivb6.chm::/sldworks~SplineHandle~SplinePointNumber.html).

## Examples

See the [ISplineHandle](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISplineHandle.html) examples.

## See Also

[ISplineHandle Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISplineHandle.html)
[ISplineHandle Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISplineHandle_members.html)
[ISketchSpline:DeletePoint Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISketchSpline~DeletePoint.html)
[ISketchSpline:GetPoints2 Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISketchSpline~GetPoints2.html)
[ISketchSpline::InsertPoint Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISketchSpline~InsertPoint.html)
[ISketchSpline::IEnumPoints Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISketchSpline~IEnumPoints.html)

## Availability

SOLIDWORKS 2007 FCS, Revision Number 15.0
