---
title: "GetSortedHistory2 Method (IEdmHistory5)"
project: "SOLIDWORKS PDM Professional API Help"
interface: "IEdmHistory5"
member: "GetSortedHistory2"
kind: "method"
source: "epdmapi/EPDM.Interop.epdm~EPDM.Interop.epdm.IEdmHistory5~GetSortedHistory2.html"
---

# GetSortedHistory2 Method (IEdmHistory5)

Gets the history listing for the specified history types.

## Syntax

### Visual Basic

```vb
Sub GetSortedHistory2( _
   ByRef ppoRetHistory() As EdmHistoryItem2, _
   Optional ByVal lEdmHistoryTypes As System.Integer _
)
```

### C#

```csharp
void GetSortedHistory2(
   out EdmHistoryItem2[] ppoRetHistory,
   System.int lEdmHistoryTypes
)
```

### C++/CLI

```cpp
void GetSortedHistory2(
   [Out] array<EdmHistoryItem2>^ ppoRetHistory,
   System.int lEdmHistoryTypes
)
```

### Parameters

- `ppoRetHistory`: Array of [EdmHistoryItem2](EPDM.Interop.epdm~EPDM.Interop.epdm.EdmHistoryItem2.html) structures; one structure for each history item (see **Remarks**)
- `lEdmHistoryTypes`: Combination of [EdmHistoryType](EPDM.Interop.epdm~EPDM.Interop.epdm.EdmHistoryType.html) bits; indicates the kinds of records to retrieve

## Examples

See the [IEdmHistory3](EPDM.Interop.epdm~EPDM.Interop.epdm.IEdmHistory3.html) examples.

## Remarks

This method works in both Web 2 and thick client applications.

Call this method after calling [IEdmHistory::AddFile](EPDM.Interop.epdm~EPDM.Interop.epdm.IEdmHistory~AddFile.html) and [IEdmHistory::AddFolder](EPDM.Interop.epdm~EPDM.Interop.epdm.IEdmHistory~AddFolder.html).

The returned array of history items in ppoRetHistory is sorted with the most recent records at the beginning.

Call [IEdmHistory5::GetEventDescription2](EPDM.Interop.epdm~EPDM.Interop.epdm.IEdmHistory5~GetEventDescription2.html), passing one of the EdmHistoryItem structures returned by this method, to obtain its event description.

[Return codes](ReturnCodes.htm):

- S_OK: The method successfully executed.
- S_FALSE: One of the arguments is invalid.

## See Also

[IEdmHistory5 Interface](EPDM.Interop.epdm~EPDM.Interop.epdm.IEdmHistory5.html)
[IEdmHistory5 Members](EPDM.Interop.epdm~EPDM.Interop.epdm.IEdmHistory5_members.html)
[IEdmHistory5::GetHistory2 Method ()](EPDM.Interop.epdm~EPDM.Interop.epdm.IEdmHistory5~GetHistory2.html)
[IEdmHistory5::GetEventDescription2 Method ()](EPDM.Interop.epdm~EPDM.Interop.epdm.IEdmHistory5~GetEventDescription2.html)
[IEdmHistory5::Rollback2 Method ()](EPDM.Interop.epdm~EPDM.Interop.epdm.IEdmHistory5~Rollback2.html)

## Availability

SOLIDWORKS PDM Professional 2026 SP02
