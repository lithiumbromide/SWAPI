---
title: "GetNextFileID Method (IEdmLabel5)"
project: "SOLIDWORKS PDM Professional API Help"
interface: "IEdmLabel5"
member: "GetNextFileID"
kind: "method"
source: "API_GB/EPDM.Interop.epdm~EPDM.Interop.epdm.IEdmLabel5~GetNextFileID.html"
---

# GetNextFileID Method (IEdmLabel5)

Gets the next ID of a file with this label in the enumeration.

## Syntax

### Visual Basic

```vb
Function GetNextFileID( _
   ByVal poPos As IEdmPos5, _
   ByRef plVersion As System.Integer _
) As System.Integer
```

### C#

```csharp
System.int GetNextFileID(
   IEdmPos5 poPos,
   out System.int plVersion
)
```

### C++/CLI

```cpp
System.int GetNextFileID(
   IEdmPos5^ poPos,
   [Out] System.int plVersion
)
```

### Parameters

- `poPos`: [IEdmPos5](EPDM.Interop.epdm~EPDM.Interop.epdm.IEdmPos5.html); position of the next file (see **Remarks**)
- `plVersion`: Version of file on which this label is set

### Return Value

ID of file on which this label is set

## Remarks

Before calling this method the first time, you must populate poPos with the interface to the position of the first file with this label, IEdmPos5. Call [IEdmLabel5::GetFirstFilePosition](EPDM.Interop.epdm~EPDM.Interop.epdm.IEdmLabel5~GetFirstFilePosition.html) to obtain IEdmPos5.

After calling this method the first time, poPos is automatically incremented every time it is called. Call this method repeatedly to obtain the rest of the file IDs.

Be sure to call [IEdmPos5::IsNull](EPDM.Interop.epdm~EPDM.Interop.epdm.IEdmPos5~IsNull.html) before you call this method to ensure you have not reached the end of the enumeration.

[Return codes](ReturnCodes.htm):

- S_OK: The method successfully executed.
- E_EDM_END_OF_LIST: You have gone past the end of the list.

## See Also

[IEdmLabel5 Interface](EPDM.Interop.epdm~EPDM.Interop.epdm.IEdmLabel5.html)
[IEdmLabel5 Members](EPDM.Interop.epdm~EPDM.Interop.epdm.IEdmLabel5_members.html)

## Availability

SOLIDWORKS PDM Professional Version 5.2
