---
title: "ShowDlg Method (IEdmBatchItemGeneration)"
project: "SOLIDWORKS PDM Professional API Help"
interface: "IEdmBatchItemGeneration"
member: "ShowDlg"
kind: "method"
source: "API_GB/EPDM.Interop.epdm~EPDM.Interop.epdm.IEdmBatchItemGeneration~ShowDlg.html"
---

# ShowDlg Method (IEdmBatchItemGeneration)

Shows the item creation dialog box.

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

True if the user clicked **OK**, false if the user clicked **Cancel**

## Examples

See the example in the [IEdmBatchItemGeneration](EPDM.Interop.epdm~EPDM.Interop.epdm.IEdmBatchItemGeneration.html) topic.

## Remarks

[Return codes](ReturnCodes.htm):

- S_OK: The method successfully executed.
- S_FALSE: One of the arguments is invalid.

## See Also

[IEdmBatchItemGeneration Interface](EPDM.Interop.epdm~EPDM.Interop.epdm.IEdmBatchItemGeneration.html)
[IEdmBatchItemGeneration Members](EPDM.Interop.epdm~EPDM.Interop.epdm.IEdmBatchItemGeneration_members.html)

## Availability

SOLIDWORKS PDM Professional 2010
