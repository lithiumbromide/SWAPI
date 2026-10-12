---
title: "SNCurveSource Property (ICWMaterial)"
project: "SOLIDWORKS Simulation API Help"
interface: "ICWMaterial"
member: "SNCurveSource"
kind: "property"
source: "cworksapi/SolidWorks.Interop.cosworks~SolidWorks.Interop.cosworks.ICWMaterial~SNCurveSource.html"
---

# SNCurveSource Property (ICWMaterial)

Gets or sets the source for the material S-N curve used in fatigue studies.

## Syntax

### Visual Basic (Declaration)

```vb
Property SNCurveSource As System.Integer
```

### Visual Basic (Usage)

```vb
Dim instance As ICWMaterial
Dim value As System.Integer

instance.SNCurveSource = value

value = instance.SNCurveSource
```

### C#

```csharp
System.int SNCurveSource {get; set;}
```

### C++/CLI

```cpp
property System.int SNCurveSource {
   System.int get();
   void set (    System.int value);
}
```

### Property Value

Source as defined in [swsMaterialSNCurveSource_e](SOLIDWORKS.Interop.cosworks~SOLIDWORKS.Interop.cosworks.swsMaterialSNCurveSource_e.html)

## VBA Syntax

See [CWMaterial::SNCurveSource](ms-its:cworksapivb6.chm::/CosmosWorksLib~CWMaterial~SNCurveSource.html).

## Examples

[Create Fatigue Study for Dynamic Random Vibration Study (VBA)](Create_Fatigue_Study_for_Dynamic_Random_Vibration_Study_Example_VB.htm)
[Create Fatigue Study for Dynamic Random Vibration Study (VB.NET)](Create_Fatigue_Study_for_Dynamic_Random_Vibration_Study_Example_VBNET.htm)
[Create Fatigue Study for Dynamic Random Vibration Study (C#)](Create_Fatigue_Study_for_Dynamic_Random_Vibration_Study_Example_CSharp.htm)

## Remarks

See the SOLIDWORKS Help topic, **Material Dialog Box - Fatigue SN Curves Tab**, for more information about S-N curve equations.

## See Also

[ICWMaterial Interface](SolidWorks.Interop.cosworks~SolidWorks.Interop.cosworks.ICWMaterial.html)
[ICWMaterial Members](SolidWorks.Interop.cosworks~SolidWorks.Interop.cosworks.ICWMaterial_members.html)
[ICWMaterial::GetFatigueSNCurve Method](SolidWorks.Interop.cosworks~SolidWorks.Interop.cosworks.ICWMaterial~GetFatigueSNCurve.html)
[ICWMaterial::SetFatigueSNCurve Method](SolidWorks.Interop.cosworks~SolidWorks.Interop.cosworks.ICWMaterial~SetFatigueSNCurve.html)
[ICWMaterial::SNCurveEstimateConstants Property ()](SolidWorks.Interop.cosworks~SolidWorks.Interop.cosworks.ICWMaterial~SNCurveEstimateConstants.html)
[ICWMaterial::SNCurveEstimateCutoff Property ()](SolidWorks.Interop.cosworks~SolidWorks.Interop.cosworks.ICWMaterial~SNCurveEstimateCutoff.html)
[ICWMaterial::SNCurveSlopeM Property ()](SolidWorks.Interop.cosworks~SolidWorks.Interop.cosworks.ICWMaterial~SNCurveSlopeM.html)
[ICWMaterial::SNCurveSpecificConstantB Property ()](SolidWorks.Interop.cosworks~SolidWorks.Interop.cosworks.ICWMaterial~SNCurveSpecificConstantB.html)
[ICWMaterial::SNCurveSpecificConstantBUnit Property ()](SolidWorks.Interop.cosworks~SolidWorks.Interop.cosworks.ICWMaterial~SNCurveSpecificConstantBUnit.html)

## Availability

SOLIDWORKS Simulation API 2008 SP1.0
