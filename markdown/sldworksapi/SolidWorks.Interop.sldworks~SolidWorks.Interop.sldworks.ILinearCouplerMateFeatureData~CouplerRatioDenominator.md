---
title: "CouplerRatioDenominator Property (ILinearCouplerMateFeatureData)"
project: "SOLIDWORKS API Help"
interface: "ILinearCouplerMateFeatureData"
member: "CouplerRatioDenominator"
kind: "property"
source: "sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ILinearCouplerMateFeatureData~CouplerRatioDenominator.html"
---

# CouplerRatioDenominator Property (ILinearCouplerMateFeatureData)

Gets or sets the displacement of the second mated component along its direction of motion in this linear/linear coupler mate.

## Syntax

### Visual Basic (Declaration)

```vb
Property CouplerRatioDenominator As System.Double
```

### Visual Basic (Usage)

```vb
Dim instance As ILinearCouplerMateFeatureData
Dim value As System.Double

instance.CouplerRatioDenominator = value

value = instance.CouplerRatioDenominator
```

### C#

```csharp
System.double CouplerRatioDenominator {get; set;}
```

### C++/CLI

```cpp
property System.double CouplerRatioDenominator {
   System.double get();
   void set (    System.double value);
}
```

**NOTE:** See [Differences Between Unmanaged C++ and C++/CLI Code](DifferencesBetweenUnManagedAndCPPCLI.htm).

### Property Value

Coupler ratio denominator

## VBA Syntax

See [LinearCouplerMateFeatureData::CouplerRatioDenominator](ms-its:sldworksapivb6.chm::/sldworks~LinearCouplerMateFeatureData~CouplerRatioDenominator.html).

## Examples

See the [ILinearCouplerMateFeatureData](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ILinearCouplerMateFeatureData.html) examples.

## Remarks

ILinearCouplerMateFeatureData::CouplerRatioNumerator / ILinearCouplerMateFeatureData::CouplerRatioDenominator describes the ratio of displacement between the first and second mated components.

## See Also

[ILinearCouplerMateFeatureData Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ILinearCouplerMateFeatureData.html)
[ILinearCouplerMateFeatureData Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ILinearCouplerMateFeatureData_members.html)

## Availability

SOLIDWORKS 2018 FCS, Revision Number 26.0
