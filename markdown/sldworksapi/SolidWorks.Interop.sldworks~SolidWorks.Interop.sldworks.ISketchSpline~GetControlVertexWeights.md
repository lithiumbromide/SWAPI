---
title: "GetControlVertexWeights Method (ISketchSpline)"
project: "SOLIDWORKS API Help"
interface: "ISketchSpline"
member: "GetControlVertexWeights"
kind: "method"
source: "sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISketchSpline~GetControlVertexWeights.html"
---

# GetControlVertexWeights Method (ISketchSpline)

Gets the weights of the control vetexes of this rational spline.

## Syntax

### Visual Basic (Declaration)

```vb
Function GetControlVertexWeights() As System.Object
```

### Visual Basic (Usage)

```vb
Dim instance As ISketchSpline
Dim value As System.Object

value = instance.GetControlVertexWeights()
```

### C#

```csharp
System.object GetControlVertexWeights()
```

### C++/CLI

```cpp
System.Object^ GetControlVertexWeights();
```

**NOTE:** See [Differences Between Unmanaged C++ and C++/CLI Code](DifferencesBetweenUnManagedAndCPPCLI.htm).

### Return Value

Array of control vertex weights

## VBA Syntax

See [SketchSpline::GetControlVertexWeights](ms-its:sldworksapivb6.chm::/sldworks~SketchSpline~GetControlVertexWeights.html).

## Examples

[Edit Spline (VBA)](Edit_Spline_Example_VB.htm)

## Remarks

This method:

- is valid only if [ISketchSpline::IsRationalCurve](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISketchSpline~IsRationalCurve.html) is true.
- returns an empty array if the spline is non-rational.

## See Also

[ISketchSpline Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISketchSpline.html)
[ISketchSpline Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISketchSpline_members.html)
[ISketchSpline::SetControlVertexWeights Method ()](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISketchSpline~SetControlVertexWeights.html)

## Availability

SOLIDWORKS 2019 FCS, Revision Number 27.0
