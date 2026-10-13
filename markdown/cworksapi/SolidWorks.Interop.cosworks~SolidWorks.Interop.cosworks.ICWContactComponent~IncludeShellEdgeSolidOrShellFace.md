---
title: "IncludeShellEdgeSolidOrShellFace Property (ICWContactComponent)"
project: "SOLIDWORKS Simulation API Help"
interface: "ICWContactComponent"
member: "IncludeShellEdgeSolidOrShellFace"
kind: "property"
source: "cworksapi/SolidWorks.Interop.cosworks~SolidWorks.Interop.cosworks.ICWContactComponent~IncludeShellEdgeSolidOrShellFace.html"
---

# IncludeShellEdgeSolidOrShellFace Property (ICWContactComponent)

Obsolete. Superseded by [ICWContactComponent::IncludeShellEdgeSolidOrShellFace2](SolidWorks.Interop.cosworks~SolidWorks.Interop.cosworks.ICWContactComponent~IncludeShellEdgeSolidOrShellFace2.html).

## Syntax

### Visual Basic (Declaration)

```vb
Property IncludeShellEdgeSolidOrShellFace As System.Integer
```

### Visual Basic (Usage)

```vb
Dim instance As ICWContactComponent
Dim value As System.Integer

instance.IncludeShellEdgeSolidOrShellFace = value

value = instance.IncludeShellEdgeSolidOrShellFace
```

### C#

```csharp
System.int IncludeShellEdgeSolidOrShellFace {get; set;}
```

### C++/CLI

```cpp
property System.int IncludeShellEdgeSolidOrShellFace {
   System.int get();
   void set (    System.int value);
}
```

### Property Value

1 to create contact sets, 0 to not

## VBA Syntax

See [CWContactComponent::IncludeShellEdgeSolidOrShellFace](ms-its:cworksapivb6.chm::/CosmosWorksLib~CWContactComponent~IncludeShellEdgeSolidOrShellFace.html).

## Examples

See the [ICWContactComponent](SolidWorks.Interop.cosworks~SolidWorks.Interop.cosworks.ICWContactComponent.html) examples.

## Remarks

This property sets whether to create bonded contact sets for shell edge pairs, shell edge-to-shell face pairs, and shell edge-to-solid face pairs that are non-touching and within clearance.

| This property is valid only if... | Is set to... |
| --- | --- |
| ICWContactComponent::ContactComponentType | swsContactType_e .swsContactTypeBonded |
| ICWContactComponent::IncludeClearance | 1 |

## See Also

[ICWContactComponent Interface](SolidWorks.Interop.cosworks~SolidWorks.Interop.cosworks.ICWContactComponent.html)
[ICWContactComponent Members](SolidWorks.Interop.cosworks~SolidWorks.Interop.cosworks.ICWContactComponent_members.html)
[ICWContactComponent::ClearanceValue Property ()](SolidWorks.Interop.cosworks~SolidWorks.Interop.cosworks.ICWContactComponent~ClearanceValue.html)
[ICWContactComponent::ClearanceUnit Property ()](SolidWorks.Interop.cosworks~SolidWorks.Interop.cosworks.ICWContactComponent~ClearanceUnit.html)

## Availability

SOLIDWORKS Simulation API 2017 SP0
