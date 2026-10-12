---
title: "UpdateRevisionComment Method (IEdmHistoryUpdate)"
project: "SOLIDWORKS PDM Professional API Help"
interface: "IEdmHistoryUpdate"
member: "UpdateRevisionComment"
kind: "method"
source: "API_GB/EPDM.Interop.epdm~EPDM.Interop.epdm.IEdmHistoryUpdate~UpdateRevisionComment.html"
---

# UpdateRevisionComment Method (IEdmHistoryUpdate)

Updates a revision comment.

## Syntax

### Visual Basic

```vb
Sub UpdateRevisionComment( _
   ByVal lFileID As System.Integer, _
   ByVal bsRevisionName As System.String, _
   ByVal lVersionNo As System.Integer, _
   ByVal bsNewComment As System.String _
)
```

### C#

```csharp
void UpdateRevisionComment(
   System.int lFileID,
   System.string bsRevisionName,
   System.int lVersionNo,
   System.string bsNewComment
)
```

### C++/CLI

```cpp
void UpdateRevisionComment(
   System.int lFileID,
   System.String^ bsRevisionName,
   System.int lVersionNo,
   System.String^ bsNewComment
)
```

### Parameters

- `lFileID`: ID of file for which to update a comment
- `bsRevisionName`: Name of revision for which to update a comment: "" for all revisions
- `lVersionNo`: ID of version for which to update a comment; -1 for all versions
- `bsNewComment`: New revision comment

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
