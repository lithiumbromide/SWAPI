---
title: "IFindTwoEdgeMaxDeviation Method (IModeler)"
project: "SOLIDWORKS API Help"
interface: "IModeler"
member: "IFindTwoEdgeMaxDeviation"
kind: "method"
source: "sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModeler~IFindTwoEdgeMaxDeviation.html"
---

# IFindTwoEdgeMaxDeviation Method (IModeler)

Finds the maximum distance between two edges.

## Syntax

### Visual Basic (Declaration)

```vb
Function IFindTwoEdgeMaxDeviation( _
   ByVal PEdge1 As Edge, _
   ByVal PEdge2 As Edge _
) As System.Double
```

### Visual Basic (Usage)

```vb
Dim instance As IModeler
Dim PEdge1 As Edge
Dim PEdge2 As Edge
Dim value As System.Double

value = instance.IFindTwoEdgeMaxDeviation(PEdge1, PEdge2)
```

### C#

```csharp
System.double IFindTwoEdgeMaxDeviation(
   Edge PEdge1,
   Edge PEdge2
)
```

### C++/CLI

```cpp
System.double IFindTwoEdgeMaxDeviation(
   Edge^ PEdge1,
   Edge^ PEdge2
)
```

**NOTE:** See [Differences Between Unmanaged C++ and C++/CLI Code](DifferencesBetweenUnManagedAndCPPCLI.htm).

### Parameters

- `PEdge1`: First [edge](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.IEdge.html)
- `PEdge2`: Second [edge](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.IEdge.html)

### Return Value

Maximum distance between the two edges

## VBA Syntax

See [Modeler::IFindTwoEdgeMaxDeviation](ms-its:sldworksapivb6.chm::/sldworks~Modeler~IFindTwoEdgeMaxDeviation.html).

## See Also

[IModeler Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModeler.html)
[IModeler Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModeler_members.html)
[IModeler::FindTwoEdgeMaxDeviation Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModeler~FindTwoEdgeMaxDeviation.html)

## Availability

SOLIDWORKS 99, datecode 1999207
