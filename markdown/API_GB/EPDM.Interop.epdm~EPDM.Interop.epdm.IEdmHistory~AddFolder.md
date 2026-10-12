---
title: "AddFolder Method (IEdmHistory)"
project: "SOLIDWORKS PDM Professional API Help"
interface: "IEdmHistory"
member: "AddFolder"
kind: "method"
source: "API_GB/EPDM.Interop.epdm~EPDM.Interop.epdm.IEdmHistory~AddFolder.html"
---

# AddFolder Method (IEdmHistory)

Adds a folder to the history listing.

## Syntax

### Visual Basic

```vb
Sub AddFolder( _
   ByVal lFolderID As System.Integer, _
   ByVal lEdmFolderHistoryFlags As System.Integer _
)
```

### C#

```csharp
void AddFolder(
   System.int lFolderID,
   System.int lEdmFolderHistoryFlags
)
```

### C++/CLI

```cpp
void AddFolder(
   System.int lFolderID,
   System.int lEdmFolderHistoryFlags
)
```

### Parameters

- `lFolderID`: ID of folder to add
- `lEdmFolderHistoryFlags`: Combination of [EdmFolderHistoryFlag](EPDM.Interop.epdm~EPDM.Interop.epdm.EdmFolderHistoryFlag.html) bits (see **Remarks**)

## Remarks

lEdmFolderHistoryFlags indicates whether subfolders are added recursively and whether files in the specified folder are added.

After all the files and folders have been added, call [IEdmHistory::GetHistory](EPDM.Interop.epdm~EPDM.Interop.epdm.IEdmHistory~GetHistory.html) to obtain the actual history listing.

[Return codes](ReturnCodes.htm):

- S_OK: The method successfully executed.
- S_FALSE: One of the arguments is invalid.

## See Also

[IEdmHistory Interface](EPDM.Interop.epdm~EPDM.Interop.epdm.IEdmHistory.html)
[IEdmHistory Members](EPDM.Interop.epdm~EPDM.Interop.epdm.IEdmHistory_members.html)

## Availability

SOLIDWORKS PDM Professional Version 6.4
