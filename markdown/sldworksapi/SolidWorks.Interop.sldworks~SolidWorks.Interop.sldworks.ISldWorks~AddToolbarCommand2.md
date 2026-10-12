---
title: "AddToolbarCommand2 Method (ISldWorks)"
project: "SOLIDWORKS API Help"
interface: "ISldWorks"
member: "AddToolbarCommand2"
kind: "method"
source: "sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISldWorks~AddToolbarCommand2.html"
---

# AddToolbarCommand2 Method (ISldWorks)

Specifies the application functions to call when a toolbar button is clicked or sets a separator.

## Syntax

### Visual Basic (Declaration)

```vb
Function AddToolbarCommand2( _
   ByVal Cookie As System.Integer, _
   ByVal ToolbarId As System.Integer, _
   ByVal ToolbarIndex As System.Integer, _
   ByVal ButtonCallback As System.String, _
   ByVal ButtonEnableMethod As System.String, _
   ByVal ToolTip As System.String, _
   ByVal HintString As System.String _
) As System.Boolean
```

### Visual Basic (Usage)

```vb
Dim instance As ISldWorks
Dim Cookie As System.Integer
Dim ToolbarId As System.Integer
Dim ToolbarIndex As System.Integer
Dim ButtonCallback As System.String
Dim ButtonEnableMethod As System.String
Dim ToolTip As System.String
Dim HintString As System.String
Dim value As System.Boolean

value = instance.AddToolbarCommand2(Cookie, ToolbarId, ToolbarIndex, ButtonCallback, ButtonEnableMethod, ToolTip, HintString)
```

### C#

```csharp
System.bool AddToolbarCommand2(
   System.int Cookie,
   System.int ToolbarId,
   System.int ToolbarIndex,
   System.string ButtonCallback,
   System.string ButtonEnableMethod,
   System.string ToolTip,
   System.string HintString
)
```

### C++/CLI

```cpp
System.bool AddToolbarCommand2(
   System.int Cookie,
   System.int ToolbarId,
   System.int ToolbarIndex,
   System.String^ ButtonCallback,
   System.String^ ButtonEnableMethod,
   System.String^ ToolTip,
   System.String^ HintString
)
```

**NOTE:** See [Differences Between Unmanaged C++ and C++/CLI Code](DifferencesBetweenUnManagedAndCPPCLI.htm).

### Parameters

- `Cookie`: Resource ID of the toolbar; this is the same cookie that you specified in [ISwAddin::ConnectToSW](ms-its:swpublishedapi.chm::/SOLIDWORKS.Interop.swpublished~SOLIDWORKS.Interop.swpublished.ISwAddin~ConnectToSW.html)
- `ToolbarId`: Toolbar ID from [ISldWorks::AddToolbar5](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISldWorks~AddToolbar5.html)
- `ToolbarIndex`: 0-based index of the bitmap button
- `ButtonCallback`: Function called when the user clicks the button (see **Remarks**)
- `ButtonEnableMethod`: Function called to check whether the button should be enabled; typically used to check the type of object selected (see Remarks)
- `ToolTip`: ToolTip for the toolbar button
- `HintString`: Text that SOLIDWORKS Design displays in the status bar when the user moves their mouse over this toolbar button

### Return Value

True if successful, false if unsuccessful

## VBA Syntax

See [SldWorks::AddToolbarCommand2](ms-its:sldworksapivb6.chm::/sldworks~SldWorks~AddToolbarCommand2.html).

## Examples

[Create Toolbars (C++)](Create_Toolbars_Example_CPlusPlus_COM.htm)
[Add Toolbars (C#)](Add_Toolbars_Example_CSharp.htm)
[Add Toolbars (VB.NET)](Add_Toolbars_Example_VBNET.htm)

## Remarks

See [Add-in Callback and Enable Methods](sldworksapiprogguide.chm::/OVERVIEW/Add-in_Callbacks.htm) to learn how to specify ButtonCallback and ButtonEnableMethod.

Call this method to specify the functions that get called by the SOLIDWORKS Design software when the button is pressed and to check if the button is enabled. Until this method is called, the SOLIDWORKS Design software does not display the button.

| If ButtonEnableMethod returns... | Then SOLIDWORKS Design... |
| --- | --- |
| 0 | Deselects and disables the menu item |
| 1 | Deselects and enables the menu item; this is the default menu state if no update function is specified |
| 2 | Selects and disables the menu item |
| 3 | Selects and enables the menu item |

To create a separator, all of the method's string parameters (ButtonCallback, ButtonEnableMethod, ToolTip, and HintString) must be blank strings. A bitmap button must still be defined in the add-in's resources, but it is not used.

## See Also

[ISldWorks Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISldWorks.html)
[ISldWorks Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISldWorks_members.html)
[ISldWorks::AddMenu Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISldWorks~AddMenu.html)
[ISldWorks::AddMenuItem3 Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISldWorks~AddMenuItem3.html)
[ISldWorks::AddMenuPopupItem2 Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISldWorks~AddMenuPopupItem2.html)
[ISldWorks::RemoveFromMenu Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISldWorks~RemoveFromMenu.html)
[ISldWorks::RemoveFromPopupMenu Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISldWorks~RemoveFromPopupMenu.html)
[ISldWorks::RemoveMenu Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISldWorks~RemoveMenu.html)
[ISldWorks::RemoveMenuPopupItem2 Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISldWorks~RemoveMenuPopupItem2.html)
[ISldWorks::RemoveToolbar2 Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISldWorks~RemoveToolbar2.html)
[ISldWorks::DragToolbarButton Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISldWorks~DragToolbarButton.html)
[ISldWorks::GetToolbarDock2 Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISldWorks~GetToolbarDock2.html)
[ISldWorks::GetToolbarState2 Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISldWorks~GetToolbarState2.html)
[ISldWorks::HideToolbar2 Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISldWorks~HideToolbar2.html)
[ISldWorks::SetToolbarDock2 Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISldWorks~SetToolbarDock2.html)

## Availability

SOLIDWORKS 2001Plus FCS, Revision Number 10.0
