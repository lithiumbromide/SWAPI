---
title: "AddEdgeWeldConnector Method (ICWLoadsAndRestraintsManager)"
project: "SOLIDWORKS Simulation API Help"
interface: "ICWLoadsAndRestraintsManager"
member: "AddEdgeWeldConnector"
kind: "method"
source: "cworksapi/SolidWorks.Interop.cosworks~SolidWorks.Interop.cosworks.ICWLoadsAndRestraintsManager~AddEdgeWeldConnector.html"
---

# AddEdgeWeldConnector Method (ICWLoadsAndRestraintsManager)

Creates the specified edge weld connector.

## Syntax

### Visual Basic (Declaration)

```vb
Function AddEdgeWeldConnector( _
   ByVal FirstFace As System.Object, _
   ByVal SecondFace As System.Object, _
   ByVal Edges As System.Object, _
   ByVal NEdgeWeldStyle As System.Integer, _
   ByRef ErrorCode As System.Integer _
) As CWEdgeWeldConnector
```

### Visual Basic (Usage)

```vb
Dim instance As ICWLoadsAndRestraintsManager
Dim FirstFace As System.Object
Dim SecondFace As System.Object
Dim Edges As System.Object
Dim NEdgeWeldStyle As System.Integer
Dim ErrorCode As System.Integer
Dim value As CWEdgeWeldConnector

value = instance.AddEdgeWeldConnector(FirstFace, SecondFace, Edges, NEdgeWeldStyle, ErrorCode)
```

### C#

```csharp
CWEdgeWeldConnector AddEdgeWeldConnector(
   System.object FirstFace,
   System.object SecondFace,
   System.object Edges,
   System.int NEdgeWeldStyle,
   out System.int ErrorCode
)
```

### C++/CLI

```cpp
CWEdgeWeldConnector^ AddEdgeWeldConnector(
   System.Object^ FirstFace,
   System.Object^ SecondFace,
   System.Object^ Edges,
   System.int NEdgeWeldStyle,
   [Out] System.int ErrorCode
)
```

### Parameters

- `FirstFace`: Array of Face Set1 faces
- `SecondFace`: Array of Face Set2 faces

  | If NEdgeWeldStyle = swsEdgeWeldConnectorTypes_e... | Then SecondFace array contains faces that are... |
  | --- | --- |
  | swsEdgeWeldConnectorGrooveDoubleSided - or - swsEdgeWeldConnectorGrooveSingleSided | Parallel to faces in FirstFace array |
  | swsEdgeWeldConnectorFilletDoubleSided - or - swsEdgeWeldConnectorFilletSingleSided | Perpendicular to faces in FirstFace array |
- `Edges`: Array of touching edges between the faces specified in FirstFace and SecondFace arrays
- `NEdgeWeldStyle`: Edge weld style as defined by [swsEdgeWeldConnectorTypes_e](SolidWorks.Interop.cosworks~SolidWorks.Interop.cosworks.swsEdgeWeldConnectorTypes_e.html)
- `ErrorCode`: Error code as defined by [swsEdgeWeldCreationErrorCode_e](SolidWorks.Interop.cosworks~SolidWorks.Interop.cosworks.swsEdgeWeldCreationErrorCode_e.html)

### Return Value

[ICWEdgeWeldConnector](SolidWorks.Interop.cosworks~SolidWorks.Interop.cosworks.ICWEdgeWeldConnector.html)

## VBA Syntax

See [CWLoadsAndRestraintsManager::AddEdgeWeldConnector](ms-its:cworksapivb6.chm::/CosmosWorksLib~CWLoadsAndRestraintsManager~AddEdgeWeldConnector.html).

## Examples

[Create and Edit Edge Weld Connector (VBA)](Create_and_Edit_Edge_Weld_Connector_Example_VB.htm)
[Create and Edit Edge Weld Connector (VB.NET)](Create_and_Edit_Edge_Weld_Connector_Example_VBNET.htm)
[Create and Edit Edge Weld Connector (C#)](Create_and_Edit_Edge_Weld_Connector_Example_CSharp.htm)

## See Also

[ICWLoadsAndRestraintsManager Interface](SolidWorks.Interop.cosworks~SolidWorks.Interop.cosworks.ICWLoadsAndRestraintsManager.html)
[ICWLoadsAndRestraintsManager Members](SolidWorks.Interop.cosworks~SolidWorks.Interop.cosworks.ICWLoadsAndRestraintsManager_members.html)
[ICWLoadsAndRestraintsManager::GetEdgeWeldConnector Method ()](SolidWorks.Interop.cosworks~SolidWorks.Interop.cosworks.ICWLoadsAndRestraintsManager~GetEdgeWeldConnector.html)

## Availability

SOLIDWORKS Simulation API 2015 SP0
