---
title: "GetLocalVersionNo2 Method (IEdmFile12)"
project: "SOLIDWORKS PDM Professional API Help"
interface: "IEdmFile12"
member: "GetLocalVersionNo2"
kind: "method"
source: "API_GB/EPDM.Interop.epdm~EPDM.Interop.epdm.IEdmFile12~GetLocalVersionNo2.html"
---

# GetLocalVersionNo2 Method (IEdmFile12)

Gets the version number of the local copy of this file.

## Syntax

### Visual Basic

```vb
Function GetLocalVersionNo2( _
   ByRef poPathOrFolderID As System.Object, _
   ByRef pbLocalOverwrittenVersionObsolete As System.Boolean _
) As System.Integer
```

### C#

```csharp
System.int GetLocalVersionNo2(
   ref System.object poPathOrFolderID,
   out System.bool pbLocalOverwrittenVersionObsolete
)
```

### C++/CLI

```cpp
System.int GetLocalVersionNo2(
   System.Object^% poPathOrFolderID,
   [Out] System.bool pbLocalOverwrittenVersionObsolete
)
```

### Parameters

- `poPathOrFolderID`: ID of a folder, full file path, or folder path of the local copy of this file (see **Remarks**)
- `pbLocalOverwrittenVersionObsolete`: True if the file in the user's local cache is obsolete, false if it is valid (see **Remarks**)

### Return Value

Version number; -1 if the local copy does not match any version in the archive

## Remarks

If poPathOrFolderID is a folder path, it must be terminated by a backslash ('\').

pbLocalOverwrittenVersionObsolete gets whether a file in a user's local cache is obsolete because the file was overwritten by another user who checked out the file, modified the file, and checked in the file.

[Return codes](ReturnCodes.htm):

- S_OK: The method successfully executed.
- S_FALSE: One of the arguments is invalid.

## See Also

[IEdmFile12 Interface](EPDM.Interop.epdm~EPDM.Interop.epdm.IEdmFile12.html)
[IEdmFile12 Members](EPDM.Interop.epdm~EPDM.Interop.epdm.IEdmFile12_members.html)

## Availability

SOLIDWORKS PDM Professional 2017
