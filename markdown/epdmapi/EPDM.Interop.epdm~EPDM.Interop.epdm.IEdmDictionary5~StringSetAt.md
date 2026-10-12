---
title: "StringSetAt Method (IEdmDictionary5)"
project: "SOLIDWORKS PDM Professional API Help"
interface: "IEdmDictionary5"
member: "StringSetAt"
kind: "method"
source: "epdmapi/EPDM.Interop.epdm~EPDM.Interop.epdm.IEdmDictionary5~StringSetAt.html"
---

# StringSetAt Method (IEdmDictionary5)

Sets the value for the specified string key.

## Syntax

### Visual Basic

```vb
Sub StringSetAt( _
   ByVal bsKey As System.String, _
   ByVal bsValue As System.String _
)
```

### C#

```csharp
void StringSetAt(
   System.string bsKey,
   System.string bsValue
)
```

### C++/CLI

```cpp
void StringSetAt(
   System.String^ bsKey,
   System.String^ bsValue
)
```

### Parameters

- `bsKey`: Key whose value to set
- `bsValue`: New value

## Examples

See the examples for [IEdmDictionary5](EPDM.Interop.epdm~EPDM.Interop.epdm.IEdmDictionary5.html).

## Remarks

[Return codes](ReturnCodes.htm):

- S_OK: The method successfully executed.
- S_FALSE: One of the arguments is invalid.

## See Also

[IEdmDictionary5 Interface](EPDM.Interop.epdm~EPDM.Interop.epdm.IEdmDictionary5.html)
[IEdmDictionary5 Members](EPDM.Interop.epdm~EPDM.Interop.epdm.IEdmDictionary5_members.html)
[IEdmDictionary5::StringGetAt Method ()](EPDM.Interop.epdm~EPDM.Interop.epdm.IEdmDictionary5~StringGetAt.html)
[IEdmDictionary5::StringRemoveAt Method ()](EPDM.Interop.epdm~EPDM.Interop.epdm.IEdmDictionary5~StringRemoveAt.html)
[IEdmDictionary5::LongSetAt Method ()](EPDM.Interop.epdm~EPDM.Interop.epdm.IEdmDictionary5~LongSetAt.html)

## Availability

SOLIDWORKS PDM Professional Version 5.2
