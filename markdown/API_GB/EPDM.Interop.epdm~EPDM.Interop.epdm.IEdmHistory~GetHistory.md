---
title: "GetHistory Method (IEdmHistory)"
project: "SOLIDWORKS PDM Professional API Help"
interface: "IEdmHistory"
member: "GetHistory"
kind: "method"
source: "API_GB/EPDM.Interop.epdm~EPDM.Interop.epdm.IEdmHistory~GetHistory.html"
---

# GetHistory Method (IEdmHistory)

Gets the unsorted history listing for the specified history types.

## Syntax

### Visual Basic

```vb
Sub GetHistory( _
   ByRef ppoRetHistory As EdmHistoryItem(), _
   Optional ByVal lEdmHistoryTypes As System.Integer _
)
```

### C#

```csharp
void GetHistory(
   out EdmHistoryItem[] ppoRetHistory,
   System.int lEdmHistoryTypes
)
```

### C++/CLI

```cpp
void GetHistory(
   [Out] array<EdmHistoryItem> ppoRetHistory,
   System.int lEdmHistoryTypes
)
```

### Parameters

- `ppoRetHistory`: Array of [EdmHistoryItem](EPDM.Interop.epdm~EPDM.Interop.epdm.EdmHistoryItem.html) structures; one structure for each history item (see **Remarks**)
- `lEdmHistoryTypes`: Combination of [EdmHistoryType](EPDM.Interop.epdm~EPDM.Interop.epdm.EdmHistoryType.html) bits; indicates the kinds of records to retrieve

## Remarks

Call this method after calling [IEdmHistory::AddFile](EPDM.Interop.epdm~EPDM.Interop.epdm.IEdmHistory~AddFile.html) and [IEdmHistory::AddFolder](EPDM.Interop.epdm~EPDM.Interop.epdm.IEdmHistory~AddFolder.html).

[Return codes](ReturnCodes.htm):

- S_OK: The method successfully executed.
- S_FALSE: One of the arguments is invalid.

## See Also

[IEdmHistory Interface](EPDM.Interop.epdm~EPDM.Interop.epdm.IEdmHistory.html)
[IEdmHistory Members](EPDM.Interop.epdm~EPDM.Interop.epdm.IEdmHistory_members.html)
[IEdmHistory2::Rollback Method ()](EPDM.Interop.epdm~EPDM.Interop.epdm.IEdmHistory2~Rollback.html)
[IEdmHistory3::GetSortedHistory Method ()](EPDM.Interop.epdm~EPDM.Interop.epdm.IEdmHistory3~GetSortedHistory.html)

## Availability

SOLIDWORKS PDM Professional Version 6.4
