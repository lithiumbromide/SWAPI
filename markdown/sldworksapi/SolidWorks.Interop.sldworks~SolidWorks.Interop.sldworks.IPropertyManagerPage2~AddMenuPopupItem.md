---
title: "AddMenuPopupItem Method (IPropertyManagerPage2)"
project: "SOLIDWORKS API Help"
interface: "IPropertyManagerPage2"
member: "AddMenuPopupItem"
kind: "method"
source: "sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IPropertyManagerPage2~AddMenuPopupItem.html"
---

# AddMenuPopupItem Method (IPropertyManagerPage2)

Adds a menu item to the pop-up menu for this PropertyManager page.

## Syntax

### Visual Basic (Declaration)

```vb
Function AddMenuPopupItem( _
   ByVal ID As System.Integer, _
   ByVal ItemText As System.String, _
   ByVal DocumentType As System.Integer, _
   ByVal HintText As System.String _
) As System.Boolean
```

### Visual Basic (Usage)

```vb
Dim instance As IPropertyManagerPage2
Dim ID As System.Integer
Dim ItemText As System.String
Dim DocumentType As System.Integer
Dim HintText As System.String
Dim value As System.Boolean

value = instance.AddMenuPopupItem(ID, ItemText, DocumentType, HintText)
```

### C#

```csharp
System.bool AddMenuPopupItem(
   System.int ID,
   System.string ItemText,
   System.int DocumentType,
   System.string HintText
)
```

### C++/CLI

```cpp
System.bool AddMenuPopupItem(
   System.int ID,
   System.String^ ItemText,
   System.int DocumentType,
   System.String^ HintText
)
```

**NOTE:** See [Differences Between Unmanaged C++ and C++/CLI Code](DifferencesBetweenUnManagedAndCPPCLI.htm).

### Parameters

- `ID`: Unique user-defined value for this pop-up menu item
- `ItemText`: Text for pop-up menu item
- `DocumentType`: Document types for which this pop-up menu item is displayed as defined in [swDocumentTypes_e](ms-its:swconst.chm::/SOLIDWORKS.Interop.swconst~SOLIDWORKS.Interop.swconst.swDocumentTypes_e.html)
- `HintText`: Text displayed in the SOLIDWORKS status bar when the user moves the cursor over this pop-up menu item

### Return Value

True if the pop-up menu item is added, false if not

## VBA Syntax

See [PropertyManagerPage2::AddMenuPopupItem](ms-its:sldworksapivb6.chm::/sldworks~PropertyManagerPage2~AddMenuPopupItem.html).

## Remarks

This method requires that you implement these IPropertyManagerPage2Handler8 methods:

- [IPropertyManagerPage2Handler8::OnPopupMenuItem](ms-its:swpublishedapi.chm::/SOLIDWORKS.Interop.swpublished~SOLIDWORKS.Interop.swpublished.IPropertyManagerPage2Handler8~OnPopupMenuItem.html). When the user selects a pop-up menu item, this method determines which item was selected. The add-in should then perform the appropriate action.

- [IPropertyManagerPage2Handler8::OnPopupMenuItemUpdate](ms-its:swpublishedapi.chm::/SOLIDWORKS.Interop.swpublished~SOLIDWORKS.Interop.swpublished.IPropertyManagerPage2Handler8~OnPopupMenuItemUpdate.html). When Windows attempts to select or deselect and enable or disable the pop-up menu item, SOLIDWORKS calls IPropertyManagerPage2Handler8::OnPopupMenuItemUpdate to get the state of the pop-up menu item from the add-in. Thus, IPropertyManagerPage2Handler8::OnPopupMenuItemUpdate:

  - Processes a request for the state of the specified pop-up menu item associated with the PropertyManager page.
  - Passes the state back to SOLIDWORKS.

## See Also

[IPropertyManagerPage2 Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IPropertyManagerPage2.html)
[IPropertyManagerPage2 Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IPropertyManagerPage2_members.html)

## Availability

SOLIDWORKS 2007 FCS, Revision Number 15.0
