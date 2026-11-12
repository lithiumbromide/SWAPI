---
title: "Angle Property (IAngleMateFeatureData)"
project: "SOLIDWORKS API Help"
interface: "IAngleMateFeatureData"
member: "Angle"
kind: "property"
source: "sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IAngleMateFeatureData~Angle.html"
---

# Angle Property (IAngleMateFeatureData)

Gets or sets the angle of this angle mate.

## Syntax

### Visual Basic (Declaration)

```vb
Property Angle As System.Double
```

### Visual Basic (Usage)

```vb
Dim instance As IAngleMateFeatureData
Dim value As System.Double

instance.Angle = value

value = instance.Angle
```

### C#

```csharp
System.double Angle {get; set;}
```

### C++/CLI

```cpp
property System.double Angle {
   System.double get();
   void set (    System.double value);
}
```

**NOTE:** See [Differences Between Unmanaged C++ and C++/CLI Code](DifferencesBetweenUnManagedAndCPPCLI.htm).

### Property Value

Angle in radians

## VBA Syntax

See [AngleMateFeatureData::Angle](ms-its:sldworksapivb6.chm::/sldworks~AngleMateFeatureData~Angle.html).

## Examples

See the [IAngleMateFeatureData](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IAngleMateFeatureData.html) examples.

## Remarks

If [IAngleMateFeatureData::IsAdvancedMate](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IAngleMateFeatureData~IsAdvancedMate.html) is true, then this property specifies the starting angle of this mate.

## See Also

[IAngleMateFeatureData Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IAngleMateFeatureData.html)
[IAngleMateFeatureData Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IAngleMateFeatureData_members.html)
[IAngleMateFeatureData::MinimumAngle Property ()](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IAngleMateFeatureData~MinimumAngle.html)
[IAngleMateFeatureData::MaximumAngle Property ()](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IAngleMateFeatureData~MaximumAngle.html)

## Availability

SOLIDWORKS 2018 FCS, Revision Number 26.0
