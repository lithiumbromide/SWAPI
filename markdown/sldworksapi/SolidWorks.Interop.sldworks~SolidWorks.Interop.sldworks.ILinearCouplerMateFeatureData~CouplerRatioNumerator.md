---
title: "CouplerRatioNumerator Property (ILinearCouplerMateFeatureData)"
project: "SOLIDWORKS API Help"
interface: "ILinearCouplerMateFeatureData"
member: "CouplerRatioNumerator"
kind: "property"
source: "sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ILinearCouplerMateFeatureData~CouplerRatioNumerator.html"
---

# CouplerRatioNumerator Property (ILinearCouplerMateFeatureData)

Gets or sets the displacement of the first mated component along its direction of motion in this linear/linear coupler mate.

## Syntax

### Visual Basic (Declaration)

```vb
Property CouplerRatioNumerator As System.Double
```

### Visual Basic (Usage)

```vb
Dim instance As ILinearCouplerMateFeatureData
Dim value As System.Double

instance.CouplerRatioNumerator = value

value = instance.CouplerRatioNumerator
```

### C#

```csharp
System.double CouplerRatioNumerator {get; set;}
```

### C++/CLI

```cpp
property System.double CouplerRatioNumerator {
   System.double get();
   void set (    System.double value);
}
```

**NOTE:** See [Differences Between Unmanaged C++ and C++/CLI Code](DifferencesBetweenUnManagedAndCPPCLI.htm).

### Property Value

Coupler ratio numerator

## VBA Syntax

See [LinearCouplerMateFeatureData::CouplerRatioNumerator](ms-its:sldworksapivb6.chm::/sldworks~LinearCouplerMateFeatureData~CouplerRatioNumerator.html).

## Examples

See the [ILinearCouplerMateFeatureData](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ILinearCouplerMateFeatureData.html) examples.

## See Also

[ILinearCouplerMateFeatureData Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ILinearCouplerMateFeatureData.html)
[ILinearCouplerMateFeatureData Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ILinearCouplerMateFeatureData_members.html)

## Availability

SOLIDWORKS 2018 FCS, Revision Number 26.0
