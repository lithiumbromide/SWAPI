---
title: "TorsionalStiffnessValue Property (ICWGeneralSpringConnector)"
project: "SOLIDWORKS Simulation API Help"
interface: "ICWGeneralSpringConnector"
member: "TorsionalStiffnessValue"
kind: "property"
source: "cworksapi/SolidWorks.Interop.cosworks~SolidWorks.Interop.cosworks.ICWGeneralSpringConnector~TorsionalStiffnessValue.html"
---

# TorsionalStiffnessValue Property (ICWGeneralSpringConnector)

Gets or sets the torsional stiffness value.

## Syntax

### Visual Basic (Declaration)

```vb
Property TorsionalStiffnessValue As System.Double
```

### Visual Basic (Usage)

```vb
Dim instance As ICWGeneralSpringConnector
Dim value As System.Double

instance.TorsionalStiffnessValue = value

value = instance.TorsionalStiffnessValue
```

### C#

```csharp
System.double TorsionalStiffnessValue {get; set;}
```

### C++/CLI

```cpp
property System.double TorsionalStiffnessValue {
   System.double get();
   void set (    System.double value);
}
```

### Property Value

Torsional stiffness value in force-distance/angle

## VBA Syntax

See [CWGeneralSpringConnector::TorsionalStiffnessValue](ms-its:cworksapivb6.chm::/CosmosWorksLib~CWGeneralSpringConnector~TorsionalStiffnessValue.html).

## Examples

See the [ICWGeneralSpringConnector](SolidWorks.Interop.cosworks~SolidWorks.Interop.cosworks.ICWGeneralSpringConnector.html) examples.

## Remarks

Specify the units of this property with [ICWGeneralSpringConnector::Unit](SolidWorks.Interop.cosworks~SolidWorks.Interop.cosworks.ICWGeneralSpringConnector~Unit.html).

If only this property or [ICWGeneralSpringConnector::AxialStiffnessValue](SolidWorks.Interop.cosworks~SolidWorks.Interop.cosworks.ICWGeneralSpringConnector~AxialStiffnessValue.html) are non-zero, then calling [ICWGeneralSpringConnector::SetReferenceCoordinateSystem](SolidWorks.Interop.cosworks~SolidWorks.Interop.cosworks.ICWGeneralSpringConnector~SetReferenceCoordinateSystem.html) is not necessary.

## See Also

[ICWGeneralSpringConnector Interface](SolidWorks.Interop.cosworks~SolidWorks.Interop.cosworks.ICWGeneralSpringConnector.html)
[ICWGeneralSpringConnector Members](SolidWorks.Interop.cosworks~SolidWorks.Interop.cosworks.ICWGeneralSpringConnector_members.html)

## Availability

SOLIDWORKS Simulation API 2025 SP0
