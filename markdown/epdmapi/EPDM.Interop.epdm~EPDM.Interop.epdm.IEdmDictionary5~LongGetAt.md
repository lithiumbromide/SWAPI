---
title: "LongGetAt Method (IEdmDictionary5)"
project: "SOLIDWORKS PDM Professional API Help"
interface: "IEdmDictionary5"
member: "LongGetAt"
kind: "method"
source: "epdmapi/EPDM.Interop.epdm~EPDM.Interop.epdm.IEdmDictionary5~LongGetAt.html"
---

# LongGetAt Method (IEdmDictionary5)

Gets the value for the specified integer key.

## Syntax

### Visual Basic

```vb
Function LongGetAt( _
   ByVal lKey As System.Integer, _
   ByRef pbsRetValue As System.String _
) As System.Boolean
```

### C#

```csharp
System.bool LongGetAt(
   System.int lKey,
   out System.string pbsRetValue
)
```

### C++/CLI

```cpp
System.bool LongGetAt(
   System.int lKey,
   [Out] System.String^ pbsRetValue
)
```

### Parameters

- `lKey`: Key for which to get a value
- `pbsRetValue`: Value for the specified key

### Return Value

True if the key was found, false if not

## Examples

[Get and Set Dictionary Key-Value Pairs (VB.NET)](Get_and_Set_Key_Value_Pairs_Example_VBNET.htm)
[Get and Set Dictionary Key-Value Pairs (C#)](Get_and_Set_Key_Value_Pairs_Example_CSharp.htm)

## Remarks

C++ programmers must release the returned string by calling SysFreeString.

[Return codes](ReturnCodes.htm):

- S_OK: The method successfully executed.
- S_FALSE: The key was not found.

## See Also

[IEdmDictionary5 Interface](EPDM.Interop.epdm~EPDM.Interop.epdm.IEdmDictionary5.html)
[IEdmDictionary5 Members](EPDM.Interop.epdm~EPDM.Interop.epdm.IEdmDictionary5_members.html)
[IEdmDictionary5::StringGetAt Method ()](EPDM.Interop.epdm~EPDM.Interop.epdm.IEdmDictionary5~StringGetAt.html)
[IEdmDictionary5::LongSetAt Method ()](EPDM.Interop.epdm~EPDM.Interop.epdm.IEdmDictionary5~LongSetAt.html)
[IEdmDictionary5::LongRemoveAt Method ()](EPDM.Interop.epdm~EPDM.Interop.epdm.IEdmDictionary5~LongRemoveAt.html)

## Availability

SOLIDWORKS PDM Professional Version 5.2
