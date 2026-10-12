---
title: "SNCurveEstimateConstants Property (ICWMaterial)"
project: "SOLIDWORKS Simulation API Help"
interface: "ICWMaterial"
member: "SNCurveEstimateConstants"
kind: "property"
source: "cworksapi/SolidWorks.Interop.cosworks~SolidWorks.Interop.cosworks.ICWMaterial~SNCurveEstimateConstants.html"
---

# SNCurveEstimateConstants Property (ICWMaterial)

Gets or sets whether to specify the Basquin Equation constants, B and slope (m), or let the program calculate them from the S-N curve.

## Syntax

### Visual Basic (Declaration)

```vb
Property SNCurveEstimateConstants As System.Integer
```

### Visual Basic (Usage)

```vb
Dim instance As ICWMaterial
Dim value As System.Integer

instance.SNCurveEstimateConstants = value

value = instance.SNCurveEstimateConstants
```

### C#

```csharp
System.int SNCurveEstimateConstants {get; set;}
```

### C++/CLI

```cpp
property System.int SNCurveEstimateConstants {
   System.int get();
   void set (    System.int value);
}
```

### Property Value

- 0 = Specify Basquin Equation constants, B and m
- 1 = Let the program calculate the Basquin Equation constants from the S-N curve

(see **Remarks**)

## VBA Syntax

See [CWMaterial::SNCurveEstimateConstants](ms-its:cworksapivb6.chm::/CosmosWorksLib~CWMaterial~SNCurveEstimateConstants.html).

## Examples

[Create Fatigue Study for Dynamic Random Vibration Study (VBA)](Create_Fatigue_Study_for_Dynamic_Random_Vibration_Study_Example_VB.htm)
[Create Fatigue Study for Dynamic Random Vibration Study (VB.NET)](Create_Fatigue_Study_for_Dynamic_Random_Vibration_Study_Example_VBNET.htm)
[Create Fatigue Study for Dynamic Random Vibration Study (C#)](Create_Fatigue_Study_for_Dynamic_Random_Vibration_Study_Example_CSharp.htm)

## Remarks

This property is valid only:

- for fatigue studies that are based on results from linear dynamic random vibration studies.
- if [ICWMaterial::SNCurveSource](SolidWorks.Interop.cosworks~SolidWorks.Interop.cosworks.ICWMaterial~SNCurveSource.html) is set to [swsMaterialSNCurveSource_e](SolidWorks.Interop.cosworks~SolidWorks.Interop.cosworks.swsMaterialSNCurveSource_e.html).swsMaterialSNCurveSourceEquation.

| If this property is set to... | Then use... |
| --- | --- |
| 0 | ICWMaterial::SNCurveSlopeM , ICWMaterial::SNCurveSpecificConstantB , and ICWMaterial::SNCurveSpecificConstantBUnit to specify the Basquin Equation constants. |
| 1 | ICWMaterial::SNCurveEstimateCutoff to define the cut-off point used by the program to fit a straight line to the S-N curve and calculate the Basquin Equation constants. |

See the SOLIDWORKS Help topic, **Material Dialog Box - Fatigue SN Curves Tab**, for more information about Basquin Equations.

## See Also

[ICWMaterial Interface](SolidWorks.Interop.cosworks~SolidWorks.Interop.cosworks.ICWMaterial.html)
[ICWMaterial Members](SolidWorks.Interop.cosworks~SolidWorks.Interop.cosworks.ICWMaterial_members.html)

## Availability

SOLIDWORKS Simulation API 2015 SP3
