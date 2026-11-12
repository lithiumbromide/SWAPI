---
title: "ReplaceEntityAtSecondFace Method (ICWSpotWeldConnector)"
project: "SOLIDWORKS Simulation API Help"
interface: "ICWSpotWeldConnector"
member: "ReplaceEntityAtSecondFace"
kind: "method"
source: "cworksapi/SolidWorks.Interop.cosworks~SolidWorks.Interop.cosworks.ICWSpotWeldConnector~ReplaceEntityAtSecondFace.html"
---

# ReplaceEntityAtSecondFace Method (ICWSpotWeldConnector)

Replaces the spot-weld entity (a face of a shell or solid body) on the second face.

## Syntax

### Visual Basic (Declaration)

```vb
Sub ReplaceEntityAtSecondFace( _
   ByVal DispEntity As System.Object _
)
```

### Visual Basic (Usage)

```vb
Dim instance As ICWSpotWeldConnector
Dim DispEntity As System.Object

instance.ReplaceEntityAtSecondFace(DispEntity)
```

### C#

```csharp
void ReplaceEntityAtSecondFace(
   System.object DispEntity
)
```

### C++/CLI

```cpp
void ReplaceEntityAtSecondFace(
   System.Object^ DispEntity
)
```

### Parameters

- `DispEntity`: Spot-weld entity (a face of a shell or solid body)

## VBA Syntax

See [CWSpotWeldConnector::ReplaceEntityAtSecondFace](ms-its:cworksapivb6.chm::/CosmosWorksLib~CWSpotWeldConnector~ReplaceEntityAtSecondFace.html).

## Remarks

The face must belong to a different body than the body of the first face.

## See Also

[ICWSpotWeldConnector Interface](SolidWorks.Interop.cosworks~SolidWorks.Interop.cosworks.ICWSpotWeldConnector.html)
[ICWSpotWeldConnector Members](SolidWorks.Interop.cosworks~SolidWorks.Interop.cosworks.ICWSpotWeldConnector_members.html)
[ICWSpotWeldConnector::ReplaceEntityAtFirstFace Method](SolidWorks.Interop.cosworks~SolidWorks.Interop.cosworks.ICWSpotWeldConnector~ReplaceEntityAtFirstFace.html)

## Availability

SOLIDWORKS Simulation API 2009 SP0
