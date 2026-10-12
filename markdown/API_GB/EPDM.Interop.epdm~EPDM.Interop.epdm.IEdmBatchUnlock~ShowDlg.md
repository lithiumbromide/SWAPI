---
title: "ShowDlg Method (IEdmBatchUnlock)"
project: "SOLIDWORKS PDM Professional API Help"
interface: "IEdmBatchUnlock"
member: "ShowDlg"
kind: "method"
source: "API_GB/EPDM.Interop.epdm~EPDM.Interop.epdm.IEdmBatchUnlock~ShowDlg.html"
---

# ShowDlg Method (IEdmBatchUnlock)

Displays the SOLIDWORKS PDM Professional Check In or Undo Check Out dialog box.

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

True if successful, false if not

## Examples

See the [IEdmBatchUnlock](EPDM.Interop.epdm~EPDM.Interop.epdm.IEdmBatchUnlock.html) examples.

## Remarks

See the [IEdmBatchUnlock](EPDM.Interop.epdm~EPDM.Interop.epdm.IEdmBatchUnlock.html) remarks for information about using this method.

[Return codes](ReturnCodes.htm):

- S_OK: The method successfully executed.
- S_FALSE: One of the arguments is invalid.

## See Also

[IEdmBatchUnlock Interface](EPDM.Interop.epdm~EPDM.Interop.epdm.IEdmBatchUnlock.html)
[IEdmBatchUnlock Members](EPDM.Interop.epdm~EPDM.Interop.epdm.IEdmBatchUnlock_members.html)

## Availability

Version 6.3 of SOLIDWORKS PDM Professional
