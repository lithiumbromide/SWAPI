---
title: "AddBoltConnector Method (ICWLoadsAndRestraintsManager)"
project: "SOLIDWORKS Simulation API Help"
interface: "ICWLoadsAndRestraintsManager"
member: "AddBoltConnector"
kind: "method"
source: "cworksapi/SolidWorks.Interop.cosworks~SolidWorks.Interop.cosworks.ICWLoadsAndRestraintsManager~AddBoltConnector.html"
---

# AddBoltConnector Method (ICWLoadsAndRestraintsManager)

Adds a bolt connector.

## Syntax

### Visual Basic (Declaration)

```vb
Function AddBoltConnector( _
   ByVal NBoltType As System.Integer, _
   ByVal DispArrayBoltHead As System.Object, _
   ByVal DispArrayBoltNut As System.Object, _
   ByRef ErrorCode As System.Integer _
) As CWBoltConnector
```

### Visual Basic (Usage)

```vb
Dim instance As ICWLoadsAndRestraintsManager
Dim NBoltType As System.Integer
Dim DispArrayBoltHead As System.Object
Dim DispArrayBoltNut As System.Object
Dim ErrorCode As System.Integer
Dim value As CWBoltConnector

value = instance.AddBoltConnector(NBoltType, DispArrayBoltHead, DispArrayBoltNut, ErrorCode)
```

### C#

```csharp
CWBoltConnector AddBoltConnector(
   System.int NBoltType,
   System.object DispArrayBoltHead,
   System.object DispArrayBoltNut,
   ref System.int ErrorCode
)
```

### C++/CLI

```cpp
CWBoltConnector^ AddBoltConnector(
   System.int NBoltType,
   System.Object^ DispArrayBoltHead,
   System.Object^ DispArrayBoltNut,
   System.int% ErrorCode
)
```

### Parameters

- `NBoltType`: Type of bolt as defined in [swsBoltType_e](SOLIDWORKS.Interop.cosworks~SOLIDWORKS.Interop.cosworks.swsBoltType_e.html)
- `DispArrayBoltHead`: Array of bolt heads
- `DispArrayBoltNut`: Array of bolt nuts
- `ErrorCode`: Error as defined in [swsBoltConnectorError_e](SOLIDWORKS.Interop.cosworks~SOLIDWORKS.Interop.cosworks.swsBoltConnectorError_e.html)

### Return Value

[Bolt connector](SOLIDWORKS.Interop.cosworks~SOLIDWORKS.Interop.cosworks.ICWBoltConnector.html)

## VBA Syntax

See [CWLoadsAndRestraintsManager::AddBoltConnector](ms-its:cworksapivb6.chm::/CosmosWorksLib~CWLoadsAndRestraintsManager~AddBoltConnector.html).

## Examples

[Create and Edit Bolt and Pin Connectors (VBA)](Create_and_Edit_Bolt_and_Pin_Connectors_Example_VB.htm)
[Create and Edit Bolt and Pin Connectors (VB.NET)](Create_and_Edit_Bolt_and_Pin_Connectors_Example_VBNET.htm)
[Create and Edit Bolt and Pin Connectors (C#)](Create_and_Edit_Bolt_and_Pin_Connectors_Example_CSharp.htm)

## See Also

[ICWLoadsAndRestraintsManager Interface](SolidWorks.Interop.cosworks~SolidWorks.Interop.cosworks.ICWLoadsAndRestraintsManager.html)
[ICWLoadsAndRestraintsManager Members](SolidWorks.Interop.cosworks~SolidWorks.Interop.cosworks.ICWLoadsAndRestraintsManager_members.html)

## Availability

SOLIDWORKS Simulation API 2009 SP0
