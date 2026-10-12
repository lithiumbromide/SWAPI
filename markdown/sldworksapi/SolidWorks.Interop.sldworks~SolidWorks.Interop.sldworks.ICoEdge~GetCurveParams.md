---
title: "GetCurveParams Method (ICoEdge)"
project: "SOLIDWORKS API Help"
interface: "ICoEdge"
member: "GetCurveParams"
kind: "method"
source: "sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ICoEdge~GetCurveParams.html"
---

# GetCurveParams Method (ICoEdge)

Gets the curve parameters.

## Syntax

### Visual Basic (Declaration)

```vb
Function GetCurveParams() As System.Object
```

### Visual Basic (Usage)

```vb
Dim instance As ICoEdge
Dim value As System.Object

value = instance.GetCurveParams()
```

### C#

```csharp
System.object GetCurveParams()
```

### C++/CLI

```cpp
System.Object^ GetCurveParams();
```

**NOTE:** See [Differences Between Unmanaged C++ and C++/CLI Code](DifferencesBetweenUnManagedAndCPPCLI.htm).

### Return Value

Array (see **Remarks**)

## VBA Syntax

See [CoEdge::GetCurveParams](ms-its:sldworksapivb6.chm::/sldworks~CoEdge~GetCurveParams.html).

## Examples

[Determine Type of Face (VBA)](Determine_Type_of_Face_Example_VB.htm)
[Select Tangent Faces (VBA)](Select_Tangent_Faces_Example_VB.htm)
[Select Edges of All Holes on Face (C#)](Select_Edges_of_All_Holes_on_Face_Example_CSharp.htm)
[Select Edges of All Holes on Face (VB.NET)](Select_Edges_of_All_Holes_on_Face_Example_VBNET.htm)
[Select Edges of All Holes on Face (VBA)](Select_Edges_of_All_Holes_on_Face_Example_VB.htm)

## Remarks

The return value format is an array of 10 doubles:

- retval[0] X startpoint
- retval[1] Y startpoint
- retval[2] Z startpoint
- retval[3] X endpoint
- retval[4] Y endpoint
- retval[5] Z endpoint
- retval[6] startParam
- retval[7] endParam
- retval[8] sense (Not used)
- retval[9] curve type (Not used)

## See Also

[ICoEdge Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ICoEdge.html)
[ICoEdge Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ICoEdge_members.html)
[ICoEdge::IGetCurveParams Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ICoEdge~IGetCurveParams.html)
[IEdge::GetCurveParams2 Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IEdge~GetCurveParams2.html)
[IEdge::IGetCurveParams2 Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IEdge~IGetCurveParams2.html)
[ICurve Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ICurve.html)
