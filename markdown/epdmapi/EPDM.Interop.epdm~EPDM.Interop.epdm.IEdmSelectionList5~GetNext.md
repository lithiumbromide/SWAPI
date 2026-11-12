---
title: "GetNext Method (IEdmSelectionList5)"
project: "SOLIDWORKS PDM Professional API Help"
interface: "IEdmSelectionList5"
member: "GetNext"
kind: "method"
source: "epdmapi/EPDM.Interop.epdm~EPDM.Interop.epdm.IEdmSelectionList5~GetNext.html"
---

# GetNext Method (IEdmSelectionList5)

Obsolete. Superseded by [IEdmSelectionList6::GetNext2](EPDM.Interop.epdm~EPDM.Interop.epdm.IEdmSelectionList6~GetNext2.html).

## Syntax

### Visual Basic

```vb
Sub GetNext( _
   ByVal poPos As IEdmPos5, _
   ByRef pbsItemName As System.String, _
   ByRef plItemID As System.Integer, _
   ByRef plParentFolderID As System.Integer _
)
```

### C#

```csharp
void GetNext(
   IEdmPos5 poPos,
   out System.string pbsItemName,
   out System.int plItemID,
   out System.int plParentFolderID
)
```

### C++/CLI

```cpp
void GetNext(
   IEdmPos5^ poPos,
   [Out] System.String^ pbsItemName,
   [Out] System.int plItemID,
   [Out] System.int plParentFolderID
)
```

### Parameters

- `poPos`: [IEdmPos5](EPDM.Interop.epdm~EPDM.Interop.epdm.IEdmPos5.html); position of the item to get (see **Remarks**)
- `pbsItemName`: Name of the file or folder (see **Remarks**)
- `plItemID`: ID of the file or folder
- `plParentFolderID`: ID of the parent folder of the file or folder

## Remarks

Before calling this method the first time, you must populate poPos with the interface to the position of the first item, IEdmPos5. Call [IEdmSelectionList5::GetHeadPosition](EPDM.Interop.epdm~EPDM.Interop.epdm.IEdmSelectionList5~GetHeadPosition.html) to obtain IEdmPos5.

After calling this method the first time, poPos is automatically incremented every time it is called. Call this method repeatedly to obtain the rest of the items.

Be sure to call [IEdmPos5::IsNull](EPDM.Interop.epdm~EPDM.Interop.epdm.IEdmPos5~IsNull.html) before you call this method to ensure you have not reached the end of the enumeration.

C++ programmers must free the string returned in pbsItemName with a call to SysFreeString.

[Return codes:](ReturnCodes.htm)

- S_OK: The method successfully executed.
- E_EDM_END_OF_LIST: You have gone past the end of the list.

## See Also

[IEdmSelectionList5 Interface](EPDM.Interop.epdm~EPDM.Interop.epdm.IEdmSelectionList5.html)
[IEdmSelectionList5 Members](EPDM.Interop.epdm~EPDM.Interop.epdm.IEdmSelectionList5_members.html)

## Availability

SOLIDWORKS PDM Professional Version 5.2
