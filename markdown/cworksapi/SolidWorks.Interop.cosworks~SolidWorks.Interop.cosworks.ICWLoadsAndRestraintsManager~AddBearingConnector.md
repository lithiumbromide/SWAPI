---
title: "AddBearingConnector Method (ICWLoadsAndRestraintsManager)"
project: "SOLIDWORKS Simulation API Help"
interface: "ICWLoadsAndRestraintsManager"
member: "AddBearingConnector"
kind: "method"
source: "cworksapi/SolidWorks.Interop.cosworks~SolidWorks.Interop.cosworks.ICWLoadsAndRestraintsManager~AddBearingConnector.html"
---

# AddBearingConnector Method (ICWLoadsAndRestraintsManager)

Adds the specified bearing connector.

## Syntax

### Visual Basic (Declaration)

```vb
Function AddBearingConnector( _
   ByVal CircularFaceForShaft As System.Object, _
   ByVal CircularFaceOrEdgeForHousing As System.Object, _
   ByRef ErrorCode As System.Integer _
) As CWBearingConnector
```

### Visual Basic (Usage)

```vb
Dim instance As ICWLoadsAndRestraintsManager
Dim CircularFaceForShaft As System.Object
Dim CircularFaceOrEdgeForHousing As System.Object
Dim ErrorCode As System.Integer
Dim value As CWBearingConnector

value = instance.AddBearingConnector(CircularFaceForShaft, CircularFaceOrEdgeForHousing, ErrorCode)
```

### C#

```csharp
CWBearingConnector AddBearingConnector(
   System.object CircularFaceForShaft,
   System.object CircularFaceOrEdgeForHousing,
   out System.int ErrorCode
)
```

### C++/CLI

```cpp
CWBearingConnector^ AddBearingConnector(
   System.Object^ CircularFaceForShaft,
   System.Object^ CircularFaceOrEdgeForHousing,
   [Out] System.int ErrorCode
)
```

### Parameters

- `CircularFaceForShaft`: Circular face for shaft
- `CircularFaceOrEdgeForHousing`: Circular face or edge for housing
- `ErrorCode`: Error code as defined by [swsBearingConnectorErrors_e](SolidWorks.Interop.cosworks~SolidWorks.Interop.cosworks.swsBearingConnectorErrors_e.html)

### Return Value

[ICWBearingConnector](SolidWorks.Interop.cosworks~SolidWorks.Interop.cosworks.ICWBearingConnector.html)

## VBA Syntax

See [CWLoadsAndRestraintsManager::AddBearingConnector](ms-its:cworksapivb6.chm::/CosmosWorksLib~CWLoadsAndRestraintsManager~AddBearingConnector.html).

## See Also

[ICWLoadsAndRestraintsManager Interface](SolidWorks.Interop.cosworks~SolidWorks.Interop.cosworks.ICWLoadsAndRestraintsManager.html)
[ICWLoadsAndRestraintsManager Members](SolidWorks.Interop.cosworks~SolidWorks.Interop.cosworks.ICWLoadsAndRestraintsManager_members.html)

## Availability

SOLIDWORKS Simulation API 2024
