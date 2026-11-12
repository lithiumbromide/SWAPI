---
title: "ShowWarningDlg2 Method (IEdmBatchDelete2)"
project: "SOLIDWORKS PDM Professional API Help"
interface: "IEdmBatchDelete2"
member: "ShowWarningDlg2"
kind: "method"
source: "API_GB/EPDM.Interop.epdm~EPDM.Interop.epdm.IEdmBatchDelete2~ShowWarningDlg2.html"
---

# ShowWarningDlg2 Method (IEdmBatchDelete2)

Shows a dialog box with the warnings and errors that occurred during [IEdmBatchDelete::ComputePermissions](EPDM.Interop.epdm~EPDM.Interop.epdm.IEdmBatchDelete~ComputePermissions.html).

## Syntax

### Visual Basic

```vb
Function ShowWarningDlg2( _
   ByVal hParentWnd As System.Integer, _
   ByVal bIncludeDeleted As System.Boolean _
) As System.Boolean
```

### C#

```csharp
System.bool ShowWarningDlg2(
   System.int hParentWnd,
   System.bool bIncludeDeleted
)
```

### C++/CLI

```cpp
System.bool ShowWarningDlg2(
   System.int hParentWnd,
   System.bool bIncludeDeleted
)
```

### Parameters

- `hParentWnd`: Parent window handle for the dialog box
- `bIncludeDeleted`: True to show the contents of the trash can, false to not

### Return Value

True if the user chooses to continue the operation in spite of the warnings, false if the user cancels the operation

## Examples

See the [IEdmBatchDelete](EPDM.Interop.epdm~EPDM.Interop.epdm.IEdmBatchDelete.html) examples.

## Remarks

This method supersedes [IEdmBatchDelete.ShowWarningDlg](EPDM.Interop.epdm~EPDM.Interop.epdm.IEdmBatchDelete~ShowWarningDlg.html) by adding the option to show the deleted objects in the trash can.

[Return codes](ReturnCodes.htm):

- S_OK: The method successfully executed.
- E_EDM_NOT_INITIALIZED: IEdmBatchDelete::ComputePermissions has not been called.

## See Also

[IEdmBatchDelete2 Interface](EPDM.Interop.epdm~EPDM.Interop.epdm.IEdmBatchDelete2.html)
[IEdmBatchDelete2 Members](EPDM.Interop.epdm~EPDM.Interop.epdm.IEdmBatchDelete2_members.html)

## Availability

SOLIDWORKS PDM Professional 2009
