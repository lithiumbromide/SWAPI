---
title: "GetGeneralSpringConnector Method (ICWLoadsAndRestraintsManager)"
project: "SOLIDWORKS Simulation API Help"
interface: "ICWLoadsAndRestraintsManager"
member: "GetGeneralSpringConnector"
kind: "method"
source: "cworksapi/SolidWorks.Interop.cosworks~SolidWorks.Interop.cosworks.ICWLoadsAndRestraintsManager~GetGeneralSpringConnector.html"
---

# GetGeneralSpringConnector Method (ICWLoadsAndRestraintsManager)

Gets the specified general spring connector.

## Syntax

### Visual Basic (Declaration)

```vb
Function GetGeneralSpringConnector( _
   ByVal SName As System.String, _
   ByRef ErrorCode As System.Integer _
) As CWGeneralSpringConnector
```

### Visual Basic (Usage)

```vb
Dim instance As ICWLoadsAndRestraintsManager
Dim SName As System.String
Dim ErrorCode As System.Integer
Dim value As CWGeneralSpringConnector

value = instance.GetGeneralSpringConnector(SName, ErrorCode)
```

### C#

```csharp
CWGeneralSpringConnector GetGeneralSpringConnector(
   System.string SName,
   out System.int ErrorCode
)
```

### C++/CLI

```cpp
CWGeneralSpringConnector^ GetGeneralSpringConnector(
   System.String^ SName,
   [Out] System.int ErrorCode
)
```

### Parameters

- `SName`: Name of general spring connector
- `ErrorCode`: Error code as defined by [swsGeneralSpringError_e](SolidWorks.Interop.cosworks~SolidWorks.Interop.cosworks.swsGeneralSpringError_e.html)

### Return Value

[General spring connector](SolidWorks.Interop.cosworks~SolidWorks.Interop.cosworks.ICWGeneralSpringConnector.html)

## VBA Syntax

See [CWLoadsAndRestraintsManager::GetGeneralSpringConnector](ms-its:cworksapivb6.chm::/CosmosWorksLib~CWLoadsAndRestraintsManager~GetGeneralSpringConnector.html).

## See Also

[ICWLoadsAndRestraintsManager Interface](SolidWorks.Interop.cosworks~SolidWorks.Interop.cosworks.ICWLoadsAndRestraintsManager.html)
[ICWLoadsAndRestraintsManager Members](SolidWorks.Interop.cosworks~SolidWorks.Interop.cosworks.ICWLoadsAndRestraintsManager_members.html)
[ICWLoadsAndRestraintsManager::AddGeneralSpringConnector Method ()](SolidWorks.Interop.cosworks~SolidWorks.Interop.cosworks.ICWLoadsAndRestraintsManager~AddGeneralSpringConnector.html)

## Availability

SOLIDWORKS Simulation API 2025 SP0
