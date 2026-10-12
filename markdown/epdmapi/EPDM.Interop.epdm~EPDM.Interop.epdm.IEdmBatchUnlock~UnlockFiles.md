---
title: "UnlockFiles Method (IEdmBatchUnlock)"
project: "SOLIDWORKS PDM Professional API Help"
interface: "IEdmBatchUnlock"
member: "UnlockFiles"
kind: "method"
source: "epdmapi/EPDM.Interop.epdm~EPDM.Interop.epdm.IEdmBatchUnlock~UnlockFiles.html"
---

# UnlockFiles Method (IEdmBatchUnlock)

Unlocks, checks in, or undoes the check-outs of the files in this batch.

## Syntax

### Visual Basic

```vb
Sub UnlockFiles( _
   ByVal lParentWnd As System.Integer, _
   Optional ByVal poCallback As IEdmUnlockOpCallback _
)
```

### C#

```csharp
void UnlockFiles(
   System.int lParentWnd,
   IEdmUnlockOpCallback poCallback
)
```

### C++/CLI

```cpp
void UnlockFiles(
   System.int lParentWnd,
   IEdmUnlockOpCallback^ poCallback
)
```

### Parameters

- `lParentWnd`: Parent window handle
- `poCallback`: [IEdmUnlockOpCallback](EPDM.Interop.epdm~EPDM.Interop.epdm.IEdmUnlockOpCallback.html); optional callback that you can implement to receive more information about the unlock operation

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
