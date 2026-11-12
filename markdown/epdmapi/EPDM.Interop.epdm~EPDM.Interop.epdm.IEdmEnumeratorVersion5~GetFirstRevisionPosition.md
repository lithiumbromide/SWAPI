---
title: "GetFirstRevisionPosition Method (IEdmEnumeratorVersion5)"
project: "SOLIDWORKS PDM Professional API Help"
interface: "IEdmEnumeratorVersion5"
member: "GetFirstRevisionPosition"
kind: "method"
source: "epdmapi/EPDM.Interop.epdm~EPDM.Interop.epdm.IEdmEnumeratorVersion5~GetFirstRevisionPosition.html"
---

# GetFirstRevisionPosition Method (IEdmEnumeratorVersion5)

Starts an enumeration of the revisions set on this file.

## Syntax

### Visual Basic

```vb
Function GetFirstRevisionPosition() As IEdmPos5
```

### C#

```csharp
IEdmPos5 GetFirstRevisionPosition()
```

### C++/CLI

```cpp
IEdmPos5^ GetFirstRevisionPosition();
```

### Return Value

[IEdmPos5](EPDM.Interop.epdm~EPDM.Interop.epdm.IEdmPos5.html); position of the first revision set on this file

## Remarks

After calling this method, pass the returned first revision position to [IEdmEnumeratorVersion5::GetNextRevision](EPDM.Interop.epdm~EPDM.Interop.epdm.IEdmEnumeratorVersion5~GetNextRevision.html) to get the first revision. Then call IEdmEnumeratorVersion5::GetNextRevision repeatedly to get the rest of the revisions set on this file.

C++ programmers not using smart-pointer wrapper functions must release the returned interface, IEdmPos5.

[Return codes](ReturnCodes.htm):

- S_OK: The method successfully executed.
- S_FALSE: An argument is invalid.

## See Also

[IEdmEnumeratorVersion5 Interface](EPDM.Interop.epdm~EPDM.Interop.epdm.IEdmEnumeratorVersion5.html)
[IEdmEnumeratorVersion5 Members](EPDM.Interop.epdm~EPDM.Interop.epdm.IEdmEnumeratorVersion5_members.html)

## Availability

SOLIDWORKS PDM Professional Version 5.2
