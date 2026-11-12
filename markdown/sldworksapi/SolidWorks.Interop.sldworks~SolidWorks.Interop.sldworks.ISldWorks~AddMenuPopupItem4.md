---
title: "AddMenuPopupItem4 Method (ISldWorks)"
project: "SOLIDWORKS API Help"
interface: "ISldWorks"
member: "AddMenuPopupItem4"
kind: "method"
source: "sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISldWorks~AddMenuPopupItem4.html"
---

# AddMenuPopupItem4 Method (ISldWorks)

Adds a menu item and zero or more submenus to shortcut menus of features of the specified type in documents of the specified type.

## Syntax

### Visual Basic (Declaration)

```vb
Function AddMenuPopupItem4( _
   ByVal DocumentType As System.Integer, _
   ByVal Cookie As System.Integer, _
   ByVal SelectType As System.String, _
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
Dim SelectType As System.String
Dim PopupItemName As System.String
Dim MenuCallback As System.String
Dim MenuEnableMethod As System.String
Dim HintString As System.String
Dim CustomNames As System.String
Dim value As System.Integer

value = instance.AddMenuPopupItem4(DocumentType, Cookie, SelectType, PopupItemName, MenuCallback, MenuEnableMethod, HintString, CustomNames)
```

### C#

```csharp
System.int AddMenuPopupItem4(
   System.int DocumentType,
   System.int Cookie,
   System.string SelectType,
   System.string PopupItemName,
   System.string MenuCallback,
   System.string MenuEnableMethod,
   System.string HintString,
   System.string CustomNames
)
```

### C++/CLI

```cpp
System.int AddMenuPopupItem4(
   System.int DocumentType,
   System.int Cookie,
   System.String^ SelectType,
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
- `Cookie`: Cookie as defined in [ISwAddin::ConnectToSW](ms-its:swpublishedapi.chm::/SOLIDWORKS.Interop.swpublished~SOLIDWORKS.Interop.swpublished.ISwAddin~ConnectToSW.html)
- `SelectType`: Selection type as returned by [IFeature::GetTypeName2](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.IFeature~GetTypeName2.html) (see **Remarks**)
- `PopupItemName`: Description displayed on the shortcut menu (see **Remarks**)
- `MenuCallback`: Function to call when this menu item is selected (see **Remarks**)
- `MenuEnableMethod`: Optional function that controls the state of the menu item

  If specified:

  - SOLIDWORKS calls this function before displaying the menu
  - Display of the menu item is controlled by the return value of MenuEnableMethod

  | If MenuEnableMethod returns... | Then SOLIDWORKS... |
  | --- | --- |
  | 0 | Deselects and disables the menu item |
  | 1 | Deselects and enables the menu item (this is the default menu state if no update function is specified) |
  | 2 | Selects and disables the menu item |
  | 3 | Selects and enables the menu item |
  | 4 | Hides the menu item |

  (see **Remarks**)
- `HintString`: Text to show in the SOLIDWORKS status bar when the user moves a mouse over this menu item
- `CustomNames`: Semi-colon separated list of the names of the custom features; this argument is applicable only if SelectType is a custom feature type (like Attribute); in the case of Attribute, set this field to a list of attribute definitions

### Return Value

SOLIDWORKS runtime command ID or -1 if the method fails

## VBA Syntax

See [SldWorks::AddMenuPopupItem4](ms-its:sldworksapivb6.chm::/sldworks~SldWorks~AddMenuPopupItem4.html)

## Remarks

Call this method for every unique set of DocumentType and SelectType in whose menus you want this menu item to display.

For SelectTypes that are macro features, components, faces, edges or other non-feature entities, use [ISldWorks::AddMenuPopupItem3](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISldWorks~AddMenuPopupItem3.html) instead of this method.

In PopupItemName use the at-sign (@) to create submenus. To add a separator bar after a menu item, append an at-sign to PopupItemName and enclose PopupItemName in double quotes ("").

For example, specifying:

- **Feature** adds menu item Feature to the shortcut menu.
- Feature@Color adds menu item Feature to the shortcut menu and submenu Color to Feature.
- Feature@Appearance@Color adds menu item Feature to the shortcut menu, submenu Appearance to Feature, and submenu Color to Appearance.
- "Feature@" adds menu item Feature to the shortcut menu and a separator bar after **Feature**.
- "Feature@Appearance@" adds menu item Feature to the shortcut menu, submenu Appearance to Feature, and a separator bar after Appearance.

See [Add-in Callback and Enable Methods](sldworksapiprogguide.chm::/OVERVIEW/Add-in_Callbacks.htm) to learn how to specify MenuCallback and MenuEnableMethod.

## See Also

[ISldWorks Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISldWorks.html)
[ISldWorks Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISldWorks_members.html)
[ISldWorks::AddMenu Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISldWorks~AddMenu.html)
[ISldWorks::AddToolbar4 Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISldWorks~AddToolbar4.html)
[ISldWorks::AddToolbarCommand2 Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISldWorks~AddToolbarCommand2.html)
[ISldWorks::RemoveFromMenu Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISldWorks~RemoveFromMenu.html)
[ISldWorks::RemoveMenuPopupItem2 Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISldWorks~RemoveMenuPopupItem2.html)
[ISldWorks::RemoveMenu Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISldWorks~RemoveMenu.html)

## Availability

SOLIDWORKS 2011 FCS, Revision Number 19.0
