---
title: "Rollback Method (IEdmHistory2)"
project: "SOLIDWORKS PDM Professional API Help"
interface: "IEdmHistory2"
member: "Rollback"
kind: "method"
source: "API_GB/EPDM.Interop.epdm~EPDM.Interop.epdm.IEdmHistory2~Rollback.html"
---

# Rollback Method (IEdmHistory2)

Rolls back the specified file.

## Syntax

### Visual Basic

```vb
Sub Rollback( _
   ByRef historyItem As EdmHistoryItem _
)
```

### C#

```csharp
void Rollback(
   ref EdmHistoryItem historyItem
)
```

### C++/CLI

```cpp
void Rollback(
   EdmHistoryItem% historyItem
)
```

### Parameters

- `historyItem`: [EdmHistoryItem](EPDM.Interop.epdm~EPDM.Interop.epdm.EdmHistoryItem.html) to which to roll back

## Examples

See the [IEdmHistory3](EPDM.Interop.epdm~EPDM.Interop.epdm.IEdmHistory3.html) examples.

## Remarks

To populate historyItem, get the collection of history items by calling [IEdmHistory::GetHistory](EPDM.Interop.epdm~EPDM.Interop.epdm.IEdmHistory~GetHistory.html).

[Return codes](ReturnCodes.htm):

- S_OK: The method successfully executed.
- S_FALSE: One of the arguments is invalid.

## See Also

[IEdmHistory2 Interface](EPDM.Interop.epdm~EPDM.Interop.epdm.IEdmHistory2.html)
[IEdmHistory2 Members](EPDM.Interop.epdm~EPDM.Interop.epdm.IEdmHistory2_members.html)

## Availability

SOLIDWORKS PDM Professional 2017
