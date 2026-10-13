---
title: "AddCommandItem2 Method (ICommandGroup)"
project: "SOLIDWORKS API Help"
interface: "ICommandGroup"
member: "AddCommandItem2"
kind: "method"
source: "sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ICommandGroup~AddCommandItem2.html"
---

# AddCommandItem2 Method (ICommandGroup)

Adds a combination menu item and toolbar item to a CommandGroup.

## Syntax

### Visual Basic (Declaration)

```vb
Function AddCommandItem2( _
   ByVal Name As System.String, _
   ByVal Position As System.Integer, _
   ByVal HintString As System.String, _
   ByVal ToolTip As System.String, _
   ByVal ImageListIndex As System.Integer, _
   ByVal CallbackFunction As System.String, _
   ByVal EnableMethod As System.String, _
   ByVal UserID As System.Integer, _
   ByVal MenuTBOption As System.Integer _
) As System.Integer
```

### Visual Basic (Usage)

```vb
Dim instance As ICommandGroup
Dim Name As System.String
Dim Position As System.Integer
Dim HintString As System.String
Dim ToolTip As System.String
Dim ImageListIndex As System.Integer
Dim CallbackFunction As System.String
Dim EnableMethod As System.String
Dim UserID As System.Integer
Dim MenuTBOption As System.Integer
Dim value As System.Integer

value = instance.AddCommandItem2(Name, Position, HintString, ToolTip, ImageListIndex, CallbackFunction, EnableMethod, UserID, MenuTBOption)
```

### C#

```csharp
System.int AddCommandItem2(
   System.string Name,
   System.int Position,
   System.string HintString,
   System.string ToolTip,
   System.int ImageListIndex,
   System.string CallbackFunction,
   System.string EnableMethod,
   System.int UserID,
   System.int MenuTBOption
)
```

### C++/CLI

```cpp
System.int AddCommandItem2(
   System.String^ Name,
   System.int Position,
   System.String^ HintString,
   System.String^ ToolTip,
   System.int ImageListIndex,
   System.String^ CallbackFunction,
   System.String^ EnableMethod,
   System.int UserID,
   System.int MenuTBOption
)
```

**NOTE:** See [Differences Between Unmanaged C++ and C++/CLI Code](DifferencesBetweenUnManagedAndCPPCLI.htm).

### Parameters

- `Name`: Name of the item to add to the CommandGroup
- `Position`: Position of the item within the CommandGroup

  **NOTE:** Specify 0 to add this item to the beginning of the CommandGroup, or specify -1 to add it to the end of the CommandGroup. This argument specifies the position of the item in relation to its immediate parent item.
- `HintString`: Text displayed in the SOLIDWORKS status bar when the pointer is on the item
- `ToolTip`: ToolTip displayed when the pointer is on the item
- `ImageListIndex`: Index number of the image for the item in the parent CommandGroup (see **Remarks**)
- `CallbackFunction`: Function to call when this item is selected (see **Remarks**)
- `EnableMethod`: Optional function that controls the state of the item; if specified, then SOLIDWORKS calls this function before displaying the item

  | If your method returns... | Then SOLIDWORKS... |
  | --- | --- |
  | 0 | Deselects and disables the item |
  | 1 | Deselects and enables the item; this is the default state if no update function is specified |
  | 2 | Selects and disables the item |
  | 3 | Selects and enables the item |
  | 4 | Not supported |

  (see **Remarks**)
- `UserID`: User-defined command ID or 0 if not used
- `MenuTBOption`: Command item type as defined in [swCommandItemType_e](ms-its:swconst.chm::/SOLIDWORKS.Interop.swconst~SOLIDWORKS.Interop.swconst.swCommandItemType_e.html)

### Return Value

Index of the item within the CommandGroup as assigned by SOLIDWORKS

## VBA Syntax

See [CommandGroup::AddCommandItem2](ms-its:sldworksapivb6.chm::/sldworks~CommandGroup~AddCommandItem2.html).

## Examples

[Create Flyouts in the CommandManager (C#)](Create_Flyouts_in_the_CommandManager_Example_CSharp.htm)
[Create Flyouts in the CommandManager (VB.NET)](Create_Flyouts_in_the_CommandManager_Example_VBNET.htm)
[Create Submenus in the CommandManager (C#)](Create_Submenus_in_the_CommandManager_Example_CSharp.htm)

## Remarks

See [Add-in Callback and Enable Methods](sldworksapiprogguide.chm::/OVERVIEW/Add-in_Callbacks.htm) to learn how to specify CallbackFunction and EnableMethod.

ImageListIndex is 0-based. The size of the index is equal to number of the images in the image files for that CommandGroup. See [ICommandGroup::IconList](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ICommandGroup~IconList.html) for details. You can use -1 for ImageListIndex to specify that no icon is needed for a command item of type swCommandItemType_e.swMenuItem; however, command items of type swCommandItemType_e.swToolbarItem always need an icon.

## See Also

[ICommandGroup Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ICommandGroup.html)
[ICommandGroup Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ICommandGroup_members.html)
[ICommandGroup::CommandID Property](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ICommandGroup~CommandID.html)
[ISldWorks::GetCommandID Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISldWorks~GetCommandID.html)
[ICommandGroup::HasEnabledButton Property](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ICommandGroup~HasEnabledButton.html)

## Availability

SOLIDWORKS 2007 FCS, Revision Number 15
