---
title: "IEdmBatchListing Interface"
project: "SOLIDWORKS PDM Professional API Help"
interface: "IEdmBatchListing"
member: ""
kind: "interface"
source: "epdmapi/EPDM.Interop.epdm~EPDM.Interop.epdm.IEdmBatchListing.html"
---

# IEdmBatchListing Interface

Allows you to create a listing of various file or folder properties.

**NOTE:** Click the **Members** link, located near the top of the topic, to see this interface's methods and properties.

## Syntax

### Visual Basic

```vb
Public Interface IEdmBatchListing
```

### C#

```csharp
public interface IEdmBatchListing
```

### C++/CLI

```cpp
public interface class IEdmBatchListing
```

## Remarks

This interface:

- inherits from IDispatch. See [IDispatch Interface (Automation)](http://msdn.microsoft.com/en-us/library/windows/desktop/ms221608(v=vs.85).aspx).
- is extended by [IEdmBatchListing2](EPDM.Interop.epdm~EPDM.Interop.epdm.IEdmBatchListing2.html).

To create a listing of the properties of a batched set of files or folders:

1. Access this interface by calling [IEdmVault7::CreateUtility](EPDM.Interop.epdm~EPDM.Interop.epdm.IEdmVault7~CreateUtility.html), passing in [EdmUtility](EPDM.Interop.epdm~EPDM.Interop.epdm.EdmUtility.html).EdmUtil_BatchList as a parameter.
2. Call [IEdmBatchListing::AddFile](EPDM.Interop.epdm~EPDM.Interop.epdm.IEdmBatchListing~AddFile.html) once for each file whose properties you want to list.
3. Call [IEdmBatchListing::AddFolder](EPDM.Interop.epdm~EPDM.Interop.epdm.IEdmBatchListing~AddFolder.html) once for each folder whose properties you want to list.
4. Optionally call [IEdmBatchListing::GetColumnSetNames](EPDM.Interop.epdm~EPDM.Interop.epdm.IEdmBatchListing~GetColumnSetNames.html) to get the column sets that can be used to create listings with this interface.
5. Call [IEdmBatchListing::CreateList](EPDM.Interop.epdm~EPDM.Interop.epdm.IEdmBatchListing~CreateList.html) to create the listing.
6. Call [IEdmBatchListing::GetFiles](EPDM.Interop.epdm~EPDM.Interop.epdm.IEdmBatchListing~GetFiles.html) to get the files in the listing or [IEdmBatchListing::GetFolders](EPDM.Interop.epdm~EPDM.Interop.epdm.IEdmBatchListing~GetFolders.html) to get the folders in the listing.

Using this interface to create a listing of file or folder properties is more efficient than retrieving the interfaces and properties of the files and folders individually.

## Accessors

[IEdmVault7::CreateUtility](EPDM.Interop.epdm~EPDM.Interop.epdm.IEdmVault7~CreateUtility.html)

## See Also

[IEdmBatchListing Members](EPDM.Interop.epdm~EPDM.Interop.epdm.IEdmBatchListing_members.html)
[EPDM.Interop.epdm Namespace](EPDM.Interop.epdm~EPDM.Interop.epdm_namespace.html)
