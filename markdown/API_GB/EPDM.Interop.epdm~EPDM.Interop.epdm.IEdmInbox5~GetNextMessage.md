---
title: "GetNextMessage Method (IEdmInbox5)"
project: "SOLIDWORKS PDM Professional API Help"
interface: "IEdmInbox5"
member: "GetNextMessage"
kind: "method"
source: "API_GB/EPDM.Interop.epdm~EPDM.Interop.epdm.IEdmInbox5~GetNextMessage.html"
---

# GetNextMessage Method (IEdmInbox5)

Gets the next message in the enumeration.

## Syntax

### Visual Basic

```vb
Function GetNextMessage( _
   ByVal poPos As IEdmPos5 _
) As IEdmMessage5
```

### C#

```csharp
IEdmMessage5 GetNextMessage(
   IEdmPos5 poPos
)
```

### C++/CLI

```cpp
IEdmMessage5^ GetNextMessage(
   IEdmPos5^ poPos
)
```

### Parameters

- `poPos`: [IEdmPos5](EPDM.Interop.epdm~EPDM.Interop.epdm.IEdmPos5.html); position of the next message (see **Remarks**)

### Return Value

[IEdmMessage5](EPDM.Interop.epdm~EPDM.Interop.epdm.IEdmMessage5.html)

## Examples

[Get Messages (C#)](Get_Messages_Example_CSharp.htm)
[Get Messages (VB.NET)](Get_Messages_Example_VBNET.htm)

## Remarks

Before calling this method the first time, you must populate poPos with the interface to the position of the first message, IEdmPos5. Call [IEdmInbox5::GetFirstMessagePosition](EPDM.Interop.epdm~EPDM.Interop.epdm.IEdmInbox5~GetFirstMessagePosition.html) to obtain IEdmPos5.

After calling this method the first time, poPos is automatically incremented every time it is called. Call this method repeatedly to obtain the rest of the messages.

Be sure to call [IEdmPos5::IsNull](EPDM.Interop.epdm~EPDM.Interop.epdm.IEdmPos5~IsNull.html) before you call this method to ensure you have not reached the end of the enumeration.

C++ programmers not using smart-pointer wrapper functions must release the returned interface, IEdmMessage5.

[Return codes](ReturnCodes.htm):

- S_OK: The method successfully executed.
- E_EDM_END_OF_LIST: You have gone past the end of the list.

## See Also

[IEdmInbox5 Interface](EPDM.Interop.epdm~EPDM.Interop.epdm.IEdmInbox5.html)
[IEdmInbox5 Members](EPDM.Interop.epdm~EPDM.Interop.epdm.IEdmInbox5_members.html)

## Availability

SOLIDWORKS PDM Professional Version 5.3
