---
title: "AddFileFromPath Method (IEdmBatchAdd)"
project: "SOLIDWORKS PDM Professional API Help"
interface: "IEdmBatchAdd"
member: "AddFileFromPath"
kind: "method"
source: "epdmapi/EPDM.Interop.epdm~EPDM.Interop.epdm.IEdmBatchAdd~AddFileFromPath.html"
---

# AddFileFromPath Method (IEdmBatchAdd)

Adds a file to the batch of files to be added to the vault; the file will be copied to a destination folder with the specified ID.

## Syntax

### Visual Basic

```vb
Sub AddFileFromPath( _
   ByVal bsSourcePath As System.String, _
   ByVal lDestinationFolderID As System.Integer, _
   Optional ByVal lArg As System.Integer, _
   Optional ByVal bsNewName As System.String, _
   Optional ByVal lEdmAddFlags As System.Integer _
)
```

### C#

```csharp
void AddFileFromPath(
   System.string bsSourcePath,
   System.int lDestinationFolderID,
   System.int lArg,
   System.string bsNewName,
   System.int lEdmAddFlags
)
```

### C++/CLI

```cpp
void AddFileFromPath(
   System.String^ bsSourcePath,
   System.int lDestinationFolderID,
   System.int lArg,
   System.String^ bsNewName,
   System.int lEdmAddFlags
)
```

### Parameters

- `bsSourcePath`: Path of file to add
- `lDestinationFolderID`: ID of folder to which to add the file
- `lArg`: Caller-defined argument
- `bsNewName`: Optional new name of the added file
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
