---
title: "AddFolder Method (IEdmBatchListing)"
project: "SOLIDWORKS PDM Professional API Help"
interface: "IEdmBatchListing"
member: "AddFolder"
kind: "method"
source: "API_GB/EPDM.Interop.epdm~EPDM.Interop.epdm.IEdmBatchListing~AddFolder.html"
---

# AddFolder Method (IEdmBatchListing)

Adds a folder to the batch of folders for which to create a listing.

## Syntax

### Visual Basic

```vb
Sub AddFolder( _
   ByVal oIdOrPath As System.Object, _
   ByVal lParam As System.Integer, _
   Optional ByVal lEdmListFolderFlags As System.Integer _
)
```

### C#

```csharp
void AddFolder(
   System.object oIdOrPath,
   System.int lParam,
   System.int lEdmListFolderFlags
)
```

### C++/CLI

```cpp
void AddFolder(
   System.Object^ oIdOrPath,
   System.int lParam,
   System.int lEdmListFolderFlags
)
```

### Parameters

- `oIdOrPath`: ID of folder to add; path is not supported in SOLIDWORKS PDM 2010
- `lParam`: Caller-defined argument
- `lEdmListFolderFlags`: Only [EdmListFiolderFlags](EPDM.Interop.epdm~EPDM.Interop.epdm.EdmListFolderFlags.html).EdmListFolder_Recursive is supported

## Remarks

After calling this method for each folder whose properties you want to list, call [IEdmBatchListing::CreateList](EPDM.Interop.epdm~EPDM.Interop.epdm.IEdmBatchListing~CreateList.html) to create a listing of all the folders' properties.

[Return codes](ReturnCodes.htm):

- S_OK: The method successfully executed.
- S_FALSE: One of the arguments is invalid.

## See Also

[IEdmBatchListing Interface](EPDM.Interop.epdm~EPDM.Interop.epdm.IEdmBatchListing.html)
[IEdmBatchListing Members](EPDM.Interop.epdm~EPDM.Interop.epdm.IEdmBatchListing_members.html)

## Availability

SOLIDWORKS PDM 2010
