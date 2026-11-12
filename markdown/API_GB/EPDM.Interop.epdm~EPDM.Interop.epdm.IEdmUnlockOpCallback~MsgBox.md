---
title: "MsgBox Method (IEdmUnlockOpCallback)"
project: "SOLIDWORKS PDM Professional API Help"
interface: "IEdmUnlockOpCallback"
member: "MsgBox"
kind: "method"
source: "API_GB/EPDM.Interop.epdm~EPDM.Interop.epdm.IEdmUnlockOpCallback~MsgBox.html"
---

# MsgBox Method (IEdmUnlockOpCallback)

Called by the check-in operation to display a message box with information or options that the user can choose.

## Syntax

### Visual Basic

```vb
Function MsgBox( _
   ByVal eMsg As EdmUnlockOpMsg, _
   ByVal lDocID As System.Integer, _
   ByVal lProjID As System.Integer, _
   ByVal bsPath As System.String, _
   ByRef poError As EdmUnlockErrInfo _
) As EdmUnlockOpReply
```

### C#

```csharp
EdmUnlockOpReply MsgBox(
   EdmUnlockOpMsg eMsg,
   System.int lDocID,
   System.int lProjID,
   System.string bsPath,
   ref EdmUnlockErrInfo poError
)
```

### C++/CLI

```cpp
EdmUnlockOpReply MsgBox(
   EdmUnlockOpMsg eMsg,
   System.int lDocID,
   System.int lProjID,
   System.String^ bsPath,
   EdmUnlockErrInfo% poError
)
```

### Parameters

- `eMsg`: Message to display as defined in [EdmUnlockOpMsg](EPDM.Interop.epdm~EPDM.Interop.epdm.EdmUnlockOpMsg.html)
- `lDocID`: ID of the file that caused the message
- `lProjID`: ID of the file's parent folder
- `bsPath`: Full path to the file that caused the message
- `poError`: [EdmUnlockErrInfo](EPDM.Interop.epdm~EPDM.Interop.epdm.EdmUnlockErrInfo.html) structure containing extended information about the error

### Return Value

Reply to SOLIDWORKS PDM Professional as defined in [EdmUnlockOpReply](EPDM.Interop.epdm~EPDM.Interop.epdm.EdmUnlockOpReply.html)

## Examples

See the [IEdmUnlockOpCallback](EPDM.Interop.epdm~EPDM.Interop.epdm.IEdmUnlockOpCallback.html) examples.

## Remarks

[Return codes:](ReturnCodes.htm)

- S_OK: The method successfully executed.

## See Also

[IEdmUnlockOpCallback Interface](EPDM.Interop.epdm~EPDM.Interop.epdm.IEdmUnlockOpCallback.html)
[IEdmUnlockOpCallback Members](EPDM.Interop.epdm~EPDM.Interop.epdm.IEdmUnlockOpCallback_members.html)

## Availability

SOLIDWORKS PDM Professional Version 6.3
