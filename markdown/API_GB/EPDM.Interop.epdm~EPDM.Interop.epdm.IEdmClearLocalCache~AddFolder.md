---
title: "AddFolder Method (IEdmClearLocalCache)"
project: "SOLIDWORKS PDM Professional API Help"
interface: "IEdmClearLocalCache"
member: "AddFolder"
kind: "method"
source: "API_GB/EPDM.Interop.epdm~EPDM.Interop.epdm.IEdmClearLocalCache~AddFolder.html"
---

# AddFolder Method (IEdmClearLocalCache)

Adds the specified folder to the batch of files and folders to clear from the local cache.

## Syntax

### Visual Basic

```vb
Sub AddFolder( _
   ByVal oFolderIDorPath As System.Object, _
   Optional ByVal bRecursive As System.Boolean _
)
```

### C#

```csharp
void AddFolder(
   System.object oFolderIDorPath,
   System.bool bRecursive
)
```

### C++/CLI

```cpp
void AddFolder(
   System.Object^ oFolderIDorPath,
   System.bool bRecursive
)
```

### Parameters

- `oFolderIDorPath`: ID or path of the folder to clear from the cache
- `bRecursive`: True to clear subfolders, false to not

## Remarks

After calling this method, you must call [IEdmClearLocalCache::CommitClear](EPDM.Interop.epdm~EPDM.Interop.epdm.IEdmClearLocalCache~CommitClear.html) to actually clear the folder from the cache.

[Return codes](ReturnCodes.htm):

- S_OK: The method successfully executed.
- S_FALSE: One of the arguments is invalid.

## See Also

[IEdmClearLocalCache Interface](EPDM.Interop.epdm~EPDM.Interop.epdm.IEdmClearLocalCache.html)
[IEdmClearLocalCache Members](EPDM.Interop.epdm~EPDM.Interop.epdm.IEdmClearLocalCache_members.html)

## Availability

SOLIDWORKS PDM Professional 2008
