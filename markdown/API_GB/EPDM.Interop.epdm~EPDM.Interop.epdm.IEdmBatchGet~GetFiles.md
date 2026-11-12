---
title: "GetFiles Method (IEdmBatchGet)"
project: "SOLIDWORKS PDM Professional API Help"
interface: "IEdmBatchGet"
member: "GetFiles"
kind: "method"
source: "API_GB/EPDM.Interop.epdm~EPDM.Interop.epdm.IEdmBatchGet~GetFiles.html"
---

# GetFiles Method (IEdmBatchGet)

Gets the files in the batch.

## Syntax

### Visual Basic

```vb
Sub GetFiles( _
   ByVal lParentWnd As System.Integer, _
   Optional ByVal poCallback As IEdmGetOpCallback _
)
```

### C#

```csharp
void GetFiles(
   System.int lParentWnd,
   IEdmGetOpCallback poCallback
)
```

### C++/CLI

```cpp
void GetFiles(
   System.int lParentWnd,
   IEdmGetOpCallback^ poCallback
)
```

### Parameters

- `lParentWnd`: Parent window handle
- `poCallback`: Optional pointer to a class that implements [IEdmGetOpCallback](EPDM.Interop.epdm~EPDM.Interop.epdm.IEdmGetOpCallback.html), [IEdmGetOpCallback2](EPDM.Interop.epdm~EPDM.Interop.epdm.IEdmGetOpCallback2.html), or [IEdmGetOpCallback3](EPDM.Interop.epdm~EPDM.Interop.epdm.IEdmGetOpCallback3.html) to control and monitor the operation

## Examples

See the [IEdmBatchGet](EPDM.Interop.epdm~EPDM.Interop.epdm.IEdmBatchGet.html) examples.

## Remarks

Call this method after calling [IEdmBatchGet::CreateTree](EPDM.Interop.epdm~EPDM.Interop.epdm.IEdmBatchGet~CreateTree.html) and, optionally, [IEdmBatchGet::ShowDlg](EPDM.Interop.epdm~EPDM.Interop.epdm.IEdmBatchGet~ShowDlg.html).

[Return codes](ReturnCodes.htm):

- S_OK: The method successfully executed.
- S_FALSE: One of the arguments is invalid.

## See Also

[IEdmBatchGet Interface](EPDM.Interop.epdm~EPDM.Interop.epdm.IEdmBatchGet.html)
[IEdmBatchGet Members](EPDM.Interop.epdm~EPDM.Interop.epdm.IEdmBatchGet_members.html)

## Availability

Version 6.3 of SOLIDWORKS PDM Professional
