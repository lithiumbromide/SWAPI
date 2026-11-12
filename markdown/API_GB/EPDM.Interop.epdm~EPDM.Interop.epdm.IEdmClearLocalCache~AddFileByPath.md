---
title: "AddFileByPath Method (IEdmClearLocalCache)"
project: "SOLIDWORKS PDM Professional API Help"
interface: "IEdmClearLocalCache"
member: "AddFileByPath"
kind: "method"
source: "API_GB/EPDM.Interop.epdm~EPDM.Interop.epdm.IEdmClearLocalCache~AddFileByPath.html"
---

# AddFileByPath Method (IEdmClearLocalCache)

Adds the specified file to the batch of files and folders to clear from the local cache.

## Syntax

### Visual Basic

```vb
Sub AddFileByPath( _
   ByVal bsFilePath As System.String _
)
```

### C#

```csharp
void AddFileByPath(
   System.string bsFilePath
)
```

### C++/CLI

```cpp
void AddFileByPath(
   System.String^ bsFilePath
)
```

### Parameters

- `bsFilePath`: Path and filename of the file to clear

## Examples

[Get File References for a File (C#)](Get_File_References_for_File_Example_CSharp.htm)
[Get File References for a File (VB.NET)](Get_File_References_for_File_Example_VBNET.htm)

## Remarks

After calling this method, you must call [IEdmClearLocalCache::CommitClear](EPDM.Interop.epdm~EPDM.Interop.epdm.IEdmClearLocalCache~CommitClear.html) to actually clear the file from the cache.

[Return codes](ReturnCodes.htm):

- S_OK: The method successfully executed.
- S_FALSE: One of the arguments is invalid.

## See Also

[IEdmClearLocalCache Interface](EPDM.Interop.epdm~EPDM.Interop.epdm.IEdmClearLocalCache.html)
[IEdmClearLocalCache Members](EPDM.Interop.epdm~EPDM.Interop.epdm.IEdmClearLocalCache_members.html)

## Availability

SOLIDWORKS PDM Professional 2008
