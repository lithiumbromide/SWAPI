---
title: "CreateTree Method (IEdmBatchGet)"
project: "SOLIDWORKS PDM Professional API Help"
interface: "IEdmBatchGet"
member: "CreateTree"
kind: "method"
source: "epdmapi/EPDM.Interop.epdm~EPDM.Interop.epdm.IEdmBatchGet~CreateTree.html"
---

# CreateTree Method (IEdmBatchGet)

Computes the file reference tree with the files added to the batch using [IEdmBatchGet::AddSelection](EPDM.Interop.epdm~EPDM.Interop.epdm.IEdmBatchGet~AddSelection.html) or [IEdmBatchGet::AddSelectionEx](EPDM.Interop.epdm~EPDM.Interop.epdm.IEdmBatchGet~AddSelectionEx.html).

## Syntax

### Visual Basic

```vb
Sub CreateTree( _
   ByVal lParentWnd As System.Integer, _
   ByVal lEdmGetCmdFlags As System.Integer _
)
```

### C#

```csharp
void CreateTree(
   System.int lParentWnd,
   System.int lEdmGetCmdFlags
)
```

### C++/CLI

```cpp
void CreateTree(
   System.int lParentWnd,
   System.int lEdmGetCmdFlags
)
```

### Parameters

- `lParentWnd`: Parent window handle
- `lEdmGetCmdFlags`: Combination of [EdmGetCmdFlags](EPDM.Interop.epdm~EPDM.Interop.epdm.EdmGetCmdFlags.html) bits; specifies options for retrieving files from the vault

## Examples

See the [IEdmBatchGet](EPDM.Interop.epdm~EPDM.Interop.epdm.IEdmBatchGet.html) examples.

## Remarks

After calling this method, call [IEdmBatchGet::ShowDlg](EPDM.Interop.epdm~EPDM.Interop.epdm.IEdmBatchGet~ShowDlg.html) and [IEdmBatchGet::GetFiles](EPDM.Interop.epdm~EPDM.Interop.epdm.IEdmBatchGet~GetFiles.html).

[Return codes](ReturnCodes.htm):

- S_OK: The method successfully executed.
- S_FALSE: One of the arguments is invalid.

## See Also

[IEdmBatchGet Interface](EPDM.Interop.epdm~EPDM.Interop.epdm.IEdmBatchGet.html)
[IEdmBatchGet Members](EPDM.Interop.epdm~EPDM.Interop.epdm.IEdmBatchGet_members.html)

## Availability

Version 6.3 of SOLIDWORKS PDM Professional
