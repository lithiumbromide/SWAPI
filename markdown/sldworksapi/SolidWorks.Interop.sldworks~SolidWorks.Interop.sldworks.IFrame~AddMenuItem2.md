---
title: "AddMenuItem2 Method (IFrame)"
project: "SOLIDWORKS API Help"
interface: "IFrame"
member: "AddMenuItem2"
kind: "method"
source: "sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IFrame~AddMenuItem2.html"
---

# AddMenuItem2 Method (IFrame)

Adds a menu item and bitmap or a separator to an existing menu.

## Syntax

### Visual Basic (Declaration)

```vb
Function AddMenuItem2( _
   ByVal Menu As System.String, _
   ByVal Item As System.String, _
   ByVal Position As System.Integer, _
   ByVal CallbackFcnAndModule As System.String, _
   ByVal BitmapFileName As System.String _
) As System.Boolean
```

### Visual Basic (Usage)

```vb
Dim instance As IFrame
Dim Menu As System.String
Dim Item As System.String
Dim Position As System.Integer
Dim CallbackFcnAndModule As System.String
Dim BitmapFileName As System.String
Dim value As System.Boolean

value = instance.AddMenuItem2(Menu, Item, Position, CallbackFcnAndModule, BitmapFileName)
```

### C#

```csharp
System.bool AddMenuItem2(
   System.string Menu,
   System.string Item,
   System.int Position,
   System.string CallbackFcnAndModule,
   System.string BitmapFileName
)
```

### C++/CLI

```cpp
System.bool AddMenuItem2(
   System.String^ Menu,
   System.String^ Item,
   System.int Position,
   System.String^ CallbackFcnAndModule,
   System.String^ BitmapFileName
)
```

**NOTE:** See [Differences Between Unmanaged C++ and C++/CLI Code](DifferencesBetweenUnManagedAndCPPCLI.htm).

### Parameters

- `Menu`: Name of the menu to which to add this menu item
- `Item`: Name of menu item (including accelerator key "&"); if Item is null or empty, then this method adds a separator
- `Position`: Position at which to add the new menu item; the first item is at position 0; if Position is 1, the new menu item is added to the end of the list
- `CallbackFcnAndModule`: Function called when user clicks the menu item (see **Remarks**)
- `BitmapFileName`: Path and filename of the bitmap for the menu item

### Return Value

True if menu item is added, false if not

## VBA Syntax

See [Frame::AddMenuItem2](ms-its:sldworksapivb6.chm::/sldworks~Frame~AddMenuItem2.html).

## Remarks

This method only works for the C++ application implemented as a DLL, not as an EXE. Any function exposed as a callback from a menu item must be declared as an EXPORT or included in your .def file.

You can add a new menu item to any one of the four frames (main frame, part frame, assembly frame, or drawing frame). To do this, you must get the [IFrame](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.IFrame.html) object when the desired frame is active.

For example, if you want your menu to be available when a part document is active, then call [ISldWorks::Frame](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.ISldWorks~Frame.html) when a part is first loaded or created, and use that IFrame object to call this method. Once you add your menu to the part frame, you do not need to do it again during the current SOLIDWORKS Design session.

The CallbackFcnAndModule argument specifies which function to call when this menu item is selected by the user. The syntax is as follows:

```vb
"dllname@function@updatefunction,hintstring"
```

where:

| dllname | Name of your library as specified in the project .def file. The actual DLL filename and the definition in the .def file must be the same. |
| --- | --- |
| function | Name of the function that gets called when the user clicks the menu item. This function must also be declared as an EXPORT in your .def file. See Add-in Callback and Enable Methods to learn how to specify your function. |
| updatefunction | Optional argument that controls the state of the button. If specified, then SOLIDWORKS Design calls this function before the button is displayed. Define your updatefunction to return an integer and declare it as an EXPORT or included in your .def file. The display of the button is controlled by the return value of the function as follows: return 0 - Menu item is unchecked and disabled. return 1 - Menu item is unchecked and enabled. This is the default menu state if no update function is specified. return 2 - Menu item is checked and disabled. return 3 - Menu item is checked and enabled. See Add-in Callback and Enable Methods to learn how to specify your updatefunction. |
| hintstring | Optional argument that contains a text hint displayed in the SOLIDWORKS Design status bar when the user moves the mouse over this menu item. If hintstring is specified, then it must be preceded by a comma. For example: "Userdll@AddBox@checkForUserSelects,Add a box" |

## See Also

[IFrame Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IFrame.html)
[IFrame Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IFrame_members.html)
[AddMenu Method (IFrame)](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IFrame~AddMenu.html)
[IFrame::GetSubMenuCount Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IFrame~GetSubMenuCount.html)
[IFrame::GetSubMenus Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IFrame~GetSubMenus.html)
[IFrame::IGetSubMenus Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IFrame~IGetSubMenus.html)
[IFrame::RemoveMenu Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IFrame~RemoveMenu.html)
[IFrame::RenameMenu Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IFrame~RenameMenu.html)
[ISldWorks::GetLocalizedMenuName Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISldWorks~GetLocalizedMenuName.html)
[IFrame::AddMenuPopupIcon Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IFrame~AddMenuPopupIcon.html)
[IFrame::RemoveMenuPopupIcon Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IFrame~RemoveMenuPopupIcon.html)

## Availability

SOLIDWORKS 2005 FCS, Revision Number 13.0
