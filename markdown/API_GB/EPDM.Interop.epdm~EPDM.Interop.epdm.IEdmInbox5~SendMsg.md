---
title: "SendMsg Method (IEdmInbox5)"
project: "SOLIDWORKS PDM Professional API Help"
interface: "IEdmInbox5"
member: "SendMsg"
kind: "method"
source: "API_GB/EPDM.Interop.epdm~EPDM.Interop.epdm.IEdmInbox5~SendMsg.html"
---

# SendMsg Method (IEdmInbox5)

Emails the current user.

## Syntax

### Visual Basic

```vb
Sub SendMsg( _
   ByVal bsSubject As System.String, _
   ByVal bsMessageText As System.String _
)
```

### C#

```csharp
void SendMsg(
   System.string bsSubject,
   System.string bsMessageText
)
```

### C++/CLI

```cpp
void SendMsg(
   System.String^ bsSubject,
   System.String^ bsMessageText
)
```

### Parameters

- `bsSubject`: Subject of the email
- `bsMessageText`: Message detail (see **Remarks**)

## Examples

See the [IEdmUser5::SendMsg](EPDM.Interop.epdm~EPDM.Interop.epdm.IEdmUser5~SendMsg.html) example.

## Remarks

It is possible to send HTML-formatted email, if the recipient uses a mail system that supports HTML. If so, then add HTML tags to the text in bsMessageText.

[Return codes](ReturnCodes.htm):

- S_OK: The method successfully executed.
- S_FALSE: One of the arguments is invalid.

## See Also

[IEdmInbox5 Interface](EPDM.Interop.epdm~EPDM.Interop.epdm.IEdmInbox5.html)
[IEdmInbox5 Members](EPDM.Interop.epdm~EPDM.Interop.epdm.IEdmInbox5_members.html)
[IEdmUserGroup5::SendMsg Method ()](EPDM.Interop.epdm~EPDM.Interop.epdm.IEdmUserGroup5~SendMsg.html)

## Availability

SOLIDWORKS PDM Professional Version 5.3
