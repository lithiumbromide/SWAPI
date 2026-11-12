---
title: "AddLinkConnector Method (ICWLoadsAndRestraintsManager)"
project: "SOLIDWORKS Simulation API Help"
interface: "ICWLoadsAndRestraintsManager"
member: "AddLinkConnector"
kind: "method"
source: "cworksapi/SolidWorks.Interop.cosworks~SolidWorks.Interop.cosworks.ICWLoadsAndRestraintsManager~AddLinkConnector.html"
---

# AddLinkConnector Method (ICWLoadsAndRestraintsManager)

Adds a link connector.

## Syntax

### Visual Basic (Declaration)

```vb
Function AddLinkConnector( _
   ByVal VertexPointforFirstLocation As System.Object, _
   ByVal VertexPointforSecondLocation As System.Object, _
   ByRef ErrorCode As System.Integer _
) As CWLinkConnector
```

### Visual Basic (Usage)

```vb
Dim instance As ICWLoadsAndRestraintsManager
Dim VertexPointforFirstLocation As System.Object
Dim VertexPointforSecondLocation As System.Object
Dim ErrorCode As System.Integer
Dim value As CWLinkConnector

value = instance.AddLinkConnector(VertexPointforFirstLocation, VertexPointforSecondLocation, ErrorCode)
```

### C#

```csharp
CWLinkConnector AddLinkConnector(
   System.object VertexPointforFirstLocation,
   System.object VertexPointforSecondLocation,
   out System.int ErrorCode
)
```

### C++/CLI

```cpp
CWLinkConnector^ AddLinkConnector(
   System.Object^ VertexPointforFirstLocation,
   System.Object^ VertexPointforSecondLocation,
   [Out] System.int ErrorCode
)
```

### Parameters

- `VertexPointforFirstLocation`: Vertex for first location
- `VertexPointforSecondLocation`: Vertex for second location
- `ErrorCode`: Error as defined in [swsLinkConnectorError_e](SOLIDWORKS.Interop.cosworks~SOLIDWORKS.Interop.cosworks.swsLinkConnectorError_e.html)

### Return Value

[Link connector](SOLIDWORKS.Interop.cosworks~SOLIDWORKS.Interop.cosworks.ICWLinkConnector.html)

## VBA Syntax

See [CWLoadsAndRestraintsManager::AddLinkConnector](ms-its:cworksapivb6.chm::/CosmosWorksLib~CWLoadsAndRestraintsManager~AddLinkConnector.html).

## Examples

See the [ICWLinkConnector](SolidWorks.Interop.cosworks~SolidWorks.Interop.cosworks.ICWLinkConnector.html) examples.

## See Also

[ICWLoadsAndRestraintsManager Interface](SolidWorks.Interop.cosworks~SolidWorks.Interop.cosworks.ICWLoadsAndRestraintsManager.html)
[ICWLoadsAndRestraintsManager Members](SolidWorks.Interop.cosworks~SolidWorks.Interop.cosworks.ICWLoadsAndRestraintsManager_members.html)

## Availability

SOLIDWORKS Simulation API 2009 SP0
