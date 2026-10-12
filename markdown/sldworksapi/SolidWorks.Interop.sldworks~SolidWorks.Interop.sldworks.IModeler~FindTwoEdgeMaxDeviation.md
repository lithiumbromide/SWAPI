---
title: "FindTwoEdgeMaxDeviation Method (IModeler)"
project: "SOLIDWORKS API Help"
interface: "IModeler"
member: "FindTwoEdgeMaxDeviation"
kind: "method"
source: "sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModeler~FindTwoEdgeMaxDeviation.html"
---

# FindTwoEdgeMaxDeviation Method (IModeler)

Finds the maximum distance between two edges.

## Syntax

### Visual Basic (Declaration)

```vb
Function FindTwoEdgeMaxDeviation( _
   ByVal LpEdge1 As System.Object, _
   ByVal LpEdge2 As System.Object _
) As System.Double
```

### Visual Basic (Usage)

```vb
Dim instance As IModeler
Dim LpEdge1 As System.Object
Dim LpEdge2 As System.Object
Dim value As System.Double

value = instance.FindTwoEdgeMaxDeviation(LpEdge1, LpEdge2)
```

### C#

```csharp
System.double FindTwoEdgeMaxDeviation(
   System.object LpEdge1,
   System.object LpEdge2
)
```

### C++/CLI

```cpp
System.double FindTwoEdgeMaxDeviation(
   System.Object^ LpEdge1,
   System.Object^ LpEdge2
)
```

**NOTE:** See [Differences Between Unmanaged C++ and C++/CLI Code](DifferencesBetweenUnManagedAndCPPCLI.htm).

### Parameters

- `LpEdge1`: First [edge](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.IEdge.html)
- `LpEdge2`: Second [edge](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.IEdge.html)

### Return Value

Maximum distance between the two edges

## VBA Syntax

See [Modeler::FindTwoEdgeMaxDeviation](ms-its:sldworksapivb6.chm::/sldworks~Modeler~FindTwoEdgeMaxDeviation.html).

## See Also

[IModeler Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModeler.html)
[IModeler Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModeler_members.html)
[IModeler::IFindTwoEdgeMaxDeviation Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModeler~IFindTwoEdgeMaxDeviation.html)

## Availability

SOLIDWORKS 99, datecode 1999207
