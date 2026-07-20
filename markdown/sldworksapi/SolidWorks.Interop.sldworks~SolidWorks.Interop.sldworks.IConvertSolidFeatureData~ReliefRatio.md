---
title: "ReliefRatio Property (IConvertSolidFeatureData)"
project: "SOLIDWORKS API Help"
interface: "IConvertSolidFeatureData"
member: "ReliefRatio"
kind: "property"
source: "sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IConvertSolidFeatureData~ReliefRatio.html"
---

# ReliefRatio Property (IConvertSolidFeatureData)

Gets or sets the bend relief ratio for this convert solid feature.

## Syntax

### Visual Basic (Declaration)

```vb
Property ReliefRatio As System.Double
```

### Visual Basic (Usage)

```vb
Dim instance As IConvertSolidFeatureData
Dim value As System.Double

instance.ReliefRatio = value

value = instance.ReliefRatio
```

### C#

```csharp
System.double ReliefRatio {get; set;}
```

### C++/CLI

```cpp
property System.double ReliefRatio {
   System.double get();
   void set (    System.double value);
}
```

NOTE:

See

[Differences Between Unmanaged C++ and C++/CLI Code](DifferencesBetweenUnManagedAndCPPCLI.htm)

.

### Property Value

0.05 <= Relief ratio <= 2.0

## VBA Syntax

See

[ConvertSolidFeatureData::ReliefRatio](ms-its:sldworksapivb6.chm::/sldworks~ConvertSolidFeatureData~ReliefRatio.html)

.

## Examples

See the

[IConvertSolidFeatureData](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IConvertSolidFeatureData.html)

examples.

## Remarks

The setter of this property is valid only if:

[IConvertSolidFeatureData::OverrideDefaultAutoReliefParameters](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IConvertSolidFeatureData~OverrideDefaultAutoReliefParameters.html)is true

- and -

ReliefType is Rectangular or Obround.

Relief ratio = d / part thickness,

where:

d = the width of the relief cut and the depth by which it extends past the bend region

## See Also

[IConvertSolidFeatureData Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IConvertSolidFeatureData.html)

[IConvertSolidFeatureData Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IConvertSolidFeatureData_members.html)

## Availability

SOLIDWORKS 2025 SP02, Revision Number 33.2
