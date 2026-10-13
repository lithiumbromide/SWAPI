---
title: "Evaluate Method (IEdge)"
project: "SOLIDWORKS API Help"
interface: "IEdge"
member: "Evaluate"
kind: "method"
source: "sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IEdge~Evaluate.html"
---

# Evaluate Method (IEdge)

Obsolete. Superseded by [IEdge::Evaluate2](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.IEdge~Evaluate2.html).

## Syntax

### Visual Basic (Declaration)

```vb
Function Evaluate( _
   ByVal Parameter As System.Double _
) As System.Object
```

### Visual Basic (Usage)

```vb
Dim instance As IEdge
Dim Parameter As System.Double
Dim value As System.Object

value = instance.Evaluate(Parameter)
```

### C#

```csharp
System.object Evaluate(
   System.double Parameter
)
```

### C++/CLI

```cpp
System.Object^ Evaluate(
   System.double Parameter
)
```

**NOTE:** See [Differences Between Unmanaged C++ and C++/CLI Code](DifferencesBetweenUnManagedAndCPPCLI.htm).

### Parameters

- `Parameter`: Value of the edge parameter

### Return Value

Array values containing the x,y,z value and derivative of the edge (see **Remarks**)

## VBA Syntax

See [Edge::Evaluate](ms-its:sldworksapivb6.chm::/sldworks~Edge~Evaluate.html).

## Examples

[Select Tangent Edges Via Iteration (VBA)](Select_Tangent_Edges_Example_VB.htm)

## Remarks

Use [IEdge::GetCurveParams2](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.IEdge~GetCurveParams2.html) or [IEdge::IGetCurveParams2](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.IEdge~IEvaluate.html) to determine the valid parameter range for this method.

This OLE implementation of this method returns an array of doubles as follows:

```vb
[ PointX, PointY, PointZ, TangentX, TangentY, TangentZ, Success ]
```

where the point values are in meters and Success is True if successful and false if not.

The return value for the COM implementation is different. To determine success, check the HRESULT return value. The array is as follows:

```vb
[ PointX, PointY, PointZ, TangentX, TangentY, TangentZ ]
```

where the point values are specified in meters.

## See Also

[IEdge Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IEdge.html)
[IEdge Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IEdge_members.html)
[IEdge::IEvaluate Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IEdge~IEvaluate.html)
