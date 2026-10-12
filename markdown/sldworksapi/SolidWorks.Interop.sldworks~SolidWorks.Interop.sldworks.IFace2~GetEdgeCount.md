---
title: "GetEdgeCount Method (IFace2)"
project: "SOLIDWORKS API Help"
interface: "IFace2"
member: "GetEdgeCount"
kind: "method"
source: "sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IFace2~GetEdgeCount.html"
---

# GetEdgeCount Method (IFace2)

Gets the number of the edges that bound this face.

## Syntax

### Visual Basic (Declaration)

```vb
Function GetEdgeCount() As System.Integer
```

### Visual Basic (Usage)

```vb
Dim instance As IFace2
Dim value As System.Integer

value = instance.GetEdgeCount()
```

### C#

```csharp
System.int GetEdgeCount()
```

### C++/CLI

```cpp
System.int GetEdgeCount();
```

**NOTE:** See [Differences Between Unmanaged C++ and C++/CLI Code](DifferencesBetweenUnManagedAndCPPCLI.htm).

### Return Value

Number of edges

## VBA Syntax

See [Face2::GetEdgeCount](ms-its:sldworksapivb6.chm::/sldworks~Face2~GetEdgeCount.html).

## Examples

[Traverse Bodies (C++)](Traverse_Bodies_Example_CPlusPlusCLI.htm)
[Get Faces Affected by Feature (VBA)](Get_Faces_Affected_by_Feature_Example_VB.htm)
[Get Faces Affected by Feature (VB.NET)](Get_Faces_Affected_by_Feature_Example_VBNET.htm)
[Get Faces Affected by Feature (C#)](Get_Faces_Affected_by_Feature_Example_CSharp.htm)

## See Also

[IFace2 Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IFace2.html)
[IFace2 Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IFace2_members.html)
[IEdge Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IEdge.html)
[IFace2::GetEdges Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IFace2~GetEdges.html)
[IFace2::IGetEdges Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IFace2~IGetEdges.html)
[IFace2::EnumEdges Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IFace2~EnumEdges.html)

## Availability

SOLIDWORKS 2001Plus FCS, Revision Number 10.0
