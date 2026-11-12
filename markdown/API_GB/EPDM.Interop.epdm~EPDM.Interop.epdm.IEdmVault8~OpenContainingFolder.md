---
title: "OpenContainingFolder Method (IEdmVault8)"
project: "SOLIDWORKS PDM Professional API Help"
interface: "IEdmVault8"
member: "OpenContainingFolder"
kind: "method"
source: "API_GB/EPDM.Interop.epdm~EPDM.Interop.epdm.IEdmVault8~OpenContainingFolder.html"
---

# OpenContainingFolder Method (IEdmVault8)

Opens File Explorer on the specified folder and selects the specified file.

## Syntax

### Visual Basic

```vb
Sub OpenContainingFolder( _
   ByVal oFilePathOrID As System.Object, _
   Optional ByVal oFolderPathOrID As System.Object _
)
```

### C#

```csharp
void OpenContainingFolder(
   System.object oFilePathOrID,
   System.object oFolderPathOrID
)
```

### C++/CLI

```cpp
void OpenContainingFolder(
   System.Object^ oFilePathOrID,
   System.Object^ oFolderPathOrID
)
```

### Parameters

- `oFilePathOrID`: ID or path of file to select; 0 to ignore (see **Remarks**)
- `oFolderPathOrID`: ID or path of folder on which to open File Explorer; 0 to ignore

## Examples

| OpenContainingFolder 102, 33 | Opens folder with ID, 33, and selects file with ID, 102. |
| --- | --- |
| OpenContainingFolder “c:\TheVault\SubFolder\test.txt” | Opens folder, SubFolder, and selects file, test.txt. |
| OpenContainingFolder 0, 45 | Opens the parent folder of folder with ID, 45, and selects the folder with ID, 45. |
| OpenContainingFolder 321, 0 | Opens first folder where file with ID, 321, is found and selects the file. |
| OpenContainingFolder 0, “c:\TheVault\SubFolder” | Opens the vault root folder and selects the folder, SubFolder. |

## Remarks

If oFilePathOrID is a path to a file, oFolderPathOrID is ignored.

## See Also

[IEdmVault8 Interface](EPDM.Interop.epdm~EPDM.Interop.epdm.IEdmVault8.html)
[IEdmVault8 Members](EPDM.Interop.epdm~EPDM.Interop.epdm.IEdmVault8_members.html)

## Availability

SOLIDWORKS PDM Professional Version 6.4
