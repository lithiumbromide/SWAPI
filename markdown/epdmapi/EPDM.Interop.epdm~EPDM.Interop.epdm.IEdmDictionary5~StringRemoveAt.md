---
title: "StringRemoveAt Method (IEdmDictionary5)"
project: "SOLIDWORKS PDM Professional API Help"
interface: "IEdmDictionary5"
member: "StringRemoveAt"
kind: "method"
source: "epdmapi/EPDM.Interop.epdm~EPDM.Interop.epdm.IEdmDictionary5~StringRemoveAt.html"
---

# StringRemoveAt Method (IEdmDictionary5)

Deletes the specified string key and its value.

## Syntax

### Visual Basic

```vb
Sub StringRemoveAt( _
   ByVal bsKey As System.String _
)
```

### C#

```csharp
void StringRemoveAt(
   System.string bsKey
)
```

### C++/CLI

```cpp
void StringRemoveAt(
   System.String^ bsKey
)
```

### Parameters

- `bsKey`: Key to remove

## Examples

[Create and Delete Dictionaries (C#)](Create_and_Delete_Dictionaries_Example_CSharp.htm)
[Create and Delete Dictionaries (VB.NET)](Create_and_Delete_Dictionaries_Example_VBNET.htm)

## Remarks

[Return codes](ReturnCodes.htm):

- S_OK: The method successfully executed.
- S_FALSE: One of the arguments is invalid

## See Also

[IEdmDictionary5 Interface](EPDM.Interop.epdm~EPDM.Interop.epdm.IEdmDictionary5.html)
[IEdmDictionary5 Members](EPDM.Interop.epdm~EPDM.Interop.epdm.IEdmDictionary5_members.html)
[IEdmDictionary5::LongRemoveAt Method ()](EPDM.Interop.epdm~EPDM.Interop.epdm.IEdmDictionary5~LongRemoveAt.html)
[IEdmDictionary5::StringSetAt Method ()](EPDM.Interop.epdm~EPDM.Interop.epdm.IEdmDictionary5~StringSetAt.html)

## Availability

SOLIDWORKS PDM Professional Version 5.2
