---
title: "MaskType Property (IDecal)"
project: "SOLIDWORKS API Help"
interface: "IDecal"
member: "MaskType"
kind: "property"
source: "sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IDecal~MaskType.html"
---

# MaskType Property (IDecal)

Gets or sets the type of mask used with this decal.

## Syntax

### Visual Basic (Declaration)

```vb
Property MaskType As System.Integer
```

### Visual Basic (Usage)

```vb
Dim instance As IDecal
Dim value As System.Integer

instance.MaskType = value

value = instance.MaskType
```

### C#

```csharp
System.int MaskType {get; set;}
```

### C++/CLI

```cpp
property System.int MaskType {
   System.int get();
   void set (    System.int value);
}
```

**NOTE:** See [Differences Between Unmanaged C++ and C++/CLI Code](DifferencesBetweenUnManagedAndCPPCLI.htm).

### Property Value

Type of mask:

- 0 = No mask
- 1 = Image mask file
- 2 = Selective color mask
- 3 = Use decal image alpha channel

## VBA Syntax

See [Decal::MaskType](ms-its:sldworksapivb6.chm::/sldworks~Decal~MaskType.html).

## Examples

[Get Mask Types of Each Decal (VBA)](Get_Mask_Types_of_Each_Decal_Example_VB.htm)

## See Also

[IDecal Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IDecal.html)
[IDecal Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IDecal_members.html)
[IDecal::GetMaskExcludedColorsCount Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IDecal~GetMaskExcludedColorsCount.html)
[IDecal::IGetMaskExcludedColors Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IDecal~IGetMaskExcludedColors.html)
[IDecal::ISetMaskExcludedColors Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IDecal~ISetMaskExcludedColors.html)
[IDecal::MaskFilename Property](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IDecal~MaskFilename.html)
[IDecal::MaskInvert Property](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IDecal~MaskInvert.html)

## Availability

SOLIDWORKS 2008 FCS, Revision Number 16.0
