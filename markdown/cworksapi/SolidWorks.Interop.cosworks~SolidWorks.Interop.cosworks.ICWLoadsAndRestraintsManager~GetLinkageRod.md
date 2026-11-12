---
title: "GetLinkageRod Method (ICWLoadsAndRestraintsManager)"
project: "SOLIDWORKS Simulation API Help"
interface: "ICWLoadsAndRestraintsManager"
member: "GetLinkageRod"
kind: "method"
source: "cworksapi/SolidWorks.Interop.cosworks~SolidWorks.Interop.cosworks.ICWLoadsAndRestraintsManager~GetLinkageRod.html"
---

# GetLinkageRod Method (ICWLoadsAndRestraintsManager)

Gets the specified linkage rod connector.

## Syntax

### Visual Basic (Declaration)

```vb
Function GetLinkageRod( _
   ByVal SName As System.String, _
   ByRef ErrorCode As System.Integer _
) As CWLinkageRod
```

### Visual Basic (Usage)

```vb
Dim instance As ICWLoadsAndRestraintsManager
Dim SName As System.String
Dim ErrorCode As System.Integer
Dim value As CWLinkageRod

value = instance.GetLinkageRod(SName, ErrorCode)
```

### C#

```csharp
CWLinkageRod GetLinkageRod(
   System.string SName,
   out System.int ErrorCode
)
```

### C++/CLI

```cpp
CWLinkageRod^ GetLinkageRod(
   System.String^ SName,
   [Out] System.int ErrorCode
)
```

### Parameters

- `SName`: Name of the linkage rod connector as shown **Connections > Connectors** branch of the simulation study tree
- `ErrorCode`: Error as defined in [swsLinkConnectorError_e](SOLIDWORKS.Interop.cosworks~SOLIDWORKS.Interop.cosworks.swsLinkConnectorError_e.html)

### Return Value

[ICWLinkageRod](SolidWorks.Interop.cosworks~SolidWorks.Interop.cosworks.ICWLinkageRod.html)

## VBA Syntax

See [CWLoadsAndRestraintsManager::GetLinkageRod](ms-its:cworksapivb6.chm::/CosmosWorksLib~CWLoadsAndRestraintsManager~GetLinkageRod.html).

## Examples

See the [ICWLinkageRod](SolidWorks.Interop.cosworks~SolidWorks.Interop.cosworks.ICWLinkageRod.html) examples.

## See Also

[ICWLoadsAndRestraintsManager Interface](SolidWorks.Interop.cosworks~SolidWorks.Interop.cosworks.ICWLoadsAndRestraintsManager.html)
[ICWLoadsAndRestraintsManager Members](SolidWorks.Interop.cosworks~SolidWorks.Interop.cosworks.ICWLoadsAndRestraintsManager_members.html)

## Availability

SOLIDWORKS Simulation API 2022 SP0
