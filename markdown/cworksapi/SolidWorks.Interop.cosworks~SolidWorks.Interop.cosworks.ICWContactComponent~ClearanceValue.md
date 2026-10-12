---
title: "ClearanceValue Property (ICWContactComponent)"
project: "SOLIDWORKS Simulation API Help"
interface: "ICWContactComponent"
member: "ClearanceValue"
kind: "property"
source: "cworksapi/SolidWorks.Interop.cosworks~SolidWorks.Interop.cosworks.ICWContactComponent~ClearanceValue.html"
---

# ClearanceValue Property (ICWContactComponent)

Gets or sets the maximum clearance (gap) between non-touching faces or shell edges.

## Syntax

### Visual Basic (Declaration)

```vb
Property ClearanceValue As System.Double
```

### Visual Basic (Usage)

```vb
Dim instance As ICWContactComponent
Dim value As System.Double

instance.ClearanceValue = value

value = instance.ClearanceValue
```

### C#

```csharp
System.double ClearanceValue {get; set;}
```

### C++/CLI

```cpp
property System.double ClearanceValue {
   System.double get();
   void set (    System.double value);
}
```

### Property Value

Maximum clearance (gap) between non-touching faces or shell edges

## VBA Syntax

See [CWContactComponent::ClearanceValue](ms-its:cworksapivb6.chm::/CosmosWorksLib~CWContactComponent~ClearanceValue.html).

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
[ICWContactComponent::ClearanceUnit Property ()](SolidWorks.Interop.cosworks~SolidWorks.Interop.cosworks.ICWContactComponent~ClearanceUnit.html)
[ICWContactComponent::IncludeShellEdgeSolidOrShellFace Property ()](SolidWorks.Interop.cosworks~SolidWorks.Interop.cosworks.ICWContactComponent~IncludeShellEdgeSolidOrShellFace.html)

## Availability

SOLIDWORKS Simulation API 2017 SP0
