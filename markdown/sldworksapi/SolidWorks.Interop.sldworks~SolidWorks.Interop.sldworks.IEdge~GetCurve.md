---
title: "GetCurve Method (IEdge)"
project: "SOLIDWORKS API Help"
interface: "IEdge"
member: "GetCurve"
kind: "method"
source: "sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IEdge~GetCurve.html"
---

# GetCurve Method (IEdge)

Gets the underlying curve for this edge.

## Syntax

### Visual Basic (Declaration)

```vb
Function GetCurve() As System.Object
```

### Visual Basic (Usage)

```vb
Dim instance As IEdge
Dim value As System.Object

value = instance.GetCurve()
```

### C#

```csharp
System.object GetCurve()
```

### C++/CLI

```cpp
System.Object^ GetCurve();
```

NOTE:

See

[Differences Between Unmanaged C++ and C++/CLI Code](DifferencesBetweenUnManagedAndCPPCLI.htm)

.

### Return Value

Pointer to the underlying

[curve](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.ICurve.html)

for this edge

## VBA Syntax

See

[Edge::GetCurve](ms-its:sldworksapivb6.chm::/sldworks~Edge~GetCurve.html)

.

## Examples

[Dimension Edge in Drawing (VBA)](Dimension_Edge_in_Drawing_Example_VB.htm)

[Get Edge Curve Parameterization (VBA)](Get_Edge_Curve_Parameterization_Example_VB.htm)

[Get Entities Attached to Cosmetic Thread (VBA)](Get_Entities_Attached_To_Cosmetic_Thread_Example_VB.htm)

[Get Intersecting Face and Edge (VBA)](Get_Intersecting_Face_and_Edge_Example_VB.htm)

[Get Length of Edge (VBA)](Get_Length_of_Edge_Example_VB.htm)

[Select Tangent Edges Via Iteration (VBA)](Select_Tangent_Edges_Example_VB.htm)

[Fill Holes in Part (C#)](Fill_Holes_in_Part_Example_CSharp.htm)

[Fill Holes in Part (VB.NET)](Fill_Holes_in_Part_Example_VBNET.htm)

[Fill Holes in Part (VBA)](Fill_Holes_in_Part_Example_VB.htm)

[Select Edges of All Holes on Face (C#)](Select_Edges_of_All_Holes_on_Face_Example_CSharp.htm)

[Select Edges of All Holes on Face (VB.NET)](Select_Edges_of_All_Holes_on_Face_Example_VBNET.htm)

[Select Edges of All Holes on Face (VBA)](Select_Edges_of_All_Holes_on_Face_Example_VB.htm)

## See Also

[IEdge Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IEdge.html)

[IEdge Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IEdge_members.html)

[ICoEdge::GetEdge Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ICoEdge~GetEdge.html)

[ICoEdge::GetCurve Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ICoEdge~GetCurve.html)

[IEdge::GetCurveParams2 Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IEdge~GetCurveParams2.html)

[ICoEdge::GetCurveParams Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ICoEdge~GetCurveParams.html)
