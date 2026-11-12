---
title: "AddMenuPopupItem2 Method (ISldWorks)"
project: "SOLIDWORKS API Help"
interface: "ISldWorks"
member: "AddMenuPopupItem2"
kind: "method"
source: "sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISldWorks~AddMenuPopupItem2.html"
---

# AddMenuPopupItem2 Method (ISldWorks)

Obsolete. Superseded by [ISldWorks::AddMenuPopupItem3](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.ISldWorks~AddMenuPopupItem3.html) and [ISldWorks::AddMenuPopupItem4](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISldWorks~AddMenuPopupItem4.html).

## Syntax

### Visual Basic (Declaration)

```vb
Function AddMenuPopupItem2( _
   ByVal DocumentType As System.Integer, _
   ByVal Cookie As System.Integer, _
   ByVal SelectType As System.Integer, _
   ByVal PopupItemName As System.String, _
   ByVal MenuCallback As System.String, _
   ByVal MenuEnableMethod As System.String, _
   ByVal HintString As System.String, _
   ByVal CustomNames As System.String _
) As System.Boolean
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
Dim value As System.Boolean

value = instance.AddMenuPopupItem2(DocumentType, Cookie, SelectType, PopupItemName, MenuCallback, MenuEnableMethod, HintString, CustomNames)
```

### C#

```csharp
System.bool AddMenuPopupItem2(
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
System.bool AddMenuPopupItem2(
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
- `PopupItemName`: Description displayed on the shortcut menu
- `MenuCallback`: Function to be called when the user clicks your menu item (see description in [ISldWorks::AddMenuItem3](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.ISldWorks~AddMenuItem3.html))
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
- `HintString`: Text to show in the SOLIDWORKS status bar when the user moves their mouse over this menu item; if you specify a HintString, it must be preceded by a comma
- `CustomNames`: Semi-colon separated list of the names of the custom feature types; this argument is applicable only if SelectType is a custom feature type (like swSelATTRIBUTES); in the case of swSelATTRIBUTES, set this field to the name of the attribute definition

### Return Value

True if the item was added, false if not

## VBA Syntax

See [SldWorks::AddMenuPopupItem2](ms-its:sldworksapivb6.chm::/sldworks~SldWorks~AddMenuPopupItem2.html).

## See Also

[ISldWorks Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISldWorks.html)
[ISldWorks Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISldWorks_members.html)
[ISldWorks::AddMenu Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISldWorks~AddMenu.html)
[ISldWorks::AddToolbar4 Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISldWorks~AddToolbar4.html)
[ISldWorks::AddToolbarCommand2 Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISldWorks~AddToolbarCommand2.html)
[ISldWorks::RemoveFromMenu Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISldWorks~RemoveFromMenu.html)
[ISldWorks::RemoveFromPopupMenu Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISldWorks~RemoveFromPopupMenu.html)
[ISldWorks::RemoveMenu Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISldWorks~RemoveMenu.html)
[ISldWorks::RemoveMenuPopupItem2 Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISldWorks~RemoveMenuPopupItem2.html)

## Availability

SOLIDWORKS 2003 FCS, Revision Number 11.0
