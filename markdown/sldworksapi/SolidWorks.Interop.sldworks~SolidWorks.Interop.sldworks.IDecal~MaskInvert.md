---
title: "MaskInvert Property (IDecal)"
project: "SOLIDWORKS API Help"
interface: "IDecal"
member: "MaskInvert"
kind: "property"
source: "sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IDecal~MaskInvert.html"
---

# MaskInvert Property (IDecal)

Gets or sets whether the mask is inverted.

## Syntax

### Visual Basic (Declaration)

```vb
Property MaskInvert As System.Boolean
```

### Visual Basic (Usage)

```vb
Dim instance As IDecal
Dim value As System.Boolean

instance.MaskInvert = value

value = instance.MaskInvert
```

### C#

```csharp
System.bool MaskInvert {get; set;}
```

### C++/CLI

```cpp
property System.bool MaskInvert {
   System.bool get();
   void set (    System.bool value);
}
```

**NOTE:** See [Differences Between Unmanaged C++ and C++/CLI Code](DifferencesBetweenUnManagedAndCPPCLI.htm).

### Property Value

True if the mask is inverted, false if not

## VBA Syntax

See [Decal::MaskInvert](ms-its:sldworksapivb6.chm::/sldworks~Decal~MaskInvert.html).

## See Also

[IDecal Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IDecal.html)
[IDecal Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IDecal_members.html)
[IDecal::GetMaskExcludedColorsCount Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IDecal~GetMaskExcludedColorsCount.html)
[IDecal::IGetMaskExcludedColors Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IDecal~IGetMaskExcludedColors.html)
[IDecal::ISetMaskExcludedColors Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IDecal~ISetMaskExcludedColors.html)
[IDecal::MaskFilename Property](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IDecal~MaskFilename.html)
[IDecal::MaskType Property](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IDecal~MaskType.html)

## Availability

SOLIDWORKS 2008 FCS, Revision Number 16.0
