---
title: "AddSpotWeldConnector Method (ICWLoadsAndRestraintsManager)"
project: "SOLIDWORKS Simulation API Help"
interface: "ICWLoadsAndRestraintsManager"
member: "AddSpotWeldConnector"
kind: "method"
source: "cworksapi/SolidWorks.Interop.cosworks~SolidWorks.Interop.cosworks.ICWLoadsAndRestraintsManager~AddSpotWeldConnector.html"
---

# AddSpotWeldConnector Method (ICWLoadsAndRestraintsManager)

Adds a spot weld connector.

## Syntax

### Visual Basic (Declaration)

```vb
Function AddSpotWeldConnector( _
   ByVal FirstFace As System.Object, _
   ByVal SecondFace As System.Object, _
   ByVal DispArrayWeldLocations As System.Object, _
   ByRef ErrorCode As System.Integer _
) As CWSpotWeldConnector
```

### Visual Basic (Usage)

```vb
Dim instance As ICWLoadsAndRestraintsManager
Dim FirstFace As System.Object
Dim SecondFace As System.Object
Dim DispArrayWeldLocations As System.Object
Dim ErrorCode As System.Integer
Dim value As CWSpotWeldConnector

value = instance.AddSpotWeldConnector(FirstFace, SecondFace, DispArrayWeldLocations, ErrorCode)
```

### C#

```csharp
CWSpotWeldConnector AddSpotWeldConnector(
   System.object FirstFace,
   System.object SecondFace,
   System.object DispArrayWeldLocations,
   ref System.int ErrorCode
)
```

### C++/CLI

```cpp
CWSpotWeldConnector^ AddSpotWeldConnector(
   System.Object^ FirstFace,
   System.Object^ SecondFace,
   System.Object^ DispArrayWeldLocations,
   System.int% ErrorCode
)
```

### Parameters

- `FirstFace`: Face of a shell or solid body
- `SecondFace`: Face of a shell or solid body that belongs to a different body than FirstFace
- `DispArrayWeldLocations`: Array of vertices or an array of reference points to project on the faces to determine the locations of the spot welds
- `ErrorCode`: Error as defined in [swsSpotWeldConnectorError_e](SOLIDWORKS.Interop.cosworks~SOLIDWORKS.Interop.cosworks.swsSpotWeldConnectorError_e.html)

### Return Value

[Spot weld connector](SOLIDWORKS.Interop.cosworks~SOLIDWORKS.Interop.cosworks.ICWSpotWeldConnector.html)

## VBA Syntax

See [CWLoadsAndRestraintsManager::AddSpotWeldConnector](ms-its:cworksapivb6.chm::/CosmosWorksLib~CWLoadsAndRestraintsManager~AddSpotWeldConnector.html).

## Examples

[Add Spot Weld Connector (VBA)](Add_Spot_Weld_Connector_Example_VB.htm)
[Add Spot Weld Connector (VB.NET)](Add_Spot_Weld_Connector_Example_VBNET.htm)
[Add Spot Weld Connector (C#)](Add_Spot_Weld_Connector_Example_CSharp.htm)

## See Also

[ICWLoadsAndRestraintsManager Interface](SolidWorks.Interop.cosworks~SolidWorks.Interop.cosworks.ICWLoadsAndRestraintsManager.html)
[ICWLoadsAndRestraintsManager Members](SolidWorks.Interop.cosworks~SolidWorks.Interop.cosworks.ICWLoadsAndRestraintsManager_members.html)

## Availability

SOLIDWORKS Simulation API 2009 SP0
