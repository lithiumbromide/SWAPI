---
title: "StringGetFirstPosition Method (IEdmDictionary5)"
project: "SOLIDWORKS PDM Professional API Help"
interface: "IEdmDictionary5"
member: "StringGetFirstPosition"
kind: "method"
source: "epdmapi/EPDM.Interop.epdm~EPDM.Interop.epdm.IEdmDictionary5~StringGetFirstPosition.html"
---

# StringGetFirstPosition Method (IEdmDictionary5)

Starts an enumeration of all of the key-value pairs that have string keys.

## Syntax

### Visual Basic

```vb
Function StringGetFirstPosition() As IEdmPos5
```

### C#

```csharp
IEdmPos5 StringGetFirstPosition()
```

### C++/CLI

```cpp
IEdmPos5^ StringGetFirstPosition();
```

### Return Value

[IEdmPos5](EPDM.Interop.epdm~EPDM.Interop.epdm.IEdmPos5.html); position of the first key-value pair

## Examples

[Create and Delete Dictionaries (C#)](Create_and_Delete_Dictionaries_Example_CSharp.htm)
[Create and Delete Dictionaries (VB.NET)](Create_and_Delete_Dictionaries_Example_VBNET.htm)

## Remarks

After calling this method, pass the position of the first key-value pair to [IEdmDictionary5::StringGetNextAssoc](EPDM.Interop.epdm~EPDM.Interop.epdm.IEdmDictionary5~StringGetNextAssoc.html) to get the first key-value pair in the search result. Then call IEdmDictionary5::StringGetNextAssoc repeatedly to get the rest of the key-value pairs in the search result.

C++ programmers not using smart-pointer wrapper functions must release the returned pointer to IEdmPos5.

[Return codes](ReturnCodes.htm):

- S_OK: The method successfully executed.
- S_FALSE: One of the arguments is invalid.

## See Also

[IEdmDictionary5 Interface](EPDM.Interop.epdm~EPDM.Interop.epdm.IEdmDictionary5.html)
[IEdmDictionary5 Members](EPDM.Interop.epdm~EPDM.Interop.epdm.IEdmDictionary5_members.html)
[IEdmDictionary5::LongGetFirstPosition Method ()](EPDM.Interop.epdm~EPDM.Interop.epdm.IEdmDictionary5~LongGetFirstPosition.html)

## Availability

SOLIDWORKS PDM Professional Version 5.2
