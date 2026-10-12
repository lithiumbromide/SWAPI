---
title: "MaximumAngle Property (IAngleMateFeatureData)"
project: "SOLIDWORKS API Help"
interface: "IAngleMateFeatureData"
member: "MaximumAngle"
kind: "property"
source: "sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IAngleMateFeatureData~MaximumAngle.html"
---

# MaximumAngle Property (IAngleMateFeatureData)

Gets or sets the maximum angle of this limit angle mate.

## Syntax

### Visual Basic (Declaration)

```vb
Property MaximumAngle As System.Double
```

### Visual Basic (Usage)

```vb
Dim instance As IAngleMateFeatureData
Dim value As System.Double

instance.MaximumAngle = value

value = instance.MaximumAngle
```

### C#

```csharp
System.double MaximumAngle {get; set;}
```

### C++/CLI

```cpp
property System.double MaximumAngle {
   System.double get();
   void set (    System.double value);
}
```

**NOTE:** See [Differences Between Unmanaged C++ and C++/CLI Code](DifferencesBetweenUnManagedAndCPPCLI.htm).

### Property Value

Maximum angle in radians

## VBA Syntax

See [AngleMateFeatureData::MaximumAngle](ms-its:sldworksapivb6.chm::/sldworks~AngleMateFeatureData~MaximumAngle.html).

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
