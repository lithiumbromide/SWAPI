---
title: "GetNextFolder Method (IEdmLabel5)"
project: "SOLIDWORKS PDM Professional API Help"
interface: "IEdmLabel5"
member: "GetNextFolder"
kind: "method"
source: "API_GB/EPDM.Interop.epdm~EPDM.Interop.epdm.IEdmLabel5~GetNextFolder.html"
---

# GetNextFolder Method (IEdmLabel5)

Gets the next folder with this label in the enumeration.

## Syntax

### Visual Basic

```vb
Function GetNextFolder( _
   ByVal poPos As IEdmPos5 _
) As IEdmFolder5
```

### C#

```csharp
IEdmFolder5 GetNextFolder(
   IEdmPos5 poPos
)
```

### C++/CLI

```cpp
IEdmFolder5^ GetNextFolder(
   IEdmPos5^ poPos
)
```

### Parameters

- `poPos`: [IEdmPos5](EPDM.Interop.epdm~EPDM.Interop.epdm.IEdmPos5.html); position of the next folder (see **Remarks**)

### Return Value

[IEdmFolder5](EPDM.Interop.epdm~EPDM.Interop.epdm.IEdmFolder5.html)

## Remarks

Before calling this method the first time, you must populate poPos with the interface to the position of the first folder with this label, IEdmPos5. Call [IEdmLabel5::GetFirstFolderPosition](EPDM.Interop.epdm~EPDM.Interop.epdm.IEdmLabel5~GetFirstFolderPosition.html) to obtain IEdmPos5.

After calling this method the first time, poPos is automatically incremented every time it is called. Call this method repeatedly to obtain the rest of the folders with this label.

Be sure to call [IEdmPos5::IsNull](EPDM.Interop.epdm~EPDM.Interop.epdm.IEdmPos5~IsNull.html) before you call this method to ensure you have not reached the end of the enumeration.

If you only need the ID of the next folder with this label, call [IEdmLabel5::GetNextFolderID](EPDM.Interop.epdm~EPDM.Interop.epdm.IEdmLabel5~GetNextFolderID.html) instead of this method.

C++ programmers not using smart-pointer wrapper functions must release the returned interface, IEdmFile5.

[Return codes](ReturnCodes.htm):

- S_OK: The method successfully executed.
- E_EDM_END_OF_LIST: You have gone past the end of the list.

## See Also

[IEdmLabel5 Interface](EPDM.Interop.epdm~EPDM.Interop.epdm.IEdmLabel5.html)
[IEdmLabel5 Members](EPDM.Interop.epdm~EPDM.Interop.epdm.IEdmLabel5_members.html)

## Availability

SOLIDWORKS PDM Professional Version 5.2
