---
title: "ConfirmReplace Method (IEdmGetOpCallback)"
project: "SOLIDWORKS PDM Professional API Help"
interface: "IEdmGetOpCallback"
member: "ConfirmReplace"
kind: "method"
source: "API_GB/EPDM.Interop.epdm~EPDM.Interop.epdm.IEdmGetOpCallback~ConfirmReplace.html"
---

# ConfirmReplace Method (IEdmGetOpCallback)

Gets whether to replace an existing file.

## Syntax

### Visual Basic

```vb
Function ConfirmReplace( _
   ByVal eReason As EdmGetConfirmReason, _
   ByVal bsPath As System.String _
) As System.Boolean
```

### C#

```csharp
System.bool ConfirmReplace(
   EdmGetConfirmReason eReason,
   System.string bsPath
)
```

### C++/CLI

```cpp
System.bool ConfirmReplace(
   EdmGetConfirmReason eReason,
   System.String^ bsPath
)
```

### Parameters

- `eReason`: Reason for calling this method as defined in [EdmGetConfirmReason](EPDM.Interop.epdm~EPDM.Interop.epdm.EdmGetConfirmReason.html)
- `bsPath`: Full path to the local file

### Return Value

True to replace an existing file, false to leave an existing file

## Remarks

[Return codes](ReturnCodes.htm):

- S_OK: The method successfully executed.
- S_FALSE: One of the arguments is invalid.

## See Also

[IEdmGetOpCallback Interface](EPDM.Interop.epdm~EPDM.Interop.epdm.IEdmGetOpCallback.html)
[IEdmGetOpCallback Members](EPDM.Interop.epdm~EPDM.Interop.epdm.IEdmGetOpCallback_members.html)

## Availability

SOLIDWORKS PDM Professional Version 6.3
