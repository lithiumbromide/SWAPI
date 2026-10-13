---
title: "AxialStiffnessValue Property (ICWGeneralSpringConnector)"
project: "SOLIDWORKS Simulation API Help"
interface: "ICWGeneralSpringConnector"
member: "AxialStiffnessValue"
kind: "property"
source: "cworksapi/SolidWorks.Interop.cosworks~SolidWorks.Interop.cosworks.ICWGeneralSpringConnector~AxialStiffnessValue.html"
---

# AxialStiffnessValue Property (ICWGeneralSpringConnector)

Gets or sets the axial stiffness value.

## Syntax

### Visual Basic (Declaration)

```vb
Property AxialStiffnessValue As System.Double
```

### Visual Basic (Usage)

```vb
Dim instance As ICWGeneralSpringConnector
Dim value As System.Double

instance.AxialStiffnessValue = value

value = instance.AxialStiffnessValue
```

### C#

```csharp
System.double AxialStiffnessValue {get; set;}
```

### C++/CLI

```cpp
property System.double AxialStiffnessValue {
   System.double get();
   void set (    System.double value);
}
```

### Property Value

Axial stiffness value in force/distance

## VBA Syntax

See [CWGeneralSpringConnector::AxialStiffnessValue](ms-its:cworksapivb6.chm::/CosmosWorksLib~CWGeneralSpringConnector~AxialStiffnessValue.html).

## Examples

See the [ICWGeneralSpringConnector](SolidWorks.Interop.cosworks~SolidWorks.Interop.cosworks.ICWGeneralSpringConnector.html) examples.

## Remarks

Specify the units of this property with [ICWGeneralSpringConnector::Unit](SolidWorks.Interop.cosworks~SolidWorks.Interop.cosworks.ICWGeneralSpringConnector~Unit.html).

If only this property or [ICWGeneralSpringConnector::TorsionalStiffnessValue](SolidWorks.Interop.cosworks~SolidWorks.Interop.cosworks.ICWGeneralSpringConnector~TorsionalStiffnessValue.html) are non-zero, then calling [ICWGeneralSpringConnector::SetReferenceCoordinateSystem](SolidWorks.Interop.cosworks~SolidWorks.Interop.cosworks.ICWGeneralSpringConnector~SetReferenceCoordinateSystem.html) is not necessary.

## See Also

[ICWGeneralSpringConnector Interface](SolidWorks.Interop.cosworks~SolidWorks.Interop.cosworks.ICWGeneralSpringConnector.html)
[ICWGeneralSpringConnector Members](SolidWorks.Interop.cosworks~SolidWorks.Interop.cosworks.ICWGeneralSpringConnector_members.html)

## Availability

SOLIDWORKS Simulation API 2025 SP0
