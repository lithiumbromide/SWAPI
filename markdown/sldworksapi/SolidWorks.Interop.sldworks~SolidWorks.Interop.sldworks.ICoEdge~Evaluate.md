---
title: "Evaluate Method (ICoEdge)"
project: "SOLIDWORKS API Help"
interface: "ICoEdge"
member: "Evaluate"
kind: "method"
source: "sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ICoEdge~Evaluate.html"
---

# Evaluate Method (ICoEdge)

Obsolete. Superseded by [ICoEdge::Evaluate2](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.ICoEdge~Evaluate2.html).

## Syntax

### Visual Basic (Declaration)

```vb
Function Evaluate( _
   ByVal Param As System.Double _
) As System.Object
```

### Visual Basic (Usage)

```vb
Dim instance As ICoEdge
Dim Param As System.Double
Dim value As System.Object

value = instance.Evaluate(Param)
```

### C#

```csharp
System.object Evaluate(
   System.double Param
)
```

### C++/CLI

```cpp
System.Object^ Evaluate(
   System.double Param
)
```

**NOTE:** See [Differences Between Unmanaged C++ and C++/CLI Code](DifferencesBetweenUnManagedAndCPPCLI.htm).

### Parameters

- `Param`: Curve parameter desired (U value desired for evaluation)

### Return Value

Array of doubles (see **Remarks**)

## VBA Syntax

See [CoEdge::Evaluate](ms-its:sldworksapivb6.chm::/sldworks~CoEdge~Evaluate.html).

## Examples

[Determine Type of Face (VBA)](Determine_Type_of_Face_Example_VB.htm)
[Select Tangent Faces (VBA)](Select_Tangent_Faces_Example_VB.htm)
[Select Edges of All Holes on Face (C#)](Select_Edges_of_All_Holes_on_Face_Example_CSharp.htm)
[Select Edges of All Holes on Face (VB.NET)](Select_Edges_of_All_Holes_on_Face_Example_VBNET.htm)
[Select Edges of All Holes on Face (VBA)](Select_Edges_of_All_Holes_on_Face_Example_VB.htm)

## Remarks

The tangency vector is defined to be in the direction of the coedge.

The format of the return value is an array of 6 doubles:

- retval[0] x location on the curve
- retval[1] y location on the curve
- retval[2] z location on the curve
- retval[3] x vector describing the tangency at the parameter location on the coedge
- retval[4] y vector describing the tangency at the parameter location on the coedge
- retval[5] z vector describing the tangency at the parameter location on the coedge

## See Also

[ICoEdge Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ICoEdge.html)
[ICoEdge Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ICoEdge_members.html)
[ICoEdge::IEvaluate Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ICoEdge~IEvaluate.html)
[ICoEdge::GetCurveParams Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ICoEdge~GetCurveParams.html)
[ICoEdge::IGetCurveParams Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ICoEdge~IGetCurveParams.html)
