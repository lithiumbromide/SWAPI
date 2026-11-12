---
title: "ProgressBegin Method (IEdmGetOpCallback)"
project: "SOLIDWORKS PDM Professional API Help"
interface: "IEdmGetOpCallback"
member: "ProgressBegin"
kind: "method"
source: "epdmapi/EPDM.Interop.epdm~EPDM.Interop.epdm.IEdmGetOpCallback~ProgressBegin.html"
---

# ProgressBegin Method (IEdmGetOpCallback)

Marks the beginning of the process.

## Syntax

### Visual Basic

```vb
Sub ProgressBegin( _
   ByVal eType As EdmProgressType, _
   ByVal lSteps As System.Integer _
)
```

### C#

```csharp
void ProgressBegin(
   EdmProgressType eType,
   System.int lSteps
)
```

### C++/CLI

```cpp
void ProgressBegin(
   EdmProgressType eType,
   System.int lSteps
)
```

### Parameters

- `eType`: Type of progress bar as defined in [EdmProgressType](EPDM.Interop.epdm~EPDM.Interop.epdm.EdmProgressType.html)
- `lSteps`: Number of times that [IEdmGetOpCallback::ProgressStep](EPDM.Interop.epdm~EPDM.Interop.epdm.IEdmGetOpCallback~ProgressStep.html) is to be called

## Remarks

Implement this method to display a progress bar. After this method is called, SOLIDWORKS PDM Professional calls IEdmGetOpCallback::ProgressStep lSteps times.

[Return codes](ReturnCodes.htm):

- S_OK: The method successfully executed.
- S_FALSE: One of the arguments is invalid.

## See Also

[IEdmGetOpCallback Interface](EPDM.Interop.epdm~EPDM.Interop.epdm.IEdmGetOpCallback.html)
[IEdmGetOpCallback Members](EPDM.Interop.epdm~EPDM.Interop.epdm.IEdmGetOpCallback_members.html)

## Availability

SOLIDWORKS PDM Professional Version 6.3
