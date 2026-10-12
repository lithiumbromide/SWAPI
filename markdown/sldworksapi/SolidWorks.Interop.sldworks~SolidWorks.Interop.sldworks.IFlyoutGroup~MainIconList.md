---
title: "MainIconList Property (IFlyoutGroup)"
project: "SOLIDWORKS API Help"
interface: "IFlyoutGroup"
member: "MainIconList"
kind: "property"
source: "sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IFlyoutGroup~MainIconList.html"
---

# MainIconList Property (IFlyoutGroup)

Gets or sets the paths for the icons for the buttons for this flyout.

## Syntax

### Visual Basic (Declaration)

```vb
Property MainIconList As System.Object
```

### Visual Basic (Usage)

```vb
Dim instance As IFlyoutGroup
Dim value As System.Object

instance.MainIconList = value

value = instance.MainIconList
```

### C#

```csharp
System.object MainIconList {get; set;}
```

### C++/CLI

```cpp
property System.Object^ MainIconList {
   System.Object^ get();
   void set (    System.Object^ value);
}
```

**NOTE:** See [Differences Between Unmanaged C++ and C++/CLI Code](DifferencesBetweenUnManagedAndCPPCLI.htm).

### Property Value

Array of strings of the paths for the icons for the buttons for this flyout (see **Remarks**)

## VBA Syntax

See [FlyoutGroup::MainIconList](ms-its:sldworksapivb6.chm::/sldworks~FlyoutGroup~MainIconList.html).

## Examples

[Create Flyouts in the CommandManager (C#)](Create_Flyouts_in_the_CommandManager_Example_CSharp.htm)
[Create Flyouts in the CommandManager (VB.NET)](Create_Flyouts_in_the_CommandManager_Example_VBNET.htm)

## Remarks

This property supports scaling for high resolution screens with high resolution operating system scaling options.

The array of strings of the paths to the image files can contain icons of the following sizes:

- 20 x 20 pixels
- 32 x 32 pixels
- 40 x 40 pixels
- 64 x 64 pixels
- 96 x 96 pixels
- 128 x128 pixels

Each image file (**.bmp** or **.png**) contains a single icon. Each icon should use a 256-color palette.

The order in which you specify the icons must be the same for this property and [IFlyoutGroup::IconList](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IFlyoutGroup~IconList.html). For example, if you specify an array of paths to 20 x 20 pixels, 32 x 32 pixels, and 40 x 40 pixels icons for this property, then you must specify an array of paths to 20 x 20 pixels, 32 x 32 pixels, and 40 x 40 pixels icons for IFlyoutGroup::IconList.

## See Also

[IFlyoutGroup Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IFlyoutGroup.html)
[IFlyoutGroup Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IFlyoutGroup_members.html)
[ISldWorks::GetImageSize Method ()](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISldWorks~GetImageSize.html)

## Availability

SOLIDWORKS 2016 FCS, Revision Number 24.0
