---
title: "ShowDlg Method (IEdmBatchChangeState)"
project: "SOLIDWORKS PDM Professional API Help"
interface: "IEdmBatchChangeState"
member: "ShowDlg"
kind: "method"
source: "API_GB/EPDM.Interop.epdm~EPDM.Interop.epdm.IEdmBatchChangeState~ShowDlg.html"
---

# ShowDlg Method (IEdmBatchChangeState)

Shows the change state or revoke transition dialog box.

## Syntax

### Visual Basic

```vb
Function ShowDlg( _
   ByVal lParentWnd As System.Integer _
) As System.Boolean
```

### C#

```csharp
System.bool ShowDlg(
   System.int lParentWnd
)
```

### C++/CLI

```cpp
System.bool ShowDlg(
   System.int lParentWnd
)
```

### Parameters

- `lParentWnd`: Parent window handle for the dialog box

### Return Value

True if the user clicked **OK**, false if the user clicked **Cancel**

## Examples

See the [IEdmBatchChangeState4](EPDM.Interop.epdm~EPDM.Interop.epdm.IEdmBatchChangeState4.html) examples.

## Remarks

Before calling this method, you must call [IEdmBatchChangeState::CreateTree](EPDM.Interop.epdm~EPDM.Interop.epdm.IEdmBatchChangeState~CreateTree.html) if changing states or [IEdmBatchChangeState2::CreateTreeForRevoke](EPDM.Interop.epdm~EPDM.Interop.epdm.IEdmBatchChangeState2~CreateTreeForRevoke.html) if revoking transitions.

[Return codes](ReturnCodes.htm):

- S_OK: The method successfully executed.
- S_FALSE: One of the arguments is invalid.

## See Also

[IEdmBatchChangeState Interface](EPDM.Interop.epdm~EPDM.Interop.epdm.IEdmBatchChangeState.html)
[IEdmBatchChangeState Members](EPDM.Interop.epdm~EPDM.Interop.epdm.IEdmBatchChangeState_members.html)

## Availability

SOLIDWORKS PDM Professional 2009; for the revoke transition dialog, SOLIDWORKS PDM Professional 2013
