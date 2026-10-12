---
title: "GetMaskExcludedColorsCount Method (IDecal)"
project: "SOLIDWORKS API Help"
interface: "IDecal"
member: "GetMaskExcludedColorsCount"
kind: "method"
source: "sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IDecal~GetMaskExcludedColorsCount.html"
---

# GetMaskExcludedColorsCount Method (IDecal)

Gets the number of colors excluded from the mask image for this decal.

## Syntax

### Visual Basic (Declaration)

```vb
Function GetMaskExcludedColorsCount() As System.Integer
```

### Visual Basic (Usage)

```vb
Dim instance As IDecal
Dim value As System.Integer

value = instance.GetMaskExcludedColorsCount()
```

### C#

```csharp
System.int GetMaskExcludedColorsCount()
```

### C++/CLI

```cpp
System.int GetMaskExcludedColorsCount();
```

**NOTE:** See [Differences Between Unmanaged C++ and C++/CLI Code](DifferencesBetweenUnManagedAndCPPCLI.htm).

### Return Value

Number of colors excluded from the mask image

## VBA Syntax

See [Decal::GetMaskExcludedColorsCount](ms-its:sldworksapivb6.chm::/sldworks~Decal~GetMaskExcludedColorsCount.html).

## Remarks

Call this method before calling [IDecal::IGetMaskExcludedColors](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.IDecal~IGetMaskExcludedColors.html) to get the size of the array for that method.

## See Also

[IDecal Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IDecal.html)
[IDecal Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IDecal_members.html)
[IDecal::ISetMaskExcludedColors Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IDecal~ISetMaskExcludedColors.html)
[IDecal::MaskFilename Property](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IDecal~MaskFilename.html)
[IDecal::MaskInvert Property](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IDecal~MaskInvert.html)
[IDecal::MaskType Property](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IDecal~MaskType.html)

## Availability

SOLIDWORKS 2008 FCS, Revision Number 16.0
