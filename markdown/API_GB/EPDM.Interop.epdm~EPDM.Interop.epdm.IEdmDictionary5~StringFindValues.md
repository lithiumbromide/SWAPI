---
title: "StringFindValues Method (IEdmDictionary5)"
project: "SOLIDWORKS PDM Professional API Help"
interface: "IEdmDictionary5"
member: "StringFindValues"
kind: "method"
source: "API_GB/EPDM.Interop.epdm~EPDM.Interop.epdm.IEdmDictionary5~StringFindValues.html"
---

# StringFindValues Method (IEdmDictionary5)

Starts an enumeration of all of the key-value pairs that have string keys whose values contain the specified text.

## Syntax

### Visual Basic

```vb
Function StringFindValues( _
   ByVal bsValueSubString As System.String _
) As IEdmPos5
```

### C#

```csharp
IEdmPos5 StringFindValues(
   System.string bsValueSubString
)
```

### C++/CLI

```cpp
IEdmPos5^ StringFindValues(
   System.String^ bsValueSubString
)
```

### Parameters

- `bsValueSubString`: Text to search for

### Return Value

[IEdmPos5](EPDM.Interop.epdm~EPDM.Interop.epdm.IEdmPos5.html); position of the first key-value pair in the search result

## Examples

[Change Card Variables Add-in (VB.NET)](Change_Card_Variables_Addin_Example_VBNET.htm)
[Change Card Variables Add-in (C#)](Change_Card_Variables_Addin_Example_CSharp.htm)

## Remarks

After calling this method, call [IEdmDictionary5::StringGetNextAssoc](EPDM.Interop.epdm~EPDM.Interop.epdm.IEdmDictionary5~StringGetNextAssoc.html) repeatedly to enumerate the rest of the key-value pairs in the search result.

C++ programmers not using smart-pointer wrapper functions must release the returned pointer to IEdmPos5.

[Return codes](ReturnCodes.htm):

- S_OK: The method successfully executed.
- S_FALSE: One of the arguments is invalid.

## See Also

[IEdmDictionary5 Interface](EPDM.Interop.epdm~EPDM.Interop.epdm.IEdmDictionary5.html)
[IEdmDictionary5 Members](EPDM.Interop.epdm~EPDM.Interop.epdm.IEdmDictionary5_members.html)
[IEdmDictionary5::LongFindValues Method ()](EPDM.Interop.epdm~EPDM.Interop.epdm.IEdmDictionary5~LongFindValues.html)
[IEdmDictionary5::LongFindKeys Method ()](EPDM.Interop.epdm~EPDM.Interop.epdm.IEdmDictionary5~LongFindKeys.html)
[IEdmDictionary5::StringFindKeys Method ()](EPDM.Interop.epdm~EPDM.Interop.epdm.IEdmDictionary5~StringFindKeys.html)

## Availability

SOLIDWORKS PDM Professional Version 5.2
