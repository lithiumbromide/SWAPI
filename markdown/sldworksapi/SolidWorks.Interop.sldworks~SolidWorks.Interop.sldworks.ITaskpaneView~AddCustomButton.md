---
title: "AddCustomButton Method (ITaskpaneView)"
project: "SOLIDWORKS API Help"
interface: "ITaskpaneView"
member: "AddCustomButton"
kind: "method"
source: "sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ITaskpaneView~AddCustomButton.html"
---

# AddCustomButton Method (ITaskpaneView)

Obsolete. Superseded by [ITaskpaneView::AddCustomButton2](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ITaskpaneView~AddCustomButton2.html).

## Syntax

### Visual Basic (Declaration)

```vb
Function AddCustomButton( _
   ByVal BitmapPath As System.String, _
   ByVal ToolTip As System.String _
) As System.Boolean
```

### Visual Basic (Usage)

```vb
Dim instance As ITaskpaneView
Dim BitmapPath As System.String
Dim ToolTip As System.String
Dim value As System.Boolean

value = instance.AddCustomButton(BitmapPath, ToolTip)
```

### C#

```csharp
System.bool AddCustomButton(
   System.string BitmapPath,
   System.string ToolTip
)
```

### C++/CLI

```cpp
System.bool AddCustomButton(
   System.String^ BitmapPath,
   System.String^ ToolTip
)
```

**NOTE:** See [Differences Between Unmanaged C++ and C++/CLI Code](DifferencesBetweenUnManagedAndCPPCLI.htm).

### Parameters

- `BitmapPath`: Path and filename of the bitmap for the custom button
- `ToolTip`: ToolTip for the custom button

### Return Value

True if the custom button is added to the Task Pane, false if not

## VBA Syntax

See [TaskpaneView::AddCustomButton](ms-its:sldworksapivb6.chm::/sldworks~TaskpaneView~AddCustomButton.html).

## Remarks

Button images can be either BMP (bitmap) or PNG and should be 16 pixels wide x 16 pixels high. The bitmap image can be 8-, 16-, 24-, or 32-bit depth.

## See Also

[ITaskpaneView Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ITaskpaneView.html)
[ITaskpaneView Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ITaskpaneView_members.html)
[ITaskPaneView::AddStandardButton Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ITaskpaneView~AddStandardButton.html)
[DTaskpaneViewEvents_TaskPaneToolbarButtonClickedEventHandler Delegate](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.DTaskpaneViewEvents_TaskPaneToolbarButtonClickedEventHandler.html)
[ITaskpaneView::GetButtonState Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ITaskpaneView~GetButtonState.html)
[ITaskpaneView::SetButtonState Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ITaskpaneView~SetButtonState.html)

## Availability

SOLIDWORKS 2011 FCS, Revision Number 19.0
