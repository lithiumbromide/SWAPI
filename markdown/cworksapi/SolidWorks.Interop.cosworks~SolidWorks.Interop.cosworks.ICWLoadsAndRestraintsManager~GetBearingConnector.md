---
title: "GetBearingConnector Method (ICWLoadsAndRestraintsManager)"
project: "SOLIDWORKS Simulation API Help"
interface: "ICWLoadsAndRestraintsManager"
member: "GetBearingConnector"
kind: "method"
source: "cworksapi/SolidWorks.Interop.cosworks~SolidWorks.Interop.cosworks.ICWLoadsAndRestraintsManager~GetBearingConnector.html"
---

# GetBearingConnector Method (ICWLoadsAndRestraintsManager)

Gets the specified bearing connector.

## Syntax

### Visual Basic (Declaration)

```vb
Function GetBearingConnector( _
   ByVal SName As System.String, _
   ByRef ErrorCode As System.Integer _
) As CWBearingConnector
```

### Visual Basic (Usage)

```vb
Dim instance As ICWLoadsAndRestraintsManager
Dim SName As System.String
Dim ErrorCode As System.Integer
Dim value As CWBearingConnector

value = instance.GetBearingConnector(SName, ErrorCode)
```

### C#

```csharp
CWBearingConnector GetBearingConnector(
   System.string SName,
   out System.int ErrorCode
)
```

### C++/CLI

```cpp
CWBearingConnector^ GetBearingConnector(
   System.String^ SName,
   [Out] System.int ErrorCode
)
```

### Parameters

- `SName`: Name of bearing connector
- `ErrorCode`: Error code as defined by [swsBearingConnectorErrors_e](SolidWorks.Interop.cosworks~SolidWorks.Interop.cosworks.swsBearingConnectorErrors_e.html)

### Return Value

[ICWBearingConnector](SolidWorks.Interop.cosworks~SolidWorks.Interop.cosworks.ICWBearingConnector.html)

## VBA Syntax

See [CWLoadsAndRestraintsManager::GetBearingConnector](ms-its:cworksapivb6.chm::/CosmosWorksLib~CWLoadsAndRestraintsManager~GetBearingConnector.html).

## See Also

[ICWLoadsAndRestraintsManager Interface](SolidWorks.Interop.cosworks~SolidWorks.Interop.cosworks.ICWLoadsAndRestraintsManager.html)
[ICWLoadsAndRestraintsManager Members](SolidWorks.Interop.cosworks~SolidWorks.Interop.cosworks.ICWLoadsAndRestraintsManager_members.html)

## Availability

SOLIDWORKS Simulation API 2024
