---
title: "ClearanceUnit Property (ICWContactComponent)"
project: "SOLIDWORKS Simulation API Help"
interface: "ICWContactComponent"
member: "ClearanceUnit"
kind: "property"
source: "cworksapi/SolidWorks.Interop.cosworks~SolidWorks.Interop.cosworks.ICWContactComponent~ClearanceUnit.html"
---

# ClearanceUnit Property (ICWContactComponent)

Gets or sets the units of clearance between non-touching faces.

## Syntax

### Visual Basic (Declaration)

```vb
Property ClearanceUnit As System.Integer
```

### Visual Basic (Usage)

```vb
Dim instance As ICWContactComponent
Dim value As System.Integer

instance.ClearanceUnit = value

value = instance.ClearanceUnit
```

### C#

```csharp
System.int ClearanceUnit {get; set;}
```

### C++/CLI

```cpp
property System.int ClearanceUnit {
   System.int get();
   void set (    System.int value);
}
```

### Property Value

Units of clearance as defined in [swsPinballUnit_e](SolidWorks.Interop.cosworks~SolidWorks.Interop.cosworks.swsPinballUnit_e.html)

## VBA Syntax

See [CWContactComponent::ClearanceUnit](ms-its:cworksapivb6.chm::/CosmosWorksLib~CWContactComponent~ClearanceUnit.html).

## Examples

See the [ICWContactComponent](SolidWorks.Interop.cosworks~SolidWorks.Interop.cosworks.ICWContactComponent.html) examples.

## Remarks

| This property is valid only if... | Is set to... |
| --- | --- |
| ICWContactComponent::ContactComponentType | swsContactType_e .swsContactTypeBonded |
| ICWContactComponent::IncludeClearance | 1 |

## See Also

[ICWContactComponent Interface](SolidWorks.Interop.cosworks~SolidWorks.Interop.cosworks.ICWContactComponent.html)
[ICWContactComponent Members](SolidWorks.Interop.cosworks~SolidWorks.Interop.cosworks.ICWContactComponent_members.html)
[ICWContactComponent::ClearanceValue Property ()](SolidWorks.Interop.cosworks~SolidWorks.Interop.cosworks.ICWContactComponent~ClearanceValue.html)
[ICWContactComponent::IncludeShellEdgeSolidOrShellFace Property ()](SolidWorks.Interop.cosworks~SolidWorks.Interop.cosworks.ICWContactComponent~IncludeShellEdgeSolidOrShellFace.html)

## Availability

SOLIDWORKS Simulation API 2017 SP0
