---
title: "CopyTree Method (IEdmVault19)"
project: "SOLIDWORKS PDM Professional API Help"
interface: "IEdmVault19"
member: "CopyTree"
kind: "method"
source: "API_GB/EPDM.Interop.epdm~EPDM.Interop.epdm.IEdmVault19~CopyTree.html"
---

# CopyTree Method (IEdmVault19)

Copies the specified assembly and its referenced parts and drawings to the specified destination folder.

## Syntax

### Visual Basic

```vb
Sub CopyTree( _
   ByVal lSrcFileID As System.Integer, _
   ByVal lSrcFileProjID As System.Integer, _
   ByVal lDestinationFolderPath As System.String, _
   ByVal vbShowDlg As System.Boolean, _
   ByVal vbShowProgressBar As System.Boolean, _
   ByVal oCopyTreeOptions As EdmCopyTreeOptions, _
   ByVal lHwnd As System.Integer _
)
```

### C#

```csharp
void CopyTree(
   System.int lSrcFileID,
   System.int lSrcFileProjID,
   System.string lDestinationFolderPath,
   System.bool vbShowDlg,
   System.bool vbShowProgressBar,
   EdmCopyTreeOptions oCopyTreeOptions,
   System.int lHwnd
)
```

### C++/CLI

```cpp
void CopyTree(
   System.int lSrcFileID,
   System.int lSrcFileProjID,
   System.String^ lDestinationFolderPath,
   System.bool vbShowDlg,
   System.bool vbShowProgressBar,
   EdmCopyTreeOptions oCopyTreeOptions,
   System.int lHwnd
)
```

### Parameters

- `lSrcFileID`: ID of the assembly to copy
- `lSrcFileProjID`: ID of the parent folder of lSrcFileID; only valid if lSrcFileID is not 0 or blank
- `lDestinationFolderPath`: Full path name of destination folder
- `vbShowDlg`: True to display the copy dialog, false to not
- `vbShowProgressBar`: True to display a progress bar during the copy procedure, false to not
- `oCopyTreeOptions`: Copy tree options as defined in [EdmCopyTreeOptions](EPDM.Interop.epdm~EPDM.Interop.epdm.EdmCopyTreeOptions.html)
- `lHwnd`: Parent window handle

## Examples

See the [IEdmVault19](EPDM.Interop.epdm~EPDM.Interop.epdm.IEdmVault19.html) examples.

## See Also

[IEdmVault19 Interface](EPDM.Interop.epdm~EPDM.Interop.epdm.IEdmVault19.html)
[IEdmVault19 Members](EPDM.Interop.epdm~EPDM.Interop.epdm.IEdmVault19_members.html)

## Availability

SOLIDWORKS PDM Professional 2018
