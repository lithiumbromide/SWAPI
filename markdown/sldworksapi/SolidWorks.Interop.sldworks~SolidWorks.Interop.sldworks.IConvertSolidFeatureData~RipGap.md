---
title: "RipGap Property (IConvertSolidFeatureData)"
project: "SOLIDWORKS API Help"
interface: "IConvertSolidFeatureData"
member: "RipGap"
kind: "property"
source: "sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IConvertSolidFeatureData~RipGap.html"
---

# RipGap Property (IConvertSolidFeatureData)

Gets or sets the default gap for all rips in this convert solid feature.

## Syntax

### Visual Basic (Declaration)

```vb
Property RipGap As System.Double
```

### Visual Basic (Usage)

```vb
Dim instance As IConvertSolidFeatureData
Dim value As System.Double

instance.RipGap = value

value = instance.RipGap
```

### C#

```csharp
System.double RipGap {get; set;}
```

### C++/CLI

```cpp
property System.double RipGap {
   System.double get();
   void set (    System.double value);
}
```

NOTE:

See

[Differences Between Unmanaged C++ and C++/CLI Code](DifferencesBetweenUnManagedAndCPPCLI.htm)

.

### Property Value

Rip gap

## VBA Syntax

See

[ConvertSolidFeatureData::RipGap](ms-its:sldworksapivb6.chm::/sldworks~ConvertSolidFeatureData~RipGap.html)

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
