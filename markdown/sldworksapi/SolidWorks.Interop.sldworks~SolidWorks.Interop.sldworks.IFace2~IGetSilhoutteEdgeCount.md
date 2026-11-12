---
title: "IGetSilhoutteEdgeCount Method (IFace2)"
project: "SOLIDWORKS API Help"
interface: "IFace2"
member: "IGetSilhoutteEdgeCount"
kind: "method"
source: "sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IFace2~IGetSilhoutteEdgeCount.html"
---

# IGetSilhoutteEdgeCount Method (IFace2)

Gets the number of silhouette edges for this face.

## Syntax

### Visual Basic (Declaration)

```vb
Function IGetSilhoutteEdgeCount( _
   ByRef Root As System.Double, _
   ByRef Normal As System.Double _
) As System.Integer
```

### Visual Basic (Usage)

```vb
Dim instance As IFace2
Dim Root As System.Double
Dim Normal As System.Double
Dim value As System.Integer

value = instance.IGetSilhoutteEdgeCount(Root, Normal)
```

### C#

```csharp
System.int IGetSilhoutteEdgeCount(
   ref System.double Root,
   ref System.double Normal
)
```

### C++/CLI

```cpp
System.int IGetSilhoutteEdgeCount(
   System.double% Root,
   System.double% Normal
)
```

**NOTE:** See [Differences Between Unmanaged C++ and C++/CLI Code](DifferencesBetweenUnManagedAndCPPCLI.htm).

### Parameters

- `Root`: Array of doubles defining the root point
- `Normal`: Array of doubles defining the direction vector

### Return Value

Number of silhouette edges

## VBA Syntax

See [Face2::IGetSilhoutteEdgeCount](ms-its:sldworksapivb6.chm::/sldworks~Face2~IGetSilhoutteEdgeCount.html).

## Remarks

This method calculates the number of edges returned by [IFace2::IGetSilhoutteEdges](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.IFace2~IGetSilhoutteEdges.html) for a given vector root point (root) and a vector direction (normal). Call this method before calling IFace2::IGetSilhoutte.

## See Also

[IFace2 Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IFace2.html)
[IFace2 Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IFace2_members.html)
[IFace2::GetSilhoutteEdgesVB Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IFace2~GetSilhoutteEdgesVB.html)

## Availability

SOLIDWORKS 2001Plus FCS, Revision Number 10.0
