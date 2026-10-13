---
title: "LongGetNextAssoc Method (IEdmDictionary5)"
project: "SOLIDWORKS PDM Professional API Help"
interface: "IEdmDictionary5"
member: "LongGetNextAssoc"
kind: "method"
source: "epdmapi/EPDM.Interop.epdm~EPDM.Interop.epdm.IEdmDictionary5~LongGetNextAssoc.html"
---

# LongGetNextAssoc Method (IEdmDictionary5)

Gets the key-value pair at the next position of an enumeration.

## Syntax

### Visual Basic

```vb
Sub LongGetNextAssoc( _
   ByVal poPos As IEdmPos5, _
   ByRef plRetKey As System.Integer, _
   ByRef pbsRetValue As System.String _
)
```

### C#

```csharp
void LongGetNextAssoc(
   IEdmPos5 poPos,
   out System.int plRetKey,
   out System.string pbsRetValue
)
```

### C++/CLI

```cpp
void LongGetNextAssoc(
   IEdmPos5^ poPos,
   [Out] System.int plRetKey,
   [Out] System.String^ pbsRetValue
)
```

### Parameters

- `poPos`: [IEdmPos5](EPDM.Interop.epdm~EPDM.Interop.epdm.IEdmPos5.html); position of the next key-value pair (see **Remarks**)
- `plRetKey`: Key in the next pair
- `pbsRetValue`: Value in the next pair

## Examples

[Get and Set Dictionary Key-Value Pairs (VB.NET)](Get_and_Set_Key_Value_Pairs_Example_VBNET.htm)
[Get and Set Dictionary Key-Value Pairs (C#)](Get_and_Set_Key_Value_Pairs_Example_CSharp.htm)

## Remarks

Before calling this method the first time, you must populate poPos with the interface to the position of the first key-value pair. Call one of the following to obtain IEdmPos5 for the position of the first pair:

- [IEdmDictionary5::LongGetFirstPosition](EPDM.Interop.epdm~EPDM.Interop.epdm.IEdmDictionary5~LongGetFirstPosition.html)
- [IEdmDictionary5::LongFindKeys](EPDM.Interop.epdm~EPDM.Interop.epdm.IEdmDictionary5~LongFindKeys.html)
- [IEdmDictionary5::LongFindValues](EPDM.Interop.epdm~EPDM.Interop.epdm.IEdmDictionary5~LongFindValues.html)

After calling this method the first time, poPos is automatically incremented every time it is called. Call this method repeatedly to obtain the rest of the key-value pairs.

Between calls, you should call [IEdmPos5::IsNull](EPDM.Interop.epdm~EPDM.Interop.epdm.IEdmPos5~IsNull.html) to verify that you have not gone past the last key-value pair.

C++ programmers must release the returned string by calling SysFreeString.

[Return codes](ReturnCodes.htm):

- S_OK: The method successfully executed.
- E_EDM_END_OF_LIST: You have gone past the end of the list.

## See Also

[IEdmDictionary5 Interface](EPDM.Interop.epdm~EPDM.Interop.epdm.IEdmDictionary5.html)
[IEdmDictionary5 Members](EPDM.Interop.epdm~EPDM.Interop.epdm.IEdmDictionary5_members.html)
[IEdmDictionary5::StringGetNextAssoc Method ()](EPDM.Interop.epdm~EPDM.Interop.epdm.IEdmDictionary5~StringGetNextAssoc.html)

## Availability

SOLIDWORKS PDM Professional Version 5.2
