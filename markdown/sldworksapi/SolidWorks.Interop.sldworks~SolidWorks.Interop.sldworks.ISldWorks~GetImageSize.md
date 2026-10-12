---
title: "GetImageSize Method (ISldWorks)"
project: "SOLIDWORKS API Help"
interface: "ISldWorks"
member: "GetImageSize"
kind: "method"
source: "sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISldWorks~GetImageSize.html"
---

# GetImageSize Method (ISldWorks)

Gets:

- small, medium, and large image sizes suitable for the current DPI setting of the display device.
- default image size for the current DPI setting of the display device for images that are not based on the SOLIDWORKS icon size setting.

## Syntax

### Visual Basic (Declaration)

```vb
Function GetImageSize( _
   ByRef Small As System.Integer, _
   ByRef Medium As System.Integer, _
   ByRef Large As System.Integer _
) As System.Integer
```

### Visual Basic (Usage)

```vb
Dim instance As ISldWorks
Dim Small As System.Integer
Dim Medium As System.Integer
Dim Large As System.Integer
Dim value As System.Integer

value = instance.GetImageSize(Small, Medium, Large)
```

### C#

```csharp
System.int GetImageSize(
   out System.int Small,
   out System.int Medium,
   out System.int Large
)
```

### C++/CLI

```cpp
System.int GetImageSize(
   [Out] System.int Small,
   [Out] System.int Medium,
   [Out] System.int Large
)
```

**NOTE:** See [Differences Between Unmanaged C++ and C++/CLI Code](DifferencesBetweenUnManagedAndCPPCLI.htm).

### Parameters

- `Small`: Small image size suitable for the current DPI setting of the display device
- `Medium`: Medium image size suitable for the current DPI setting of the display device
- `Large`: Large image size suitable for the current DPI setting of the display device

### Return Value

Default image size for the current DPI setting of the display device for images that are not based on the SOLIDWORKS icon size setting as defined in [swImageSizeToUse_e](ms-its:swconst.chm::/SolidWorks.Interop.swconst~SolidWorks.Interop.swconst.swImageSizeToUse_e.html)

## VBA Syntax

See [SldWorks::GetImageSize](ms-its:sldworksapivb6.chm::/sldworks~SldWorks~GetImageSize.html).

## Examples

[Create Flyouts in the CommandManager (C#)](Create_Flyouts_in_the_CommandManager_Example_CSharp.htm)
[Create Flyouts in the CommandManager (VB.NET)](Create_Flyouts_in_the_CommandManager_Example_VBNET.htm)

## Remarks

You can use this method to determine the correct size for:

- buttons for your PropertyManager pages.
- icons for your macro features.

## See Also

[ISldWorks Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISldWorks.html)
[ISldWorks Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISldWorks_members.html)
[ICommandGroup::IconList Property ()](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ICommandGroup~IconList.html)
[ICommandGroup::MainIconList Property ()](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ICommandGroup~MainIconList.html)
[ICommandManager::CreateFlyoutGroup2 Method ()](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ICommandManager~CreateFlyoutGroup2.html)
[IFlyoutGroup::IconList Property ()](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IFlyoutGroup~IconList.html)
[IFlyoutGroup::MainIconList Property ()](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IFlyoutGroup~MainIconList.html)
[IFrame::AddMenuPopupIcon3 Method ()](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IFrame~AddMenuPopupIcon3.html)
[IPropertyManagerPageBitmapButton::SetBitmapsByName3 Method ()](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IPropertyManagerPageBitmapButton~SetBitmapsByName3.html)
[ISldWorks::AddMenuItem5 Method ()](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISldWorks~AddMenuItem5.html)
[ISldWorks::AddToolbar5 Method ()](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISldWorks~AddToolbar5.html)
[ITaskPaneView::AddCustomButton2 Method ()](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ITaskpaneView~AddCustomButton2.html)
[ISldWorks::CreateTaskpaneView3 Method ()](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISldWorks~CreateTaskpaneView3.html)

## Availability

SOLIDWORKS 2017 FCS, Revision Number 25.0
