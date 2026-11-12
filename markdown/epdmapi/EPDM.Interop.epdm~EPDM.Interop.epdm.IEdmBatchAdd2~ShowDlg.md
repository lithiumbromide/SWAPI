---
title: "ShowDlg Method (IEdmBatchAdd2)"
project: "SOLIDWORKS PDM Professional API Help"
interface: "IEdmBatchAdd2"
member: "ShowDlg"
kind: "method"
source: "epdmapi/EPDM.Interop.epdm~EPDM.Interop.epdm.IEdmBatchAdd2~ShowDlg.html"
---

# ShowDlg Method (IEdmBatchAdd2)

Shows a dialog box containing information about the file and folders that are about to be added to the vault by [IEdmBatchAdd::CommitAdd](EPDM.Interop.epdm~EPDM.Interop.epdm.IEdmBatchAdd~CommitAdd.html).

## Syntax

### Visual Basic

```vb
Function ShowDlg( _
   ByVal hParentWnd As System.Integer, _
   ByVal lEdmAddFileDlgFlags As System.Integer, _
   Optional ByVal bsMessage As System.String, _
   Optional ByVal bsCaption As System.String _
) As System.Boolean
```

### C#

```csharp
System.bool ShowDlg(
   System.int hParentWnd,
   System.int lEdmAddFileDlgFlags,
   System.string bsMessage,
   System.string bsCaption
)
```

### C++/CLI

```cpp
System.bool ShowDlg(
   System.int hParentWnd,
   System.int lEdmAddFileDlgFlags,
   System.String^ bsMessage,
   System.String^ bsCaption
)
```

### Parameters

- `hParentWnd`: Parent window handle for the dialog box
- `lEdmAddFileDlgFlags`: Combination of [EdmAddFileDlgFlag](EPDM.Interop.epdm~EPDM.Interop.epdm.EdmAddFileDlgFlag.html) bits
- `bsMessage`: Message to display in the dialog box
- `bsCaption`: Dialog box caption

### Return Value

True if the user clicked **OK**, false if the user clicked **Cancel**

## Examples

See the [IEdmBatchAdd](EPDM.Interop.epdm~EPDM.Interop.epdm.IEdmBatchAdd.html) examples.

## Remarks

[Return codes](ReturnCodes.htm):

- S_OK: The method successfully executed.
- S_FALSE: One of the arguments is invalid.

## See Also

[IEdmBatchAdd2 Interface](EPDM.Interop.epdm~EPDM.Interop.epdm.IEdmBatchAdd2.html)
[IEdmBatchAdd2 Members](EPDM.Interop.epdm~EPDM.Interop.epdm.IEdmBatchAdd2_members.html)

## Availability

SOLIDWORKS PDM Professional 2009
