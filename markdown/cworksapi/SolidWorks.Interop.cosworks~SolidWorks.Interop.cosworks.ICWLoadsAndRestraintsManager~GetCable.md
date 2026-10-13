---
title: "GetCable Method (ICWLoadsAndRestraintsManager)"
project: "SOLIDWORKS Simulation API Help"
interface: "ICWLoadsAndRestraintsManager"
member: "GetCable"
kind: "method"
source: "cworksapi/SolidWorks.Interop.cosworks~SolidWorks.Interop.cosworks.ICWLoadsAndRestraintsManager~GetCable.html"
---

# GetCable Method (ICWLoadsAndRestraintsManager)

Gets the specified cable.

## Syntax

### Visual Basic (Declaration)

```vb
Function GetCable( _
   ByVal SName As System.String, _
   ByRef ErrorCode As System.Integer _
) As CWCable
```

### Visual Basic (Usage)

```vb
Dim instance As ICWLoadsAndRestraintsManager
Dim SName As System.String
Dim ErrorCode As System.Integer
Dim value As CWCable

value = instance.GetCable(SName, ErrorCode)
```

### C#

```csharp
CWCable GetCable(
   System.string SName,
   out System.int ErrorCode
)
```

### C++/CLI

```cpp
CWCable^ GetCable(
   System.String^ SName,
   [Out] System.int ErrorCode
)
```

### Parameters

- `SName`: Name of cable
- `ErrorCode`: Error as defined by [swsLoadsAndRestraintsErrors_e](SolidWorks.Interop.cosworks~SolidWorks.Interop.cosworks.swsLoadsAndRestraintsError_e.html)

### Return Value

[ICWCable](SolidWorks.Interop.cosworks~SolidWorks.Interop.cosworks.ICWCable.html)

## VBA Syntax

See [CWLoadsAndRestraintsManager::GetCable](ms-its:cworksapivb6.chm::/CosmosWorksLib~CWLoadsAndRestraintsManager~GetCable.html).

## Examples

See the [ICWCable](SolidWorks.Interop.cosworks~SolidWorks.Interop.cosworks.ICWCable.html) example.

## See Also

[ICWLoadsAndRestraintsManager Interface](SolidWorks.Interop.cosworks~SolidWorks.Interop.cosworks.ICWLoadsAndRestraintsManager.html)
[ICWLoadsAndRestraintsManager Members](SolidWorks.Interop.cosworks~SolidWorks.Interop.cosworks.ICWLoadsAndRestraintsManager_members.html)
[ICWLoadsAndRestraintsManager::AddCable Method ()](SolidWorks.Interop.cosworks~SolidWorks.Interop.cosworks.ICWLoadsAndRestraintsManager~AddCable.html)

## Availability

SOLIDWORKS Simulation API 2026 SP0
