---
title: "ShowCommitErrorsDlg Method (IEdmBatchDelete)"
project: "SOLIDWORKS PDM Professional API Help"
interface: "IEdmBatchDelete"
member: "ShowCommitErrorsDlg"
kind: "method"
source: "API_GB/EPDM.Interop.epdm~EPDM.Interop.epdm.IEdmBatchDelete~ShowCommitErrorsDlg.html"
---

# ShowCommitErrorsDlg Method (IEdmBatchDelete)

Shows a dialog box containing the errors that occurred during [IEdmBatchDelete::CommitDelete](EPDM.Interop.epdm~EPDM.Interop.epdm.IEdmBatchDelete~CommitDelete.html).

## Syntax

### Visual Basic

```vb
Sub ShowCommitErrorsDlg( _
   ByVal hParentWnd As System.Integer _
)
```

### C#

```csharp
void ShowCommitErrorsDlg(
   System.int hParentWnd
)
```

### C++/CLI

```cpp
void ShowCommitErrorsDlg(
   System.int hParentWnd
)
```

### Parameters

- `hParentWnd`: Parent window handle for the dialog box

## Examples

See the [IEdmBatchDelete](EPDM.Interop.epdm~EPDM.Interop.epdm.IEdmBatchDelete.html) examples.

## Remarks

[Return codes](ReturnCodes.htm):

- S_OK: The method successfully executed.
- E_EDM_NOT_INITIALIZED: IEdmBatchDelete::CommitDelete has not been called.

## See Also

[IEdmBatchDelete Interface](EPDM.Interop.epdm~EPDM.Interop.epdm.IEdmBatchDelete.html)
[IEdmBatchDelete Members](EPDM.Interop.epdm~EPDM.Interop.epdm.IEdmBatchDelete_members.html)

## Availability

SOLIDWORKS PDM Professional 2008
