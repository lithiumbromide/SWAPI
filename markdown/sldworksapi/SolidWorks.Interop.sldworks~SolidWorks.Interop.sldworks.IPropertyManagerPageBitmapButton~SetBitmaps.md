---
title: "SetBitmaps Method (IPropertyManagerPageBitmapButton)"
project: "SOLIDWORKS API Help"
interface: "IPropertyManagerPageBitmapButton"
member: "SetBitmaps"
kind: "method"
source: "sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IPropertyManagerPageBitmapButton~SetBitmaps.html"
---

# SetBitmaps Method (IPropertyManagerPageBitmapButton)

Obsolete. Superseded by [IPropertyManagerPageBitmapButton::SetBitmapsx64](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IPropertyManagerPageBitmapButton~SetBitmapsx64.html).

This method is unsafe to use with 64-bit SOLIDWORKS, i.e. all versions since SOLIDWORKS 2016.

The 32-bit integer returned may be to small to contain the 64-bit window handle/pointer, and will be truncated silently. A critical exception will occur sometime later, when the truncated handle/pointer is used.

Sets the images for this button.

## Syntax

### Visual Basic (Declaration)

```vb
Function SetBitmaps( _
   ByVal ModuleHandle As System.Integer, _
   ByVal BitmapUp As System.Integer, _
   ByVal BitmapDown As System.Integer, _
   ByVal BitmapDisabled As System.Integer _
) As System.Boolean
```

### Visual Basic (Usage)

```vb
Dim instance As IPropertyManagerPageBitmapButton
Dim ModuleHandle As System.Integer
Dim BitmapUp As System.Integer
Dim BitmapDown As System.Integer
Dim BitmapDisabled As System.Integer
Dim value As System.Boolean

value = instance.SetBitmaps(ModuleHandle, BitmapUp, BitmapDown, BitmapDisabled)
```

### C#

```csharp
System.bool SetBitmaps(
   System.int ModuleHandle,
   System.int BitmapUp,
   System.int BitmapDown,
   System.int BitmapDisabled
)
```

### C++/CLI

```cpp
System.bool SetBitmaps(
   System.int ModuleHandle,
   System.int BitmapUp,
   System.int BitmapDown,
   System.int BitmapDisabled
)
```

**NOTE:** See [Differences Between Unmanaged C++ and C++/CLI Code](DifferencesBetweenUnManagedAndCPPCLI.htm).

### Parameters

- `ModuleHandle`: Module handle of the application instance that contains the image resource
- `BitmapUp`: Resource ID of the not-clicked state image resource
- `BitmapDown`: Resource ID of the clicked state image resource
- `BitmapDisabled`: Resource ID of the disabled state image resource

### Return Value

True if successful, false if not

## VBA Syntax

See [PropertyManagerPageBitmapButton::SetBitmaps](ms-its:sldworksapivb6.chm::/sldworks~PropertyManagerPageBitmapButton~SetBitmaps.html).

## Remarks

**All applications are required to be compatible with SOLIDWORKS x64. You must replace all calls to 32-bit only APIs with calls to their 64-bit safe counterparts.**

See [Eliminating 32-bit only API use](sldworksapiprogguide.chm::/Overview/Eliminating_32-Bit_Only_API_Use.htm) for more information.

The ModuleHandle argument for this method is the handle to the instance (HINSTANCE) of the user DLL, and the resource IDs for the not-clicked, clicked, and disabled states are the image resource integers. The SOLIDWORKS Design application loads the images from the user DLL and uses them on this bitmap button control.

You must call this method after calling either of the following methods to create the button control:

- [IPropertyManagerPage2::AddControl](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.IPropertyManagerPage2~AddControl.html) or [IPropertyManagerPage2::IAddControl](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.IPropertyManagerPage2~IAddControl.html)
- [IPropertyManagerPageGroup::AddControl](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.IPropertyManagerPageGroup~AddControl.html) or [IPropertyManagerPageGroup::IAddControl](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.IPropertyManagerPageGroup~IAddControl.html)

## See Also

[IPropertyManagerPageBitmapButton Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IPropertyManagerPageBitmapButton.html)
[IPropertyManagerPageBitmapButton Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IPropertyManagerPageBitmapButton_members.html)

## Availability

SOLIDWORKS 2004 FCS, Revision Number 12.0
