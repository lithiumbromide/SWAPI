---
title: "RemoveItemFromThirdPartyPopupMenu Method (ISldWorks)"
project: "SOLIDWORKS API Help"
interface: "ISldWorks"
member: "RemoveItemFromThirdPartyPopupMenu"
kind: "method"
source: "sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISldWorks~RemoveItemFromThirdPartyPopupMenu.html"
---

# RemoveItemFromThirdPartyPopupMenu Method (ISldWorks)

Removes a menu item and icon from a third-party pop-up (shortcut) menu.

## Syntax

### Visual Basic (Declaration)

```vb
Function RemoveItemFromThirdPartyPopupMenu( _
   ByVal RegisterId As System.Integer, _
   ByVal DocType As System.Integer, _
   ByVal Item As System.String, _
   ByVal IconIndex As System.Integer _
) As System.Boolean
```

### Visual Basic (Usage)

```vb
Dim instance As ISldWorks
Dim RegisterId As System.Integer
Dim DocType As System.Integer
Dim Item As System.String
Dim IconIndex As System.Integer
Dim value As System.Boolean

value = instance.RemoveItemFromThirdPartyPopupMenu(RegisterId, DocType, Item, IconIndex)
```

### C#

```csharp
System.bool RemoveItemFromThirdPartyPopupMenu(
   System.int RegisterId,
   System.int DocType,
   System.string Item,
   System.int IconIndex
)
```

### C++/CLI

```cpp
System.bool RemoveItemFromThirdPartyPopupMenu(
   System.int RegisterId,
   System.int DocType,
   System.String^ Item,
   System.int IconIndex
)
```

**NOTE:** See [Differences Between Unmanaged C++ and C++/CLI Code](DifferencesBetweenUnManagedAndCPPCLI.htm).

### Parameters

- `RegisterId`: ID of the shortcut menu from [ISldWorks::RegisterThirdPartyPopupMenu](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.ISldWorks~RegisterThirdPartyPopupMenu.html)
- `DocType`: Document type where to display the shortcut menu, as defined in [swDocumentTypes_e](ms-its:swconst.chm::/SOLIDWORKS.Interop.swconst~SOLIDWORKS.Interop.swconst.swDocumentTypes_e.html)
- `Item`: Name of the shortcut menu item
- `IconIndex`: 1-based index of the icon (see **Remarks**)

### Return Value

True if the shortcut menu item or icon is removed, false if not

## Examples

[Add Shortcut Menus to Add-ins (VB.NET)](Add_Shortcut_Menus_to_Add-ins_VBNET.htm)
[Add Shortcut Menus to Add-ins (C#)](Add_Shortcut_Menus_to_Add-ins_CSharp.htm)

## Remarks

To remove:

- a menu item, specify a valid name for Item only. If you specify both Item and IconIndex, only Item is evaluated; IconIndex is ignored.
- a menu bar icon, specify an empty string for Item and pass the 1-based index value of the icon for IconIndex.

Read about [Add-in Shortcut Menus](ms-its:sldworksapiprogguide.chm::/OVERVIEW/Add-in_Shortcut_Menus.htm).

## See Also

[ISldWorks Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISldWorks.html)
[ISldWorks Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISldWorks_members.html)
[ISldWorks::AddItemToThirdPartyPopupMenu Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISldWorks~AddItemToThirdPartyPopupMenu.html)
[ISldWorks::SetThirdPartyPopupMenuState Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISldWorks~SetThirdPartyPopupMenuState.html)
[ISldWorks::ShowThirdPartyPopupMenu Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISldWorks~ShowThirdPartyPopupMenu.html)
[ISldWorks::AddItemToThirdPartyPopupMenu2 Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISldWorks~AddItemToThirdPartyPopupMenu2.html)

## Availability

SOLIDWORKS 2010 FCS, Revision Number 18.0
