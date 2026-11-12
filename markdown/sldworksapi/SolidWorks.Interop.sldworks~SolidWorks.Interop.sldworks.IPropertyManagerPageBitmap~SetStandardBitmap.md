---
title: "SetStandardBitmap Method (IPropertyManagerPageBitmap)"
project: "SOLIDWORKS API Help"
interface: "IPropertyManagerPageBitmap"
member: "SetStandardBitmap"
kind: "method"
source: "sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IPropertyManagerPageBitmap~SetStandardBitmap.html"
---

# SetStandardBitmap Method (IPropertyManagerPageBitmap)

Sets the bitmap or PNG image for this control.

## Syntax

### Visual Basic (Declaration)

```vb
Function SetStandardBitmap( _
   ByVal Bitmap As System.Integer _
) As System.Boolean
```

### Visual Basic (Usage)

```vb
Dim instance As IPropertyManagerPageBitmap
Dim Bitmap As System.Integer
Dim value As System.Boolean

value = instance.SetStandardBitmap(Bitmap)
```

### C#

```csharp
System.bool SetStandardBitmap(
   System.int Bitmap
)
```

### C++/CLI

```cpp
System.bool SetStandardBitmap(
   System.int Bitmap
)
```

**NOTE:** See [Differences Between Unmanaged C++ and C++/CLI Code](DifferencesBetweenUnManagedAndCPPCLI.htm).

### Parameters

- `Bitmap`: Control standard type as defined in [swBitmapControlStandardTypes_e](ms-its:swconst.chm::/SOLIDWORKS.Interop.swconst~SOLIDWORKS.Interop.swconst.swBitmapControlStandardTypes_e.html)

### Return Value

True if the bitmap or PNG image is set, false if not

## VBA Syntax

See [PropertyManagerPageBitmap::SetStandardBitmap](ms-its:sldworksapivb6.chm::/sldworks~PropertyManagerPageBitmap~SetStandardBitmap.html).

## Examples

See the [IPropertyManagerPageBitmap](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IPropertyManagerPageBitmap.html) examples.

## Remarks

You can use this method before, during, or after the PropertyManager page is displayed or closed. If you use this method when the PropertyManager page is displayed, use a bitmap or PNG image that is the same size.

## See Also

[IPropertyManagerPageBitmap Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IPropertyManagerPageBitmap.html)
[IPropertyManagerPageBitmap Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IPropertyManagerPageBitmap_members.html)

## Availability

SOLIDWORKS 2007 FCS, Revision Number 15.0
