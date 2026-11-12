---
title: "ShowWarningDlg Method (IEdmBatchDelete)"
project: "SOLIDWORKS PDM Professional API Help"
interface: "IEdmBatchDelete"
member: "ShowWarningDlg"
kind: "method"
source: "epdmapi/EPDM.Interop.epdm~EPDM.Interop.epdm.IEdmBatchDelete~ShowWarningDlg.html"
---

# ShowWarningDlg Method (IEdmBatchDelete)

Obsolete. Superseded by [IEdmBatchDelete2::ShowWarningDlg2](EPDM.Interop.epdm~EPDM.Interop.epdm.IEdmBatchDelete2~ShowWarningDlg2.html).

## Syntax

### Visual Basic

```vb
Function ShowWarningDlg( _
   ByVal hParentWnd As System.Integer _
) As System.Boolean
```

### C#

```csharp
System.bool ShowWarningDlg(
   System.int hParentWnd
)
```

### C++/CLI

```cpp
System.bool ShowWarningDlg(
   System.int hParentWnd
)
```

### Parameters

- `hParentWnd`: Parent window handle for the dialog box

### Return Value

True if the user chooses to continue the operation in spite of the warnings, false if the user cancels the operation

## Remarks

[Return codes](ReturnCodes.htm):

- S_OK: The method successfully executed.
- E_EDM_NOT_INITIALIZED: IEdmBatchDelete::ComputePermissions has not been called.

## See Also

[IEdmBatchDelete Interface](EPDM.Interop.epdm~EPDM.Interop.epdm.IEdmBatchDelete.html)
[IEdmBatchDelete Members](EPDM.Interop.epdm~EPDM.Interop.epdm.IEdmBatchDelete_members.html)

## Availability

SOLIDWORKS PDM Professional 2008
