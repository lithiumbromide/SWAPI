---
title: "AddPinConnector Method (ICWLoadsAndRestraintsManager)"
project: "SOLIDWORKS Simulation API Help"
interface: "ICWLoadsAndRestraintsManager"
member: "AddPinConnector"
kind: "method"
source: "cworksapi/SolidWorks.Interop.cosworks~SolidWorks.Interop.cosworks.ICWLoadsAndRestraintsManager~AddPinConnector.html"
---

# AddPinConnector Method (ICWLoadsAndRestraintsManager)

Adds a pin connector.

## Syntax

### Visual Basic (Declaration)

```vb
Function AddPinConnector( _
   ByVal DispArrayComp1 As System.Object, _
   ByVal DispArrayComp2 As System.Object, _
   ByRef ErrorCode As System.Integer _
) As CWPinConnector
```

### Visual Basic (Usage)

```vb
Dim instance As ICWLoadsAndRestraintsManager
Dim DispArrayComp1 As System.Object
Dim DispArrayComp2 As System.Object
Dim ErrorCode As System.Integer
Dim value As CWPinConnector

value = instance.AddPinConnector(DispArrayComp1, DispArrayComp2, ErrorCode)
```

### C#

```csharp
CWPinConnector AddPinConnector(
   System.object DispArrayComp1,
   System.object DispArrayComp2,
   ref System.int ErrorCode
)
```

### C++/CLI

```cpp
CWPinConnector^ AddPinConnector(
   System.Object^ DispArrayComp1,
   System.Object^ DispArrayComp2,
   System.int% ErrorCode
)
```

### Parameters

- `DispArrayComp1`: Array of one full cylindrical face or of multiple cylindrical faces of smaller angles belonging to the same body and coaxial with the same radius
- `DispArrayComp2`: Array of one full cylindrical face or of multiple cylindrical faces of smaller angles belonging to the same body, but different than the body in DispArrayComp1, and coaxial with the same radius
- `ErrorCode`: Error as defined in [swsPinConnectorError_e](SOLIDWORKS.Interop.cosworks~SOLIDWORKS.Interop.cosworks.swsPinConnectorError_e.html)

### Return Value

[Pin connector](SOLIDWORKS.Interop.cosworks~SOLIDWORKS.Interop.cosworks.ICWPinConnector.html)

## VBA Syntax

See [CWLoadsAndRestraintsManager::AddPinConnector](ms-its:cworksapivb6.chm::/CosmosWorksLib~CWLoadsAndRestraintsManager~AddPinConnector.html).

## Examples

[Add Pin Connector (VBA)](Add_Pin_Connector_Example_VB.htm)
[Add Pin Connector (VB.NET)](Add_Pin_Connector_Example_VBNET.htm)
[Add Pin Connector (C#)](Add_Pin_Connector_Example_CSharp.htm)

## See Also

[ICWLoadsAndRestraintsManager Interface](SolidWorks.Interop.cosworks~SolidWorks.Interop.cosworks.ICWLoadsAndRestraintsManager.html)
[ICWLoadsAndRestraintsManager Members](SolidWorks.Interop.cosworks~SolidWorks.Interop.cosworks.ICWLoadsAndRestraintsManager_members.html)

## Availability

SOLIDWORKS Simulation API 2009 SP0
