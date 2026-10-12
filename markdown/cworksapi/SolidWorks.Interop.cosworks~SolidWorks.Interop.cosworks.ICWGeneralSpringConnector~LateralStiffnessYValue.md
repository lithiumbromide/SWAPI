---
title: "LateralStiffnessYValue Property (ICWGeneralSpringConnector)"
project: "SOLIDWORKS Simulation API Help"
interface: "ICWGeneralSpringConnector"
member: "LateralStiffnessYValue"
kind: "property"
source: "cworksapi/SolidWorks.Interop.cosworks~SolidWorks.Interop.cosworks.ICWGeneralSpringConnector~LateralStiffnessYValue.html"
---

# LateralStiffnessYValue Property (ICWGeneralSpringConnector)

Gets or sets the lateral stiffness Y value.

## Syntax

### Visual Basic (Declaration)

```vb
Property LateralStiffnessYValue As System.Double
```

### Visual Basic (Usage)

```vb
Dim instance As ICWGeneralSpringConnector
Dim value As System.Double

instance.LateralStiffnessYValue = value

value = instance.LateralStiffnessYValue
```

### C#

```csharp
System.double LateralStiffnessYValue {get; set;}
```

### C++/CLI

```cpp
property System.double LateralStiffnessYValue {
   System.double get();
   void set (    System.double value);
}
```

### Property Value

Lateral stiffness Y value in force/distance

## VBA Syntax

See [CWGeneralSpringConnector::LateralStiffnessYValue](ms-its:cworksapivb6.chm::/CosmosWorksLib~CWGeneralSpringConnector~LateralStiffnessYValue.html).

## Examples

See the [ICWGeneralSpringConnector](SolidWorks.Interop.cosworks~SolidWorks.Interop.cosworks.ICWGeneralSpringConnector.html) examples.

## Remarks

Specify the units of this property with [ICWGeneralSpringConnector::Unit](SolidWorks.Interop.cosworks~SolidWorks.Interop.cosworks.ICWGeneralSpringConnector~Unit.html).

## See Also

[ICWGeneralSpringConnector Interface](SolidWorks.Interop.cosworks~SolidWorks.Interop.cosworks.ICWGeneralSpringConnector.html)
[ICWGeneralSpringConnector Members](SolidWorks.Interop.cosworks~SolidWorks.Interop.cosworks.ICWGeneralSpringConnector_members.html)

## Availability

SOLIDWORKS Simulation API 2025 SP0
