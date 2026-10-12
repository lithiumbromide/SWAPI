---
title: "AddTail Method (IEdmSelectionList5)"
project: "SOLIDWORKS PDM Professional API Help"
interface: "IEdmSelectionList5"
member: "AddTail"
kind: "method"
source: "epdmapi/EPDM.Interop.epdm~EPDM.Interop.epdm.IEdmSelectionList5~AddTail.html"
---

# AddTail Method (IEdmSelectionList5)

Obsolete. Superseded by [IEdmSelectionList6::AddTail2](EPDM.Interop.epdm~EPDM.Interop.epdm.IEdmSelectionList6~AddTail2.html).

## Syntax

### Visual Basic

```vb
Sub AddTail( _
   ByVal bsItemName As System.String, _
   ByVal lItemID As System.Integer, _
   ByVal lParentFolderID As System.Integer _
)
```

### C#

```csharp
void AddTail(
   System.string bsItemName,
   System.int lItemID,
   System.int lParentFolderID
)
```

### C++/CLI

```cpp
void AddTail(
   System.String^ bsItemName,
   System.int lItemID,
   System.int lParentFolderID
)
```

### Parameters

- `bsItemName`: File or folder name
- `lItemID`: ID of file or folder
- `lParentFolderID`: ID of parent folder of file or folder

## Remarks

[Return codes:](ReturnCodes.htm)

- S_OK: The method successfully executed.

## See Also

[IEdmSelectionList5 Interface](EPDM.Interop.epdm~EPDM.Interop.epdm.IEdmSelectionList5.html)
[IEdmSelectionList5 Members](EPDM.Interop.epdm~EPDM.Interop.epdm.IEdmSelectionList5_members.html)

## Availability

SOLIDWORKS PDM Professional Version 5.2
