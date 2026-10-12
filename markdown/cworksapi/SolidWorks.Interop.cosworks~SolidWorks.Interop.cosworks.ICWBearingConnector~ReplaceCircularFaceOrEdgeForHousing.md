---
title: "ReplaceCircularFaceOrEdgeForHousing Method (ICWBearingConnector)"
project: "SOLIDWORKS Simulation API Help"
interface: "ICWBearingConnector"
member: "ReplaceCircularFaceOrEdgeForHousing"
kind: "method"
source: "cworksapi/SolidWorks.Interop.cosworks~SolidWorks.Interop.cosworks.ICWBearingConnector~ReplaceCircularFaceOrEdgeForHousing.html"
---

# ReplaceCircularFaceOrEdgeForHousing Method (ICWBearingConnector)

Replaces the housing circular face or edge with the specified face or edge.

## Syntax

### Visual Basic (Declaration)

```vb
Function ReplaceCircularFaceOrEdgeForHousing( _
   ByVal CircularFaceOrEdge As System.Object _
) As System.Integer
```

### Visual Basic (Usage)

```vb
Dim instance As ICWBearingConnector
Dim CircularFaceOrEdge As System.Object
Dim value As System.Integer

value = instance.ReplaceCircularFaceOrEdgeForHousing(CircularFaceOrEdge)
```

### C#

```csharp
System.int ReplaceCircularFaceOrEdgeForHousing(
   System.object CircularFaceOrEdge
)
```

### C++/CLI

```cpp
System.int ReplaceCircularFaceOrEdgeForHousing(
   System.Object^ CircularFaceOrEdge
)
```

### Parameters

- `CircularFaceOrEdge`: Circular face or edge

### Return Value

Error code as defined by [swsBearingConnectorErrors_e](SolidWorks.Interop.cosworks~SolidWorks.Interop.cosworks.swsBearingConnectorErrors_e.html)

## VBA Syntax

See [CWBearingConnector::ReplaceCircularFaceOrEdgeForHousing](ms-its:cworksapivb6.chm::/CosmosWorksLib~CWBearingConnector~ReplaceCircularFaceOrEdgeForHousing.html).

## See Also

[ICWBearingConnector Interface](SolidWorks.Interop.cosworks~SolidWorks.Interop.cosworks.ICWBearingConnector.html)
[ICWBearingConnector Members](SolidWorks.Interop.cosworks~SolidWorks.Interop.cosworks.ICWBearingConnector_members.html)

## Availability

SOLIDWORKS Simulation API 2024 SP0
