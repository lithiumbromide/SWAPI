---
title: "Spacing Property (ICircularPatternFeatureData)"
project: "SOLIDWORKS API Help"
interface: "ICircularPatternFeatureData"
member: "Spacing"
kind: "property"
source: "sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ICircularPatternFeatureData~Spacing.html"
---

# Spacing Property (ICircularPatternFeatureData)

Gets or sets the spacing between pattern instances in Direction 1 of the circular pattern feature.

## Syntax

### Visual Basic (Declaration)

```vb
Property Spacing As System.Double
```

### Visual Basic (Usage)

```vb
Dim instance As ICircularPatternFeatureData
Dim value As System.Double

instance.Spacing = value

value = instance.Spacing
```

### C#

```csharp
System.double Spacing {get; set;}
```

### C++/CLI

```cpp
property System.double Spacing {
   System.double get();
   void set (    System.double value);
}
```

**NOTE:** See [Differences Between Unmanaged C++ and C++/CLI Code](DifferencesBetweenUnManagedAndCPPCLI.htm).

### Property Value

Distance in radians between pattern instances in Direction 1

## VBA Syntax

See [CircularPatternFeatureData::Spacing](ms-its:sldworksapivb6.chm::/sldworks~CircularPatternFeatureData~Spacing.html).

## Remarks

See [Accessing Selections that Define Features](sldworksAPIProgGuide.chm::/Miscellaneous/Accessing_Selections_that_Define_Features.htm) for additional details on using this property.

## See Also

[ICircularPatternFeatureData Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ICircularPatternFeatureData.html)
[ICircularPatternFeatureData Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ICircularPatternFeatureData_members.html)
[ICircularPatternFeatureData::EqualSpacing Property](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ICircularPatternFeatureData~EqualSpacing.html)
[ICircularPatternFeatureData::TotalInstances Property](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ICircularPatternFeatureData~TotalInstances.html)
[ICircularPatternFeatureData::Spacing2 Property](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ICircularPatternFeatureData~Spacing2.html)
[ICircularPatternFeatureData::InstancesToVary Property ()](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ICircularPatternFeatureData~InstancesToVary.html)

## Availability

SOLIDWORKS 2001 FCS, Revision Number 9.0
