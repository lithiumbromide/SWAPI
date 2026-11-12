---
title: "AddMenuPopupItem3 Method (ISldWorks)"
project: "SOLIDWORKS API Help"
interface: "ISldWorks"
member: "AddMenuPopupItem3"
kind: "method"
source: "sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISldWorks~AddMenuPopupItem3.html"
---

# AddMenuPopupItem3 Method (ISldWorks)

Adds a menu item and zero or more submenus to shortcut menus of entities of the specified type in documents of the specified type.

## Syntax

### Visual Basic (Declaration)

```vb
Function AddMenuPopupItem3( _
   ByVal DocumentType As System.Integer, _
   ByVal Cookie As System.Integer, _
   ByVal SelectType As System.Integer, _
   ByVal PopupItemName As System.String, _
   ByVal MenuCallback As System.String, _
   ByVal MenuEnableMethod As System.String, _
   ByVal HintString As System.String, _
   ByVal CustomNames As System.String _
) As System.Integer
```

### Visual Basic (Usage)

```vb
Dim instance As ISldWorks
Dim DocumentType As System.Integer
Dim Cookie As System.Integer
Dim SelectType As System.Integer
Dim PopupItemName As System.String
Dim MenuCallback As System.String
Dim MenuEnableMethod As System.String
Dim HintString As System.String
Dim CustomNames As System.String
Dim value As System.Integer

value = instance.AddMenuPopupItem3(DocumentType, Cookie, SelectType, PopupItemName, MenuCallback, MenuEnableMethod, HintString, CustomNames)
```

### C#

```csharp
System.int AddMenuPopupItem3(
   System.int DocumentType,
   System.int Cookie,
   System.int SelectType,
   System.string PopupItemName,
   System.string MenuCallback,
   System.string MenuEnableMethod,
   System.string HintString,
   System.string CustomNames
)
```

### C++/CLI

```cpp
System.int AddMenuPopupItem3(
   System.int DocumentType,
   System.int Cookie,
   System.int SelectType,
   System.String^ PopupItemName,
   System.String^ MenuCallback,
   System.String^ MenuEnableMethod,
   System.String^ HintString,
   System.String^ CustomNames
)
```

**NOTE:** See [Differences Between Unmanaged C++ and C++/CLI Code](DifferencesBetweenUnManagedAndCPPCLI.htm).

### Parameters

- `DocumentType`: Document type as defined by [swDocumentTypes_e](ms-its:swconst.chm::/SOLIDWORKS.Interop.swconst~SOLIDWORKS.Interop.swconst.swDocumentTypes_e.html)
- `Cookie`: Cookie specified as defined in [ISwAddin::ConnectToSW](ms-its:swpublishedapi.chm::/SOLIDWORKS.Interop.swpublished~SOLIDWORKS.Interop.swpublished.ISwAddin~ConnectToSW.html)
- `SelectType`: Selection type as defined in [swSelectType_e](ms-its:swconst.chm::/SOLIDWORKS.Interop.swconst~SOLIDWORKS.Interop.swconst.swSelectType_e.html)
- `PopupItemName`: Description displayed on the shortcut menu (see **Remarks**)
- `MenuCallback`: Function to be called when the user clicks your menu item (see description in [ISldWorks::AddMenuItem4](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.ISldWorks~AddMenuItem4.html)) (see **Remarks**)
- `MenuEnableMethod`: Optional function that controls the state of the menu item

  If specified:

  - SOLIDWORKS calls this function before displaying the menu
  - Display of the menu item is controlled by the return value of MenuEnableMethod

  | If your method returns... | Then SOLIDWORKS... |
  | --- | --- |
  | 0 | Deselects and disables the menu item. |
  | 1 | Deselects and enables the menu item (this is the default menu state if no update function is specified) |
  | 2 | Selects and disables the menu item |
  | 3 | Selects and enables the menu item |
  | 4 | Hides the menu item |

  (See **Remarks**)
- `HintString`: Text to show in the SOLIDWORKS status bar when the user moves their mouse over this menu item; if you specify a HintString, it must be preceded by a comma
- `CustomNames`: Semi-colon separated list of the names of the custom feature types; this argument is applicable only if SelectType is a custom feature type (like swSelATTRIBUTES); in the case of swSelATTRIBUTES, set this field to the name of the attribute definition

### Return Value

SOLIDWORKS runtime command ID or -1 if the method fails

## VBA Syntax

See [SldWorks::AddMenuPopupItem3](ms-its:sldworksapivb6.chm::/sldworks~SldWorks~AddMenuPopupItem3.html)

## Remarks

Call this method for every unique set of DocumentType and SelectType in whose menus you want this menu item to display.

In PopupItemName use the at-sign (@) to create submenus. To add a separator bar after a menu item, append an at-sign to PopupItemName and enclose PopupItemName in double quotes ("").

For example, specifying:

- Edge adds menu item Edge to the shortcut menu.
- Edge@Color adds menu item Edge to the shortcut menu and submenu Color to Edge.
- Edge@Appearance@Color adds menu item Edge to the shortcut menu, submenu Appearance to Edge, and submenu Color to Appearance.
- "Edge@" adds menu item Edge to the shortcut menu and a separator bar after **Edge**.
- "Edge@Appearance@" adds menu item Edge to the shortcut menu, submenu Appearance to Edge, and a separator bar after Appearance.

See [Add-in Callback and Enable Methods](sldworksapiprogguide.chm::/OVERVIEW/Add-in_Callbacks.htm) to learn how to specify MenuCallback and MenuEnableMethod.

## See Also

[ISldWorks Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISldWorks.html)
[ISldWorks Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISldWorks_members.html)
[ISldWorks::AddMenu Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISldWorks~AddMenu.html)
[ISldWorks::AddToolbar4 Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISldWorks~AddToolbar4.html)
[ISldWorks::AddToolbarCommand2 Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISldWorks~AddToolbarCommand2.html)
[ISldWorks::RemoveFromMenu Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISldWorks~RemoveFromMenu.html)
[ISldWorks::RemoveMenu Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISldWorks~RemoveMenu.html)
[ISldWorks::RemoveMenuPopupItem2 Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISldWorks~RemoveMenuPopupItem2.html)

## Availability

SOLIDWORKS 2009 FCS, Revision Number 17.0
