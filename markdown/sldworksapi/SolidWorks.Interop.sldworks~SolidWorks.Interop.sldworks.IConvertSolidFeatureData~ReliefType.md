---
title: "ReliefType Property (IConvertSolidFeatureData)"
project: "SOLIDWORKS API Help"
interface: "IConvertSolidFeatureData"
member: "ReliefType"
kind: "property"
source: "sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IConvertSolidFeatureData~ReliefType.html"
---

# ReliefType Property (IConvertSolidFeatureData)

Gets or sets the bend relief type in this convert solid feature.

## Syntax

### Visual Basic (Declaration)

```vb
Property ReliefType As System.Integer
```

### Visual Basic (Usage)

```vb
Dim instance As IConvertSolidFeatureData
Dim value As System.Integer

instance.ReliefType = value

value = instance.ReliefType
```

### C#

```csharp
System.int ReliefType {get; set;}
```

### C++/CLI

```cpp
property System.int ReliefType {
   System.int get();
   void set (    System.int value);
}
```

NOTE:

See

[Differences Between Unmanaged C++ and C++/CLI Code](DifferencesBetweenUnManagedAndCPPCLI.htm)

.

### Property Value

Bend relief type as defined by

[swSheetMetalAutoReliefTypes_e](ms-its:swconst.chm::/SOLIDWORKS.Interop.swconst~SOLIDWORKS.Interop.swconst.swSheetMetalAutoReliefTypes_e.html)

## VBA Syntax

See

[ConvertSolidFeatureData::ReliefType](ms-its:sldworksapivb6.chm::/sldworks~ConvertSolidFeatureData~ReliefType.html)

.

## Examples

See the

[IConvertSolidFeatureData](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IConvertSolidFeatureData.html)

examples.

## Remarks

The setter of this property is valid only if[IConvertSolidFeatureData::OverrideDefaultAutoReliefParameters](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IConvertSolidFeatureData~OverrideDefaultAutoReliefParameters.html)is true.

## See Also

[IConvertSolidFeatureData Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IConvertSolidFeatureData.html)

[IConvertSolidFeatureData Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IConvertSolidFeatureData_members.html)

## Availability

SOLIDWORKS 2025 SP02, Revision Number 33.2
