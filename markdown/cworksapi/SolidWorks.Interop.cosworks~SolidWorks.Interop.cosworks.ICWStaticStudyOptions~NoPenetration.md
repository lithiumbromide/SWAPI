---
title: "NoPenetration Property (ICWStaticStudyOptions)"
project: "SOLIDWORKS Simulation API Help"
interface: "ICWStaticStudyOptions"
member: "NoPenetration"
kind: "property"
source: "cworksapi/SolidWorks.Interop.cosworks~SolidWorks.Interop.cosworks.ICWStaticStudyOptions~NoPenetration.html"
---

# NoPenetration Property (ICWStaticStudyOptions)

Obsolete. Superseded by [ICWStaticStudyOptions::NoPenetration2](SolidWorks.Interop.cosworks~SolidWorks.Interop.cosworks.ICWStaticStudyOptions~LargeDisplacement2.html).

## Syntax

### Visual Basic (Declaration)

```vb
Property NoPenetration As System.Integer
```

### Visual Basic (Usage)

```vb
Dim instance As ICWStaticStudyOptions
Dim value As System.Integer

instance.NoPenetration = value

value = instance.NoPenetration
```

### C#

```csharp
System.int NoPenetration {get; set;}
```

### C++/CLI

```cpp
property System.int NoPenetration {
   System.int get();
   void set (    System.int value);
}
```

### Property Value

1 to improve accuracy for no penetration contacting surfaces, 0 to not

## VBA Syntax

See [CWStaticStudyOptions::NoPenetration](ms-its:cworksapivb6.chm::/CosmosWorksLib~CWStaticStudyOptions~NoPenetration.html).

## Examples

See the [ICWStaticStudyOptions](SolidWorks.Interop.cosworks~SolidWorks.Interop.cosworks.ICWStaticStudyOptions.html) examples.

## See Also

[ICWStaticStudyOptions Interface](SolidWorks.Interop.cosworks~SolidWorks.Interop.cosworks.ICWStaticStudyOptions.html)
[ICWStaticStudyOptions Members](SolidWorks.Interop.cosworks~SolidWorks.Interop.cosworks.ICWStaticStudyOptions_members.html)
[ICWStaticStudyOptions::IncludeGlobalFriction Property ()](SolidWorks.Interop.cosworks~SolidWorks.Interop.cosworks.ICWStaticStudyOptions~IncludeGlobalFriction.html)
[ICWStaticStudyOptions::IgnoreClearanceForSurfaceContact Property ()](SolidWorks.Interop.cosworks~SolidWorks.Interop.cosworks.ICWStaticStudyOptions~IgnoreClearanceForSurfaceContact.html)
[ICWStaticStudyOptions::FrictionCoefficient Property ()](SolidWorks.Interop.cosworks~SolidWorks.Interop.cosworks.ICWStaticStudyOptions~FrictionCoefficient.html)

## Availability

SOLIDWORKS Simulation API 2017 SP0
