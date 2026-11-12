---
title: "GetSilhoutteEdgesVB Method (IFace2)"
project: "SOLIDWORKS API Help"
interface: "IFace2"
member: "GetSilhoutteEdgesVB"
kind: "method"
source: "sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IFace2~GetSilhoutteEdgesVB.html"
---

# GetSilhoutteEdgesVB Method (IFace2)

Gets the silhouette edges.

## Syntax

### Visual Basic (Declaration)

```vb
Function GetSilhoutteEdgesVB( _
   ByVal Xroot As System.Double, _
   ByVal Yroot As System.Double, _
   ByVal Zroot As System.Double, _
   ByVal Xnormal As System.Double, _
   ByVal Ynormal As System.Double, _
   ByVal Znormal As System.Double _
) As System.Object
```

### Visual Basic (Usage)

```vb
Dim instance As IFace2
Dim Xroot As System.Double
Dim Yroot As System.Double
Dim Zroot As System.Double
Dim Xnormal As System.Double
Dim Ynormal As System.Double
Dim Znormal As System.Double
Dim value As System.Object

value = instance.GetSilhoutteEdgesVB(Xroot, Yroot, Zroot, Xnormal, Ynormal, Znormal)
```

### C#

```csharp
System.object GetSilhoutteEdgesVB(
   System.double Xroot,
   System.double Yroot,
   System.double Zroot,
   System.double Xnormal,
   System.double Ynormal,
   System.double Znormal
)
```

### C++/CLI

```cpp
System.Object^ GetSilhoutteEdgesVB(
   System.double Xroot,
   System.double Yroot,
   System.double Zroot,
   System.double Xnormal,
   System.double Ynormal,
   System.double Znormal
)
```

**NOTE:** See [Differences Between Unmanaged C++ and C++/CLI Code](DifferencesBetweenUnManagedAndCPPCLI.htm).

### Parameters

- `Xroot`: X component of the root point
- `Yroot`: Y component of the root point
- `Zroot`: Z component of the root point
- `Xnormal`: X component of the direction vector
- `Ynormal`: Y component of the direction vector
- `Znormal`: Z component of the direction vector

### Return Value

Array of [edges](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.IEdge.html)

## VBA Syntax

See [Face2::GetSilhoutteEdgesVB](ms-its:sldworksapivb6.chm::/sldworks~Face2~GetSilhoutteEdgesVB.html).

## Remarks

The return array has two elements for each edge: the first is the silhouette edge and the second is unused. To iterate through the edges, an application needs to step through every second element.

The returned edges are transient and cannot be selected.

## See Also

[IFace2 Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IFace2.html)
[IFace2 Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IFace2_members.html)
[IFace2::IGetSilhoutteEdges Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IFace2~IGetSilhoutteEdges.html)
[IFace2::IGetSilhoutteEdgeCount Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IFace2~IGetSilhoutteEdgeCount.html)
[IModelDoc2::InsertSplitLineSil Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelDoc2~InsertSplitLineSil.html)

## Availability

SOLIDWORKS 2001Plus FCS, Revision Number 10.0
