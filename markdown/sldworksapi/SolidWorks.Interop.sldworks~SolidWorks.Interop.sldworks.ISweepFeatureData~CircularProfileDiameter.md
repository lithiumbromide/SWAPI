---
title: "CircularProfileDiameter Property (ISweepFeatureData)"
project: "SOLIDWORKS API Help"
interface: "ISweepFeatureData"
member: "CircularProfileDiameter"
kind: "property"
source: "sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISweepFeatureData~CircularProfileDiameter.html"
---

# CircularProfileDiameter Property (ISweepFeatureData)

Gets or sets the diameter of the circular profile for this sweep feature.

## Syntax

### Visual Basic (Declaration)

```vb
Property CircularProfileDiameter As System.Double
```

### Visual Basic (Usage)

```vb
Dim instance As ISweepFeatureData
Dim value As System.Double

instance.CircularProfileDiameter = value

value = instance.CircularProfileDiameter
```

### C#

```csharp
System.double CircularProfileDiameter {get; set;}
```

### C++/CLI

```cpp
property System.double CircularProfileDiameter {
   System.double get();
   void set (    System.double value);
}
```

**NOTE:** See [Differences Between Unmanaged C++ and C++/CLI Code](DifferencesBetweenUnManagedAndCPPCLI.htm).

### Property Value

Diameter of the circular profile

## VBA Syntax

See [SweepFeatureData::CircularProfileDiameter](ms-its:sldworksapivb6.chm::/sldworks~SweepFeatureData~CircularProfileDiameter.html).

## Examples

See the [ISweepFeatureData](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISweepFeatureData.html) examples.

## Remarks

This property is valid only if [ISweepFeatureData::CircularProfile](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISweepFeatureData~CircularProfile.html) is set to true.

## See Also

[ISweepFeatureData Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISweepFeatureData.html)
[ISweepFeatureData Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISweepFeatureData_members.html)

## Availability

SOLIDWORKS 2017 FCS, Revision Number 25.0
