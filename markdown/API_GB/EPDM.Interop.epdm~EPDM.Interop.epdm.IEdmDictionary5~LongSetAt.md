---
title: "LongSetAt Method (IEdmDictionary5)"
project: "SOLIDWORKS PDM Professional API Help"
interface: "IEdmDictionary5"
member: "LongSetAt"
kind: "method"
source: "API_GB/EPDM.Interop.epdm~EPDM.Interop.epdm.IEdmDictionary5~LongSetAt.html"
---

# LongSetAt Method (IEdmDictionary5)

Sets the value for the specified integer key.

## Syntax

### Visual Basic

```vb
Sub LongSetAt( _
   ByVal lKey As System.Integer, _
   ByVal bsValue As System.String _
)
```

### C#

```csharp
void LongSetAt(
   System.int lKey,
   System.string bsValue
)
```

### C++/CLI

```cpp
void LongSetAt(
   System.int lKey,
   System.String^ bsValue
)
```

### Parameters

- `lKey`: Key whose value to set
- `bsValue`: New value

## Examples

[Get and Set Dictionary Key-Value Pairs (VB.NET)](Get_and_Set_Key_Value_Pairs_Example_VBNET.htm)
[Get and Set Dictionary Key-Value Pairs (C#)](Get_and_Set_Key_Value_Pairs_Example_CSharp.htm)

## Remarks

[Return codes](ReturnCodes.htm):

- S_OK: The method successfully executed.
- S_FALSE: One of the arguments is invalid.

## See Also

[IEdmDictionary5 Interface](EPDM.Interop.epdm~EPDM.Interop.epdm.IEdmDictionary5.html)
[IEdmDictionary5 Members](EPDM.Interop.epdm~EPDM.Interop.epdm.IEdmDictionary5_members.html)
[IEdmDictionary5::StringSetAt Method ()](EPDM.Interop.epdm~EPDM.Interop.epdm.IEdmDictionary5~StringSetAt.html)
[IEdmDictionary5::LongRemoveAt Method ()](EPDM.Interop.epdm~EPDM.Interop.epdm.IEdmDictionary5~LongRemoveAt.html)
[IEdmDictionary5::LongGetAt Method ()](EPDM.Interop.epdm~EPDM.Interop.epdm.IEdmDictionary5~LongGetAt.html)

## Availability

SOLIDWORKS PDM Professional Version 5.2
