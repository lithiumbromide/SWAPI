---
title: "ReplaceEntityAtFirstFace Method (ICWSpotWeldConnector)"
project: "SOLIDWORKS Simulation API Help"
interface: "ICWSpotWeldConnector"
member: "ReplaceEntityAtFirstFace"
kind: "method"
source: "cworksapi/SolidWorks.Interop.cosworks~SolidWorks.Interop.cosworks.ICWSpotWeldConnector~ReplaceEntityAtFirstFace.html"
---

# ReplaceEntityAtFirstFace Method (ICWSpotWeldConnector)

Replaces the spot-weld entity (a face of a shell or solid body) on the first face.

## Syntax

### Visual Basic (Declaration)

```vb
Sub ReplaceEntityAtFirstFace( _
   ByVal DispEntity As System.Object _
)
```

### Visual Basic (Usage)

```vb
Dim instance As ICWSpotWeldConnector
Dim DispEntity As System.Object

instance.ReplaceEntityAtFirstFace(DispEntity)
```

### C#

```csharp
void ReplaceEntityAtFirstFace(
   System.object DispEntity
)
```

### C++/CLI

```cpp
void ReplaceEntityAtFirstFace(
   System.Object^ DispEntity
)
```

### Parameters

- `DispEntity`: Spot-weld entity (a face of a shell or solid body)

## VBA Syntax

See [CWSpotWeldConnector::ReplaceEntityAtFirstFace](ms-its:cworksapivb6.chm::/CosmosWorksLib~CWSpotWeldConnector~ReplaceEntityAtFirstFace.html).

## See Also

[ICWSpotWeldConnector Interface](SolidWorks.Interop.cosworks~SolidWorks.Interop.cosworks.ICWSpotWeldConnector.html)
[ICWSpotWeldConnector Members](SolidWorks.Interop.cosworks~SolidWorks.Interop.cosworks.ICWSpotWeldConnector_members.html)
[ICWSpotWeldConnector::ReplaceEntityAtSecondFace Method](SolidWorks.Interop.cosworks~SolidWorks.Interop.cosworks.ICWSpotWeldConnector~ReplaceEntityAtSecondFace.html)

## Availability

SOLIDWORKS Simulation API 2009 SP0
