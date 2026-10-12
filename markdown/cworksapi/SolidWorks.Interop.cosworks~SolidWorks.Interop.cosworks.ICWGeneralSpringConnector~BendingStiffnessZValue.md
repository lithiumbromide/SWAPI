---
title: "BendingStiffnessZValue Property (ICWGeneralSpringConnector)"
project: "SOLIDWORKS Simulation API Help"
interface: "ICWGeneralSpringConnector"
member: "BendingStiffnessZValue"
kind: "property"
source: "cworksapi/SolidWorks.Interop.cosworks~SolidWorks.Interop.cosworks.ICWGeneralSpringConnector~BendingStiffnessZValue.html"
---

# BendingStiffnessZValue Property (ICWGeneralSpringConnector)

Gets or sets the bending stiffness Z value.

## Syntax

### Visual Basic (Declaration)

```vb
Property BendingStiffnessZValue As System.Double
```

### Visual Basic (Usage)

```vb
Dim instance As ICWGeneralSpringConnector
Dim value As System.Double

instance.BendingStiffnessZValue = value

value = instance.BendingStiffnessZValue
```

### C#

```csharp
System.double BendingStiffnessZValue {get; set;}
```

### C++/CLI

```cpp
property System.double BendingStiffnessZValue {
   System.double get();
   void set (    System.double value);
}
```

### Property Value

Bending stiffness Z value in force-distance/angle

## VBA Syntax

See [CWGeneralSpringConnector::BendingStiffnessZValue](ms-its:cworksapivb6.chm::/CosmosWorksLib~CWGeneralSpringConnector~BendingStiffnessZValue.html).

## Examples

See the [ICWGeneralSpringConnector](SolidWorks.Interop.cosworks~SolidWorks.Interop.cosworks.ICWGeneralSpringConnector.html) examples.

## Remarks

Specify the units of this property with [ICWGeneralSpringConnector::Unit](SolidWorks.Interop.cosworks~SolidWorks.Interop.cosworks.ICWGeneralSpringConnector~Unit.html).

## See Also

[ICWGeneralSpringConnector Interface](SolidWorks.Interop.cosworks~SolidWorks.Interop.cosworks.ICWGeneralSpringConnector.html)
[ICWGeneralSpringConnector Members](SolidWorks.Interop.cosworks~SolidWorks.Interop.cosworks.ICWGeneralSpringConnector_members.html)

## Availability

SOLIDWORKS Simulation API 2025 SP0
