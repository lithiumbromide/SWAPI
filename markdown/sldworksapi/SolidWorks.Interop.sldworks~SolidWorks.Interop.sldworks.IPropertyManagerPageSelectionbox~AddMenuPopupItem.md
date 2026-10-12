---
title: "AddMenuPopupItem Method (IPropertyManagerPageSelectionbox)"
project: "SOLIDWORKS API Help"
interface: "IPropertyManagerPageSelectionbox"
member: "AddMenuPopupItem"
kind: "method"
source: "sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IPropertyManagerPageSelectionbox~AddMenuPopupItem.html"
---

# AddMenuPopupItem Method (IPropertyManagerPageSelectionbox)

Adds a menu item to the pop-up menu for this selection box of the PropertyManager page.

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
Dim instance As IPropertyManagerPageSelectionbox
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

See [PropertyManagerPageSelectionbox::AddMenuPopupItem](ms-its:sldworksapivb6.chm::/Sldworks~PropertyManagerPageSelectionbox~AddMenuPopupItem.html).

## Remarks

This method requires that you implement these [IPropertyManagerPage2Handler5](ms-its:swpublishedapi.chm::/SOLIDWORKS.Interop.swpublished~SOLIDWORKS.Interop.swpublished.IPropertyManagerPage2Handler5.html) methods:

- [IPropertyManagerPage2Handler5::OnPopupMenuItem](ms-its:swpublishedapi.chm::/SOLIDWORKS.Interop.swpublished~SOLIDWORKS.Interop.swpublished.IPropertyManagerPage2Handler5~OnPopupMenuItem.html). When the user selects a pop-up menu item, this method determines which item was selected. The add-in should then perform the appropriate action.

- [IPropertyManagerPage2Handler5::OnPopupMenuItemUpdate](ms-its:swpublishedapi.chm::/SOLIDWORKS.Interop.swpublished~SOLIDWORKS.Interop.swpublished.IPropertyManagerPage2Handler5~OnPopupMenuItemUpdate.html). When Windows attempts to select or deselect and enable or disable the pop-up menu item, SOLIDWORKS calls IPropertyManagerPage2Handler5::OnPopupMenuItemUpdate to get the state of the pop-up menu item from the add-in. Thus, IPropertyManagerPage2Handler5::OnPopupMenuItemUpdate:

  - Processes a request for the state of the specified pop-up menu item associated with the PropertyManager page.
  - Passes the state back to SOLIDWORKS.

## See Also

[IPropertyManagerPageSelectionbox Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IPropertyManagerPageSelectionbox.html)
[IPropertyManagerPageSelectionbox Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IPropertyManagerPageSelectionbox_members.html)

## Availability

SOLIDWORKS 2008 FCS, Revision Number 16.0
