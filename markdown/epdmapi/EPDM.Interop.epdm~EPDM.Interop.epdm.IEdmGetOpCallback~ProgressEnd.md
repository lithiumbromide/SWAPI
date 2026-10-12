---
title: "ProgressEnd Method (IEdmGetOpCallback)"
project: "SOLIDWORKS PDM Professional API Help"
interface: "IEdmGetOpCallback"
member: "ProgressEnd"
kind: "method"
source: "epdmapi/EPDM.Interop.epdm~EPDM.Interop.epdm.IEdmGetOpCallback~ProgressEnd.html"
---

# ProgressEnd Method (IEdmGetOpCallback)

Marks the end of the operation.

## Syntax

### Visual Basic

```vb
Sub ProgressEnd( _
   ByVal eType As EdmProgressType _
)
```

### C#

```csharp
void ProgressEnd(
   EdmProgressType eType
)
```

### C++/CLI

```cpp
void ProgressEnd(
   EdmProgressType eType
)
```

### Parameters

- `eType`: Type of progress bar as defined in [EdmProgressType](EPDM.Interop.epdm~EPDM.Interop.epdm.EdmProgressType.html)

## Remarks

[Return codes](ReturnCodes.htm):

- S_OK: The method successfully executed.
- S_FALSE: One of the arguments is invalid.

## See Also

[IEdmGetOpCallback Interface](EPDM.Interop.epdm~EPDM.Interop.epdm.IEdmGetOpCallback.html)
[IEdmGetOpCallback Members](EPDM.Interop.epdm~EPDM.Interop.epdm.IEdmGetOpCallback_members.html)

## Availability

SOLIDWORKS PDM Professional Version 6.3
