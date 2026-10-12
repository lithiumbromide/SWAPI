---
title: "AddSelectionEx Method (IEdmBatchGet)"
project: "SOLIDWORKS PDM Professional API Help"
interface: "IEdmBatchGet"
member: "AddSelectionEx"
kind: "method"
source: "epdmapi/EPDM.Interop.epdm~EPDM.Interop.epdm.IEdmBatchGet~AddSelectionEx.html"
---

# AddSelectionEx Method (IEdmBatchGet)

Adds a file with the specified ID and version to the batch of files to get.

## Syntax

### Visual Basic

```vb
Sub AddSelectionEx( _
   ByVal poVault As EdmVault5, _
   ByVal lFileID As System.Integer, _
   ByVal lParentFolderID As System.Integer, _
   ByVal oVersionOrFileDate As System.Object _
)
```

### C#

```csharp
void AddSelectionEx(
   EdmVault5 poVault,
   System.int lFileID,
   System.int lParentFolderID,
   System.object oVersionOrFileDate
)
```

### C++/CLI

```cpp
void AddSelectionEx(
   EdmVault5^ poVault,
   System.int lFileID,
   System.int lParentFolderID,
   System.Object^ oVersionOrFileDate
)
```

### Parameters

- `poVault`: [IEdmVault5](EPDM.Interop.epdm~EPDM.Interop.epdm.IEdmVault5.html); vault from which to get the file
- `lFileID`: ID of file to get
- `lParentFolderID`: ID of the file's parent folder
- `oVersionOrFileDate`: Number or modified date of the version of the file to get

## Remarks

[Return codes](ReturnCodes.htm):

- S_OK: The method successfully executed.
- S_FALSE: One of the arguments is invalid.

## See Also

[IEdmBatchGet Interface](EPDM.Interop.epdm~EPDM.Interop.epdm.IEdmBatchGet.html)
[IEdmBatchGet Members](EPDM.Interop.epdm~EPDM.Interop.epdm.IEdmBatchGet_members.html)

## Availability

Version 6.3 of SOLIDWORKS PDM Professional
