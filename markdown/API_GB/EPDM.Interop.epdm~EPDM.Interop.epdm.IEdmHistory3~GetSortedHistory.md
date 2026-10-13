---
title: "GetSortedHistory Method (IEdmHistory3)"
project: "SOLIDWORKS PDM Professional API Help"
interface: "IEdmHistory3"
member: "GetSortedHistory"
kind: "method"
source: "API_GB/EPDM.Interop.epdm~EPDM.Interop.epdm.IEdmHistory3~GetSortedHistory.html"
---

# GetSortedHistory Method (IEdmHistory3)

Gets the history listing for the specified history types.

## Syntax

### Visual Basic

```vb
Sub GetSortedHistory( _
   ByRef ppoRetHistory As EdmHistoryItem(), _
   Optional ByVal lEdmHistoryTypes As System.Integer _
)
```

### C#

```csharp
void GetSortedHistory(
   out EdmHistoryItem[] ppoRetHistory,
   System.int lEdmHistoryTypes
)
```

### C++/CLI

```cpp
void GetSortedHistory(
   [Out] array<EdmHistoryItem> ppoRetHistory,
   System.int lEdmHistoryTypes
)
```

### Parameters

- `ppoRetHistory`: Array of [EdmHistoryItem](EPDM.Interop.epdm~EPDM.Interop.epdm.EdmHistoryItem.html) structures; one structure for each history item (see **Remarks**)
- `lEdmHistoryTypes`: Combination of [EdmHistoryType](EPDM.Interop.epdm~EPDM.Interop.epdm.EdmHistoryType.html) bits; indicates the kinds of records to retrieve

## Examples

See the [IEdmHistory3](EPDM.Interop.epdm~EPDM.Interop.epdm.IEdmHistory3.html) examples.

## Remarks

This method works in both Web 2 and thick client applications.

Call this method after calling [IEdmHistory::AddFile](EPDM.Interop.epdm~EPDM.Interop.epdm.IEdmHistory~AddFile.html) and [IEdmHistory::AddFolder](EPDM.Interop.epdm~EPDM.Interop.epdm.IEdmHistory~AddFolder.html).

The returned array of history items in ppoRetHistory is sorted with the most recent records at the beginning.

Call [IEdmHistory3::GetEventDescription](EPDM.Interop.epdm~EPDM.Interop.epdm.IEdmHistory3~GetEventDescription.html), passing one of the EdmHistoryItem structures returned by this method, to obtain its event description.

[Return codes](ReturnCodes.htm):

- S_OK: The method successfully executed.
- S_FALSE: One of the arguments is invalid.

## See Also

[IEdmHistory3 Interface](EPDM.Interop.epdm~EPDM.Interop.epdm.IEdmHistory3.html)
[IEdmHistory3 Members](EPDM.Interop.epdm~EPDM.Interop.epdm.IEdmHistory3_members.html)
[IEdmHistory2::Rollback Method ()](EPDM.Interop.epdm~EPDM.Interop.epdm.IEdmHistory2~Rollback.html)
[IEdmHistory::GetHistory Method ()](EPDM.Interop.epdm~EPDM.Interop.epdm.IEdmHistory~GetHistory.html)

## Availability

SOLIDWORKS PDM Professional 2020
