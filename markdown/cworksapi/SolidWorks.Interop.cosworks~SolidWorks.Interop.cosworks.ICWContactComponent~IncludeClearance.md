---
title: "IncludeClearance Property (ICWContactComponent)"
project: "SOLIDWORKS Simulation API Help"
interface: "ICWContactComponent"
member: "IncludeClearance"
kind: "property"
source: "cworksapi/SolidWorks.Interop.cosworks~SolidWorks.Interop.cosworks.ICWContactComponent~IncludeClearance.html"
---

# IncludeClearance Property (ICWContactComponent)

Obsolete. Superseded by [ICWContactComponent::IncludeClearance2](SolidWorks.Interop.cosworks~SolidWorks.Interop.cosworks.ICWContactComponent~IncludeClearance2.html).

## Syntax

### Visual Basic (Declaration)

```vb
Property IncludeClearance As System.Integer
```

### Visual Basic (Usage)

```vb
Dim instance As ICWContactComponent
Dim value As System.Integer

instance.IncludeClearance = value

value = instance.IncludeClearance
```

### C#

```csharp
System.int IncludeClearance {get; set;}
```

### C++/CLI

```cpp
property System.int IncludeClearance {
   System.int get();
   void set (    System.int value);
}
```

### Property Value

1 to specify clearance for non-touching faces, 0 to not

## VBA Syntax

See [CWContactComponent::IncludeClearance](ms-its:cworksapivb6.chm::/CosmosWorksLib~CWContactComponent~IncludeClearance.html).

## Examples

See the [ICWContactComponent](SolidWorks.Interop.cosworks~SolidWorks.Interop.cosworks.ICWContactComponent.html) examples.

## See Also

[ICWContactComponent Interface](SolidWorks.Interop.cosworks~SolidWorks.Interop.cosworks.ICWContactComponent.html)
[ICWContactComponent Members](SolidWorks.Interop.cosworks~SolidWorks.Interop.cosworks.ICWContactComponent_members.html)
[ICWContactComponent::ClearanceValue Property ()](SolidWorks.Interop.cosworks~SolidWorks.Interop.cosworks.ICWContactComponent~ClearanceValue.html)
[ICWContactComponent::ClearanceUnit Property ()](SolidWorks.Interop.cosworks~SolidWorks.Interop.cosworks.ICWContactComponent~ClearanceUnit.html)
[ICWContactComponent::IncludeShellEdgeSolidOrShellFace Property ()](SolidWorks.Interop.cosworks~SolidWorks.Interop.cosworks.ICWContactComponent~IncludeShellEdgeSolidOrShellFace.html)

## Availability

SOLIDWORKS Simulation API 2017 SP0
