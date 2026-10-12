---
title: "AddElasticConnector Method (ICWLoadsAndRestraintsManager)"
project: "SOLIDWORKS Simulation API Help"
interface: "ICWLoadsAndRestraintsManager"
member: "AddElasticConnector"
kind: "method"
source: "cworksapi/SolidWorks.Interop.cosworks~SolidWorks.Interop.cosworks.ICWLoadsAndRestraintsManager~AddElasticConnector.html"
---

# AddElasticConnector Method (ICWLoadsAndRestraintsManager)

Adds an elastic support fixture.

## Syntax

### Visual Basic (Declaration)

```vb
Function AddElasticConnector( _
   ByVal DispArray As System.Object, _
   ByRef ErrorCode As System.Integer _
) As CWElasticConnector
```

### Visual Basic (Usage)

```vb
Dim instance As ICWLoadsAndRestraintsManager
Dim DispArray As System.Object
Dim ErrorCode As System.Integer
Dim value As CWElasticConnector

value = instance.AddElasticConnector(DispArray, ErrorCode)
```

### C#

```csharp
CWElasticConnector AddElasticConnector(
   System.object DispArray,
   ref System.int ErrorCode
)
```

### C++/CLI

```cpp
CWElasticConnector^ AddElasticConnector(
   System.Object^ DispArray,
   System.int% ErrorCode
)
```

### Parameters

- `DispArray`: Array of faces for the elastic support fixture
- `ErrorCode`: Error as defined in [swsElasticConnectorError_e](SOLIDWORKS.Interop.cosworks~SOLIDWORKS.Interop.cosworks.swsElasticConnectorError_e.html)

### Return Value

[Elastic support fixture](SolidWorks.Interop.cosworks~SolidWorks.Interop.cosworks.ICWElasticConnector.html)

## VBA Syntax

See [CWLoadsAndRestraintsManager::AddElasticConnector](ms-its:cworksapivb6.chm::/CosmosWorksLib~CWLoadsAndRestraintsManager~AddElasticConnector.html).

## Examples

[Add Elastic Support Fixture (VBA)](Add_Elastic_Support_Connector_Example_VB.htm)
[Add Elastic Support Fixture (VB.NET)](Add_Elastic_Support_Connector_Example_VBNET.htm)
[Add Elastic Support Fixture (C#)](Add_Elastic_Support_Connector_Example_CSharp.htm)

## See Also

[ICWLoadsAndRestraintsManager Interface](SolidWorks.Interop.cosworks~SolidWorks.Interop.cosworks.ICWLoadsAndRestraintsManager.html)
[ICWLoadsAndRestraintsManager Members](SolidWorks.Interop.cosworks~SolidWorks.Interop.cosworks.ICWLoadsAndRestraintsManager_members.html)

## Availability

SOLIDWORKS Simulation API 2009 SP0
