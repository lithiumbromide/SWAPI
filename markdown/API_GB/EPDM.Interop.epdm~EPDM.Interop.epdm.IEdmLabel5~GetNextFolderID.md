---
title: "GetNextFolderID Method (IEdmLabel5)"
project: "SOLIDWORKS PDM Professional API Help"
interface: "IEdmLabel5"
member: "GetNextFolderID"
kind: "method"
source: "API_GB/EPDM.Interop.epdm~EPDM.Interop.epdm.IEdmLabel5~GetNextFolderID.html"
---

# GetNextFolderID Method (IEdmLabel5)

Gets the next ID of a folder with this label in the enumeration.

## Syntax

### Visual Basic

```vb
Function GetNextFolderID( _
   ByVal poPos As IEdmPos5 _
) As System.Integer
```

### C#

```csharp
System.int GetNextFolderID(
   IEdmPos5 poPos
)
```

### C++/CLI

```cpp
System.int GetNextFolderID(
   IEdmPos5^ poPos
)
```

### Parameters

- `poPos`: [IEdmPos5](EPDM.Interop.epdm~EPDM.Interop.epdm.IEdmPos5.html); position of the next folder (see **Remarks**)

### Return Value

ID of folder on which this label is set

## Remarks

Before calling this method the first time, you must populate poPos with the interface to the position of the first folder with this label, IEdmPos5. Call [IEdmLabel5::GetFirstFolderPosition](EPDM.Interop.epdm~EPDM.Interop.epdm.IEdmLabel5~GetFirstFolderPosition.html) to obtain IEdmPos5.

After calling this method the first time, poPos is automatically incremented every time it is called. Call this method repeatedly to obtain the rest of the folder IDs.

Be sure to call [IEdmPos5::IsNull](EPDM.Interop.epdm~EPDM.Interop.epdm.IEdmPos5~IsNull.html) before you call this method to ensure you have not reached the end of the enumeration.

[Return codes](ReturnCodes.htm):

- S_OK: The method successfully executed.
- E_EDM_END_OF_LIST: You have gone past the end of the list.

## See Also

[IEdmLabel5 Interface](EPDM.Interop.epdm~EPDM.Interop.epdm.IEdmLabel5.html)
[IEdmLabel5 Members](EPDM.Interop.epdm~EPDM.Interop.epdm.IEdmLabel5_members.html)

## Availability

SOLIDWORKS PDM Professional Version 5.2
