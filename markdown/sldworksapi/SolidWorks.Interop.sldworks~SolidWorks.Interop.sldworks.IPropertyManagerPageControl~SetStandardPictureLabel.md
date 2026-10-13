---
title: "SetStandardPictureLabel Method (IPropertyManagerPageControl)"
project: "SOLIDWORKS API Help"
interface: "IPropertyManagerPageControl"
member: "SetStandardPictureLabel"
kind: "method"
source: "sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IPropertyManagerPageControl~SetStandardPictureLabel.html"
---

# SetStandardPictureLabel Method (IPropertyManagerPageControl)

Sets the bitmap's or PNG image's label for this control on a PropertyManager page.

## Syntax

### Visual Basic (Declaration)

```vb
Function SetStandardPictureLabel( _
   ByVal Bitmap As System.Integer _
) As System.Boolean
```

### Visual Basic (Usage)

```vb
Dim instance As IPropertyManagerPageControl
Dim Bitmap As System.Integer
Dim value As System.Boolean

value = instance.SetStandardPictureLabel(Bitmap)
```

### C#

```csharp
System.bool SetStandardPictureLabel(
   System.int Bitmap
)
```

### C++/CLI

```cpp
System.bool SetStandardPictureLabel(
   System.int Bitmap
)
```

**NOTE:** See [Differences Between Unmanaged C++ and C++/CLI Code](DifferencesBetweenUnManagedAndCPPCLI.htm).

### Parameters

- `Bitmap`: Label type as defined in [swControlBitmapLabelType_e](ms-its:swconst.chm::/SOLIDWORKS.Interop.swconst~SOLIDWORKS.Interop.swconst.swControlBitmapLabelType_e.html)

### Return Value

True if successful, false if not

## VBA Syntax

See [PropertyManagerPageControl::SetStandardPictureLabel](ms-its:sldworksapivb6.chm::/sldworks~PropertyManagerPageControl~SetStandardPictureLabel.html).

## Examples

[Cut Body in Half Using Macro Feature (VBA)](Cut_Body_in_Half_using_Macro_Feature_Example_VB.htm)

## Remarks

You can only use this method on a PropertyManager page before the page is displayed, while it is displayed, or when it is closed.

## See Also

[IPropertyManagerPageControl Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IPropertyManagerPageControl.html)
[IPropertyManagerPageControl Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IPropertyManagerPageControl_members.html)

## Availability

SOLIDWORKS 2001Plus FCS, Revision Number 10.0
