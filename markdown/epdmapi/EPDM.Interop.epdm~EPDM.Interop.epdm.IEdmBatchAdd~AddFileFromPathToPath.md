---
title: "AddFileFromPathToPath Method (IEdmBatchAdd)"
project: "SOLIDWORKS PDM Professional API Help"
interface: "IEdmBatchAdd"
member: "AddFileFromPathToPath"
kind: "method"
source: "epdmapi/EPDM.Interop.epdm~EPDM.Interop.epdm.IEdmBatchAdd~AddFileFromPathToPath.html"
---

# AddFileFromPathToPath Method (IEdmBatchAdd)

Adds a file to the batch of files to be added to the vault; the file will be copied to the specified destination folder path.

## Syntax

### Visual Basic

```vb
Sub AddFileFromPathToPath( _
   ByVal bsSourcePath As System.String, _
   ByVal bsDestinationFolderPath As System.String, _
   Optional ByVal lArg As System.Integer, _
   Optional ByVal bsNewName As System.String, _
   Optional ByVal lEdmAddFlags As System.Integer _
)
```

### C#

```csharp
void AddFileFromPathToPath(
   System.string bsSourcePath,
   System.string bsDestinationFolderPath,
   System.int lArg,
   System.string bsNewName,
   System.int lEdmAddFlags
)
```

### C++/CLI

```cpp
void AddFileFromPathToPath(
   System.String^ bsSourcePath,
   System.String^ bsDestinationFolderPath,
   System.int lArg,
   System.String^ bsNewName,
   System.int lEdmAddFlags
)
```

### Parameters

- `bsSourcePath`: Path of file to add
- `bsDestinationFolderPath`: Path of folder to which to add the file
- `lArg`: Caller-defined argument
- `bsNewName`: Optional new name of the added file
- `lEdmAddFlags`: Combination of [EdmAddFlag](EPDM.Interop.epdm~EPDM.Interop.epdm.EdmAddFlag.html) bits

## Examples

See the [IEdmBatchAdd](EPDM.Interop.epdm~EPDM.Interop.epdm.IEdmBatchAdd.html) examples.

## Remarks

Before calling this method, use [IEdmBatchAdd::SetFileNameSerNo](EPDM.Interop.epdm~EPDM.Interop.epdm.IEdmBatchAdd~SetFileNameSerNo.html) to specify how to create the name for the new file's data card.

If the specified bsDestinationFolderPath does not exist in the vault, it will be created when the file is added.

After calling this method, you must call [IEdmBatchAdd::CommitAdd](EPDM.Interop.epdm~EPDM.Interop.epdm.IEdmBatchAdd~CommitAdd.html) to actually add the file to the vault.

[Return codes](ReturnCodes.htm):

- S_OK: The method successfully executed.
- S_FALSE: One of the arguments is invalid.

## See Also

[IEdmBatchAdd Interface](EPDM.Interop.epdm~EPDM.Interop.epdm.IEdmBatchAdd.html)
[IEdmBatchAdd Members](EPDM.Interop.epdm~EPDM.Interop.epdm.IEdmBatchAdd_members.html)

## Availability

Version 6.4 of SOLIDWORKS PDM Professional
