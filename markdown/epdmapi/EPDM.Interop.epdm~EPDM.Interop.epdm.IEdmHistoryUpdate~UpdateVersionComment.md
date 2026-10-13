---
title: "UpdateVersionComment Method (IEdmHistoryUpdate)"
project: "SOLIDWORKS PDM Professional API Help"
interface: "IEdmHistoryUpdate"
member: "UpdateVersionComment"
kind: "method"
source: "epdmapi/EPDM.Interop.epdm~EPDM.Interop.epdm.IEdmHistoryUpdate~UpdateVersionComment.html"
---

# UpdateVersionComment Method (IEdmHistoryUpdate)

Updates a version comment.

## Syntax

### Visual Basic

```vb
Sub UpdateVersionComment( _
   ByVal lFileID As System.Integer, _
   ByVal lVersionNo As System.Integer, _
   ByVal bsNewComment As System.String _
)
```

### C#

```csharp
void UpdateVersionComment(
   System.int lFileID,
   System.int lVersionNo,
   System.string bsNewComment
)
```

### C++/CLI

```cpp
void UpdateVersionComment(
   System.int lFileID,
   System.int lVersionNo,
   System.String^ bsNewComment
)
```

### Parameters

- `lFileID`: ID of file for which to update a comment
- `lVersionNo`: ID of version for which to update a comment; -1 for all versions
- `bsNewComment`: New version comment

## Examples

See the [IEdmHistoryUpdate](EPDM.Interop.epdm~EPDM.Interop.epdm.IEdmHistoryUpdate.html) examples.

## Remarks

After calling this method, you must call [IEdmHistoryUpdate::CommitUpdates](EPDM.Interop.epdm~EPDM.Interop.epdm.IEdmHistoryUpdate~CommitUpdates.html) to write the change to the database.

[Return codes](ReturnCodes.htm):

- S_OK: The method successfully executed.
- S_FALSE: One of the arguments is invalid.

## See Also

[IEdmHistoryUpdate Interface](EPDM.Interop.epdm~EPDM.Interop.epdm.IEdmHistoryUpdate.html)
[IEdmHistoryUpdate Members](EPDM.Interop.epdm~EPDM.Interop.epdm.IEdmHistoryUpdate_members.html)

## Availability

SOLIDWORKS PDM Professional 2008
