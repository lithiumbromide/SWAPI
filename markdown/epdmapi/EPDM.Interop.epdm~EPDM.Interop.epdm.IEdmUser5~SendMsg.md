---
title: "SendMsg Method (IEdmUser5)"
project: "SOLIDWORKS PDM Professional API Help"
interface: "IEdmUser5"
member: "SendMsg"
kind: "method"
source: "epdmapi/EPDM.Interop.epdm~EPDM.Interop.epdm.IEdmUser5~SendMsg.html"
---

# SendMsg Method (IEdmUser5)

Sends email to this user.

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

[Send Message to Users (C#)](Send_Message_to_Users_Example_CSharp.htm)
[Send Message to Users (VB.NET)](Send_Message_to_Users_Example_VBNET.htm)
[Add and Remove User and Group from Folder (C#)](Add_and_Remove_User_and_Group_from_Folder_Example_CSharp.htm)
[Add and Remove User and Group from Folder (VB.NET)](Add_and_Remove_User_and_Group_from_Folder_Example_VBNET.htm)

## Remarks

It is possible to send HTML-formatted mail, if the recipient uses a mail system that supports HTML. In so, add HTML tags to the text in bsMessageText.

For example, bsMessageText might contain:

<html><body><h1>Hello!</h1>How are you?</body></html>

[Return codes](ReturnCodes.htm):

- S_OK: The method successfully executed.

## See Also

[IEdmUser5 Interface](EPDM.Interop.epdm~EPDM.Interop.epdm.IEdmUser5.html)
[IEdmUser5 Members](EPDM.Interop.epdm~EPDM.Interop.epdm.IEdmUser5_members.html)
[IEdmUserGroup5::SendMsg Method ()](EPDM.Interop.epdm~EPDM.Interop.epdm.IEdmUserGroup5~SendMsg.html)
[IEdmInbox5::SendMsg Method ()](EPDM.Interop.epdm~EPDM.Interop.epdm.IEdmInbox5~SendMsg.html)

## Availability

SOLIDWORKS PDM Professional Version 5.2
