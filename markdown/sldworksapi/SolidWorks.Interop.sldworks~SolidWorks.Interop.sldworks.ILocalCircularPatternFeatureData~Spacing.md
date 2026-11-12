---
title: "Spacing Property (ILocalCircularPatternFeatureData)"
project: "SOLIDWORKS API Help"
interface: "ILocalCircularPatternFeatureData"
member: "Spacing"
kind: "property"
source: "sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ILocalCircularPatternFeatureData~Spacing.html"
---

# Spacing Property (ILocalCircularPatternFeatureData)

Gets or sets the distance between pattern instances in Direction 1 for this circular component pattern feature.

## Syntax

### Visual Basic (Declaration)

```vb
Property Spacing As System.Double
```

### Visual Basic (Usage)

```vb
Dim instance As ILocalCircularPatternFeatureData
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

See [LocalCircularPatternFeatureData::Spacing](ms-its:sldworksapivb6.chm::/sldworks~LocalCircularPatternFeatureData~Spacing.html).

## Remarks

This property is automatically set to 360 if [ILocalCircularPatternFeatureData::EqualSpacing](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ILocalCircularPatternFeatureData~EqualSpacing.html) is set to true.

## See Also

[ILocalCircularPatternFeatureData Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ILocalCircularPatternFeatureData.html)
[ILocalCircularPatternFeatureData Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ILocalCircularPatternFeatureData_members.html)
[ILocalCircularPatternFeatureData::TotalInstances Property](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ILocalCircularPatternFeatureData~TotalInstances.html)
[ILocalCircularPatternFeatureData::Spacing2 Property ()](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ILocalCircularPatternFeatureData~Spacing2.html)

## Availability

SOLIDWORKS 2001 SP2, Revision Number 9.2
