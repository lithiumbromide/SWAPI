---
title: "GetSolidBodyByName Method (ICWSolidManager)"
project: "SOLIDWORKS Simulation API Help"
interface: "ICWSolidManager"
member: "GetSolidBodyByName"
kind: "method"
source: "cworksapi/SolidWorks.Interop.cosworks~SolidWorks.Interop.cosworks.ICWSolidManager~GetSolidBodyByName.html"
---

# GetSolidBodyByName Method (ICWSolidManager)

Gets the specified solid body.

## Syntax

### Visual Basic (Declaration)

```vb
Function GetSolidBodyByName( _
   ByVal SBodyName As System.String, _
   ByRef ErrorCode As System.Integer _
) As CWSolidBody
```

### Visual Basic (Usage)

```vb
Dim instance As ICWSolidManager
Dim SBodyName As System.String
Dim ErrorCode As System.Integer
Dim value As CWSolidBody

value = instance.GetSolidBodyByName(SBodyName, ErrorCode)
```

### C#

```csharp
CWSolidBody GetSolidBodyByName(
   System.string SBodyName,
   out System.int ErrorCode
)
```

### C++/CLI

```cpp
CWSolidBody^ GetSolidBodyByName(
   System.String^ SBodyName,
   [Out] System.int ErrorCode
)
```

### Parameters

- `SBodyName`: Name of solid body
- `ErrorCode`: 0 if successful, 1 if not

### Return Value

[ICWSolidBody](SolidWorks.Interop.cosworks~SolidWorks.Interop.cosworks.ICWSolidBody.html)

## VBA Syntax

See [CWSolidManager::GetSolidBodyByName](ms-its:cworksapivb6.chm::/CosmosWorksLib~CWSolidManager~GetSolidBodyByName.html).

## See Also

[ICWSolidManager Interface](SolidWorks.Interop.cosworks~SolidWorks.Interop.cosworks.ICWSolidManager.html)
[ICWSolidManager Members](SolidWorks.Interop.cosworks~SolidWorks.Interop.cosworks.ICWSolidManager_members.html)

## Availability

SOLIDWORKS Simulation API 2017 SP0
