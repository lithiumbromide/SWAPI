---
title: "Rollback2 Method (IEdmHistory5)"
project: "SOLIDWORKS PDM Professional API Help"
interface: "IEdmHistory5"
member: "Rollback2"
kind: "method"
source: "epdmapi/EPDM.Interop.epdm~EPDM.Interop.epdm.IEdmHistory5~Rollback2.html"
---

# Rollback2 Method (IEdmHistory5)

Rolls back the specified file.

## Syntax

### Visual Basic

```vb
Sub Rollback2( _
   ByRef historyItem As EdmHistoryItem2 _
)
```

### C#

```csharp
void Rollback2(
   ref EdmHistoryItem2 historyItem
)
```

### C++/CLI

```cpp
void Rollback2(
   EdmHistoryItem2% historyItem
)
```

### Parameters

- `historyItem`: [EdmHistoryItem2](EPDM.Interop.epdm~EPDM.Interop.epdm.EdmHistoryItem2.html) to which to roll back

## Examples

See the [IEdmHistory3](EPDM.Interop.epdm~EPDM.Interop.epdm.IEdmHistory3.html) examples.

## Remarks

To populate historyItem, get the collection of history items by calling [IEdmHistory5::GetHistory2](EPDM.Interop.epdm~EPDM.Interop.epdm.IEdmHistory5~GetHistory2.html).

[Return codes](ReturnCodes.htm):

- S_OK: The method successfully executed.
- S_FALSE: One of the arguments is invalid.

## See Also

[IEdmHistory5 Interface](EPDM.Interop.epdm~EPDM.Interop.epdm.IEdmHistory5.html)
[IEdmHistory5 Members](EPDM.Interop.epdm~EPDM.Interop.epdm.IEdmHistory5_members.html)
[IEdmHistory5::GetHistory2 Method ()](EPDM.Interop.epdm~EPDM.Interop.epdm.IEdmHistory5~GetHistory2.html)
[IEdmHistory5::GetSortedHistory2 Method ()](EPDM.Interop.epdm~EPDM.Interop.epdm.IEdmHistory5~GetSortedHistory2.html)
[IEdmHistory5::GetEventDescription2 Method ()](EPDM.Interop.epdm~EPDM.Interop.epdm.IEdmHistory5~GetEventDescription2.html)

## Availability

SOLIDWORKS PDM Professional 2026 SP02
