---
title: "SetPictureLabelByName Method (IPropertyManagerPageControl)"
project: "SOLIDWORKS API Help"
interface: "IPropertyManagerPageControl"
member: "SetPictureLabelByName"
kind: "method"
source: "sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IPropertyManagerPageControl~SetPictureLabelByName.html"
---

# SetPictureLabelByName Method (IPropertyManagerPageControl)

Sets the bitmap label for this control on a PropertyManager page.

## Syntax

### Visual Basic (Declaration)

```vb
Function SetPictureLabelByName( _
   ByVal ColorBitmap As System.String, _
   ByVal MaskBitmap As System.String _
) As System.Boolean
```

### Visual Basic (Usage)

```vb
Dim instance As IPropertyManagerPageControl
Dim ColorBitmap As System.String
Dim MaskBitmap As System.String
Dim value As System.Boolean

value = instance.SetPictureLabelByName(ColorBitmap, MaskBitmap)
```

### C#

```csharp
System.bool SetPictureLabelByName(
   System.string ColorBitmap,
   System.string MaskBitmap
)
```

### C++/CLI

```cpp
System.bool SetPictureLabelByName(
   System.String^ ColorBitmap,
   System.String^ MaskBitmap
)
```

**NOTE:** See [Differences Between Unmanaged C++ and C++/CLI Code](DifferencesBetweenUnManagedAndCPPCLI.htm).

### Parameters

- `ColorBitmap`: Fully qualified path to the location of the bitmap (i.e., the graphic to use) on disk
- `MaskBitmap`: Fully qualified path to the location of the alpha mask bitmap on disk

### Return Value

True if successful, false if not

## VBA Syntax

See [PropertyManagerPageControl::SetPictureLabelByName](ms-its:sldworksapivb6.chm::/sldworks~PropertyManagerPageControl~SetPictureLabelByName.html).

## Remarks

The image format for the two bitmaps is 18 x 18 pixels x 256 colors. The pixels in MaskBitmap specify transparency through shades of grey with boundaries of black pixels = 100% opaque and white pixels = 100% transparent.

You can only use this method on a PropertyManager page before the page is displayed, while it is displayed, or when it is closed.

## See Also

[IPropertyManagerPageControl Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IPropertyManagerPageControl.html)
[IPropertyManagerPageControl Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IPropertyManagerPageControl_members.html)

## Availability

SOLIDWORKS 2001Plus FCS, Revision Number 10.0
