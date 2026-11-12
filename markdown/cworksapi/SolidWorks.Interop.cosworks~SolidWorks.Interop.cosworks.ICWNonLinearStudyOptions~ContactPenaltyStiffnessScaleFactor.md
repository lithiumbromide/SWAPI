---
title: "ContactPenaltyStiffnessScaleFactor Property (ICWNonLinearStudyOptions)"
project: "SOLIDWORKS Simulation API Help"
interface: "ICWNonLinearStudyOptions"
member: "ContactPenaltyStiffnessScaleFactor"
kind: "property"
source: "cworksapi/SolidWorks.Interop.cosworks~SolidWorks.Interop.cosworks.ICWNonLinearStudyOptions~ContactPenaltyStiffnessScaleFactor.html"
---

# ContactPenaltyStiffnessScaleFactor Property (ICWNonLinearStudyOptions)

Gets or sets the surface-to-surface contact penalty stiffness scale factor for this nonlinear study.

## Syntax

### Visual Basic (Declaration)

```vb
Property ContactPenaltyStiffnessScaleFactor As System.Double
```

### Visual Basic (Usage)

```vb
Dim instance As ICWNonLinearStudyOptions
Dim value As System.Double

instance.ContactPenaltyStiffnessScaleFactor = value

value = instance.ContactPenaltyStiffnessScaleFactor
```

### C#

```csharp
System.double ContactPenaltyStiffnessScaleFactor {get; set;}
```

### C++/CLI

```cpp
property System.double ContactPenaltyStiffnessScaleFactor {
   System.double get();
   void set (    System.double value);
}
```

### Property Value

0.01 (approximate) <= Contact penalty stiffness scale factor < = 1.0 (precise)

## VBA Syntax

See [CWNonLinearStudyOptions::ContactPenaltyStiffnessScaleFactor](ms-its:cworksapivb6.chm::/CosmosWorksLib~CWNonLinearStudyOptions~ContactPenaltyStiffnessScaleFactor.html).

## Remarks

This property corresponds to right-clicking on the nonlinear_study in the Study Manager and setting **Properties > Contact penalty stiffness scale factor**.

For nonlinear simulation, a formula for penalty stiffness is used while solving surface-to-surface contact problems. The formula more accurately predicts physical behavior. During the design process, such accuracy may not be useful. Relaxing the accuracy gives a quicker solution, allowing you to quickly discover how to adjust the design. This property allows you to adjust the scale factor of this penalty stiffness formula as needed during the design process.

## See Also

[ICWNonLinearStudyOptions Interface](SolidWorks.Interop.cosworks~SolidWorks.Interop.cosworks.ICWNonLinearStudyOptions.html)
[ICWNonLinearStudyOptions Members](SolidWorks.Interop.cosworks~SolidWorks.Interop.cosworks.ICWNonLinearStudyOptions_members.html)
[ICWNonLinearStudyOptions::ContactPenaltyStiffnessScaleFactorGlobalDefault Property ()](SolidWorks.Interop.cosworks~SolidWorks.Interop.cosworks.ICWNonLinearStudyOptions~ContactPenaltyStiffnessScaleFactorGlobalDefault.html)

## Availability

SOLIDWORKS Simulation API 2025 SP0
