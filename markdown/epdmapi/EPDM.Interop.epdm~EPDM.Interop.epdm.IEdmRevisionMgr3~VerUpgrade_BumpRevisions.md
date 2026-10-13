---
title: "VerUpgrade_BumpRevisions Method (IEdmRevisionMgr3)"
project: "SOLIDWORKS PDM Professional API Help"
interface: "IEdmRevisionMgr3"
member: "VerUpgrade_BumpRevisions"
kind: "method"
source: "epdmapi/EPDM.Interop.epdm~EPDM.Interop.epdm.IEdmRevisionMgr3~VerUpgrade_BumpRevisions.html"
---

# VerUpgrade_BumpRevisions Method (IEdmRevisionMgr3)

Moves all revisions set on the second-to-latest version to the latest version.

## Syntax

### Visual Basic

```vb
Sub VerUpgrade_BumpRevisions( _
   ByVal poFiles() As EdmSelItem _
)
```

### C#

```csharp
void VerUpgrade_BumpRevisions(
   EdmSelItem[] poFiles
)
```

### C++/CLI

```cpp
void VerUpgrade_BumpRevisions(
   array<EdmSelItem>^ poFiles
)
```

### Parameters

- `poFiles`: Array of [EdmSelItem](EPDM.Interop.epdm~EPDM.Interop.epdm.EdmSelItem.html) structures; one structure for each file on which to bump the revision number (see **Remarks**)

## Remarks

You need to be logged in as a user that has permission to update revision numbers ([EdmSysRightFlags](EPDM.Interop.epdm~EPDM.Interop.epdm.EdmSysRightFlags.html).EdmSysRight_ModifyRevisionNumbers) in order to use this method. The reason you need this high level of permission is that this method overrides other permission settings on the file and changes the content of file history.

poFiles contains the array of files on which to bump revision numbers. Files lacking revisions on the second-to-latest version are ignored.

[Return codes:](ReturnCodes.htm)

- S_OK: The method successfully executed.

## See Also

[IEdmRevisionMgr3 Interface](EPDM.Interop.epdm~EPDM.Interop.epdm.IEdmRevisionMgr3.html)
[IEdmRevisionMgr3 Members](EPDM.Interop.epdm~EPDM.Interop.epdm.IEdmRevisionMgr3_members.html)

## Availability

SOLIDWORKS PDM Professional 2009
