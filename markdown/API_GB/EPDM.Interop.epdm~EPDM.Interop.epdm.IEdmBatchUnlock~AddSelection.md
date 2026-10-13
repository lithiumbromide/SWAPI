---
title: "AddSelection Method (IEdmBatchUnlock)"
project: "SOLIDWORKS PDM Professional API Help"
interface: "IEdmBatchUnlock"
member: "AddSelection"
kind: "method"
source: "API_GB/EPDM.Interop.epdm~EPDM.Interop.epdm.IEdmBatchUnlock~AddSelection.html"
---

# AddSelection Method (IEdmBatchUnlock)

Specifies the batch of files to be unlocked.

## Syntax

### Visual Basic

```vb
Sub AddSelection( _
   ByVal poVault As EdmVault5, _
   ByRef ppoSelection As EdmSelItem() _
)
```

### C#

```csharp
void AddSelection(
   EdmVault5 poVault,
   ref EdmSelItem[] ppoSelection
)
```

### C++/CLI

```cpp
void AddSelection(
   EdmVault5^ poVault,
   array<EdmSelItem>% ppoSelection
)
```

### Parameters

- `poVault`: [IEdmVault5](EPDM.Interop.epdm~EPDM.Interop.epdm.IEdmVault5.html); vault to which the files belong
- `ppoSelection`: Array of [IEdmSelItem](EPDM.Interop.epdm~EPDM.Interop.epdm.EdmSelItem2.html) structures; one structure for each file to unlock

## Examples

See the [IEdmBatchUnlock](EPDM.Interop.epdm~EPDM.Interop.epdm.IEdmBatchUnlock.html) examples.

## Remarks

See the [IEdmBatchUnlock](EPDM.Interop.epdm~EPDM.Interop.epdm.IEdmBatchUnlock.html) remarks for information about using this method.

When you call this method, SOLIDWORKS PDM Professional automatically adds the file's references to the unlock file set.

[Return codes](ReturnCodes.htm):

- S_OK: The method successfully executed.
- S_FALSE: One of the arguments is invalid.

## See Also

[IEdmBatchUnlock Interface](EPDM.Interop.epdm~EPDM.Interop.epdm.IEdmBatchUnlock.html)
[IEdmBatchUnlock Members](EPDM.Interop.epdm~EPDM.Interop.epdm.IEdmBatchUnlock_members.html)

## Availability

Version 6.3 of SOLIDWORKS PDM Professional
