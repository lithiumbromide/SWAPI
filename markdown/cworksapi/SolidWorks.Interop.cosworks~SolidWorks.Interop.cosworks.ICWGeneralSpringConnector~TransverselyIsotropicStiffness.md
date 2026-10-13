---
title: "TransverselyIsotropicStiffness Property (ICWGeneralSpringConnector)"
project: "SOLIDWORKS Simulation API Help"
interface: "ICWGeneralSpringConnector"
member: "TransverselyIsotropicStiffness"
kind: "property"
source: "cworksapi/SolidWorks.Interop.cosworks~SolidWorks.Interop.cosworks.ICWGeneralSpringConnector~TransverselyIsotropicStiffness.html"
---

# TransverselyIsotropicStiffness Property (ICWGeneralSpringConnector)

Gets or sets whether to specify isotropic spring stiffness parameters.

## Syntax

### Visual Basic (Declaration)

```vb
Property TransverselyIsotropicStiffness As System.Boolean
```

### Visual Basic (Usage)

```vb
Dim instance As ICWGeneralSpringConnector
Dim value As System.Boolean

instance.TransverselyIsotropicStiffness = value

value = instance.TransverselyIsotropicStiffness
```

### C#

```csharp
System.bool TransverselyIsotropicStiffness {get; set;}
```

### C++/CLI

```cpp
property System.bool TransverselyIsotropicStiffness {
   System.bool get();
   void set (    System.bool value);
}
```

### Property Value

True enables four isotropic spring stiffness parameters, false enables six general spring stiffness parameters

## VBA Syntax

See [CWGeneralSpringConnector::TransverselyIsotropicStiffness](ms-its:cworksapivb6.chm::/CosmosWorksLib~CWGeneralSpringConnector~TransverselyIsotropicStiffness.html).

## Examples

See the [ICWGeneralSpringConnector](SolidWorks.Interop.cosworks~SolidWorks.Interop.cosworks.ICWGeneralSpringConnector.html) examples.

## Remarks

If this property is set to...

- False, then at least one of these stiffness properties must be non-zero:

  - [ICWGeneralSpringConnector::AxialStiffnessValue](SolidWorks.Interop.cosworks~SolidWorks.Interop.cosworks.ICWGeneralSpringConnector~AxialStiffnessValue.html)
  - [ICWGeneralSpringConnector::BendingStiffnessYValue](SolidWorks.Interop.cosworks~SolidWorks.Interop.cosworks.ICWGeneralSpringConnector~BendingStiffnessYValue.html)
  - [ICWGeneralSpringConnector::BendingStiffnessZValue](SolidWorks.Interop.cosworks~SolidWorks.Interop.cosworks.ICWGeneralSpringConnector~BendingStiffnessZValue.html)
  - [ICWGeneralSpringConnector::LateralStiffnessYValue](SolidWorks.Interop.cosworks~SolidWorks.Interop.cosworks.ICWGeneralSpringConnector~LateralStiffnessYValue.html)
  - [ICWGeneralSpringConnector::LateralStiffnessZValue](SolidWorks.Interop.cosworks~SolidWorks.Interop.cosworks.ICWGeneralSpringConnector~LateralStiffnessZValue.html)
  - [ICWGeneralSpringConnector::TorsionalStiffnessValue](SolidWorks.Interop.cosworks~SolidWorks.Interop.cosworks.ICWGeneralSpringConnector~TorsionalStiffnessValue.html)
- True, then setting these properties is not valid:

  - ICWGeneralSpringConnector::LateralStiffnessYValue
  - ICWGeneralSpringConnector::BendingStiffnessZValue

## See Also

[ICWGeneralSpringConnector Interface](SolidWorks.Interop.cosworks~SolidWorks.Interop.cosworks.ICWGeneralSpringConnector.html)
[ICWGeneralSpringConnector Members](SolidWorks.Interop.cosworks~SolidWorks.Interop.cosworks.ICWGeneralSpringConnector_members.html)

## Availability

SOLIDWORKS Simulation API 2025 SP0
