---
title: "ThicknessSide Property (IThickenFeatureData)"
project: "SOLIDWORKS API Help"
interface: "IThickenFeatureData"
member: "ThicknessSide"
kind: "property"
source: "sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IThickenFeatureData~ThicknessSide.html"
---

# ThicknessSide Property (IThickenFeatureData)

Gets or sets which side to apply thickness.

## Syntax

### Visual Basic (Declaration)

```vb
Property ThicknessSide As System.Short
```

### Visual Basic (Usage)

```vb
Dim instance As IThickenFeatureData
Dim value As System.Short

instance.ThicknessSide = value

value = instance.ThicknessSide
```

### C#

```csharp
System.short ThicknessSide {get; set;}
```

### C++/CLI

```cpp
property System.short ThicknessSide {
   System.short get();
   void set (    System.short value);
}
```

**NOTE:** See [Differences Between Unmanaged C++ and C++/CLI Code](DifferencesBetweenUnManagedAndCPPCLI.htm).

### Property Value

Side thickness type as defined in [swThickenThicknessType_e](ms-its:swconst.chm::/SOLIDWORKS.Interop.swconst~SOLIDWORKS.Interop.swconst.swThickenThicknessType_e.html)

## VBA Syntax

See [ThickenFeatureData::ThicknessSide](ms-its:sldworksapivb6.chm::/sldworks~ThickenFeatureData~ThicknessSide.html).

## Examples

See the [IThickenFeatureData](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IThickenFeatureData.html) examples.

## See Also

[IThickenFeatureData Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IThickenFeatureData.html)
[IThickenFeatureData Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IThickenFeatureData_members.html)
[IThickenFeatureData::Thickness Property](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IThickenFeatureData~Thickness.html)

## Availability

SOLIDWORKS 2001Plus FCS, Revision Number 10.0
