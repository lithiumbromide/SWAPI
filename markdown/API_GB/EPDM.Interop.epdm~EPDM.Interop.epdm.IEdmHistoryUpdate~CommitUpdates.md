---
title: "CommitUpdates Method (IEdmHistoryUpdate)"
project: "SOLIDWORKS PDM Professional API Help"
interface: "IEdmHistoryUpdate"
member: "CommitUpdates"
kind: "method"
source: "API_GB/EPDM.Interop.epdm~EPDM.Interop.epdm.IEdmHistoryUpdate~CommitUpdates.html"
---

# CommitUpdates Method (IEdmHistoryUpdate)

Commits all of the updates in this batch.

## Syntax

### Visual Basic

```vb
Sub CommitUpdates()
```

### C#

```csharp
void CommitUpdates()
```

### C++/CLI

```cpp
void CommitUpdates();
```

## Examples

See the [IEdmHistoryUpdate](EPDM.Interop.epdm~EPDM.Interop.epdm.IEdmHistoryUpdate.html) examples.

## Remarks

This method must be called after calling [IEdmHistoryUpdate::UpdateVersionComment](EPDM.Interop.epdm~EPDM.Interop.epdm.IEdmHistoryUpdate~UpdateVersionComment.html) and [IEdmHistoryUpdate::UpdateRevisionComment](EPDM.Interop.epdm~EPDM.Interop.epdm.IEdmHistoryUpdate~UpdateRevisionComment.html), or all updates are discarded.

[Return codes](ReturnCodes.htm):

- S_OK: The method successfully executed.

## See Also

[IEdmHistoryUpdate Interface](EPDM.Interop.epdm~EPDM.Interop.epdm.IEdmHistoryUpdate.html)
[IEdmHistoryUpdate Members](EPDM.Interop.epdm~EPDM.Interop.epdm.IEdmHistoryUpdate_members.html)

## Availability

SOLIDWORKS PDM Professional 2008
