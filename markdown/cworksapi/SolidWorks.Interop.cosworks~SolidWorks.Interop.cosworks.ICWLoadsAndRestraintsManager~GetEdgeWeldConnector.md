---
title: "GetEdgeWeldConnector Method (ICWLoadsAndRestraintsManager)"
project: "SOLIDWORKS Simulation API Help"
interface: "ICWLoadsAndRestraintsManager"
member: "GetEdgeWeldConnector"
kind: "method"
source: "cworksapi/SolidWorks.Interop.cosworks~SolidWorks.Interop.cosworks.ICWLoadsAndRestraintsManager~GetEdgeWeldConnector.html"
---

# GetEdgeWeldConnector Method (ICWLoadsAndRestraintsManager)

Gets the edge weld connector at the specified index.

## Syntax

### Visual Basic (Declaration)

```vb
Function GetEdgeWeldConnector( _
   ByVal NIndex As System.Integer, _
   ByRef ErrorCode As System.Integer _
) As CWEdgeWeldConnector
```

### Visual Basic (Usage)

```vb
Dim instance As ICWLoadsAndRestraintsManager
Dim NIndex As System.Integer
Dim ErrorCode As System.Integer
Dim value As CWEdgeWeldConnector

value = instance.GetEdgeWeldConnector(NIndex, ErrorCode)
```

### C#

```csharp
CWEdgeWeldConnector GetEdgeWeldConnector(
   System.int NIndex,
   out System.int ErrorCode
)
```

### C++/CLI

```cpp
CWEdgeWeldConnector^ GetEdgeWeldConnector(
   System.int NIndex,
   [Out] System.int ErrorCode
)
```

### Parameters

- `NIndex`: Index of the edge weld connector to get (see **Remarks**)
- `ErrorCode`: Error code as defined by [swsEdgeWeldCreationErrorCode_e](SolidWorks.Interop.cosworks~SolidWorks.Interop.cosworks.swsEdgeWeldCreationErrorCode_e.html)

### Return Value

[ICWEdgeWeldConnector](SolidWorks.Interop.cosworks~SolidWorks.Interop.cosworks.ICWEdgeWeldConnector.html)

## VBA Syntax

See [CWLoadsAndRestraintsManager::GetEdgeWeldConnector](ms-its:cworksapivb6.chm::/CosmosWorksLib~CWLoadsAndRestraintsManager~GetEdgeWeldConnector.html).

## Examples

[Create and Edit Edge Weld Connector (VBA)](Create_and_Edit_Edge_Weld_Connector_Example_VB.htm)
[Create and Edit Edge Weld Connector (VB.NET)](Create_and_Edit_Edge_Weld_Connector_Example_VBNET.htm)
[Create and Edit Edge Weld Connector (C#)](Create_and_Edit_Edge_Weld_Connector_Example_CSharp.htm)

## Remarks

Call [ICWLoadsAndRestraintsManager::Count](SolidWorks.Interop.cosworks~SolidWorks.Interop.cosworks.ICWLoadsAndRestraintsManager~Count.html) to determine NIndex. The vertical position of a load or restraint in the Simulation Study tree does not correspond to NIndex. You must use [ICWLoadsAndRestraintsManager::GetLoadsAndRestraints](SolidWorks.Interop.cosworks~SolidWorks.Interop.cosworks.ICWLoadsAndRestraintsManager~GetLoadsAndRestraints.html) to determine the mapping between NIndex and the study's loads and restraints.

## See Also

[ICWLoadsAndRestraintsManager Interface](SolidWorks.Interop.cosworks~SolidWorks.Interop.cosworks.ICWLoadsAndRestraintsManager.html)
[ICWLoadsAndRestraintsManager Members](SolidWorks.Interop.cosworks~SolidWorks.Interop.cosworks.ICWLoadsAndRestraintsManager_members.html)
[ICWLoadsAndRestraintsManager::AddEdgeWeldConnector Method ()](SolidWorks.Interop.cosworks~SolidWorks.Interop.cosworks.ICWLoadsAndRestraintsManager~AddEdgeWeldConnector.html)

## Availability

SOLIDWORKS Simulation API 2015 SP0
