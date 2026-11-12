---
title: "AddCustomButton2 Method (ITaskpaneView)"
project: "SOLIDWORKS API Help"
interface: "ITaskpaneView"
member: "AddCustomButton2"
kind: "method"
source: "sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ITaskpaneView~AddCustomButton2.html"
---

# AddCustomButton2 Method (ITaskpaneView)

Adds a custom button to the Task Pane.

## Syntax

### Visual Basic (Declaration)

```vb
Function AddCustomButton2( _
   ByVal ImageList As System.Object, _
   ByVal ToolTip As System.String _
) As System.Boolean
```

### Visual Basic (Usage)

```vb
Dim instance As ITaskpaneView
Dim ImageList As System.Object
Dim ToolTip As System.String
Dim value As System.Boolean

value = instance.AddCustomButton2(ImageList, ToolTip)
```

### C#

```csharp
System.bool AddCustomButton2(
   System.object ImageList,
   System.string ToolTip
)
```

### C++/CLI

```cpp
System.bool AddCustomButton2(
   System.Object^ ImageList,
   System.String^ ToolTip
)
```

**NOTE:** See [Differences Between Unmanaged C++ and C++/CLI Code](DifferencesBetweenUnManagedAndCPPCLI.htm).

### Parameters

- `ImageList`: Array of strings for the paths for the image files for the custom button (see **Remarks**)
- `ToolTip`: ToolTip for the custom button

### Return Value

True if the custom button is added to the Task Pane, false if not

## VBA Syntax

See [TaskpaneView::AddCustomButton2](ms-its:sldworksapivb6.chm::/sldworks~TaskpaneView~AddCustomButton2.html).

## Remarks

This method supports scaling for high resolution screens with high resolution operating system scaling options.

ImageList images can be:

- 20 x 20 pixels
- 32 x 32 pixels
- 40 x 40 pixels
- 64 x 64 pixels
- 96 x 96 pixels
- 128 x128 pixels

The images should use 256-color palette.

The size of the custom button displayed is dictated by both the monitor's or laptop's screen resolution and SOLIDWORKS icon size. You must set the custom button size before executing a macro or application that calls this method.

For example, if running Windows 7:

1. To set your monitor's or laptop's screen resolution:

  1. Click **Start > Control Panel > Appearance and Personalization > Display**.
  2. Select a different icon size.
  3. Click **Apply**.
  4. Click **Log off now**.
2. Log back in.
3. Start SOLIDWORKS and open a part, assembly, or drawing.
4. Click **Tools > Customize** and on the Toolbars tab, click the **Icon size** that matches the size that you set in step 1b and click **OK** two twice.

## See Also

[ITaskpaneView Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ITaskpaneView.html)
[ITaskpaneView Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ITaskpaneView_members.html)
[ITaskpaneView::AddStandardButton Method ()](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ITaskpaneView~AddStandardButton.html)
[ITaskpaneView::GetButtonState Method ()](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ITaskpaneView~GetButtonState.html)
[ITaskpaneView::SetButtonState Method ()](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ITaskpaneView~SetButtonState.html)
[DTaskpaneViewEvents_TaskPaneToolbarButtonClickedEventHandler Delegate (ITaskpaneView)](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.DTaskpaneViewEvents_TaskPaneToolbarButtonClickedEventHandler.html)
[ISldWorks::GetImageSize Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISldWorks~GetImageSize.html)

## Availability

SOLIDWORKS 2016 FCS, Revision Number 24.0
