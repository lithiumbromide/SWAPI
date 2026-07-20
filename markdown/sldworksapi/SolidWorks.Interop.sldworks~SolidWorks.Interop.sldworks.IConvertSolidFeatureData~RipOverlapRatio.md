---
title: "RipOverlapRatio Property (IConvertSolidFeatureData)"
project: "SOLIDWORKS API Help"
interface: "IConvertSolidFeatureData"
member: "RipOverlapRatio"
kind: "property"
source: "sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IConvertSolidFeatureData~RipOverlapRatio.html"
---

# RipOverlapRatio Property (IConvertSolidFeatureData)

Gets or sets the default ratio for all overlap and underlap rips in this convert solid feature.

## Syntax

### Visual Basic (Declaration)

```vb
Property RipOverlapRatio As System.Double
```

### Visual Basic (Usage)

```vb
Dim instance As IConvertSolidFeatureData
Dim value As System.Double

instance.RipOverlapRatio = value

value = instance.RipOverlapRatio
```

### C#

```csharp
System.double RipOverlapRatio {get; set;}
```

### C++/CLI

```cpp
property System.double RipOverlapRatio {
   System.double get();
   void set (    System.double value);
}
```

NOTE:

See

[Differences Between Unmanaged C++ and C++/CLI Code](DifferencesBetweenUnManagedAndCPPCLI.htm)

.

### Property Value

Default ratio for overlap and underlap rips; 0.0 <= Rip overlap ratio <= 1.0

## VBA Syntax

See

[ConvertSolidFeatureData::RipOverlapRatio](ms-its:sldworksapivb6.chm::/sldworks~ConvertSolidFeatureData~RipOverlapRatio.html)

.

## Examples

See the

[IConvertSolidFeatureData](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IConvertSolidFeatureData.html)

examples.

## See Also

[IConvertSolidFeatureData Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IConvertSolidFeatureData.html)

[IConvertSolidFeatureData Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IConvertSolidFeatureData_members.html)

## Availability

SOLIDWORKS 2025 SP02, Revision Number 33.2
