---
title: "BendingStiffnessYValue Property (ICWGeneralSpringConnector)"
project: "SOLIDWORKS Simulation API Help"
interface: "ICWGeneralSpringConnector"
member: "BendingStiffnessYValue"
kind: "property"
source: "cworksapi/SolidWorks.Interop.cosworks~SolidWorks.Interop.cosworks.ICWGeneralSpringConnector~BendingStiffnessYValue.html"
---

# BendingStiffnessYValue Property (ICWGeneralSpringConnector)

Gets or sets the bending stiffness Y value.

## Syntax

### Visual Basic (Declaration)

```vb
Property BendingStiffnessYValue As System.Double
```

### Visual Basic (Usage)

```vb
Dim instance As ICWGeneralSpringConnector
Dim value As System.Double

instance.BendingStiffnessYValue = value

value = instance.BendingStiffnessYValue
```

### C#

```csharp
System.double BendingStiffnessYValue {get; set;}
```

### C++/CLI

```cpp
property System.double BendingStiffnessYValue {
   System.double get();
   void set (    System.double value);
}
```

### Property Value

Bending stiffness Y value in force-distance/angle

## VBA Syntax

See [CWGeneralSpringConnector::BendingStiffnessYValue](ms-its:cworksapivb6.chm::/CosmosWorksLib~CWGenera;SpringConnector~BendingStiffnessYValue.html).

## Examples

See the [ICWGeneralSpringConnector](SolidWorks.Interop.cosworks~SolidWorks.Interop.cosworks.ICWGeneralSpringConnector.html) examples.

## Remarks

Specify the units of this property with [ICWGeneralSpringConnector::Unit](SolidWorks.Interop.cosworks~SolidWorks.Interop.cosworks.ICWGeneralSpringConnector~Unit.html).

## See Also

[ICWGeneralSpringConnector Interface](SolidWorks.Interop.cosworks~SolidWorks.Interop.cosworks.ICWGeneralSpringConnector.html)
[ICWGeneralSpringConnector Members](SolidWorks.Interop.cosworks~SolidWorks.Interop.cosworks.ICWGeneralSpringConnector_members.html)

## Availability

SOLIDWORKS Simulation API 2025 SP0
