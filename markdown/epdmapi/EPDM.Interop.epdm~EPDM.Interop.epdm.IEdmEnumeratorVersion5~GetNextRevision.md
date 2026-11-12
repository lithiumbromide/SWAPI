---
title: "GetNextRevision Method (IEdmEnumeratorVersion5)"
project: "SOLIDWORKS PDM Professional API Help"
interface: "IEdmEnumeratorVersion5"
member: "GetNextRevision"
kind: "method"
source: "epdmapi/EPDM.Interop.epdm~EPDM.Interop.epdm.IEdmEnumeratorVersion5~GetNextRevision.html"
---

# GetNextRevision Method (IEdmEnumeratorVersion5)

Gets the revision at the next position of this enumeration.

## Syntax

### Visual Basic

```vb
Function GetNextRevision( _
   ByVal poPos As IEdmPos5 _
) As IEdmRevision5
```

### C#

```csharp
IEdmRevision5 GetNextRevision(
   IEdmPos5 poPos
)
```

### C++/CLI

```cpp
IEdmRevision5^ GetNextRevision(
   IEdmPos5^ poPos
)
```

### Parameters

- `poPos`: [IEdmPos5](EPDM.Interop.epdm~EPDM.Interop.epdm.IEdmPos5.html); position of the next revision

### Return Value

[IEdmRevision5](EPDM.Interop.epdm~EPDM.Interop.epdm.IEdmRevision5.html)

## Remarks

Before calling this method the first time, you must populate poPos with the interface to the position of the first revision, IEdmPos5. Call [IEdmEnumeratorVersion5::GetFirstRevisionPosition](EPDM.Interop.epdm~EPDM.Interop.epdm.IEdmEnumeratorVersion5~GetFirstRevisionPosition.html) to obtain IEdmPos5.

After calling this method the first time, poPos is automatically incremented every time it is called. Call this method repeatedly to obtain the rest of the revisions.

Be sure to call [IEdmPos5::IsNull](EPDM.Interop.epdm~EPDM.Interop.epdm.IEdmPos5~IsNull.html) before you call this method to ensure you have not reached the end of the enumeration.

C++ programmers not using smart-pointer wrapper functions must release the returned interface, IEdmPos5.

[Return codes](ReturnCodes.htm):

- S_OK: The method successfully executed.
- E_EDM_END_OF_LIST: You have gone past the end of the list.

## See Also

[IEdmEnumeratorVersion5 Interface](EPDM.Interop.epdm~EPDM.Interop.epdm.IEdmEnumeratorVersion5.html)
[IEdmEnumeratorVersion5 Members](EPDM.Interop.epdm~EPDM.Interop.epdm.IEdmEnumeratorVersion5_members.html)

## Availability

SOLIDWORKS PDM Professional Version 5.2
