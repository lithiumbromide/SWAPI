---
title: "AddSelection Method (IEdmBatchGet)"
project: "SOLIDWORKS PDM Professional API Help"
interface: "IEdmBatchGet"
member: "AddSelection"
kind: "method"
source: "API_GB/EPDM.Interop.epdm~EPDM.Interop.epdm.IEdmBatchGet~AddSelection.html"
---

# AddSelection Method (IEdmBatchGet)

Adds one or more files or folders to the batch of files or folders to get.

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

- `poVault`: [IEdmVault5](EPDM.Interop.epdm~EPDM.Interop.epdm.IEdmVault5.html); vault from which to get the files or folders
- `ppoSelection`: Array of [EdmSelItem](EPDM.Interop.epdm~EPDM.Interop.epdm.EdmSelItem.html) structures; one structure for each file or folder

## Examples

See the [IEdmBatchGet](EPDM.Interop.epdm~EPDM.Interop.epdm.IEdmBatchGet.html) examples.

## Remarks

[Return codes](ReturnCodes.htm):

- S_OK: The method successfully executed.
- S_FALSE: One of the arguments is invalid.

## See Also

[IEdmBatchGet Interface](EPDM.Interop.epdm~EPDM.Interop.epdm.IEdmBatchGet.html)
[IEdmBatchGet Members](EPDM.Interop.epdm~EPDM.Interop.epdm.IEdmBatchGet_members.html)

## Availability

Version 6.3 of SOLIDWORKS PDM Professional
