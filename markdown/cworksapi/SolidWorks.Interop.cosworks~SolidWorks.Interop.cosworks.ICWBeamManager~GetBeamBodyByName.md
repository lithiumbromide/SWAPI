---
title: "GetBeamBodyByName Method (ICWBeamManager)"
project: "SOLIDWORKS Simulation API Help"
interface: "ICWBeamManager"
member: "GetBeamBodyByName"
kind: "method"
source: "cworksapi/SolidWorks.Interop.cosworks~SolidWorks.Interop.cosworks.ICWBeamManager~GetBeamBodyByName.html"
---

# GetBeamBodyByName Method (ICWBeamManager)

Gets the specified beam body.

## Syntax

### Visual Basic (Declaration)

```vb
Function GetBeamBodyByName( _
   ByVal SBeamBodyName As System.String, _
   ByRef ErrorCode As System.Integer _
) As CWBeamBody
```

### Visual Basic (Usage)

```vb
Dim instance As ICWBeamManager
Dim SBeamBodyName As System.String
Dim ErrorCode As System.Integer
Dim value As CWBeamBody

value = instance.GetBeamBodyByName(SBeamBodyName, ErrorCode)
```

### C#

```csharp
CWBeamBody GetBeamBodyByName(
   System.string SBeamBodyName,
   out System.int ErrorCode
)
```

### C++/CLI

```cpp
CWBeamBody^ GetBeamBodyByName(
   System.String^ SBeamBodyName,
   [Out] System.int ErrorCode
)
```

### Parameters

- `SBeamBodyName`: Name of beam body
- `ErrorCode`: 0 if successful, 1 if not

### Return Value

[ICWBeamBody](SolidWorks.Interop.cosworks~SolidWorks.Interop.cosworks.ICWBeamBody.html)

## VBA Syntax

See [CWBeamManager::GetBeamBodyByName](ms-its:cworksapivb6.chm::/CosmosWorksLib~CWBeamManager~GetBeamBodyByName.html).

## See Also

[ICWBeamManager Interface](SolidWorks.Interop.cosworks~SolidWorks.Interop.cosworks.ICWBeamManager.html)
[ICWBeamManager Members](SolidWorks.Interop.cosworks~SolidWorks.Interop.cosworks.ICWBeamManager_members.html)
[ICWBeamManager::GetBeamBodyAt Method ()](SolidWorks.Interop.cosworks~SolidWorks.Interop.cosworks.ICWBeamManager~GetBeamBodyAt.html)

## Availability

SOLIDWORKS Simulation API 2017 SP0
