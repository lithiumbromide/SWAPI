---
title: "StringTestAndSetAt Method (IEdmDictionary5)"
project: "SOLIDWORKS PDM Professional API Help"
interface: "IEdmDictionary5"
member: "StringTestAndSetAt"
kind: "method"
source: "API_GB/EPDM.Interop.epdm~EPDM.Interop.epdm.IEdmDictionary5~StringTestAndSetAt.html"
---

# StringTestAndSetAt Method (IEdmDictionary5)

Creates the specified string key if it does not exist and sets its value.

## Syntax

### Visual Basic

```vb
Function StringTestAndSetAt( _
   ByVal bsKey As System.String, _
   ByVal bsValue As System.String _
) As System.Boolean
```

### C#

```csharp
System.bool StringTestAndSetAt(
   System.string bsKey,
   System.string bsValue
)
```

### C++/CLI

```cpp
System.bool StringTestAndSetAt(
   System.String^ bsKey,
   System.String^ bsValue
)
```

### Parameters

- `bsKey`: Key for which to set a value
- `bsValue`: New value

### Return Value

True if the value of a new key is successfully set, false if not

## Examples

[Change Card Variables Add-in (VB.NET)](Change_Card_Variables_Addin_Example_VBNET.htm)
[Change Card Variables Add-in (C#)](Change_Card_Variables_Addin_Example_CSharp.htm)
[Create and Delete Dictionaries (C#)](Create_and_Delete_Dictionaries_Example_CSharp.htm)
[Create and Delete Dictionaries (VB.NET)](Create_and_Delete_Dictionaries_Example_VBNET.htm)

## Remarks

The testing and setting are both performed in a single operation. A test-and-set function like this is useful when you need a semaphore to synchronize several clients accessing the same data. See the example in [IEdmDictionary5::LongTestAndSetAt](EPDM.Interop.epdm~EPDM.Interop.epdm.IEdmDictionary5~LongTestAndSetAt.html).

[Return codes](ReturnCodes.htm):

- S_OK: The method successfully executed.
- S_FALSE: One of the arguments is invalid.

## See Also

[IEdmDictionary5 Interface](EPDM.Interop.epdm~EPDM.Interop.epdm.IEdmDictionary5.html)
[IEdmDictionary5 Members](EPDM.Interop.epdm~EPDM.Interop.epdm.IEdmDictionary5_members.html)
[IEdmDictionary5::StringSetAt Method ()](EPDM.Interop.epdm~EPDM.Interop.epdm.IEdmDictionary5~StringSetAt.html)

## Availability

SOLIDWORKS PDM Professional Version 5.2
