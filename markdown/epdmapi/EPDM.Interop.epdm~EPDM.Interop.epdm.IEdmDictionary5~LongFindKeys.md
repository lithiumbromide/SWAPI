---
title: "LongFindKeys Method (IEdmDictionary5)"
project: "SOLIDWORKS PDM Professional API Help"
interface: "IEdmDictionary5"
member: "LongFindKeys"
kind: "method"
source: "epdmapi/EPDM.Interop.epdm~EPDM.Interop.epdm.IEdmDictionary5~LongFindKeys.html"
---

# LongFindKeys Method (IEdmDictionary5)

Starts an enumeration of all of the key-value pairs that have integer keys in the specified range.

## Syntax

### Visual Basic

```vb
Function LongFindKeys( _
   ByVal lMinKey As System.Integer, _
   ByVal lMaxKey As System.Integer _
) As IEdmPos5
```

### C#

```csharp
IEdmPos5 LongFindKeys(
   System.int lMinKey,
   System.int lMaxKey
)
```

### C++/CLI

```cpp
IEdmPos5^ LongFindKeys(
   System.int lMinKey,
   System.int lMaxKey
)
```

### Parameters

- `lMinKey`: Minimum key
- `lMaxKey`: Maximum key

### Return Value

[IEdmPos5](EPDM.Interop.epdm~EPDM.Interop.epdm.IEdmPos5.html); position of the first key in the search result

## Examples

[Get and Set Dictionary Key-Value Pairs (VB.NET)](Get_and_Set_Key_Value_Pairs_Example_VBNET.htm)
[Get and Set Dictionary Key-Value Pairs (C#)](Get_and_Set_Key_Value_Pairs_Example_CSharp.htm)

## Remarks

After calling this method, call [IEdmDictionary5::LongGetNextAssoc](EPDM.Interop.epdm~EPDM.Interop.epdm.IEdmDictionary5~LongGetNextAssoc.html) repeatedly to enumerate the rest of the key-value pairs in the search result.

[Return codes](ReturnCodes.htm):

- S_OK: The method successfully executed.
- S_FALSE: One of the arguments is invalid.

## See Also

[IEdmDictionary5 Interface](EPDM.Interop.epdm~EPDM.Interop.epdm.IEdmDictionary5.html)
[IEdmDictionary5 Members](EPDM.Interop.epdm~EPDM.Interop.epdm.IEdmDictionary5_members.html)
[IEdmDictionary5::StringFindKeys Method ()](EPDM.Interop.epdm~EPDM.Interop.epdm.IEdmDictionary5~StringFindKeys.html)
[IEdmDictionary5::StringFindValues Method ()](EPDM.Interop.epdm~EPDM.Interop.epdm.IEdmDictionary5~StringFindValues.html)
[IEdmDictionary5::LongFindValues Method ()](EPDM.Interop.epdm~EPDM.Interop.epdm.IEdmDictionary5~LongFindValues.html)

## Availability

SOLIDWORKS PDM Professional Version 5.2
