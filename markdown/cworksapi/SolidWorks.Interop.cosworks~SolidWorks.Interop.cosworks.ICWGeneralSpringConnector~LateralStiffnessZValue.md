---
title: "LateralStiffnessZValue Property (ICWGeneralSpringConnector)"
project: "SOLIDWORKS Simulation API Help"
interface: "ICWGeneralSpringConnector"
member: "LateralStiffnessZValue"
kind: "property"
source: "cworksapi/SolidWorks.Interop.cosworks~SolidWorks.Interop.cosworks.ICWGeneralSpringConnector~LateralStiffnessZValue.html"
---

# LateralStiffnessZValue Property (ICWGeneralSpringConnector)

Gets or sets the lateral stiffness Z value.

## Syntax

### Visual Basic (Declaration)

```vb
Property LateralStiffnessZValue As System.Double
```

### Visual Basic (Usage)

```vb
Dim instance As ICWGeneralSpringConnector
Dim value As System.Double

instance.LateralStiffnessZValue = value

value = instance.LateralStiffnessZValue
```

### C#

```csharp
System.double LateralStiffnessZValue {get; set;}
```

### C++/CLI

```cpp
property System.double LateralStiffnessZValue {
   System.double get();
   void set (    System.double value);
}
```

### Property Value

Lateral stiffness Z value in force/distance

## VBA Syntax

See [CWGeneralSpringConnector::LateralStiffnessZValue](ms-its:cworksapivb6.chm::/CosmosWorksLib~CWGeneralSpringConnector~LateralStiffnessZValue.html).

## Examples

See the [ICWGeneralSpringConnector](SolidWorks.Interop.cosworks~SolidWorks.Interop.cosworks.ICWGeneralSpringConnector.html) examples.

## Remarks

Specify the units of this property with [ICWGeneralSpringConnector::Unit](SolidWorks.Interop.cosworks~SolidWorks.Interop.cosworks.ICWGeneralSpringConnector~Unit.html).

## See Also

[ICWGeneralSpringConnector Interface](SolidWorks.Interop.cosworks~SolidWorks.Interop.cosworks.ICWGeneralSpringConnector.html)
[ICWGeneralSpringConnector Members](SolidWorks.Interop.cosworks~SolidWorks.Interop.cosworks.ICWGeneralSpringConnector_members.html)

## Availability

SOLIDWORKS Simulation API 2025 SP0
