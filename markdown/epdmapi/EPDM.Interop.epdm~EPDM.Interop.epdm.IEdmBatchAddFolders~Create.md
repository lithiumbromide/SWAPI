---
title: "Create Method (IEdmBatchAddFolders)"
project: "SOLIDWORKS PDM Professional API Help"
interface: "IEdmBatchAddFolders"
member: "Create"
kind: "method"
source: "epdmapi/EPDM.Interop.epdm~EPDM.Interop.epdm.IEdmBatchAddFolders~Create.html"
---

# Create Method (IEdmBatchAddFolders)

Creates all the folders that were added to the batch using [IEdmBatchAddFolders::AddFolder](EPDM.Interop.epdm~EPDM.Interop.epdm.IEdmBatchAddFolders~AddFolder.html).

## Syntax

### Visual Basic

```vb
Sub Create( _
   ByVal lHwnd As System.Integer, _
   ByRef ppoRetFolders() As EdmFolderInfo, _
   Optional ByVal lEdmBatchCreateFolderFlags As System.Integer _
)
```

### C#

```csharp
void Create(
   System.int lHwnd,
   out EdmFolderInfo[] ppoRetFolders,
   System.int lEdmBatchCreateFolderFlags
)
```

### C++/CLI

```cpp
void Create(
   System.int lHwnd,
   [Out] array<EdmFolderInfo>^ ppoRetFolders,
   System.int lEdmBatchCreateFolderFlags
)
```

### Parameters

- `lHwnd`: Parent window handle that is passed to add-ins that are notified about folders added to the vault
- `ppoRetFolders`: Array of [EdmFolderInfo](EPDM.Interop.epdm~EPDM.Interop.epdm.EdmFolderInfo.html) structures; one structure for each folder added
- `lEdmBatchCreateFolderFlags`: Combination of [EdmBatchCreateFolderFlag](EPDM.Interop.epdm~EPDM.Interop.epdm.EdmBatchCreateFolderFlag.html) bits

## Examples

See the [IEdmBatchAddFolders](EPDM.Interop.epdm~EPDM.Interop.epdm.IEdmBatchAddFolders.html) examples.

## Remarks

[Return codes](ReturnCodes.htm):

- S_OK: The method successfully executed.
- E_EDM_COULD_NOT_CREATE_LOCAL_FOLDER: The folders were created in the vault but could not be created in the local cache.

## See Also

[IEdmBatchAddFolders Interface](EPDM.Interop.epdm~EPDM.Interop.epdm.IEdmBatchAddFolders.html)
[IEdmBatchAddFolders Members](EPDM.Interop.epdm~EPDM.Interop.epdm.IEdmBatchAddFolders_members.html)

## Availability

Version 6.3 of SOLIDWORKS PDM Professional
