---
title: "AddItemToThirdPartyPopupMenu2 Method (ISldWorks)"
project: "SOLIDWORKS API Help"
interface: "ISldWorks"
member: "AddItemToThirdPartyPopupMenu2"
kind: "method"
source: "sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISldWorks~AddItemToThirdPartyPopupMenu2.html"
---

# AddItemToThirdPartyPopupMenu2 Method (ISldWorks)

Adds menu items to a pop-up (shortcut) menu in a SOLIDWORKS add-in.

## Syntax

### Visual Basic (Declaration)

```vb
Function AddItemToThirdPartyPopupMenu2( _
   ByVal RegisterId As System.Integer, _
   ByVal DocType As System.Integer, _
   ByVal Item As System.String, _
   ByVal Identifier As System.Integer, _
   ByVal CallbackFunction As System.String, _
   ByVal EnableFunction As System.String, _
   ByVal CustomName As System.String, _
   ByVal HintString As System.String, _
   ByVal BitmapFileName As System.String, _
   ByVal MenuItemTypeOption As System.Integer _
) As System.Boolean
```

### Visual Basic (Usage)

```vb
Dim instance As ISldWorks
Dim RegisterId As System.Integer
Dim DocType As System.Integer
Dim Item As System.String
Dim Identifier As System.Integer
Dim CallbackFunction As System.String
Dim EnableFunction As System.String
Dim CustomName As System.String
Dim HintString As System.String
Dim BitmapFileName As System.String
Dim MenuItemTypeOption As System.Integer
Dim value As System.Boolean

value = instance.AddItemToThirdPartyPopupMenu2(RegisterId, DocType, Item, Identifier, CallbackFunction, EnableFunction, CustomName, HintString, BitmapFileName, MenuItemTypeOption)
```

### C#

```csharp
System.bool AddItemToThirdPartyPopupMenu2(
   System.int RegisterId,
   System.int DocType,
   System.string Item,
   System.int Identifier,
   System.string CallbackFunction,
   System.string EnableFunction,
   System.string CustomName,
   System.string HintString,
   System.string BitmapFileName,
   System.int MenuItemTypeOption
)
```

### C++/CLI

```cpp
System.bool AddItemToThirdPartyPopupMenu2(
   System.int RegisterId,
   System.int DocType,
   System.String^ Item,
   System.int Identifier,
   System.String^ CallbackFunction,
   System.String^ EnableFunction,
   System.String^ CustomName,
   System.String^ HintString,
   System.String^ BitmapFileName,
   System.int MenuItemTypeOption
)
```

**NOTE:** See [Differences Between Unmanaged C++ and C++/CLI Code](DifferencesBetweenUnManagedAndCPPCLI.htm).

### Parameters

- `RegisterId`: ID of shortcut menu from [ISldWorks::RegisterThirdPartyPopupMenu](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.ISldWorks~RegisterThirdPartyPopupMenu.html)
- `DocType`: Document type where to display shortcut menu, as defined in [swDocumentTypes_e](ms-its:swconst.chm::/SOLIDWORKS.Interop.swconst~SOLIDWORKS.Interop.swconst.swDocumentTypes_e.html)
- `Item`: Unique display name of shortcut menu item (see **Remarks**); specify an empty string if adding an icon to the menu bar
- `Identifier`: ID of the add-in; value of the Cookie argument passed by [ISwAddin::ConnectToSW](ms-its:swpublishedapi.chm::/SOLIDWORKS.Interop.swpublished~SOLIDWORKS.Interop.swpublished.ISwAddin~ConnectToSW.html)
- `CallbackFunction`: Function called when user clicks the shortcut menu item; specify an empty string if MenuItemTypeOption is:

  - [swMenuItemType_e](ms-its:swconst.chm::/SOLIDWORKS.Interop.swconst~SOLIDWORKS.Interop.swconst.swMenuItemType_e.html).swMenuItemType_Break
  - [swMenuItemType_e](ms-its:swconst.chm::/SOLIDWORKS.Interop.swconst~SOLIDWORKS.Interop.swconst.swMenuItemType_e.html).swMenuItemType_Separator

  (see **Remarks**)
- `EnableFunction`: Optional function that controls the state of the shortcut menu item

  If specified, SOLIDWORKS:

  1. calls this function before displaying the menu
  2. displays the menu item according to the return value of this function

  | If EnableFunction returns... | Then SOLIDWORKS... |
  | --- | --- |
  | 0 | Deselects and disables the menu item |
  | 1 | Deselects and enables the menu item; this is the default menu state if EnableFunction is not specified |
  | 2 | Selects and disables the menu item |
  | 3 | Selects and enables the menu item |

  Specify an empty string if MenuItemTypeOption is:

  - [swMenuItemType_e](ms-its:swconst.chm::/SOLIDWORKS.Interop.swconst~SOLIDWORKS.Interop.swconst.swMenuItemType_e.html).swMenuItemType_Break
  - [swMenuItemType_e](ms-its:swconst.chm::/SOLIDWORKS.Interop.swconst~SOLIDWORKS.Interop.swconst.swMenuItemType_e.html).swMenuItemType_Separator

  (see **Remarks**)
- `CustomName`: Empty string
- `HintString`: Text to display in the SOLIDWORKS status bar when users move the mouse over this shortcut menu item
- `BitmapFileName`: Path and filename of bitmap for icons (menu bar or menu item)

  Specify an empty string if MenuItemTypeOption is:

  - [swMenuItemType_e](ms-its:swconst.chm::/SOLIDWORKS.Interop.swconst~SOLIDWORKS.Interop.swconst.swMenuItemType_e.html).swMenuItemType_Break
  - [swMenuItemType_e](ms-its:swconst.chm::/SOLIDWORKS.Interop.swconst~SOLIDWORKS.Interop.swconst.swMenuItemType_e.html).swMenuItemType_Separator
- `MenuItemTypeOption`: Type of menu item as defined in [swMenuItemType_e](ms-its:swconst.chm::/SOLIDWORKS.Interop.swconst~SOLIDWORKS.Interop.swconst.swMenuItemType_e.html)

### Return Value

True if the shortcut menu item is added, false if not

## Examples

### VB.NET

```
'To create and register a shortcut menu:
   registerID = SwApp.RegisterThirdPartyPopupMenu()

'To add an actionable menu item to a shortcut menu:
   resultCode = SwApp.AddItemToThirdPartyPopupMenu2(
   registerID,
   CInt(swDocumentTypes_e.swDocPART),
   "Test1",
   addinID,
   "TestCallback",
   "EnableTest",
   "",
   "Test1",
   cmdGroup.SmallMainIcon,
   CInt(swMenuItemType_e.swMenuItemType_Default))

'To add a separator bar to a shortcut menu
   resultCode = SwApp.AddItemToThirdPartyPopupMenu2(
   registerID,
   CInt(swDocumentTypes_e.swDocPART),
   "Separator1",
   addinID
   "",
   "",
   "",
   "",
   "",
   CInt(swMenuItemType_e.swMenuItemType_Separator))

'To add a section title or break to a shortcut menu:
   resultCode = SwApp.AddItemToThirdPartyPopupMenu2(
   registerID,
   CInt(swDocumentTypes_e.swDocPART),
   "Menu Break",
   addinID,
   "",
   "",
   "",
   "",
   "",
   CInt(swMenuItemType_e.swMenuItemType_Break))

'To add an icon to the menu bar above a shortcut menu:
   resultCode = SwApp.AddItemToThirdPartyPopupMenu2(
   registerID,
   CInt(swDocumentTypes_e.swDocPART),
   "",
   addinID,
   "TestCallback",
   "EnableTest",
   "",
   "NoOp",
   cmdGroup.SmallMainIcon,
   CInt(swMenuItemType_e.swMenuItemType_Default))
```

## Examples

[Add Shortcut Menus to Add-ins (VB.NET)](Add_Shortcut_Menus_to_Add-ins_VBNET.htm)
[Add Shortcut Menus to Add-ins (C#)](Add_Shortcut_Menus_to_Add-ins_CSharp.htm)

## Remarks

See [Add-in Callback and Enable Methods](sldworksapiprogguide.chm::/OVERVIEW/Add-in_Callbacks.htm) to learn how to specify CallbackFunction and EnableFunction.

Read about [Add-in Shortcut Menus](ms-its:sldworksapiprogguide.chm::/OVERVIEW/Add-in_Shortcut_Menus.htm).

## See Also

[ISldWorks Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISldWorks.html)
[ISldWorks Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISldWorks_members.html)
[ISldWorks::AddItemToThirdPartyPopupMenu Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISldWorks~AddItemToThirdPartyPopupMenu.html)

## Availability

SOLIDWORKS 2011 FCS, Revision Number 19.0
