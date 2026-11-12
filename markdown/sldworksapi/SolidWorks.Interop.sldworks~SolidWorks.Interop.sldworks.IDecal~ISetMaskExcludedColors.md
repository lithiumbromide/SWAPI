---
title: "ISetMaskExcludedColors Method (IDecal)"
project: "SOLIDWORKS API Help"
interface: "IDecal"
member: "ISetMaskExcludedColors"
kind: "method"
source: "sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IDecal~ISetMaskExcludedColors.html"
---

# ISetMaskExcludedColors Method (IDecal)

Sets the colors to exclude from the mask image for this decal.

## Syntax

### Visual Basic (Declaration)

```vb
Sub ISetMaskExcludedColors( _
   ByVal Count As System.Integer, _
   ByRef MaskColors As System.Integer _
)
```

### Visual Basic (Usage)

```vb
Dim instance As IDecal
Dim Count As System.Integer
Dim MaskColors As System.Integer

instance.ISetMaskExcludedColors(Count, MaskColors)
```

### C#

```csharp
void ISetMaskExcludedColors(
   System.int Count,
   ref System.int MaskColors
)
```

### C++/CLI

```cpp
void ISetMaskExcludedColors(
   System.int Count,
   System.int% MaskColors
)
```

**NOTE:** See [Differences Between Unmanaged C++ and C++/CLI Code](DifferencesBetweenUnManagedAndCPPCLI.htm).

### Parameters

- `Count`: Number of colors to exclude from the mask image
- `MaskColors`: - in-process, unmanaged C++: Pointer to an array of the RGB colors excluded from the mask image

  VBA, VB.NET, C#, and C++/CLI: Not supported

  See [In-process Methods](sldworksapiprogguide.chm::/OVERVIEW/In-process_Methods.htm) for details about this type of method.

## VBA Syntax

See [Decal::ISetMaskExcludedColors](ms-its:sldworksapivb6.chm::/sldworks~Decal~ISetMaskExcludedColors.html).

## See Also

[IDecal Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IDecal.html)
[IDecal Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IDecal_members.html)
[IDecal::GetMaskExcludedColorsCount Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IDecal~GetMaskExcludedColorsCount.html)
[IDecal::IGetMaskExcludedColors Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IDecal~IGetMaskExcludedColors.html)
[IDecal::MaskFilename Property](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IDecal~MaskFilename.html)
[IDecal::MaskInvert Property](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IDecal~MaskInvert.html)
[IDecal::MaskType Property](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IDecal~MaskType.html)

## Availability

SOLIDWORKS 2008 FCS, Revision Number 16.0
