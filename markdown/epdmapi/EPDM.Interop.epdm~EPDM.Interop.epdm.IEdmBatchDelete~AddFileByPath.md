---
title: "AddFileByPath Method (IEdmBatchDelete)"
project: "SOLIDWORKS PDM Professional API Help"
interface: "IEdmBatchDelete"
member: "AddFileByPath"
kind: "method"
source: "epdmapi/EPDM.Interop.epdm~EPDM.Interop.epdm.IEdmBatchDelete~AddFileByPath.html"
---

# AddFileByPath Method (IEdmBatchDelete)

Adds a file with the specified path to the batch of files to be deleted.

## Syntax

### Visual Basic

```vb
Sub AddFileByPath( _
   ByVal bsPath As System.String _
)
```

### C#

```csharp
void AddFileByPath(
   System.string bsPath
)
```

### C++/CLI

```cpp
void AddFileByPath(
   System.String^ bsPath
)
```

### Parameters

- `bsPath`: Path of file to delete

## Examples

See the [IEdmBatchDelete](EPDM.Interop.epdm~EPDM.Interop.epdm.IEdmBatchDelete.html) examples.

## Remarks

After calling this method, call [IEdmBatchDelete::CommitDelete](EPDM.Interop.epdm~EPDM.Interop.epdm.IEdmBatchDelete~CommitDelete.html) to delete the file from the vault.

[Return codes](ReturnCodes.htm):

- S_OK: The method successfully executed.
- S_FALSE: One of the arguments is invalid.

## See Also

[IEdmBatchDelete Interface](EPDM.Interop.epdm~EPDM.Interop.epdm.IEdmBatchDelete.html)
[IEdmBatchDelete Members](EPDM.Interop.epdm~EPDM.Interop.epdm.IEdmBatchDelete_members.html)

## Availability

SOLIDWORKS PDM Professional 2008
