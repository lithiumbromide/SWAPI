---
title: "AddMenuPopupIcon2 Method (IFrame)"
project: "SOLIDWORKS API Help"
interface: "IFrame"
member: "AddMenuPopupIcon2"
kind: "method"
source: "sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IFrame~AddMenuPopupIcon2.html"
---

# AddMenuPopupIcon2 Method (IFrame)

Obsolete. Superseded by [IFrame::AddMenuPopupIcon3](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IFrame~AddMenuPopupIcon3.html).

## Syntax

### Visual Basic (Declaration)

```vb
Function AddMenuPopupIcon2( _
   ByVal DocType As System.Integer, _
   ByVal SelectType As System.Integer, _
   ByVal HintString As System.String, _
   ByVal Identifier As System.Integer, _
   ByVal CallbackFunction As System.String, _
   ByVal CallbackUpdateFunction As System.String, _
   ByVal CustomNames As System.String, _
   ByVal BitmapFilePath As System.String _
) As System.Boolean
```

### Visual Basic (Usage)

```vb
Dim instance As IFrame
Dim DocType As System.Integer
Dim SelectType As System.Integer
Dim HintString As System.String
Dim Identifier As System.Integer
Dim CallbackFunction As System.String
Dim CallbackUpdateFunction As System.String
Dim CustomNames As System.String
Dim BitmapFilePath As System.String
Dim value As System.Boolean

value = instance.AddMenuPopupIcon2(DocType, SelectType, HintString, Identifier, CallbackFunction, CallbackUpdateFunction, CustomNames, BitmapFilePath)
```

### C#

```csharp
System.bool AddMenuPopupIcon2(
   System.int DocType,
   System.int SelectType,
   System.string HintString,
   System.int Identifier,
   System.string CallbackFunction,
   System.string CallbackUpdateFunction,
   System.string CustomNames,
   System.string BitmapFilePath
)
```

### C++/CLI

```cpp
System.bool AddMenuPopupIcon2(
   System.int DocType,
   System.int SelectType,
   System.String^ HintString,
   System.int Identifier,
   System.String^ CallbackFunction,
   System.String^ CallbackUpdateFunction,
   System.String^ CustomNames,
   System.String^ BitmapFilePath
)
```

**NOTE:** See [Differences Between Unmanaged C++ and C++/CLI Code](DifferencesBetweenUnManagedAndCPPCLI.htm).

### Parameters

- `DocType`: [Document type](ms-its:swconst.chm::/SOLIDWORKS.Interop.swconst~SOLIDWORKS.Interop.swconst.swDocumentTypes_e.html) whose context-sensitive menus display the icon
- `SelectType`: [Selection type](ms-its:swconst.chm::/SOLIDWORKS.Interop.swconst~SOLIDWORKS.Interop.swconst.swSelectType_e.html) whose context-sensitive menus display the icon
- `HintString`: Text displayed in the SOLIDWORKS status bar when the user moves the pointer over the icon
- `Identifier`: ID of the add-in; value of the Cookie argument passed by [ISwAddin::ConnectToSW](ms-its:swpublishedapi.chm::/SOLIDWORKS.Interop.swpublished~SOLIDWORKS.Interop.swpublished.ISwAddin~ConnectToSW.html)
- `CallbackFunction`: Function called when user clicks the context-sensitive menu icon (**see Remarks**)
- `CallbackUpdateFunction`: Optional function that controls the state of the icon; if specified, then SOLIDWORKS calls this function before displaying the icon

  | If CallbackUpdateFunction returns... | Then SOLIDWORKS... |
  | --- | --- |
  | 0 | Deselects and disables the item |
  | 1 | Deselects and enables the item; this is the default state if no update function is specified |
  | 4 | Hides the item |

  (see **Remarks**)
- `CustomNames`: Names of custom feature types (see **Remarks**)
- `BitmapFilePath`: Path and file name of the bitmap for the context-sensitive menu icon

### Return Value

True if the context-sensitive menu icon is added, false if not

## VBA Syntax

See [Frame::AddMenuPopupIcon2](ms-its:sldworksapivb6.chm::/sldworks~Frame~AddMenuPopupIcon2.html).

## Examples

[Add Shortcut Menus to Add-ins (C#)](Add_Shortcut_Menus_to_Add-ins_CSharp.htm)
[Add Shortcut Menus to Add-ins (VB.NET)](Add_Shortcut_Menus_to_Add-ins_VBNET.htm)

## Remarks

See [Add-in Callback and Enable Methods](sldworksapiprogguide.chm::/OVERVIEW/Add-in_Callbacks.htm) to learn how to specify CallbackFunction and CallbackUpdateFunction.

When the icon is clicked, the function specified in CallbackFunction can perform actions such as [displaying a third-party pop-up menu](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.ISldWorks~ShowThirdPartyPopupMenu.html).

CustomNames is a semi-colon separated list of the names of the custom feature types. This argument is applicable only if SelectType is a custom feature type (like swSelATTRIBUTES); in the case of swSelATTRIBUTES, set this field to the name of the attribute definition.

## See Also

[IFrame Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IFrame.html)
[IFrame Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IFrame_members.html)
[IFrame::AddMenu Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IFrame~AddMenu.html)
[IFrame::AddMenuItem2 Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IFrame~AddMenuItem2.html)
[IFrame::AddMenuPopupItem2 Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IFrame~AddMenuPopupItem2.html)
[IFrame::GetMenu Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IFrame~GetMenu.html)
[IFrame::GetMenux64 Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IFrame~GetMenux64.html)
[IFrame::GetSubMenuCount Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IFrame~GetSubMenuCount.html)
[IFrame::GetSubMenus Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IFrame~GetSubMenus.html)
[IFrame::IGetSubMenus Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IFrame~IGetSubMenus.html)
[IFrame::RemoveMenu Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IFrame~RemoveMenu.html)
[IFrame::RemoveMenuPopupIcon Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IFrame~RemoveMenuPopupIcon.html)
[IFrame::RenameMenu Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IFrame~RenameMenu.html)
[IFrame::MenuPinned Property](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IFrame~MenuPinned.html)
[IFrame::AddMenuPopupIcon Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IFrame~AddMenuPopupIcon.html)
[ISldWorks::AddItemToThirdPartyPopupMenu2 Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISldWorks~AddItemToThirdPartyPopupMenu2.html)

## Availability

SOLIDWORKS 2011 FCS, Revision Number 19.0
