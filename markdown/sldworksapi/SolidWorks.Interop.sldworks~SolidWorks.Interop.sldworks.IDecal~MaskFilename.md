---
title: "MaskFilename Property (IDecal)"
project: "SOLIDWORKS API Help"
interface: "IDecal"
member: "MaskFilename"
kind: "property"
source: "sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IDecal~MaskFilename.html"
---

# MaskFilename Property (IDecal)

Gets or sets the path and filename for the image to use as a mask for this decal.

## Syntax

### Visual Basic (Declaration)

```vb
Property MaskFilename As System.String
```

### Visual Basic (Usage)

```vb
Dim instance As IDecal
Dim value As System.String

instance.MaskFilename = value

value = instance.MaskFilename
```

### C#

```csharp
System.string MaskFilename {get; set;}
```

### C++/CLI

```cpp
property System.String^ MaskFilename {
   System.String^ get();
   void set (    System.String^ value);
}
```

**NOTE:** See [Differences Between Unmanaged C++ and C++/CLI Code](DifferencesBetweenUnManagedAndCPPCLI.htm).

### Property Value

Fully qualified path and filename of the image to use as a mask

## VBA Syntax

See [Decal::MaskFilename](ms-its:sldworksapivb6.chm::/sldworks~Decal~MaskFilename.html).

## See Also

[IDecal Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IDecal.html)
[IDecal Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IDecal_members.html)
[IDecal::GetMaskExcludedColorsCount Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IDecal~GetMaskExcludedColorsCount.html)
[IDecal::IGetMaskExcludedColors Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IDecal~IGetMaskExcludedColors.html)
[IDecal::ISetMaskExcludedColors Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IDecal~ISetMaskExcludedColors.html)
[IDecal::MaskInvert Property](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IDecal~MaskInvert.html)
[IDecal::MaskType Property](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IDecal~MaskType.html)

## Availability

SOLIDWORKS 2008 FCS, Revision Number 16.0
