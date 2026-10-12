---
title: "AddFolderPath Method (IEdmBatchAdd)"
project: "SOLIDWORKS PDM Professional API Help"
interface: "IEdmBatchAdd"
member: "AddFolderPath"
kind: "method"
source: "epdmapi/EPDM.Interop.epdm~EPDM.Interop.epdm.IEdmBatchAdd~AddFolderPath.html"
---

# AddFolderPath Method (IEdmBatchAdd)

Adds the specified folder path to the batch of folders to be added to the vault.

## Syntax

### Visual Basic

```vb
Sub AddFolderPath( _
   ByVal bsLocalPath As System.String, _
   ByVal lArg As System.Integer, _
   Optional ByVal lEdmBatchAddFolderFlags As System.Integer, _
   Optional ByVal poData As EdmFolderData, _
   Optional ByVal lSourceFolderID As System.Integer _
)
```

### C#

```csharp
void AddFolderPath(
   System.string bsLocalPath,
   System.int lArg,
   System.int lEdmBatchAddFolderFlags,
   EdmFolderData poData,
   System.int lSourceFolderID
)
```

### C++/CLI

```cpp
void AddFolderPath(
   System.String^ bsLocalPath,
   System.int lArg,
   System.int lEdmBatchAddFolderFlags,
   EdmFolderData^ poData,
   System.int lSourceFolderID
)
```

### Parameters

- `bsLocalPath`: File system path to folder to create; path leads in to the file vault; all folders missing in the path are created
- `lArg`: Caller-defined argument
- `lEdmBatchAddFolderFlags`: Combination of [EdmBatchAddFolderFlag](EPDM.Interop.epdm~EPDM.Interop.epdm.EdmBatchAddFolderFlag.html) bits
- `poData`: Optional [IEdmFolderData5](EPDM.Interop.epdm~EPDM.Interop.epdm.IEdmFolderData5.html); extra information about the folder to create
- `lSourceFolderID`: Optional ID of source folder from which to copy properties

## Examples

See the [IEdmBatchAdd](EPDM.Interop.epdm~EPDM.Interop.epdm.IEdmBatchAdd.html) examples.

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
