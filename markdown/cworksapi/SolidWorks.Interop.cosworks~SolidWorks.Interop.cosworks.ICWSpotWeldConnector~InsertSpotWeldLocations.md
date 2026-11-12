---
title: "InsertSpotWeldLocations Method (ICWSpotWeldConnector)"
project: "SOLIDWORKS Simulation API Help"
interface: "ICWSpotWeldConnector"
member: "InsertSpotWeldLocations"
kind: "method"
source: "cworksapi/SolidWorks.Interop.cosworks~SolidWorks.Interop.cosworks.ICWSpotWeldConnector~InsertSpotWeldLocations.html"
---

# InsertSpotWeldLocations Method (ICWSpotWeldConnector)

Inserts the spot-weld locations.

## Syntax

### Visual Basic (Declaration)

```vb
Sub InsertSpotWeldLocations( _
   ByVal DispEntity As System.Object _
)
```

### Visual Basic (Usage)

```vb
Dim instance As ICWSpotWeldConnector
Dim DispEntity As System.Object

instance.InsertSpotWeldLocations(DispEntity)
```

### C#

```csharp
void InsertSpotWeldLocations(
   System.object DispEntity
)
```

### C++/CLI

```cpp
void InsertSpotWeldLocations(
   System.Object^ DispEntity
)
```

### Parameters

- `DispEntity`: Vertex for spot-weld location

## VBA Syntax

See [CWSpotWeldConnector::InsertSpotWeldLocations](ms-its:cworksapivb6.chm::/CosmosWorksLib~CWSpotWeldConnector~InsertSpotWeldLocations.html).

## Remarks

Spot-weld locations can be vertices or reference points. Reference points are projected on the faces to determine the locations of the spot welds.

## See Also

[ICWSpotWeldConnector Interface](SolidWorks.Interop.cosworks~SolidWorks.Interop.cosworks.ICWSpotWeldConnector.html)
[ICWSpotWeldConnector Members](SolidWorks.Interop.cosworks~SolidWorks.Interop.cosworks.ICWSpotWeldConnector_members.html)
[ICWSpotWeldLocations::GetSpotWeldLocationCount Method](SolidWorks.Interop.cosworks~SolidWorks.Interop.cosworks.ICWSpotWeldConnector~GetSpotWeldLocationCount.html)
[ICWSpotWeldLocations::RemoveSpotWeldLocationAt Method](SolidWorks.Interop.cosworks~SolidWorks.Interop.cosworks.ICWSpotWeldConnector~RemoveSpotWeldLocationAt.html)

## Availability

SOLIDWORKS Simulation API 2009 SP0
