---
title: "CommitClear Method (IEdmClearLocalCache)"
project: "SOLIDWORKS PDM Professional API Help"
interface: "IEdmClearLocalCache"
member: "CommitClear"
kind: "method"
source: "epdmapi/EPDM.Interop.epdm~EPDM.Interop.epdm.IEdmClearLocalCache~CommitClear.html"
---

# CommitClear Method (IEdmClearLocalCache)

Clears the files and folders specified by [IEdmClearLocalCache::AddFilebyPath](EPDM.Interop.epdm~EPDM.Interop.epdm.IEdmClearLocalCache~AddFileByPath.html) and [IEdmClearLocalCache::AddFolder](EPDM.Interop.epdm~EPDM.Interop.epdm.IEdmClearLocalCache~AddFolder.html) from the local cache.

## Syntax

### Visual Basic

```vb
Sub CommitClear( _
   Optional ByVal poCallback As EdmCallback _
)
```

### C#

```csharp
void CommitClear(
   EdmCallback poCallback
)
```

### C++/CLI

```cpp
void CommitClear(
   EdmCallback^ poCallback
)
```

### Parameters

- `poCallback`: Optional pointer to a class that implements [IEdmCallback](EPDM.Interop.epdm~EPDM.Interop.epdm.IEdmCallback.html) to provide progress feedback to the user

## Examples

[Get File References for a File (C#)](Get_File_References_for_File_Example_CSharp.htm)
[Get File References for a File (VB.NET)](Get_File_References_for_File_Example_VBNET.htm)

## Remarks

[Return codes](ReturnCodes.htm):

- S_OK: The method successfully executed.
- S_FALSE: One of the arguments is invalid.

## See Also

[IEdmClearLocalCache Interface](EPDM.Interop.epdm~EPDM.Interop.epdm.IEdmClearLocalCache.html)
[IEdmClearLocalCache Members](EPDM.Interop.epdm~EPDM.Interop.epdm.IEdmClearLocalCache_members.html)

## Availability

SOLIDWORKS PDM Professional 2008
