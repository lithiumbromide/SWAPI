---
title: "SetControlVertexWeights Method (ISketchSpline)"
project: "SOLIDWORKS API Help"
interface: "ISketchSpline"
member: "SetControlVertexWeights"
kind: "method"
source: "sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISketchSpline~SetControlVertexWeights.html"
---

# SetControlVertexWeights Method (ISketchSpline)

Sets the weights of the control vetexes of this rational spline.

## Syntax

### Visual Basic (Declaration)

```vb
Function SetControlVertexWeights( _
   ByVal ControlWeightValues As System.Object _
) As System.Boolean
```

### Visual Basic (Usage)

```vb
Dim instance As ISketchSpline
Dim ControlWeightValues As System.Object
Dim value As System.Boolean

value = instance.SetControlVertexWeights(ControlWeightValues)
```

### C#

```csharp
System.bool SetControlVertexWeights(
   System.object ControlWeightValues
)
```

### C++/CLI

```cpp
System.bool SetControlVertexWeights(
   System.Object^ ControlWeightValues
)
```

**NOTE:** See [Differences Between Unmanaged C++ and C++/CLI Code](DifferencesBetweenUnManagedAndCPPCLI.htm).

### Parameters

- `ControlWeightValues`: Array of control vertex weights

### Return Value

True if weights successfully set, false if not

## VBA Syntax

See [SketchSpline::SetControlVertexWeights](ms-its:sldworksapivb6.chm::/sldworks~SketchSpline~SetControlVertexWeights.html).

## Remarks

This method:

- is valid only if [ISketchSpline::IsRationalCurve](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISketchSpline~IsRationalCurve.html) is true.
- returns false if the number of weights in ControlWeightValues is not equal to the number of control vertexes of the spline.

## See Also

[ISketchSpline Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISketchSpline.html)
[ISketchSpline Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISketchSpline_members.html)
[ISketchSpline::GetControlVertexWeights Method ()](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISketchSpline~GetControlVertexWeights.html)

## Availability

SOLIDWORKS 2019 FCS, Revision Number 27.0
