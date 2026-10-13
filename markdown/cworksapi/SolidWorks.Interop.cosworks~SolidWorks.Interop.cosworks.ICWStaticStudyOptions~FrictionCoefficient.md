---
title: "FrictionCoefficient Property (ICWStaticStudyOptions)"
project: "SOLIDWORKS Simulation API Help"
interface: "ICWStaticStudyOptions"
member: "FrictionCoefficient"
kind: "property"
source: "cworksapi/SolidWorks.Interop.cosworks~SolidWorks.Interop.cosworks.ICWStaticStudyOptions~FrictionCoefficient.html"
---

# FrictionCoefficient Property (ICWStaticStudyOptions)

Gets or sets the value of the coefficient of friction.

## Syntax

### Visual Basic (Declaration)

```vb
Property FrictionCoefficient As System.Double
```

### Visual Basic (Usage)

```vb
Dim instance As ICWStaticStudyOptions
Dim value As System.Double

instance.FrictionCoefficient = value

value = instance.FrictionCoefficient
```

### C#

```csharp
System.double FrictionCoefficient {get; set;}
```

### C++/CLI

```cpp
property System.double FrictionCoefficient {
   System.double get();
   void set (    System.double value);
}
```

### Property Value

0.0 <= Friction coefficient <= 1.0

## VBA Syntax

See [CWStaticStudyOptions::FrictionCoefficient](ms-its:cworksapivb6.chm::/CosmosWorksLib~CWStaticStudyOptions~FrictionCoefficient.html).

## Examples

See the [ICWStaticStudyOptions](SolidWorks.Interop.cosworks~SolidWorks.Interop.cosworks.ICWStaticStudyOptions.html) examples.

## Remarks

This property is valid only if [ICWStaticStudyOptions::IncludeGlobalFriction](SolidWorks.Interop.cosworks~SolidWorks.Interop.cosworks.ICWStaticStudyOptions~IncludeGlobalFriction.html) is set to 1.

## See Also

[ICWStaticStudyOptions Interface](SolidWorks.Interop.cosworks~SolidWorks.Interop.cosworks.ICWStaticStudyOptions.html)
[ICWStaticStudyOptions Members](SolidWorks.Interop.cosworks~SolidWorks.Interop.cosworks.ICWStaticStudyOptions_members.html)
[ICWStaticStudyOptions::IncludeGlobalFriction Property ()](SolidWorks.Interop.cosworks~SolidWorks.Interop.cosworks.ICWStaticStudyOptions~IncludeGlobalFriction.html)
[ICWStaticStudyOptions::IgnoreClearanceForSurfaceContact Property ()](SolidWorks.Interop.cosworks~SolidWorks.Interop.cosworks.ICWStaticStudyOptions~IgnoreClearanceForSurfaceContact.html)
[ICWStaticStudyOptions::NoPenetration Property ()](SolidWorks.Interop.cosworks~SolidWorks.Interop.cosworks.ICWStaticStudyOptions~NoPenetration.html)

## Availability

SOLIDWORKS Simulation API 2008 SP1.0
