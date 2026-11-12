---
title: "SNCurveSpecificConstantBUnit Property (ICWMaterial)"
project: "SOLIDWORKS Simulation API Help"
interface: "ICWMaterial"
member: "SNCurveSpecificConstantBUnit"
kind: "property"
source: "cworksapi/SolidWorks.Interop.cosworks~SolidWorks.Interop.cosworks.ICWMaterial~SNCurveSpecificConstantBUnit.html"
---

# SNCurveSpecificConstantBUnit Property (ICWMaterial)

Gets or sets the units of the Basquin Equation constants.

## Syntax

### Visual Basic (Declaration)

```vb
Property SNCurveSpecificConstantBUnit As System.Integer
```

### Visual Basic (Usage)

```vb
Dim instance As ICWMaterial
Dim value As System.Integer

instance.SNCurveSpecificConstantBUnit = value

value = instance.SNCurveSpecificConstantBUnit
```

### C#

```csharp
System.int SNCurveSpecificConstantBUnit {get; set;}
```

### C++/CLI

```cpp
property System.int SNCurveSpecificConstantBUnit {
   System.int get();
   void set (    System.int value);
}
```

### Property Value

Units of the Basquin Equation constants as defined in [swsPressureUnit_e](SolidWorks.Interop.cosworks~SolidWorks.Interop.cosworks.swsPressureUnit_e.html)

## VBA Syntax

See [CWMaterial::SNCurveSpecificConstantBUnit](ms-its:cworksapivb6.chm::/CosmosWorksLib~CWMaterial~SNCurveSpecificConstantBUnit.html).

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

## Availability

SOLIDWORKS Simulation API 2015 SP3
