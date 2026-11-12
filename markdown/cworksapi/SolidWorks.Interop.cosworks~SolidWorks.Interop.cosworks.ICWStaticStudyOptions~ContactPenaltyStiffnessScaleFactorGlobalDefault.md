---
title: "ContactPenaltyStiffnessScaleFactorGlobalDefault Property (ICWStaticStudyOptions)"
project: "SOLIDWORKS Simulation API Help"
interface: "ICWStaticStudyOptions"
member: "ContactPenaltyStiffnessScaleFactorGlobalDefault"
kind: "property"
source: "cworksapi/SolidWorks.Interop.cosworks~SolidWorks.Interop.cosworks.ICWStaticStudyOptions~ContactPenaltyStiffnessScaleFactorGlobalDefault.html"
---

# ContactPenaltyStiffnessScaleFactorGlobalDefault Property (ICWStaticStudyOptions)

Gets or sets the global default for the contact penalty stiffness scale factor.

## Syntax

### Visual Basic (Declaration)

```vb
Property ContactPenaltyStiffnessScaleFactorGlobalDefault As System.Double
```

### Visual Basic (Usage)

```vb
Dim instance As ICWStaticStudyOptions
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

0.01 (approximate ) <= Contact penalty stiffness scale factor <= 1.0 (precise)

## VBA Syntax

See [CWStaticStudyOptions::ContactPenaltyStiffnessScaleFactorGlobalDefault](ms-its:cworksapivb6.chm::/CosmosWorksLib~CWStaticStudyOptions~ContactPenaltyStiffnessScaleFactorGlobalDefault.html).

## Remarks

This property is analogous to the **Contact penalty stiffness scale factor** setting on the **Simulation menu > Options > Default Options > Interaction** tab.

## See Also

[ICWStaticStudyOptions Interface](SolidWorks.Interop.cosworks~SolidWorks.Interop.cosworks.ICWStaticStudyOptions.html)
[ICWStaticStudyOptions Members](SolidWorks.Interop.cosworks~SolidWorks.Interop.cosworks.ICWStaticStudyOptions_members.html)
[ICWStaticStudyOptions::ContactPenaltyStiffnessScaleFactor Property ()](SolidWorks.Interop.cosworks~SolidWorks.Interop.cosworks.ICWStaticStudyOptions~ContactPenaltyStiffnessScaleFactor.html)

## Availability

SOLIDWORKS Simulation API 2023 SP0
