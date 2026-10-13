---
title: "ContactPenaltyStiffnessScaleFactor Property (ICWStaticStudyOptions)"
project: "SOLIDWORKS Simulation API Help"
interface: "ICWStaticStudyOptions"
member: "ContactPenaltyStiffnessScaleFactor"
kind: "property"
source: "cworksapi/SolidWorks.Interop.cosworks~SolidWorks.Interop.cosworks.ICWStaticStudyOptions~ContactPenaltyStiffnessScaleFactor.html"
---

# ContactPenaltyStiffnessScaleFactor Property (ICWStaticStudyOptions)

Gets or sets the contact penalty stiffness scale factor for this static study.

## Syntax

### Visual Basic (Declaration)

```vb
Property ContactPenaltyStiffnessScaleFactor As System.Double
```

### Visual Basic (Usage)

```vb
Dim instance As ICWStaticStudyOptions
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

0.01 (approximate ) <= Contact penalty stiffness scale factor <= 1.0 (precise)

## VBA Syntax

See [CWStaticStudyOptions::ContactPenaltyStiffnessScaleFactor](ms-its:cworksapivb6.chm::/CosmosWorksLib~CWStaticStudyOptions~ContactPenaltyStiffnessScaleFactor.html).

## Remarks

This property is analogous to the **Contact penalty stiffness scale factor** setting on the **Simulation** **Study RMB menu > Properties > Options** tab.

## See Also

[ICWStaticStudyOptions Interface](SolidWorks.Interop.cosworks~SolidWorks.Interop.cosworks.ICWStaticStudyOptions.html)
[ICWStaticStudyOptions Members](SolidWorks.Interop.cosworks~SolidWorks.Interop.cosworks.ICWStaticStudyOptions_members.html)
[ICWStaticStudyOptions::ContactPenaltyStiffnessScaleFactorGlobalDefault Property ()](SolidWorks.Interop.cosworks~SolidWorks.Interop.cosworks.ICWStaticStudyOptions~ContactPenaltyStiffnessScaleFactorGlobalDefault.html)

## Availability

SOLIDWORKS Simulation API 2023 SP0
