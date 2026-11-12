---
title: "GetNextFile Method (IEdmLabel5)"
project: "SOLIDWORKS PDM Professional API Help"
interface: "IEdmLabel5"
member: "GetNextFile"
kind: "method"
source: "epdmapi/EPDM.Interop.epdm~EPDM.Interop.epdm.IEdmLabel5~GetNextFile.html"
---

# GetNextFile Method (IEdmLabel5)

Gets the next file with this label in the enumeration.

## Syntax

### Visual Basic

```vb
Function GetNextFile( _
   ByVal poPos As IEdmPos5, _
   ByRef plVersion As System.Integer _
) As IEdmFile5
```

### C#

```csharp
IEdmFile5 GetNextFile(
   IEdmPos5 poPos,
   out System.int plVersion
)
```

### C++/CLI

```cpp
IEdmFile5^ GetNextFile(
   IEdmPos5^ poPos,
   [Out] System.int plVersion
)
```

### Parameters

- `poPos`: [IEdmPos5](EPDM.Interop.epdm~EPDM.Interop.epdm.IEdmPos5.html); position of the next file (see **Remarks**)
- `plVersion`: Version of file on which this label is set

### Return Value

[IEdmFile5](EPDM.Interop.epdm~EPDM.Interop.epdm.IEdmFile5.html)

## Remarks

Before calling this method the first time, you must populate poPos with the interface to the position of the first file with this label, IEdmPos5. Call [IEdmLabel5::GetFirstFilePosition](EPDM.Interop.epdm~EPDM.Interop.epdm.IEdmLabel5~GetFirstFilePosition.html) to obtain IEdmPos5.

After calling this method the first time, poPos is automatically incremented every time it is called. Call this method repeatedly to obtain the rest of the files with this label.

Be sure to call [IEdmPos5::IsNull](EPDM.Interop.epdm~EPDM.Interop.epdm.IEdmPos5~IsNull.html) before you call this method to ensure you have not reached the end of the enumeration.

If you only need the ID of the next file with this label, call [IEdmLabel5::GetNextFileID](EPDM.Interop.epdm~EPDM.Interop.epdm.IEdmLabel5~GetNextFileID.html) instead of this method.

C++ programmers not using smart-pointer wrapper functions must release the returned interface, IEdmFile5.

[Return codes](ReturnCodes.htm):

- S_OK: The method successfully executed.
- E_EDM_END_OF_LIST: You have gone past the end of the list.

## See Also

[IEdmLabel5 Interface](EPDM.Interop.epdm~EPDM.Interop.epdm.IEdmLabel5.html)
[IEdmLabel5 Members](EPDM.Interop.epdm~EPDM.Interop.epdm.IEdmLabel5_members.html)

## Availability

SOLIDWORKS PDM Professional Version 5.2
