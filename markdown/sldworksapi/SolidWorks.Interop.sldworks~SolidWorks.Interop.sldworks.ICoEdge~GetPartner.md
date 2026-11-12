---
title: "GetPartner Method (ICoEdge)"
project: "SOLIDWORKS API Help"
interface: "ICoEdge"
member: "GetPartner"
kind: "method"
source: "sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ICoEdge~GetPartner.html"
---

# GetPartner Method (ICoEdge)

Gets the partner for this coedge.

## Syntax

### Visual Basic (Declaration)

```vb
Function GetPartner() As System.Object
```

### Visual Basic (Usage)

```vb
Dim instance As ICoEdge
Dim value As System.Object

value = instance.GetPartner()
```

### C#

```csharp
System.object GetPartner()
```

### C++/CLI

```cpp
System.Object^ GetPartner();
```

**NOTE:** See [Differences Between Unmanaged C++ and C++/CLI Code](DifferencesBetweenUnManagedAndCPPCLI.htm).

### Return Value

Partner coedge

## VBA Syntax

See [CoEdge::GetPartner](ms-its:sldworksapivb6.chm::/sldworks~CoEdge~GetPartner.html).

## Examples

[Determine Type of Face (VBA)](Determine_Type_of_Face_Example_VB.htm)
[Select Tangent Edges via Iteration (VBA)](Select_Tangent_Edges_Example_VB.htm)
[Select Tangent Faces (VBA)](Select_Tangent_Faces_Example_VB.htm)
[Select Edges of All Holes on Face (C#)](Select_Edges_of_All_Holes_on_Face_Example_CSharp.htm)
[Select Edges of All Holes on Face (VB.NET)](Select_Edges_of_All_Holes_on_Face_Example_VBNET.htm)
[Select Edges of All Holes on Face (VBA)](Select_Edges_of_All_Holes_on_Face_Example_VB.htm)

## See Also

[ICoEdge Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ICoEdge.html)
[ICoEdge Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ICoEdge_members.html)
[ICoEdge::IGetPartner Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ICoEdge~IGetPartner.html)
