---
title: "AddSpringConnector Method (ICWLoadsAndRestraintsManager)"
project: "SOLIDWORKS Simulation API Help"
interface: "ICWLoadsAndRestraintsManager"
member: "AddSpringConnector"
kind: "method"
source: "cworksapi/SolidWorks.Interop.cosworks~SolidWorks.Interop.cosworks.ICWLoadsAndRestraintsManager~AddSpringConnector.html"
---

# AddSpringConnector Method (ICWLoadsAndRestraintsManager)

Adds a spring connector.

## Syntax

### Visual Basic (Declaration)

```vb
Function AddSpringConnector( _
   ByVal NSpringSubType As System.Integer, _
   ByVal DispArrayComp1 As System.Object, _
   ByVal DispArrayComp2 As System.Object, _
   ByRef ErrorCode As System.Integer _
) As CWSpringConnector
```

### Visual Basic (Usage)

```vb
Dim instance As ICWLoadsAndRestraintsManager
Dim NSpringSubType As System.Integer
Dim DispArrayComp1 As System.Object
Dim DispArrayComp2 As System.Object
Dim ErrorCode As System.Integer
Dim value As CWSpringConnector

value = instance.AddSpringConnector(NSpringSubType, DispArrayComp1, DispArrayComp2, ErrorCode)
```

### C#

```csharp
CWSpringConnector AddSpringConnector(
   System.int NSpringSubType,
   System.object DispArrayComp1,
   System.object DispArrayComp2,
   ref System.int ErrorCode
)
```

### C++/CLI

```cpp
CWSpringConnector^ AddSpringConnector(
   System.int NSpringSubType,
   System.Object^ DispArrayComp1,
   System.Object^ DispArrayComp2,
   System.int% ErrorCode
)
```

### Parameters

- `NSpringSubType`: Spring connector type as defined in [swsSpringConnectorType_e](SOLIDWORKS.Interop.cosworks~SOLIDWORKS.Interop.cosworks.swsSpringConnectorType_e.html)
- `DispArrayComp1`: Array of planar faces, cylindrical faces, or vertices from a body depending on NSpringSubType
- `DispArrayComp2`: Array of planar faces, cylindrical faces, or vertices, depending on NSpringSubType, from another body
- `ErrorCode`: Error as defined in [swsSpringConnectorError_e](SOLIDWORKS.Interop.cosworks~SOLIDWORKS.Interop.cosworks.swsSpringConnectorError_e.html)

### Return Value

[Spring connector](SOLIDWORKS.Interop.cosworks~SOLIDWORKS.Interop.cosworks.ICWSpringConnector.html)

## VBA Syntax

See [CWLoadsAndRestraintsManager::AddSpringConnector](ms-its:cworksapivb6.chm::/CosmosWorksLib~CWLoadsAndRestraintsManager~AddSpringConnector.html).

## Examples

[Add Spring Connector (VBA)](Add_Spring_Connector_Example_VB.htm)
[Add Spring Connector (VB.NET)](Add_Spring_Connector_Example_VBNET.htm)
[Add Spring Connector (C#)](Add_Spring_Connector_Example_CSharp.htm)

## See Also

[ICWLoadsAndRestraintsManager Interface](SolidWorks.Interop.cosworks~SolidWorks.Interop.cosworks.ICWLoadsAndRestraintsManager.html)
[ICWLoadsAndRestraintsManager Members](SolidWorks.Interop.cosworks~SolidWorks.Interop.cosworks.ICWLoadsAndRestraintsManager_members.html)

## Availability

SOLIDWORKS Simulation API 2009 SP0
