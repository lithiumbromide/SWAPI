---
title: "IncludeShellEdgeSolidOrShellFace2 Property (ICWContactComponent)"
project: "SOLIDWORKS Simulation API Help"
interface: "ICWContactComponent"
member: "IncludeShellEdgeSolidOrShellFace2"
kind: "property"
source: "cworksapi/SolidWorks.Interop.cosworks~SolidWorks.Interop.cosworks.ICWContactComponent~IncludeShellEdgeSolidOrShellFace2.html"
---

# IncludeShellEdgeSolidOrShellFace2 Property (ICWContactComponent)

Sets whether to create contact sets.

## Syntax

### Visual Basic (Declaration)

```vb
Property IncludeShellEdgeSolidOrShellFace2 As System.Boolean
```

### Visual Basic (Usage)

```vb
Dim instance As ICWContactComponent
Dim value As System.Boolean

instance.IncludeShellEdgeSolidOrShellFace2 = value

value = instance.IncludeShellEdgeSolidOrShellFace2
```

### C#

```csharp
System.bool IncludeShellEdgeSolidOrShellFace2 {get; set;}
```

### C++/CLI

```cpp
property System.bool IncludeShellEdgeSolidOrShellFace2 {
   System.bool get();
   void set (    System.bool value);
}
```

### Property Value

-1 or true to create contact sets, 0 or false to not

## VBA Syntax

See [CWContactComponent::IncludeShellEdgeSolidOrShellFace2](ms-its:cworksapivb6.chm::/CosmosWorksLib~CWContactComponent~IncludeShellEdgeSolidOrShellFace2.html).

## Remarks

To set this property, you can specify either the boolean or the integer.

This property sets whether to create bonded contact sets for shell edge pairs, shell edge-to-shell face pairs, and shell edge-to-solid face pairs that are non-touching and within clearance.

| This property is valid only if... | Is set to... |
| --- | --- |
| ICWContactComponent::ContactComponentType | swsContactType_e .swsContactTypeBonded |
| ICWContactComponent::IncludeClearance2 | -1 or true |

## See Also

[ICWContactComponent Interface](SolidWorks.Interop.cosworks~SolidWorks.Interop.cosworks.ICWContactComponent.html)
[ICWContactComponent Members](SolidWorks.Interop.cosworks~SolidWorks.Interop.cosworks.ICWContactComponent_members.html)

## Availability

SOLIDWORKS Simulation API 2022 SP0
