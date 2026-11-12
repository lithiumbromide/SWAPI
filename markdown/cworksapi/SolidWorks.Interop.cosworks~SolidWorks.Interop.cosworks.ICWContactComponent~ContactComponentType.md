---
title: "ContactComponentType Property (ICWContactComponent)"
project: "SOLIDWORKS Simulation API Help"
interface: "ICWContactComponent"
member: "ContactComponentType"
kind: "property"
source: "cworksapi/SolidWorks.Interop.cosworks~SolidWorks.Interop.cosworks.ICWContactComponent~ContactComponentType.html"
---

# ContactComponentType Property (ICWContactComponent)

Gets or sets the type of contact.

## Syntax

### Visual Basic (Declaration)

```vb
Property ContactComponentType As System.Integer
```

### Visual Basic (Usage)

```vb
Dim instance As ICWContactComponent
Dim value As System.Integer

instance.ContactComponentType = value

value = instance.ContactComponentType
```

### C#

```csharp
System.int ContactComponentType {get; set;}
```

### C++/CLI

```cpp
property System.int ContactComponentType {
   System.int get();
   void set (    System.int value);
}
```

### Property Value

Type of contact for:

- [static](SOLIDWORKS.Interop.cosworks~SOLIDWORKS.Interop.cosworks.ICWStaticStudyOptions.html), [nonlinear](SOLIDWORKS.Interop.cosworks~SOLIDWORKS.Interop.cosworks.ICWNonLinearStudyOptions.html), [buckling](SOLIDWORKS.Interop.cosworks~SOLIDWORKS.Interop.cosworks.ICWBucklingStudyOptions.html) and [thermal](SOLIDWORKS.Interop.cosworks~SOLIDWORKS.Interop.cosworks.ICWThermalStudyOptions.html) studies as defined in [swsContactType_e](SOLIDWORKS.Interop.cosworks~SOLIDWORKS.Interop.cosworks.swsContactType_e.html)
- [frequency](SOLIDWORKS.Interop.cosworks~SOLIDWORKS.Interop.cosworks.ICWFrequencyStudyOptions.html) studies as defined in [swsContactType_e](SOLIDWORKS.Interop.cosworks~SOLIDWORKS.Interop.cosworks.swsContactType_e.html), excluding swsContactTypeStaticNoPenetration

## VBA Syntax

See [CWContactComponent::ContactComponentType](ms-its:cworksapivb6.chm::/CosmosWorksLib~CWContactComponent~ContactComponentType.html).

## Examples

See the [ICWContactComponent](SolidWorks.Interop.cosworks~SolidWorks.Interop.cosworks.ICWContactComponent.html) examples.

## Remarks

See the SOLIDWORKS Simulation Help for guidelines about studies with contact conditions.

## See Also

[ICWContactComponent Interface](SolidWorks.Interop.cosworks~SolidWorks.Interop.cosworks.ICWContactComponent.html)
[ICWContactComponent Members](SolidWorks.Interop.cosworks~SolidWorks.Interop.cosworks.ICWContactComponent_members.html)

## Availability

SOLIDWORKS Simulation API 2008 SP1.0
