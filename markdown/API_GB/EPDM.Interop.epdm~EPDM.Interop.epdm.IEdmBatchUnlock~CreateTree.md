---
title: "CreateTree Method (IEdmBatchUnlock)"
project: "SOLIDWORKS PDM Professional API Help"
interface: "IEdmBatchUnlock"
member: "CreateTree"
kind: "method"
source: "API_GB/EPDM.Interop.epdm~EPDM.Interop.epdm.IEdmBatchUnlock~CreateTree.html"
---

# CreateTree Method (IEdmBatchUnlock)

Creates the file reference tree.

## Syntax

### Visual Basic

```vb
Function CreateTree( _
   ByVal lParentWnd As System.Integer, _
   ByVal lEdmUnlockBuildTreeFlags As System.Integer, _
   Optional ByVal poCallback As IEdmUnlockOpCallback _
) As System.Boolean
```

### C#

```csharp
System.bool CreateTree(
   System.int lParentWnd,
   System.int lEdmUnlockBuildTreeFlags,
   IEdmUnlockOpCallback poCallback
)
```

### C++/CLI

```cpp
System.bool CreateTree(
   System.int lParentWnd,
   System.int lEdmUnlockBuildTreeFlags,
   IEdmUnlockOpCallback^ poCallback
)
```

### Parameters

- `lParentWnd`: Parent window handle
- `lEdmUnlockBuildTreeFlags`: Combination of [EdmUnlockBuildTreeFlags](EPDM.Interop.epdm~EPDM.Interop.epdm.EdmUnlockBuildTreeFlags.html) bits
- `poCallback`: [IEdmUnlockOpCallback](EPDM.Interop.epdm~EPDM.Interop.epdm.IEdmUnlockOpCallback.html); optional callback that you can implement to receive more information about the unlock operation

### Return Value

True if at least one file is valid for the operation, false if no files are valid for the operation

## Examples

See the [IEdmBatchUnlock](EPDM.Interop.epdm~EPDM.Interop.epdm.IEdmBatchUnlock.html) examples.

## Remarks

See the [IEdmBatchUnlock](EPDM.Interop.epdm~EPDM.Interop.epdm.IEdmBatchUnlock.html) remarks for information about using this method.

[Return codes](ReturnCodes.htm):

- S_OK: The method successfully executed.
- S_FALSE: One of the arguments is invalid.

## See Also

[IEdmBatchUnlock Interface](EPDM.Interop.epdm~EPDM.Interop.epdm.IEdmBatchUnlock.html)
[IEdmBatchUnlock Members](EPDM.Interop.epdm~EPDM.Interop.epdm.IEdmBatchUnlock_members.html)

## Availability

Version 6.3 of SOLIDWORKS PDM Professional
