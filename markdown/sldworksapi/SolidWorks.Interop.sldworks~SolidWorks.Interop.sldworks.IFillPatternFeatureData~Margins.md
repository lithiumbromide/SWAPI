---
title: "Margins Property (IFillPatternFeatureData)"
project: "SOLIDWORKS API Help"
interface: "IFillPatternFeatureData"
member: "Margins"
kind: "property"
source: "sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IFillPatternFeatureData~Margins.html"
---

# Margins Property (IFillPatternFeatureData)

Gets or sets the distance between the fill boundary and the outermost pattern instance in the layout of this fill pattern feature.

## Syntax

### Visual Basic (Declaration)

```vb
Property Margins As System.Double
```

### Visual Basic (Usage)

```vb
Dim instance As IFillPatternFeatureData
Dim value As System.Double

instance.Margins = value

value = instance.Margins
```

### C#

```csharp
System.double Margins {get; set;}
```

### C++/CLI

```cpp
property System.double Margins {
   System.double get();
   void set (    System.double value);
}
```

**NOTE:** See [Differences Between Unmanaged C++ and C++/CLI Code](DifferencesBetweenUnManagedAndCPPCLI.htm).

### Property Value

Distance between the fill boundary and the outermost pattern instance in the layout; 0 for no margin

## VBA Syntax

See [FillPatternFeatureData::Margins](ms-its:sldworksapivb6.chm::/sldworks~FillPatternFeatureData~Margins.html).

## Examples

See the [IFillPatternFeatureData](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IFillPatternFeatureData.html) example.

## See Also

[IFillPatternFeatureData Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IFillPatternFeatureData.html)
[IFillPatternFeatureData Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IFillPatternFeatureData_members.html)
[IFillPatternFeatureData::PatternLayoutType Property ()](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IFillPatternFeatureData~PatternLayoutType.html)

## Availability

SOLIDWORKS 2014 FCS, Revision Number 22.0
