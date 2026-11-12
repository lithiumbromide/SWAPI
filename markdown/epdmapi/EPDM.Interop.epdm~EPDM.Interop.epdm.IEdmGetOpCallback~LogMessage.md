---
title: "LogMessage Method (IEdmGetOpCallback)"
project: "SOLIDWORKS PDM Professional API Help"
interface: "IEdmGetOpCallback"
member: "LogMessage"
kind: "method"
source: "epdmapi/EPDM.Interop.epdm~EPDM.Interop.epdm.IEdmGetOpCallback~LogMessage.html"
---

# LogMessage Method (IEdmGetOpCallback)

Notifies about an error that occurred during the process.

## Syntax

### Visual Basic

```vb
Sub LogMessage( _
   ByVal eMsgID As EdmGetOpMsg, _
   ByVal hCode As System.Integer, _
   ByVal bsDetails As System.String _
)
```

### C#

```csharp
void LogMessage(
   EdmGetOpMsg eMsgID,
   System.int hCode,
   System.string bsDetails
)
```

### C++/CLI

```cpp
void LogMessage(
   EdmGetOpMsg eMsgID,
   System.int hCode,
   System.String^ bsDetails
)
```

### Parameters

- `eMsgID`: Message to display to the user as defined in [EdmGetOpMsg](EPDM.Interop.epdm~EPDM.Interop.epdm.EdmGetOpMsg.html)
- `hCode`: Error code causing this method to be called
- `bsDetails`: Reason for calling this method

## Remarks

[Return codes](ReturnCodes.htm):

- S_OK: The method successfully executed.
- S_FALSE: One of the arguments is invalid.

## See Also

[IEdmGetOpCallback Interface](EPDM.Interop.epdm~EPDM.Interop.epdm.IEdmGetOpCallback.html)
[IEdmGetOpCallback Members](EPDM.Interop.epdm~EPDM.Interop.epdm.IEdmGetOpCallback_members.html)

## Availability

SOLIDWORKS PDM Professional Version 6.3
