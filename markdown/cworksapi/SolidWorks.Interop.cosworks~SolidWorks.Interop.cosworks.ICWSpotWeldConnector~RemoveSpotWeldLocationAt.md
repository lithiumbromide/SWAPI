---
title: "RemoveSpotWeldLocationAt Method (ICWSpotWeldConnector)"
project: "SOLIDWORKS Simulation API Help"
interface: "ICWSpotWeldConnector"
member: "RemoveSpotWeldLocationAt"
kind: "method"
source: "cworksapi/SolidWorks.Interop.cosworks~SolidWorks.Interop.cosworks.ICWSpotWeldConnector~RemoveSpotWeldLocationAt.html"
---

# RemoveSpotWeldLocationAt Method (ICWSpotWeldConnector)

Removes the spot-weld location at the specified index.

## Syntax

### Visual Basic (Declaration)

```vb
Sub RemoveSpotWeldLocationAt( _
   ByVal NIndex As System.Integer _
)
```

### Visual Basic (Usage)

```vb
Dim instance As ICWSpotWeldConnector
Dim NIndex As System.Integer

instance.RemoveSpotWeldLocationAt(NIndex)
```

### C#

```csharp
void RemoveSpotWeldLocationAt(
   System.int NIndex
)
```

### C++/CLI

```cpp
void RemoveSpotWeldLocationAt(
   System.int NIndex
)
```

### Parameters

- `NIndex`: 0-based index at which to remove the spot weld

## VBA Syntax

See [CWSpotWeldConnector::RemoveSpotWeldLocationAt](ms-its:cworksapivb6.chm::/CosmosWorksLib~CWSpotWeldConnector~RemoveSpotWeldLocationAt.html).

## Remarks

Before calling this method, call [ICWSpotWeldLocation::GetSpotWeldLocationCount](SOLIDWORKS.Interop.cosworks~SOLIDWORKS.Interop.cosworks.ICWSpotWeldConnector~GetSpotWeldLocationCount.html) to determine the value of NIndex.

## See Also

[ICWSpotWeldConnector Interface](SolidWorks.Interop.cosworks~SolidWorks.Interop.cosworks.ICWSpotWeldConnector.html)
[ICWSpotWeldConnector Members](SolidWorks.Interop.cosworks~SolidWorks.Interop.cosworks.ICWSpotWeldConnector_members.html)
[ICWSpotWEldConnector::InsertSpotWeldLocations Method](SolidWorks.Interop.cosworks~SolidWorks.Interop.cosworks.ICWSpotWeldConnector~InsertSpotWeldLocations.html)

## Availability

SOLIDWORKS Simulation API 2009 SP0
