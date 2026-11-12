---
title: "ShowDlg Method (IEdmBatchGet)"
project: "SOLIDWORKS PDM Professional API Help"
interface: "IEdmBatchGet"
member: "ShowDlg"
kind: "method"
source: "API_GB/EPDM.Interop.epdm~EPDM.Interop.epdm.IEdmBatchGet~ShowDlg.html"
---

# ShowDlg Method (IEdmBatchGet)

Displays a dialog in which are listed the files to get or check out.

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

- `lParentWnd`: Parent window handle

### Return Value

True if the user clicked **Get** or **Check Out**, false if the user clicked **Cancel**

## Examples

See the [IEdmBatchGet](EPDM.Interop.epdm~EPDM.Interop.epdm.IEdmBatchGet.html) examples.

## Remarks

Call this method after calling [IEdmBatchGet::CreateTree](EPDM.Interop.epdm~EPDM.Interop.epdm.IEdmBatchGet~CreateTree.html) and before calling [IEdmBatchGet::GetFiles](EPDM.Interop.epdm~EPDM.Interop.epdm.IEdmBatchGet~GetFiles.html).

[Return code](ReturnCodes.htm):

- S_OK: The method successfully executed.

## See Also

[IEdmBatchGet Interface](EPDM.Interop.epdm~EPDM.Interop.epdm.IEdmBatchGet.html)
[IEdmBatchGet Members](EPDM.Interop.epdm~EPDM.Interop.epdm.IEdmBatchGet_members.html)

## Availability

Version 6.3 of SOLIDWORKS PDM Professional
