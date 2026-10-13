---
title: "OnUpdateUI Method (IEdmMenu5)"
project: "SOLIDWORKS PDM Professional API Help"
interface: "IEdmMenu5"
member: "OnUpdateUI"
kind: "method"
source: "API_GB/EPDM.Interop.epdm~EPDM.Interop.epdm.IEdmMenu5~OnUpdateUI.html"
---

# OnUpdateUI Method (IEdmMenu5)

Updates the menu based on a new selection of files and folders.

## Syntax

### Visual Basic

```vb
Sub OnUpdateUI( _
   ByVal lSelFileCount As System.Integer, _
   ByVal lSelFolderCount As System.Integer, _
   Optional ByVal bAllItemsInSameFolder As System.Boolean _
)
```

### C#

```csharp
void OnUpdateUI(
   System.int lSelFileCount,
   System.int lSelFolderCount,
   System.bool bAllItemsInSameFolder
)
```

### C++/CLI

```cpp
void OnUpdateUI(
   System.int lSelFileCount,
   System.int lSelFolderCount,
   System.bool bAllItemsInSameFolder
)
```

### Parameters

- `lSelFileCount`: Number of selected files
- `lSelFolderCount`: Number of selected folders
- `bAllItemsInSameFolder`: True if all of the selected files and folders are located in the same parent folder, false if not

## Remarks

Some items in the menu might be grayed out or removed due to the currently selected number of files and folders. This method updates the menu based on a new selection of files and folders.

[Return code](ReturnCodes.htm) S_OK indicates that the method successfully executed.

## See Also

[IEdmMenu5 Interface](EPDM.Interop.epdm~EPDM.Interop.epdm.IEdmMenu5.html)
[IEdmMenu5 Members](EPDM.Interop.epdm~EPDM.Interop.epdm.IEdmMenu5_members.html)

## Availability

Version 5.2 of SOLIDWORKS PDM Professional
