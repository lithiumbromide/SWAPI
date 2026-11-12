---
title: "AlignDimensions Method (IModelDocExtension)"
project: "SOLIDWORKS API Help"
interface: "IModelDocExtension"
member: "AlignDimensions"
kind: "method"
source: "sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelDocExtension~AlignDimensions.html"
---

# AlignDimensions Method (IModelDocExtension)

Aligns the selected dimensions in drawing documents.

## Syntax

### Visual Basic (Declaration)

```vb
Function AlignDimensions( _
   ByVal AlignType As System.Integer, _
   ByVal SpaceValue As System.Double _
) As System.Boolean
```

### Visual Basic (Usage)

```vb
Dim instance As IModelDocExtension
Dim AlignType As System.Integer
Dim SpaceValue As System.Double
Dim value As System.Boolean

value = instance.AlignDimensions(AlignType, SpaceValue)
```

### C#

```csharp
System.bool AlignDimensions(
   System.int AlignType,
   System.double SpaceValue
)
```

### C++/CLI

```cpp
System.bool AlignDimensions(
   System.int AlignType,
   System.double SpaceValue
)
```

**NOTE:** See [Differences Between Unmanaged C++ and C++/CLI Code](DifferencesBetweenUnManagedAndCPPCLI.htm).

### Parameters

- `AlignType`: Type of alignment as defined by [swAlignDimensionType_e](ms-its:swconst.chm::/SOLIDWORKS.Interop.swconst~SOLIDWORKS.Interop.swconst.swAlignDimensionType_e.html)
- `SpaceValue`: Distance between dimensions

### Return Value

True if the dimensions are aligned, false if not

## VBA Syntax

See [ModelDocExtension::AlignDimensions](ms-its:sldworksapivb6.chm::/Sldworks~ModelDocExtension~AlignDimensions.html).

## Examples

[Auto-arrange Dimensions (C#)](Auto-arrange_Dimensions_Example_CSharp.htm)
[Auto-arrange Dimensions (VB.NET)](Auto-arrange_Dimensions_Example_VBNET.htm)
[Auto-arrange Dimensions (VBA)](Auto-arrange_Dimensions_Example_VB.htm)

## See Also

[IModelDocExtension Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelDocExtension.html)
[IModelDocExtension Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelDocExtension_members.html)
[IModelDoc2::AlignParallelDimensions Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelDoc2~AlignParallelDimensions.html)
[IModelDoc2::AlignOrdinate Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelDoc2~AlignOrdinate.html)
[IModelDoc2::BreakDimensionAlignment Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelDoc2~BreakDimensionAlignment.html)

## Availability

SOLIDWORKS 2011 FCS, Revision Number 19.0
