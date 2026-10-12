---
title: "SetTitleBitmap2 Method (IPropertyManagerPage2)"
project: "SOLIDWORKS API Help"
interface: "IPropertyManagerPage2"
member: "SetTitleBitmap2"
kind: "method"
source: "sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IPropertyManagerPage2~SetTitleBitmap2.html"
---

# SetTitleBitmap2 Method (IPropertyManagerPage2)

Obsolete. Superseded by [IPropertyManagerPage2::SetTitleBitmapx64](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IPropertyManagerPage2~SetTitleBitmapx64.html).

This method is unsafe to use with 64-bit SOLIDWORKS, i.e. all versions since SOLIDWORKS 2016.

The 32-bit integer returned may be to small to contain the 64-bit window handle/pointer, and will be truncated silently. A critical exception will occur sometime later, when the truncated handle/pointer is used.

Sets the bitmap to display in the title of this PropertyManager page.

## Syntax

### Visual Basic (Declaration)

```vb
Sub SetTitleBitmap2( _
   ByVal FilePathName As System.String _
)
```

### Visual Basic (Usage)

```vb
Dim instance As IPropertyManagerPage2
Dim FilePathName As System.String

instance.SetTitleBitmap2(FilePathName)
```

### C#

```csharp
void SetTitleBitmap2(
   System.string FilePathName
)
```

### C++/CLI

```cpp
void SetTitleBitmap2(
   System.String^ FilePathName
)
```

**NOTE:** See [Differences Between Unmanaged C++ and C++/CLI Code](DifferencesBetweenUnManagedAndCPPCLI.htm).

### Parameters

- `FilePathName`: Path and filename of the bitmap to display in the title of this PropertyManager page

## VBA Syntax

See [PropertyManagerPage2::SetTitleBitmap2](ms-its:sldworksapivb6.chm::/sldworks~PropertyManagerPage2~SetTitleBitmap2.html).

## Remarks

**All applications are required to be compatible with SOLIDWORKS x64. You must replace all calls to 32-bit only APIs with calls to their 64-bit safe counterparts.**

See [Eliminating 32-bit only API use](sldworksapiprogguide.chm::/Overview/Eliminating_32-Bit_Only_API_Use.htm) for more information.

You can only use this method to set properties on the PropertyManager page before it is displayed or while it is closed. See [IPropertyManagerPage2::Show2](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.IPropertyManagerPage2~Show2.html) and [IPropertyManagerPage2::Close](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.IPropertyManagerPage2~Close.html) for details.

Create the bitmap in the resources of your application. The bitmap must have less than 256 colors. It is accessed via the path and filename passed into this method. The recommended size for bitmaps is a square from 18- to 22-cells wide. However, the bitmap can be any size, as long as it fits on the title bar.

The bitmap appears transparent by mapping any white (RGB(255,255,255)) cells to the current PropertyManager page title bar background color. Remember the special use of this color as you design your bitmap.

| If this method is... | Then the title bar contains... |
| --- | --- |
| Used | Specified bitmap starting at the left edge of the PropertyManager title bar, followed by the title bar text (see ISldWorks::CreatePropertyManagerPage or ISldWorks::ICreatePropertyManagerPage ). |
| Not used | Only the text, centered on the title bar. |

## See Also

[IPropertyManagerPage2 Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IPropertyManagerPage2.html)
[IPropertyManagerPage2 Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IPropertyManagerPage2_members.html)
[IPropertyManagerPage2::Title Property](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IPropertyManagerPage2~Title.html)

## Availability

SOLIDWORKS 2005 SP2, Revision Number 13.2
