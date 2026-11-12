---
title: "ProgressStep Method (IEdmGetOpCallback)"
project: "SOLIDWORKS PDM Professional API Help"
interface: "IEdmGetOpCallback"
member: "ProgressStep"
kind: "method"
source: "epdmapi/EPDM.Interop.epdm~EPDM.Interop.epdm.IEdmGetOpCallback~ProgressStep.html"
---

# ProgressStep Method (IEdmGetOpCallback)

Updates the progress bar.

## Syntax

### Visual Basic

```vb
Function ProgressStep( _
   ByVal eType As EdmProgressType, _
   ByVal bsMessage As System.String, _
   ByVal lProgressPos As System.Integer _
) As System.Boolean
```

### C#

```csharp
System.bool ProgressStep(
   EdmProgressType eType,
   System.string bsMessage,
   System.int lProgressPos
)
```

### C++/CLI

```cpp
System.bool ProgressStep(
   EdmProgressType eType,
   System.String^ bsMessage,
   System.int lProgressPos
)
```

### Parameters

- `eType`: Type of progress bar as defined in [EdmProgressType](EPDM.Interop.epdm~EPDM.Interop.epdm.EdmProgressType.html)
- `bsMessage`: Full path to the processed file
- `lProgressPos`: New position of the progress bar pointer

### Return Value

True to continue, false to cancel the operation

## Remarks

This method is called periodically by SOLIDWORKS PDM Professional during the operation. [IEdmGetOpCallback::ProgressBegin](EPDM.Interop.epdm~EPDM.Interop.epdm.IEdmGetOpCallback~ProgressBegin.html) is called before this method is called. Implement this method to update a progress bar and to implement a button that, when clicked, halts the operation.

[Return codes](ReturnCodes.htm):

- S_OK: The method successfully executed.
- S_FALSE: One of the arguments is invalid.

## See Also

[IEdmGetOpCallback Interface](EPDM.Interop.epdm~EPDM.Interop.epdm.IEdmGetOpCallback.html)
[IEdmGetOpCallback Members](EPDM.Interop.epdm~EPDM.Interop.epdm.IEdmGetOpCallback_members.html)

## Availability

SOLIDWORKS PDM Professional Version 6.3
