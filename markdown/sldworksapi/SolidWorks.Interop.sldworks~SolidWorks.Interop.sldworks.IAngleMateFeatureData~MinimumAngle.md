---
title: "MinimumAngle Property (IAngleMateFeatureData)"
project: "SOLIDWORKS API Help"
interface: "IAngleMateFeatureData"
member: "MinimumAngle"
kind: "property"
source: "sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IAngleMateFeatureData~MinimumAngle.html"
---

# MinimumAngle Property (IAngleMateFeatureData)

Gets or sets the minimum angle of this limit angle mate.

## Syntax

### Visual Basic (Declaration)

```vb
Property MinimumAngle As System.Double
```

### Visual Basic (Usage)

```vb
Dim instance As IAngleMateFeatureData
Dim value As System.Double

instance.MinimumAngle = value

value = instance.MinimumAngle
```

### C#

```csharp
System.double MinimumAngle {get; set;}
```

### C++/CLI

```cpp
property System.double MinimumAngle {
   System.double get();
   void set (    System.double value);
}
```

**NOTE:** See [Differences Between Unmanaged C++ and C++/CLI Code](DifferencesBetweenUnManagedAndCPPCLI.htm).

### Property Value

Minimum angle in radians

## VBA Syntax

See [AngleMateFeatureData::MinimumAngle](ms-its:sldworksapivb6.chm::/sldworks~AngleMateFeatureData~MinimumAngle.html).

## Examples

See the [IAngleMateFeatureData](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IAngleMateFeatureData.html) examples.

## Remarks

This property is valid only if [IAngleMateFeatureData::IsAdvancedMate](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IAngleMateFeatureData~IsAdvancedMate.html) is set to true.

## See Also

[IAngleMateFeatureData Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IAngleMateFeatureData.html)
[IAngleMateFeatureData Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IAngleMateFeatureData_members.html)
[IAngleMateFeatureData::Angle Property ()](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IAngleMateFeatureData~Angle.html)

## Availability

SOLIDWORKS 2018 FCS, Revision Number 26.0
