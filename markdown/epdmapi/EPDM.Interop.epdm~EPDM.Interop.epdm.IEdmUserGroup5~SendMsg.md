---
title: "SendMsg Method (IEdmUserGroup5)"
project: "SOLIDWORKS PDM Professional API Help"
interface: "IEdmUserGroup5"
member: "SendMsg"
kind: "method"
source: "epdmapi/EPDM.Interop.epdm~EPDM.Interop.epdm.IEdmUserGroup5~SendMsg.html"
---

# SendMsg Method (IEdmUserGroup5)

Sends email to all members of this user group.

## Syntax

### Visual Basic

```vb
Sub SendMsg( _
   ByVal bsSubject As System.String, _
   ByVal bsMessageText As System.String, _
   ByVal bExcludeCurrentUser As System.Boolean _
)
```

### C#

```csharp
void SendMsg(
   System.string bsSubject,
   System.string bsMessageText,
   System.bool bExcludeCurrentUser
)
```

### C++/CLI

```cpp
void SendMsg(
   System.String^ bsSubject,
   System.String^ bsMessageText,
   System.bool bExcludeCurrentUser
)
```

### Parameters

- `bsSubject`: Email subject
- `bsMessageText`: Message detail (see **Remarks**)
- `bExcludeCurrentUser`: True to not send email to the logged-in user even if he is a member of this group, false to send email to the logged-in user

## Examples

[Add and Remove User and Group from Folder (C#)](Add_and_Remove_User_and_Group_from_Folder_Example_CSharp.htm)
[Add and Remove User and Group from Folder (VB.NET)](Add_and_Remove_User_and_Group_from_Folder_Example_VBNET.htm)

## Remarks

It is possible to send HTML-formatted mail, if the recipients use a mail system that supports HTML. In so, add HTML tags to the text in bsMessageText:

<html><body><h1>Hello!</h1>How are you?</body></html>

Call [IEdmUser5::SendMsg](EPDM.Interop.epdm~EPDM.Interop.epdm.IEdmUser5~SendMsg.html) to send email to an individual user.

[Return codes:](ReturnCodes.htm)

- S_OK: The method successfully executed.

## See Also

[IEdmUserGroup5 Interface](EPDM.Interop.epdm~EPDM.Interop.epdm.IEdmUserGroup5.html)
[IEdmUserGroup5 Members](EPDM.Interop.epdm~EPDM.Interop.epdm.IEdmUserGroup5_members.html)

## Availability

SOLIDWORKS PDM Professional version 5.2
