---
title: "GetFirstMessagePosition Method (IEdmInbox5)"
project: "SOLIDWORKS PDM Professional API Help"
interface: "IEdmInbox5"
member: "GetFirstMessagePosition"
kind: "method"
source: "epdmapi/EPDM.Interop.epdm~EPDM.Interop.epdm.IEdmInbox5~GetFirstMessagePosition.html"
---

# GetFirstMessagePosition Method (IEdmInbox5)

Starts an enumeration of the messages in this inbox.

## Syntax

### Visual Basic

```vb
Function GetFirstMessagePosition( _
   Optional ByVal lEdmGetMsgFlags As System.Integer _
) As IEdmPos5
```

### C#

```csharp
IEdmPos5 GetFirstMessagePosition(
   System.int lEdmGetMsgFlags
)
```

### C++/CLI

```cpp
IEdmPos5^ GetFirstMessagePosition(
   System.int lEdmGetMsgFlags
)
```

### Parameters

- `lEdmGetMsgFlags`: Combination of [EdmGetMsgFlag](EPDM.Interop.epdm~EPDM.Interop.epdm.EdmGetMsgFlag.html) bits indicating which messages to enumerate

### Return Value

[IEdmPos5](EPDM.Interop.epdm~EPDM.Interop.epdm.IEdmPos5.html); position of the first message in the inbox

## Examples

[Get Messages (C#)](Get_Messages_Example_CSharp.htm)
[Get Messages (VB.NET)](Get_Messages_Example_VBNET.htm)

## Remarks

This method only works to enumerate messages of the user currently logged in to the vault.

After calling this method, pass the returned first message position to [IEdmInbox5::GetNextMessage](EPDM.Interop.epdm~EPDM.Interop.epdm.IEdmInbox5~GetNextMessage.html) to get the first message in the inbox. Then call IEdmInbox5::GetNextMessage repeatedly to get the rest of the messages in the inbox.

C++ programmers not using smart-pointer wrapper functions must release the returned interface, IEdmPos5.

[Return codes](ReturnCodes.htm):

- S_OK: The method successfully executed.
- E_EDM_PERMISSION_DENIED: You tried to access somebody else's messages.

## See Also

[IEdmInbox5 Interface](EPDM.Interop.epdm~EPDM.Interop.epdm.IEdmInbox5.html)
[IEdmInbox5 Members](EPDM.Interop.epdm~EPDM.Interop.epdm.IEdmInbox5_members.html)

## Availability

SOLIDWORKS PDM Professional Version 5.3
