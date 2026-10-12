---
title: "IGetMaskExcludedColors Method (IDecal)"
project: "SOLIDWORKS API Help"
interface: "IDecal"
member: "IGetMaskExcludedColors"
kind: "method"
source: "sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IDecal~IGetMaskExcludedColors.html"
---

# IGetMaskExcludedColors Method (IDecal)

Gets the colors excluded from the mask image for this decal.

## Syntax

### Visual Basic (Declaration)

```vb
Function IGetMaskExcludedColors( _
   ByVal Count As System.Integer _
) As System.Integer
```

### Visual Basic (Usage)

```vb
Dim instance As IDecal
Dim Count As System.Integer
Dim value As System.Integer

value = instance.IGetMaskExcludedColors(Count)
```

### C#

```csharp
System.int IGetMaskExcludedColors(
   System.int Count
)
```

### C++/CLI

```cpp
System.int IGetMaskExcludedColors(
   System.int Count
)
```

**NOTE:** See [Differences Between Unmanaged C++ and C++/CLI Code](DifferencesBetweenUnManagedAndCPPCLI.htm).

### Parameters

- `Count`: Number of colors excluded from the mask image

### Return Value

- in-process, unmanaged C++: Pointer to an array of the RGB colors excluded from the mask image

VBA, VB.NET, C#, and C++/CLI: Not supported

See [In-process Methods](sldworksapiprogguide.chm::/OVERVIEW/In-process_Methods.htm) for details about this type of method.

## VBA Syntax

See [Decal::IGetMaskExcludedColors](ms-its:sldworksapivb6.chm::/sldworks~Decal~IGetMaskExcludedColors.html).

## Remarks

Before calling this method, call [IDecal::GetMaskExcludedColorsCount](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.IDecal~GetMaskExcludedColorsCount.html) to get the value of Count.

## See Also

[IDecal Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IDecal.html)
[IDecal Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IDecal_members.html)
[IDecal::ISetMaskExcludedColors Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IDecal~ISetMaskExcludedColors.html)
[IDecal::MaskFilename Property](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IDecal~MaskFilename.html)
[IDecal::MaskInvert Property](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IDecal~MaskInvert.html)
[IDecal::MaskType Property](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IDecal~MaskType.html)

## Availability

SOLIDWORKS 2008FCS, Revision Number 16.0
