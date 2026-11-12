---
title: "Rename Method (IEdmFile5)"
project: "SOLIDWORKS PDM Professional API Help"
interface: "IEdmFile5"
member: "Rename"
kind: "method"
source: "epdmapi/EPDM.Interop.epdm~EPDM.Interop.epdm.IEdmFile5~Rename.html"
---

# Rename Method (IEdmFile5)

Obsolete. Superseded by [IEdmFile6::RenameEx](EPDM.Interop.epdm~EPDM.Interop.epdm.IEdmFile6~RenameEx.html).

## Syntax

### Visual Basic

```vb
Sub Rename( _
   ByVal lParentWnd As System.Integer, _
   ByVal bsName As System.String, _
   Optional ByVal bRenameLocalCopies As System.Boolean _
)
```

### C#

```csharp
void Rename(
   System.int lParentWnd,
   System.string bsName,
   System.bool bRenameLocalCopies
)
```

### C++/CLI

```cpp
void Rename(
   System.int lParentWnd,
   System.String^ bsName,
   System.bool bRenameLocalCopies
)
```

### Parameters

- `lParentWnd`: Parent window handle
- `bsName`: New file name
- `bRenameLocalCopies`: Optional; true to rename local copies, false to not; default is true

## Remarks

See [Return Codes](ReturnCodes.htm) for the complete list of potential success and error codes. The following are just a few examples:

- S_OK: The method successfully executed.
- E_EDM_NAME_ALREADY_EXISTS: The specified name already exists.
- E_EDM_PERMISSION_DENIED: The user lacks permission to rename this file.

## See Also

[IEdmFile5 Interface](EPDM.Interop.epdm~EPDM.Interop.epdm.IEdmFile5.html)
[IEdmFile5 Members](EPDM.Interop.epdm~EPDM.Interop.epdm.IEdmFile5_members.html)

## Availability

SOLIDWORKS PDM Professional Version 5.2
