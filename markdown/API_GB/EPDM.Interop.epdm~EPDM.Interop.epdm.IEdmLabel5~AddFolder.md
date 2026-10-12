---
title: "AddFolder Method (IEdmLabel5)"
project: "SOLIDWORKS PDM Professional API Help"
interface: "IEdmLabel5"
member: "AddFolder"
kind: "method"
source: "API_GB/EPDM.Interop.epdm~EPDM.Interop.epdm.IEdmLabel5~AddFolder.html"
---

# AddFolder Method (IEdmLabel5)

Sets this label on the specified folder and all of the files in that folder.

## Syntax

### Visual Basic

```vb
Sub AddFolder( _
   ByVal lFolderID As System.Integer, _
   ByVal bRecursive As System.Boolean _
)
```

### C#

```csharp
void AddFolder(
   System.int lFolderID,
   System.bool bRecursive
)
```

### C++/CLI

```cpp
void AddFolder(
   System.int lFolderID,
   System.bool bRecursive
)
```

### Parameters

- `lFolderID`: ID of folder on which to set this label
- `bRecursive`: True to recursively set this label on all subfolders, false to not

## Remarks

[Return codes](ReturnCodes.htm):

- S_OK: The method successfully executed.
- S_FALSE: One of the arguments is invalid.

## See Also

[IEdmLabel5 Interface](EPDM.Interop.epdm~EPDM.Interop.epdm.IEdmLabel5.html)
[IEdmLabel5 Members](EPDM.Interop.epdm~EPDM.Interop.epdm.IEdmLabel5_members.html)

## Availability

SOLIDWORKS PDM Professional Version 5.2
