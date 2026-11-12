---
title: "StringFindKeys Method (IEdmDictionary5)"
project: "SOLIDWORKS PDM Professional API Help"
interface: "IEdmDictionary5"
member: "StringFindKeys"
kind: "method"
source: "epdmapi/EPDM.Interop.epdm~EPDM.Interop.epdm.IEdmDictionary5~StringFindKeys.html"
---

# StringFindKeys Method (IEdmDictionary5)

Starts an enumeration of all the key-value pairs whose string keys contain the specified text.

## Syntax

### Visual Basic

```vb
Function StringFindKeys( _
   ByVal bsKeySubString As System.String _
) As IEdmPos5
```

### C#

```csharp
IEdmPos5 StringFindKeys(
   System.string bsKeySubString
)
```

### C++/CLI

```cpp
IEdmPos5^ StringFindKeys(
   System.String^ bsKeySubString
)
```

### Parameters

- `bsKeySubString`: Text to search for

### Return Value

[IEdmPos5](EPDM.Interop.epdm~EPDM.Interop.epdm.IEdmPos5.html); position of the first key-value pair in the search result

## Examples

[Get and Set Dictionary Key-Value Pairs (VB.NET)](Get_and_Set_Key_Value_Pairs_Example_VBNET.htm)
[Get and Set Dictionary Key-Value Pairs (C#)](Get_and_Set_Key_Value_Pairs_Example_CSharp.htm)

## Remarks

After calling this method, call [IEdmDictionary5::StringGetNextAssoc](EPDM.Interop.epdm~EPDM.Interop.epdm.IEdmDictionary5~StringGetNextAssoc.html) repeatedly to enumerate the rest of the key-value pairs in the search result.

[Return codes](ReturnCodes.htm):

- S_OK: The method successfully executed.
- S_FALSE: One of the arguments is invalid.

## See Also

[IEdmDictionary5 Interface](EPDM.Interop.epdm~EPDM.Interop.epdm.IEdmDictionary5.html)
[IEdmDictionary5 Members](EPDM.Interop.epdm~EPDM.Interop.epdm.IEdmDictionary5_members.html)
[IEdmDictionary5::LongFindKeys Method ()](EPDM.Interop.epdm~EPDM.Interop.epdm.IEdmDictionary5~LongFindKeys.html)
[IEdmDictionary5::LongFindValues Method ()](EPDM.Interop.epdm~EPDM.Interop.epdm.IEdmDictionary5~LongFindValues.html)
[IEdmDictionary5::StringFindValues Method ()](EPDM.Interop.epdm~EPDM.Interop.epdm.IEdmDictionary5~StringFindValues.html)

## Availability

SOLIDWORKS PDM Professional Version 5.2
