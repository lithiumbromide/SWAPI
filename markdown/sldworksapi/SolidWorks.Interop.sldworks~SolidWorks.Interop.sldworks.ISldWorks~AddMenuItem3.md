---
title: "AddMenuItem3 Method (ISldWorks)"
project: "SOLIDWORKS API Help"
interface: "ISldWorks"
member: "AddMenuItem3"
kind: "method"
source: "sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISldWorks~AddMenuItem3.html"
---

# AddMenuItem3 Method (ISldWorks)

Obsolete. Superseded by [ISldWorks::AddMenuItem4](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.ISldWorks~AddMenuItem4.html).

## Syntax

### Visual Basic (Declaration)

```vb
Function AddMenuItem3( _
   ByVal DocumentType As System.Integer, _
   ByVal Cookie As System.Integer, _
   ByVal MenuItem As System.String, _
   ByVal Position As System.Integer, _
   ByVal MenuCallback As System.String, _
   ByVal MenuEnableMethod As System.String, _
   ByVal HintString As System.String, _
   ByVal BitmapFilePath As System.String _
) As System.Boolean
```

### Visual Basic (Usage)

```vb
Dim instance As ISldWorks
Dim DocumentType As System.Integer
Dim Cookie As System.Integer
Dim MenuItem As System.String
Dim Position As System.Integer
Dim MenuCallback As System.String
Dim MenuEnableMethod As System.String
Dim HintString As System.String
Dim BitmapFilePath As System.String
Dim value As System.Boolean

value = instance.AddMenuItem3(DocumentType, Cookie, MenuItem, Position, MenuCallback, MenuEnableMethod, HintString, BitmapFilePath)
```

### C#

```csharp
System.bool AddMenuItem3(
   System.int DocumentType,
   System.int Cookie,
   System.string MenuItem,
   System.int Position,
   System.string MenuCallback,
   System.string MenuEnableMethod,
   System.string HintString,
   System.string BitmapFilePath
)
```

### C++/CLI

```cpp
System.bool AddMenuItem3(
   System.int DocumentType,
   System.int Cookie,
   System.String^ MenuItem,
   System.int Position,
   System.String^ MenuCallback,
   System.String^ MenuEnableMethod,
   System.String^ HintString,
   System.String^ BitmapFilePath
)
```

**NOTE:** See [Differences Between Unmanaged C++ and C++/CLI Code](DifferencesBetweenUnManagedAndCPPCLI.htm).

### Parameters

- `DocumentType`: Document type to add the menu item as defined by [swDocumentTypes_e](ms-its:swconst.chm::/SOLIDWORKS.Interop.swconst~SOLIDWORKS.Interop.swconst.swDocumentTypes_e.html)
- `Cookie`: Cookie specified as defined in [ISwAddin::ConnectToSW](ms-its:swpublishedapi.chm::/SOLIDWORKS.Interop.swpublished~SOLIDWORKS.Interop.swpublished.ISwAddin~ConnectToSW.html)
- `MenuItem`: Menu string ("menuItem@menuString"); SOLIDWORKS Design creates menu items only if they do not already exist

  NOTE:

  - If you do not specify menuString, then the menu item appears on the Tools menu below the **Xpress Products** menu item.
  - Use the & symbol to include an accelerator key, e.g., "MyItem@&File" adds MyItem to the File menu with an accelerator key. To display the accelerator key, press the Alt key in SOLIDWORKS Design. The accelerator key is underlined.
- `Position`: Position at which to add the new menu item

  The first item is at position 0; if Position is -1, then the new menu item is added to the bottom of the list; this argument specifies the position of the menu item in relation to its immediate parent menu
- `MenuCallback`: Function to call when this menu item is selected
- `MenuEnableMethod`: Optional function that controls the state of the menu item

  If specified:

  - SOLIDWORKS Design calls this function before displaying the menu.
  - Display of the menu item is controlled by the return value of MenuEnableMethod.

  | If your method returns... | Then SOLIDWORKS Design... |
  | --- | --- |
  | 0 | Deselects and disables the menu item |
  | 1 | Deselects and enables the menu item; this is the default menu state if no update function is specified |
  | 2 | Selects and disables the menu item |
  | 3 | Selects and enables the menu item |
- `HintString`: Text to show in the SOLIDWORKS Design status bar when the user moves their mouse over this menu item; if you specify HintString, then it must be preceded by a comma
- `BitmapFilePath`: Path and filename of bitmap

### Return Value

True if menu item and bitmap are added, false if not

## VBA Syntax

See [SldWorks::AddMenuItem3](ms-its:sldworksapivb6.chm::/sldworks~SldWorks~AddMenuItem3.html).

## Examples

**Adding a menu separator:**

' Adds a menu separator to a menu (strings not shown as BSTR for clarity)

```vb
bRet = iSldWorks.AddMenuItem3(swDocNONE, iCookie, "@subMenuString@menuString", -1, "ExistingCallBackThatDoesNothing", "", "", "", "")
```

## Remarks

For information about using this method with the [ISwAddin](ms-its:swpublishedapi.chm::/SOLIDWORKS.Interop.swpublished~SOLIDWORKS.Interop.swpublished.ISwAddin.html) object, see [Using ISwAddin to Create a SOLIDWORKS Add-in](sldworksAPIProgGuide.chm::/OVERVIEW/Using_SwAddin_to_Create_a_SOLIDWORKS_Addin.htm).

The bitmap must be 16w x 16h x 256 colors.

You can add a new menu to any one of the four frames (main, part, assembly, or drawing). To do this, call this method with the appropriate argument in the DocumentType parameter. For example, if you want your menu to be available when a part document is active, then call this method and pass swDocPART as the first argument. After you have added your menu to the part frame, you do not need to do it again during the current SOLIDWORKS Design session. Once a part document is activated by the user, SOLIDWORKS Design automatically displays your menu item.

To add a menu separator:

- leave the text for the menu item blank, so that the menu string for the MenuItem argument starts with the at-sign symbol ( @):

  "@subMenuString@menuString"
- specify an existing method for the MenuCallback argument. This method is never called, so its implementation can be empty.
- specify empty strings for the MenuEnableMethod, HintString, and bitmapFilePath arguments.

## See Also

[ISldWorks Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISldWorks.html)
[ISldWorks Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISldWorks_members.html)
[ISldWorks::AddMenu Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISldWorks~AddMenu.html)
[ISldWorks::AddMenuPopupItem2 Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISldWorks~AddMenuPopupItem2.html)
[ISldWorks::AddToolbar4 Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISldWorks~AddToolbar4.html)
[ISldWorks::RemoveMenu Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISldWorks~RemoveMenu.html)
[ISldWorks::RemoveFromMenu Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISldWorks~RemoveFromMenu.html)
[ISldWorks::RemoveFromPopupMenu Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISldWorks~RemoveFromPopupMenu.html)
[ISldWorks::RemoveMenuPopupItem2 Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISldWorks~RemoveMenuPopupItem2.html)
[ISldWorks::RemoveToolbar2 Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISldWorks~RemoveToolbar2.html)
[ISldWorks::GetLocalizedMenuName Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISldWorks~GetLocalizedMenuName.html)

## Availability

SOLIDWORKS 2005 FCS, Revision Number 13.0
