---
title: "StringGetAt Method (IEdmDictionary5)"
project: "SOLIDWORKS PDM Professional API Help"
interface: "IEdmDictionary5"
member: "StringGetAt"
kind: "method"
source: "API_GB/EPDM.Interop.epdm~EPDM.Interop.epdm.IEdmDictionary5~StringGetAt.html"
---

# StringGetAt Method (IEdmDictionary5)

Gets the value for the specified string key.

## Syntax

### Visual Basic

```vb
Function StringGetAt( _
   ByVal bsKey As System.String, _
   ByRef pbsRetValue As System.String _
) As System.Boolean
```

### C#

```csharp
System.bool StringGetAt(
   System.string bsKey,
   out System.string pbsRetValue
)
```

### C++/CLI

```cpp
System.bool StringGetAt(
   System.String^ bsKey,
   [Out] System.String^ pbsRetValue
)
```

### Parameters

- `bsKey`: Key for which to get a value
- `pbsRetValue`: Value for the specified key

### Return Value

True if the key was found, false if not

## Examples

[Change Card Variables Add-in (VB.NET)](Change_Card_Variables_Addin_Example_VBNET.htm)
[Change Card Variables Add-in (C#)](Change_Card_Variables_Addin_Example_CSharp.htm)

## Remarks

C++ programmers must release the returned string by calling SysFreeString.

[Return codes](ReturnCodes.htm):

- S_OK: The method successfully executed.
- S_FALSE: The key was not found.

## See Also

[IEdmDictionary5 Interface](EPDM.Interop.epdm~EPDM.Interop.epdm.IEdmDictionary5.html)
[IEdmDictionary5 Members](EPDM.Interop.epdm~EPDM.Interop.epdm.IEdmDictionary5_members.html)
[IEdmDictionary5::StringSetAt Method ()](EPDM.Interop.epdm~EPDM.Interop.epdm.IEdmDictionary5~StringSetAt.html)
[IEdmDictionary5::StringRemoveAt Method ()](EPDM.Interop.epdm~EPDM.Interop.epdm.IEdmDictionary5~StringRemoveAt.html)
[IEdmDictionary5::LongGetAt Method ()](EPDM.Interop.epdm~EPDM.Interop.epdm.IEdmDictionary5~LongGetAt.html)

## Availability

SOLIDWORKS PDM Professional Version 5.2
