---
title: "MaximumDeviation Property (ILoftedBendsFeatureData)"
project: "SOLIDWORKS API Help"
interface: "ILoftedBendsFeatureData"
member: "MaximumDeviation"
kind: "property"
source: "sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ILoftedBendsFeatureData~MaximumDeviation.html"
---

# MaximumDeviation Property (ILoftedBendsFeatureData)

Gets or sets the maximum deviation for the bend lines in a lofted bend feature.

## Syntax

### Visual Basic (Declaration)

```vb
Property MaximumDeviation As System.Double
```

### Visual Basic (Usage)

```vb
Dim instance As ILoftedBendsFeatureData
Dim value As System.Double

instance.MaximumDeviation = value

value = instance.MaximumDeviation
```

### C#

```csharp
System.double MaximumDeviation {get; set;}
```

### C++/CLI

```cpp
property System.double MaximumDeviation {
   System.double get();
   void set (    System.double value);
}
```

**NOTE:** See [Differences Between Unmanaged C++ and C++/CLI Code](DifferencesBetweenUnManagedAndCPPCLI.htm).

### Property Value

Maximum deviation for the bend lines in a lofted bend feature

## VBA Syntax

See [LoftedBendsFeatureData::MaximumDeviation](ms-its:sldworksapivb6.chm::/sldworks~LoftedBendsFeatureData~MaximumDeviation.html).

## See Also

[ILoftedBendsFeatureData Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ILoftedBendsFeatureData.html)
[ILoftedBendsFeatureData Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ILoftedBendsFeatureData_members.html)
[ILoftedBendsFeatureData::CanCreateBendLines Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ILoftedBendsFeatureData~CanCreateBendLines.html)
[ILoftedBendsFeatureData::BendLineControlOption Property](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ILoftedBendsFeatureData~BendLineControlOption.html)
[ILoftedBendsFeatureData::NumberOfBendLines Property](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ILoftedBendsFeatureData~NumberOfBendLines.html)
