---
title: "FixedFace2 Property (IFlatPatternFeatureData)"
project: "SOLIDWORKS API Help"
interface: "IFlatPatternFeatureData"
member: "FixedFace2"
kind: "property"
source: "sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IFlatPatternFeatureData~FixedFace2.html"
---

# FixedFace2 Property (IFlatPatternFeatureData)

Gets or sets the fixed face of this Flat-Pattern feature.

## Syntax

### Visual Basic (Declaration)

```vb
Property FixedFace2 As System.Object
```

### Visual Basic (Usage)

```vb
Dim instance As IFlatPatternFeatureData
Dim value As System.Object

instance.FixedFace2 = value

value = instance.FixedFace2
```

### C#

```csharp
System.object FixedFace2 {get; set;}
```

### C++/CLI

```cpp
property System.Object^ FixedFace2 {
   System.Object^ get();
   void set (    System.Object^ value);
}
```

**NOTE:** See [Differences Between Unmanaged C++ and C++/CLI Code](DifferencesBetweenUnManagedAndCPPCLI.htm).

### Property Value

Fixed [face](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.IFace2.html) (or [edge](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IEdge.html) for cylindrical sheet metal parts)

## VBA Syntax

See [FlatPatternFeatureData::FixedFace2](ms-its:sldworksapivb6.chm::/sldworks~FlatPatternFeatureData~FixedFace2.html).

## Examples

[Get Fixed Face of Flat-Pattern Feature (VBA)](Get_Fixed_Face_of_Flat-Pattern_Feature_Example_VB.htm)
[Get Fixed Face of Flat-Pattern Feature (VB.NET)](Get_Fixed_Face_of_Flat-Pattern_Feature_Example_VBNET.htm)
[Get Fixed Face of Flat-Pattern Feature (C#)](Get_Fixed_Face_of_Flat-Pattern_Feature_Example_CSharp.htm)

## Remarks

The difference between this method and the now obsolete IFlatPatternFeatureData::FixedFace is that this method successfully returns the fixed face of a Flat-Pattern feature in a sheet metal part created in any version of SOLIDWORKS.

See [Accessing Selections that Define Features](sldworksAPIProgGuide.chm::/Miscellaneous/Accessing_Selections_that_Define_Features.htm) for additional details on using this property.

## See Also

[IFlatPatternFeatureData Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IFlatPatternFeatureData.html)
[IFlatPatternFeatureData Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IFlatPatternFeatureData_members.html)

## Availability

SOLIDWORKS 2014 FCS, Revision Number 22.0
