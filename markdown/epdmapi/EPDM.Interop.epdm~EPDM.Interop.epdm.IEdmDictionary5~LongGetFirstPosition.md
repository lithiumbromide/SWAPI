---
title: "LongGetFirstPosition Method (IEdmDictionary5)"
project: "SOLIDWORKS PDM Professional API Help"
interface: "IEdmDictionary5"
member: "LongGetFirstPosition"
kind: "method"
source: "epdmapi/EPDM.Interop.epdm~EPDM.Interop.epdm.IEdmDictionary5~LongGetFirstPosition.html"
---

# LongGetFirstPosition Method (IEdmDictionary5)

Starts an enumeration of all of the key-value pairs that have integer keys.

## Syntax

### Visual Basic

```vb
Function LongGetFirstPosition() As IEdmPos5
```

### C#

```csharp
IEdmPos5 LongGetFirstPosition()
```

### C++/CLI

```cpp
IEdmPos5^ LongGetFirstPosition();
```

### Return Value

[IEdmPos5](EPDM.Interop.epdm~EPDM.Interop.epdm.IEdmPos5.html); position of the first key-value pair

## Examples

[Get and Set Dictionary Key-Value Pairs (VB.NET)](Get_and_Set_Key_Value_Pairs_Example_VBNET.htm)
[Get and Set Dictionary Key-Value Pairs (C#)](Get_and_Set_Key_Value_Pairs_Example_CSharp.htm)

## Remarks

After calling this method, pass the position of the first key-value pair to [IEdmDictionary5::LongGetNextAssoc](EPDM.Interop.epdm~EPDM.Interop.epdm.IEdmDictionary5~LongGetNextAssoc.html) to get the first key-value pair in the search result. Then call IEdmDictionary5::LongGetNextAssoc repeatedly to get the rest of the key-value pairs in the search result.

C++ programmers not using smart-pointer wrapper functions must release the returned pointer to IEdmPos5.

[Return codes](ReturnCodes.htm):

- S_OK: The method successfully executed.
- S_FALSE: One of the arguments is invalid.

## See Also

[IEdmDictionary5 Interface](EPDM.Interop.epdm~EPDM.Interop.epdm.IEdmDictionary5.html)
[IEdmDictionary5 Members](EPDM.Interop.epdm~EPDM.Interop.epdm.IEdmDictionary5_members.html)
[IEdmDictionary5::StringGetFirstPosition Method ()](EPDM.Interop.epdm~EPDM.Interop.epdm.IEdmDictionary5~StringGetFirstPosition.html)

## Availability

SOLIDWORKS PDM Professional Version 5.2
