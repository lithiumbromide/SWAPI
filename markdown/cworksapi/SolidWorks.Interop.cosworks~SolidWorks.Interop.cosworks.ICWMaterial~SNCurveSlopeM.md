---
title: "SNCurveSlopeM Property (ICWMaterial)"
project: "SOLIDWORKS Simulation API Help"
interface: "ICWMaterial"
member: "SNCurveSlopeM"
kind: "property"
source: "cworksapi/SolidWorks.Interop.cosworks~SolidWorks.Interop.cosworks.ICWMaterial~SNCurveSlopeM.html"
---

# SNCurveSlopeM Property (ICWMaterial)

Gets or sets the slope (m) of the S-N curve.

## Syntax

### Visual Basic (Declaration)

```vb
Property SNCurveSlopeM As System.Double
```

### Visual Basic (Usage)

```vb
Dim instance As ICWMaterial
Dim value As System.Double

instance.SNCurveSlopeM = value

value = instance.SNCurveSlopeM
```

### C#

```csharp
System.double SNCurveSlopeM {get; set;}
```

### C++/CLI

```cpp
property System.double SNCurveSlopeM {
   System.double get();
   void set (    System.double value);
}
```

### Property Value

0.0 < slope (m) of the S-N curve

## VBA Syntax

See [CWMaterial::SNCurveSlopeM](ms-its:cworksapivb6.chm::/CosmosWorksLib~CWMaterial~SNCurveSlopeM.html).

## Examples

[Create Fatigue Study for Dynamic Random Vibration Study (VBA)](Create_Fatigue_Study_for_Dynamic_Random_Vibration_Study_Example_VB.htm)
[Create Fatigue Study for Dynamic Random Vibration Study (VB.NET)](Create_Fatigue_Study_for_Dynamic_Random_Vibration_Study_Example_VBNET.htm)
[Create Fatigue Study for Dynamic Random Vibration Study (C#)](Create_Fatigue_Study_for_Dynamic_Random_Vibration_Study_Example_CSharp.htm)

## Remarks

This property is valid only:

- for fatigue studies that are based on results from linear dynamic random vibration studies.
- if [ICWMaterial::SNCurveSource](SolidWorks.Interop.cosworks~SolidWorks.Interop.cosworks.ICWMaterial~SNCurveSource.html) is set to [swsMaterialSNCurveSource_e](SolidWorks.Interop.cosworks~SolidWorks.Interop.cosworks.swsMaterialSNCurveSource_e.html).swsMaterialSNCurveSourceEquation, and [ICWMaterial::SNCurveEstimateConstants](SolidWorks.Interop.cosworks~SolidWorks.Interop.cosworks.ICWMaterial~SNCurveEstimateConstants.html) is set to 0.

See the SOLIDWORKS Help topic, **Material Dialog Box - Fatigue SN Curves Tab**, for more information about Basquin Equations.

## See Also

[ICWMaterial Interface](SolidWorks.Interop.cosworks~SolidWorks.Interop.cosworks.ICWMaterial.html)
[ICWMaterial Members](SolidWorks.Interop.cosworks~SolidWorks.Interop.cosworks.ICWMaterial_members.html)
[ICWMaterial::SNCurveSpecificConstantB Property ()](SolidWorks.Interop.cosworks~SolidWorks.Interop.cosworks.ICWMaterial~SNCurveSpecificConstantB.html)
[ICWMaterial::SNCurveSpecificConstantBUnit Property ()](SolidWorks.Interop.cosworks~SolidWorks.Interop.cosworks.ICWMaterial~SNCurveSpecificConstantBUnit.html)
[ICWMaterial::SNCurveEstimateCutoff Property ()](SolidWorks.Interop.cosworks~SolidWorks.Interop.cosworks.ICWMaterial~SNCurveEstimateCutoff.html)

## Availability

SOLIDWORKS Simulation API 2015 SP3
