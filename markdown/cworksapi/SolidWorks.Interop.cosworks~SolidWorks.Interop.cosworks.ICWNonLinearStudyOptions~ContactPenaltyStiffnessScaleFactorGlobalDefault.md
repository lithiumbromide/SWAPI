---
title: "ContactPenaltyStiffnessScaleFactorGlobalDefault Property (ICWNonLinearStudyOptions)"
project: "SOLIDWORKS Simulation API Help"
interface: "ICWNonLinearStudyOptions"
member: "ContactPenaltyStiffnessScaleFactorGlobalDefault"
kind: "property"
source: "cworksapi/SolidWorks.Interop.cosworks~SolidWorks.Interop.cosworks.ICWNonLinearStudyOptions~ContactPenaltyStiffnessScaleFactorGlobalDefault.html"
---

# ContactPenaltyStiffnessScaleFactorGlobalDefault Property (ICWNonLinearStudyOptions)

Gets or sets the global default value of the surface-to-surface contact penalty stiffness scale factor for this nonlinear study.

## Syntax

### Visual Basic (Declaration)

```vb
Property ContactPenaltyStiffnessScaleFactorGlobalDefault As System.Double
```

### Visual Basic (Usage)

```vb
Dim instance As ICWNonLinearStudyOptions
Dim value As System.Double

instance.ContactPenaltyStiffnessScaleFactorGlobalDefault = value

value = instance.ContactPenaltyStiffnessScaleFactorGlobalDefault
```

### C#

```csharp
System.double ContactPenaltyStiffnessScaleFactorGlobalDefault {get; set;}
```

### C++/CLI

```cpp
property System.double ContactPenaltyStiffnessScaleFactorGlobalDefault {
   System.double get();
   void set (    System.double value);
}
```

### Property Value

0.01 (approximate) <= Global default value of contact penalty stiffness scale factor < = 1.0 (precise)

## VBA Syntax

See [CWNonLinearStudyOptions::ContactPenaltyStiffnessScaleFactorGlobalDefault](ms-its:cworksapivb6.chm::/CosmosWorksLib~CWNonLinearStudyOptions~ContactPenaltyStiffnessScaleFactorGlobalDefault.html).

## Remarks

This property corresponds to setting a global default for all non-linear studies.

## See Also

[ICWNonLinearStudyOptions Interface](SolidWorks.Interop.cosworks~SolidWorks.Interop.cosworks.ICWNonLinearStudyOptions.html)
[ICWNonLinearStudyOptions Members](SolidWorks.Interop.cosworks~SolidWorks.Interop.cosworks.ICWNonLinearStudyOptions_members.html)
[ICWNonLinarStudyOptions::ContactPenaltyStiffnessScaleFactor Property ()](SolidWorks.Interop.cosworks~SolidWorks.Interop.cosworks.ICWNonLinearStudyOptions~ContactPenaltyStiffnessScaleFactor.html)

## Availability

SOLIDWORKS Simulation API 2025 SP0
