---
title: "LongFindValues Method (IEdmDictionary5)"
project: "SOLIDWORKS PDM Professional API Help"
interface: "IEdmDictionary5"
member: "LongFindValues"
kind: "method"
source: "API_GB/EPDM.Interop.epdm~EPDM.Interop.epdm.IEdmDictionary5~LongFindValues.html"
---

# LongFindValues Method (IEdmDictionary5)

Starts an enumeration of all of the key-value pairs that have integer keys whose values contain the specified text.

## Syntax

### Visual Basic

```vb
Function LongFindValues( _
   ByVal bsValueSubString As System.String _
) As IEdmPos5
```

### C#

```csharp
IEdmPos5 LongFindValues(
   System.string bsValueSubString
)
```

### C++/CLI

```cpp
IEdmPos5^ LongFindValues(
   System.String^ bsValueSubString
)
```

### Parameters

- `bsValueSubString`: Text to search for

### Return Value

[IEdmPos5](EPDM.Interop.epdm~EPDM.Interop.epdm.IEdmPos5.html); position of the first key in the search result

## Examples

[Get and Set Dictionary Key-Value Pairs (VB.NET)](Get_and_Set_Key_Value_Pairs_Example_VBNET.htm)
[Get and Set Dictionary Key-Value Pairs (C#)](Get_and_Set_Key_Value_Pairs_Example_CSharp.htm)

## Remarks

After calling this method, call [IEdmDictionary5::LongGetNextAssoc](EPDM.Interop.epdm~EPDM.Interop.epdm.IEdmDictionary5~LongGetNextAssoc.html) repeatedly to enumerate the rest of the key-value pairs in the search result.

C++ programmers not using smart-pointer wrapper functions must release the returned pointer to IEdmPos5.

[Return codes](ReturnCodes.htm):

- S_OK: The method successfully executed.
- S_FALSE: One of the arguments is invalid.

## See Also

[IEdmDictionary5 Interface](EPDM.Interop.epdm~EPDM.Interop.epdm.IEdmDictionary5.html)
[IEdmDictionary5 Members](EPDM.Interop.epdm~EPDM.Interop.epdm.IEdmDictionary5_members.html)
[IEdmDictionary::LongFindKeys Method ()](EPDM.Interop.epdm~EPDM.Interop.epdm.IEdmDictionary5~LongFindKeys.html)
[IEdmDictionary::StringFindKeys Method ()](EPDM.Interop.epdm~EPDM.Interop.epdm.IEdmDictionary5~StringFindKeys.html)
[IEdmDictionary::StringFindValues Method ()](EPDM.Interop.epdm~EPDM.Interop.epdm.IEdmDictionary5~StringFindValues.html)

## Availability

SOLIDWORKS PDM Professional Version 5.2
