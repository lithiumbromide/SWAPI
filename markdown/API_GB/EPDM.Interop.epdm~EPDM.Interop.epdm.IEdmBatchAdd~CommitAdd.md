---
title: "CommitAdd Method (IEdmBatchAdd)"
project: "SOLIDWORKS PDM Professional API Help"
interface: "IEdmBatchAdd"
member: "CommitAdd"
kind: "method"
source: "API_GB/EPDM.Interop.epdm~EPDM.Interop.epdm.IEdmBatchAdd~CommitAdd.html"
---

# CommitAdd Method (IEdmBatchAdd)

Adds all files and folders in the batch to the vault.

## Syntax

### Visual Basic

```vb
Function CommitAdd( _
   ByVal lHwnd As System.Integer, _
   ByRef ppoRetFiles As EdmFileInfo(), _
   Optional ByVal lEdmBatchAddFlags As System.Integer, _
   Optional ByVal poCallback As System.Object _
) As System.Integer
```

### C#

```csharp
System.int CommitAdd(
   System.int lHwnd,
   out EdmFileInfo[] ppoRetFiles,
   System.int lEdmBatchAddFlags,
   System.object poCallback
)
```

### C++/CLI

```cpp
System.int CommitAdd(
   System.int lHwnd,
   [Out] array<EdmFileInfo> ppoRetFiles,
   System.int lEdmBatchAddFlags,
   System.Object^ poCallback
)
```

### Parameters

- `lHwnd`: Parent window handle that is passed to add-ins that are notified about files and folders added to the vault
- `ppoRetFiles`: Array of [EdmFileInfo](EPDM.Interop.epdm~EPDM.Interop.epdm.EdmFileInfo.html) structures, one structure for each file and folder
- `lEdmBatchAddFlags`: Combination of [EdmBatchAddFlag](EPDM.Interop.epdm~EPDM.Interop.epdm.EdmBatchAddFlag.html) bits
- `poCallback`: Optional pointer to a class that implements [IEdmCallback](EPDM.Interop.epdm~EPDM.Interop.epdm.IEdmCallback.html) or [IEdmCallback6](EPDM.Interop.epdm~EPDM.Interop.epdm.IEdmCallback6.html) to provide the caller with more information

### Return Value

0 for success; See ppoRetFiles' EdmFileInfo.mhResult for each file added to the vault to get individual result codes

## Examples

See the [IEdmBatchAdd](EPDM.Interop.epdm~EPDM.Interop.epdm.IEdmBatchAdd.html) examples.

## Remarks

[Return codes](ReturnCodes.htm):

- S_OK: The method successfully executed.
- S_FALSE: One of the arguments is invalid.

## See Also

[IEdmBatchAdd Interface](EPDM.Interop.epdm~EPDM.Interop.epdm.IEdmBatchAdd.html)
[IEdmBatchAdd Members](EPDM.Interop.epdm~EPDM.Interop.epdm.IEdmBatchAdd_members.html)

## Availability

Version 6.4 of SOLIDWORKS PDM Professional
