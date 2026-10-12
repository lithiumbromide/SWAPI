---
title: "GetNextRef Method (IEdmEnumeratorCustomReference5)"
project: "SOLIDWORKS PDM Professional API Help"
interface: "IEdmEnumeratorCustomReference5"
member: "GetNextRef"
kind: "method"
source: "API_GB/EPDM.Interop.epdm~EPDM.Interop.epdm.IEdmEnumeratorCustomReference5~GetNextRef.html"
---

# GetNextRef Method (IEdmEnumeratorCustomReference5)

Obsolete. Supserseded by [IEdmEnumeratorCustomReference6::GetNextRef2](EPDM.Interop.epdm~EPDM.Interop.epdm.IEdmEnumeratorCustomReference6~GetNextRef2.html).

## Syntax

### Visual Basic

```vb
Function GetNextRef( _
   ByVal poPos As IEdmPos5, _
   ByRef plFileID As System.Integer, _
   ByRef plFolderID As System.Integer _
) As System.String
```

### C#

```csharp
System.string GetNextRef(
   IEdmPos5 poPos,
   out System.int plFileID,
   out System.int plFolderID
)
```

### C++/CLI

```cpp
System.String^ GetNextRef(
   IEdmPos5^ poPos,
   [Out] System.int plFileID,
   [Out] System.int plFolderID
)
```

### Parameters

- `poPos`: [IEdmPos5](EPDM.Interop.epdm~EPDM.Interop.epdm.IEdmPos5.html); position of the next custom file reference
- `plFileID`: ID of the referenced file
- `plFolderID`: ID of the parent folder of the referenced file

### Return Value

Path name of the referenced file

## Remarks

Before calling this method the first time, you must populate poPos with the interface to the position of the first custom file reference, IEdmPos5. Call [IEdmEnumeratorCustomReference5::GetFirstRefPosition](EPDM.Interop.epdm~EPDM.Interop.epdm.IEdmEnumeratorCustomReference5~GetFirstRefPosition.html) to obtain IEdmPos5.

After calling this method the first time, poPos is automatically incremented every time it is called. Call this method repeatedly to obtain the rest of the custom file references.

Be sure to call [IEdmPos5::IsNull](EPDM.Interop.epdm~EPDM.Interop.epdm.IEdmPos5~IsNull.html) before you call this method to ensure you have not reached the end of the enumeration.

[Return codes](ReturnCodes.htm):

- S_OK: The method successfully executed.
- E_EDM_END_OF_LIST: You have gone past the end of the list.

## See Also

[IEdmEnumeratorCustomReference5 Interface](EPDM.Interop.epdm~EPDM.Interop.epdm.IEdmEnumeratorCustomReference5.html)
[IEdmEnumeratorCustomReference5 Members](EPDM.Interop.epdm~EPDM.Interop.epdm.IEdmEnumeratorCustomReference5_members.html)

## Availability

SOLIDWORKS PDM Professional Version 5.2
