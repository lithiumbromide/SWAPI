---
title: "AddFileFromVault Method (IEdmBatchAdd)"
project: "SOLIDWORKS PDM Professional API Help"
interface: "IEdmBatchAdd"
member: "AddFileFromVault"
kind: "method"
source: "API_GB/EPDM.Interop.epdm~EPDM.Interop.epdm.IEdmBatchAdd~AddFileFromVault.html"
---

# AddFileFromVault Method (IEdmBatchAdd)

Adds a file with the specified ID and folder ID to the batch of files to be added to the vault; the file will be copied to a new vault folder with the specified ID.

## Syntax

### Visual Basic

```vb
Sub AddFileFromVault( _
   ByVal lSourceFileID As System.Integer, _
   ByVal lSourceFolderID As System.Integer, _
   ByVal lDestinationFolderID As System.Integer, _
   Optional ByVal lArg As System.Integer, _
   Optional ByVal bsNewName As System.String, _
   Optional ByVal lEdmAddFlags As System.Integer _
)
```

### C#

```csharp
void AddFileFromVault(
   System.int lSourceFileID,
   System.int lSourceFolderID,
   System.int lDestinationFolderID,
   System.int lArg,
   System.string bsNewName,
   System.int lEdmAddFlags
)
```

### C++/CLI

```cpp
void AddFileFromVault(
   System.int lSourceFileID,
   System.int lSourceFolderID,
   System.int lDestinationFolderID,
   System.int lArg,
   System.String^ bsNewName,
   System.int lEdmAddFlags
)
```

### Parameters

- `lSourceFileID`: ID of file to copy
- `lSourceFolderID`: ID of folder of file to copy
- `lDestinationFolderID`: ID of folder to which to copy the file
- `lArg`: Caller-defined argument.
- `bsNewName`: Optional new name of file.
- `lEdmAddFlags`: Combination of [EdmAddFlag](EPDM.Interop.epdm~EPDM.Interop.epdm.EdmAddFlag.html) bits

## Remarks

Before calling this method, use [IEdmBatchAdd::SetFileNameSerNo](EPDM.Interop.epdm~EPDM.Interop.epdm.IEdmBatchAdd~SetFileNameSerNo.html) to specify how to create the name for the new file's data card.

After calling this method, you must call [IEdmBatchAdd::CommitAdd](EPDM.Interop.epdm~EPDM.Interop.epdm.IEdmBatchAdd~CommitAdd.html) to actually add the file to the vault.

[Return codes](ReturnCodes.htm):

- S_OK: The method successfully executed.
- S_FALSE: One of the arguments is invalid.

## See Also

[IEdmBatchAdd Interface](EPDM.Interop.epdm~EPDM.Interop.epdm.IEdmBatchAdd.html)
[IEdmBatchAdd Members](EPDM.Interop.epdm~EPDM.Interop.epdm.IEdmBatchAdd_members.html)

## Availability

Version 6.4 of SOLIDWORKS PDM Professional
