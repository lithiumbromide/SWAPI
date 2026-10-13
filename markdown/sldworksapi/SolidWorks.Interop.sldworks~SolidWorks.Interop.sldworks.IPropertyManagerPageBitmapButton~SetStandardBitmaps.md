---
title: "SetStandardBitmaps Method (IPropertyManagerPageBitmapButton)"
project: "SOLIDWORKS API Help"
interface: "IPropertyManagerPageBitmapButton"
member: "SetStandardBitmaps"
kind: "method"
source: "sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IPropertyManagerPageBitmapButton~SetStandardBitmaps.html"
---

# SetStandardBitmaps Method (IPropertyManagerPageBitmapButton)

Sets the standard images for this button.

## Syntax

### Visual Basic (Declaration)

```vb
Function SetStandardBitmaps( _
   ByVal Bitmap As System.Integer _
) As System.Boolean
```

### Visual Basic (Usage)

```vb
Dim instance As IPropertyManagerPageBitmapButton
Dim Bitmap As System.Integer
Dim value As System.Boolean

value = instance.SetStandardBitmaps(Bitmap)
```

### C#

```csharp
System.bool SetStandardBitmaps(
   System.int Bitmap
)
```

### C++/CLI

```cpp
System.bool SetStandardBitmaps(
   System.int Bitmap
)
```

**NOTE:** See [Differences Between Unmanaged C++ and C++/CLI Code](DifferencesBetweenUnManagedAndCPPCLI.htm).

### Parameters

- `Bitmap`: Standard images as defined by [swPropertyManagerPageBitmapButtons_e](ms-its:swconst.chm::/SOLIDWORKS.Interop.swconst~SOLIDWORKS.Interop.swconst.swPropertyManagerPageBitmapButtons_e.html)

### Return Value

True if standard images are set, false if not

## VBA Syntax

See [PropertyManagerPageBitmapButton::SetStandardBitmaps](ms-its:sldworksapivb6.chm::/sldworks~PropertyManagerPageBitmapButton~SetStandardBitmaps.html).

## Examples

See the [IPropertyManagerPageBitmapButton](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IPropertyManagerPageBitmapButton.html) examples.

## Remarks

This is the quickest and easiest way to set images on a bitmap button control after the control is created. The not-clicked, clicked, and disabled states for the control are automatically set by the SOLIDWORKS Design application.

You must call this method after calling either of the following methods to create the bitmap button control:

- [IPropertyManagerPage2::AddControl](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.IPropertyManagerPage2~AddControl.html) or [IPropertyManagerPage2::IAddControl](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.IPropertyManagerPage2~IAddControl.html)
- [IPropertyManagerPageGroup::AddControl](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.IPropertyManagerPageGroup~AddControl.html) or [IPropertyManagerPageGroup::IAddControl](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.IPropertyManagerPageGroup~IAddControl.html)

## See Also

[IPropertyManagerPageBitmapButton Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IPropertyManagerPageBitmapButton.html)
[IPropertyManagerPageBitmapButton Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IPropertyManagerPageBitmapButton_members.html)

## Availability

SOLIDWORKS 2004 FCS, Revision Number 12.0
