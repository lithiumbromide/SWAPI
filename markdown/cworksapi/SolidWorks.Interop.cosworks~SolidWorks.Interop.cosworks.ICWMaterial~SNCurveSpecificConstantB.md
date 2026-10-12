---
title: "SNCurveSpecificConstantB Property (ICWMaterial)"
project: "SOLIDWORKS Simulation API Help"
interface: "ICWMaterial"
member: "SNCurveSpecificConstantB"
kind: "property"
source: "cworksapi/SolidWorks.Interop.cosworks~SolidWorks.Interop.cosworks.ICWMaterial~SNCurveSpecificConstantB.html"
---

# SNCurveSpecificConstantB Property (ICWMaterial)

Gets or sets the B constant of the Basquin Equation.

## Syntax

### Visual Basic (Declaration)

```vb
Property SNCurveSpecificConstantB As System.Double
```

### Visual Basic (Usage)

```vb
Dim instance As ICWMaterial
Dim value As System.Double

instance.SNCurveSpecificConstantB = value

value = instance.SNCurveSpecificConstantB
```

### C#

```csharp
System.double SNCurveSpecificConstantB {get; set;}
```

### C++/CLI

```cpp
property System.double SNCurveSpecificConstantB {
   System.double get();
   void set (    System.double value);
}
```

### Property Value

B constant of Basquin Equation (see **Remarks**)

## VBA Syntax

See [CWMaterial::SNCurveSpecificConstantB](ms-its:cworksapivb6.chm::/CosmosWorksLib~CWMaterial~SNCurveSpecificConstantB.html).

## Examples

[Create Fatigue Study for Dynamic Random Vibration Study (VBA)](Create_Fatigue_Study_for_Dynamic_Random_Vibration_Study_Example_VB.htm)
[Create Fatigue Study for Dynamic Random Vibration Study (VB.NET)](Create_Fatigue_Study_for_Dynamic_Random_Vibration_Study_Example_VBNET.htm)
[Create Fatigue Study for Dynamic Random Vibration Study (C#)](Create_Fatigue_Study_for_Dynamic_Random_Vibration_Study_Example_CSharp.htm)

## Remarks

The B constant of the Basquin Equation is the positive real value of the stress range for one cycle.

This property is valid only:

- for fatigue studies that are based on results from linear dynamic random vibration studies.
- if [ICWMaterial::SNCurveSource](SolidWorks.Interop.cosworks~SolidWorks.Interop.cosworks.ICWMaterial~SNCurveSource.html) is set to [swsMaterialSNCurveSource_e](SolidWorks.Interop.cosworks~SolidWorks.Interop.cosworks.swsMaterialSNCurveSource_e.html).swsMaterialSNCurveSourceEquation, and [ICWMaterial::SNCurveEstimateConstants](SolidWorks.Interop.cosworks~SolidWorks.Interop.cosworks.ICWMaterial~SNCurveEstimateConstants.html) is set to 0.

See the SOLIDWORKS Help topic, **Material Dialog Box - Fatigue SN Curves Tab**, for more information about Basquin Equations.

## See Also

[ICWMaterial Interface](SolidWorks.Interop.cosworks~SolidWorks.Interop.cosworks.ICWMaterial.html)
[ICWMaterial Members](SolidWorks.Interop.cosworks~SolidWorks.Interop.cosworks.ICWMaterial_members.html)
[ICWMaterial::SNCurveEstimateCutoff Property ()](SolidWorks.Interop.cosworks~SolidWorks.Interop.cosworks.ICWMaterial~SNCurveEstimateCutoff.html)
[ICWMaterial::SNCurveSlopeM Property ()](SolidWorks.Interop.cosworks~SolidWorks.Interop.cosworks.ICWMaterial~SNCurveSlopeM.html)
[ICWMaterial::SNCurveSpecificConstantBUnit Property ()](SolidWorks.Interop.cosworks~SolidWorks.Interop.cosworks.ICWMaterial~SNCurveSpecificConstantBUnit.html)

## Availability

SOLIDWORKS Simulation API 2015 SP3
