---
title: "GetFirstRefPosition Method (IEdmEnumeratorCustomReference5)"
project: "SOLIDWORKS PDM Professional API Help"
interface: "IEdmEnumeratorCustomReference5"
member: "GetFirstRefPosition"
kind: "method"
source: "epdmapi/EPDM.Interop.epdm~EPDM.Interop.epdm.IEdmEnumeratorCustomReference5~GetFirstRefPosition.html"
---

# GetFirstRefPosition Method (IEdmEnumeratorCustomReference5)

Starts an enumeration of custom file references.

## Syntax

### Visual Basic

```vb
Function GetFirstRefPosition() As IEdmPos5
```

### C#

```csharp
IEdmPos5 GetFirstRefPosition()
```

### C++/CLI

```cpp
IEdmPos5^ GetFirstRefPosition();
```

### Return Value

[IEdmPos5](EPDM.Interop.epdm~EPDM.Interop.epdm.IEdmPos5.html); position of the first custom file reference

## Examples

See the [IEdmEnumeratorCustomReference5](EPDM.Interop.epdm~EPDM.Interop.epdm.IEdmEnumeratorCustomReference5.html) examples.

## Remarks

After calling this method, pass the position of the first custom file reference to [IEdmEnumeratorCustomReference5::GetNextRef](EPDM.Interop.epdm~EPDM.Interop.epdm.IEdmEnumeratorCustomReference5~GetNextRef.html) to get the first custom file reference. Then call IEdmEnumeratorCustomReference5::GetNextRef repeatedly to get the rest of the custom file references.

C++ programmers not using smart-pointer wrapper functions must release the returned pointer to IEdmPos5.

[Return codes](ReturnCodes.htm):

- S_OK: The method successfully executed.
- S_FALSE: One of the arguments is invalid.

## See Also

[IEdmEnumeratorCustomReference5 Interface](EPDM.Interop.epdm~EPDM.Interop.epdm.IEdmEnumeratorCustomReference5.html)
[IEdmEnumeratorCustomReference5 Members](EPDM.Interop.epdm~EPDM.Interop.epdm.IEdmEnumeratorCustomReference5_members.html)

## Availability

SOLIDWORKS PDM Professional Version 5.2
