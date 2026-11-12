---
title: "LongTestAndSetAt Method (IEdmDictionary5)"
project: "SOLIDWORKS PDM Professional API Help"
interface: "IEdmDictionary5"
member: "LongTestAndSetAt"
kind: "method"
source: "epdmapi/EPDM.Interop.epdm~EPDM.Interop.epdm.IEdmDictionary5~LongTestAndSetAt.html"
---

# LongTestAndSetAt Method (IEdmDictionary5)

Creates the specified integer key if it does not exist and sets its value.

## Syntax

### Visual Basic

```vb
Function LongTestAndSetAt( _
   ByVal lKey As System.Integer, _
   ByVal bsValue As System.String _
) As System.Boolean
```

### C#

```csharp
System.bool LongTestAndSetAt(
   System.int lKey,
   System.string bsValue
)
```

### C++/CLI

```cpp
System.bool LongTestAndSetAt(
   System.int lKey,
   System.String^ bsValue
)
```

### Parameters

- `lKey`: Key for which to set a value
- `bsValue`: New value

### Return Value

True if the value of a new key is successfully set, false otherwise

## Examples

[Get and Set Dictionary Key-Value Pairs (VB.NET)](Get_and_Set_Key_Value_Pairs_Example_VBNET.htm)
[Get and Set Dictionary Key-Value Pairs (C#)](Get_and_Set_Key_Value_Pairs_Example_CSharp.htm)

## Remarks

The testing and the setting are both performed in a single operation. A test-and-set function like this can be useful if you need a semaphore to synchronize several clients accessing the same data.

[Return codes](ReturnCodes.htm):

- S_OK: The method successfully executed.
- S_FALSE: One of the arguments is invalid.

## See Also

[IEdmDictionary5 Interface](EPDM.Interop.epdm~EPDM.Interop.epdm.IEdmDictionary5.html)
[IEdmDictionary5 Members](EPDM.Interop.epdm~EPDM.Interop.epdm.IEdmDictionary5_members.html)
[IEdmDictionary5::StringTestAndSetAt Method ()](EPDM.Interop.epdm~EPDM.Interop.epdm.IEdmDictionary5~StringTestAndSetAt.html)
[IEdmDictionary5::LongSetAt Method ()](EPDM.Interop.epdm~EPDM.Interop.epdm.IEdmDictionary5~LongSetAt.html)

## Availability

SOLIDWORKS PDM Professional Version 5.2
