---
title: "IncludeClearance2 Property (ICWContactComponent)"
project: "SOLIDWORKS Simulation API Help"
interface: "ICWContactComponent"
member: "IncludeClearance2"
kind: "property"
source: "cworksapi/SolidWorks.Interop.cosworks~SolidWorks.Interop.cosworks.ICWContactComponent~IncludeClearance2.html"
---

# IncludeClearance2 Property (ICWContactComponent)

Sets whether to specify clearance for non-touching faces in this contact.

## Syntax

### Visual Basic (Declaration)

```vb
Property IncludeClearance2 As System.Boolean
```

### Visual Basic (Usage)

```vb
Dim instance As ICWContactComponent
Dim value As System.Boolean

instance.IncludeClearance2 = value

value = instance.IncludeClearance2
```

### C#

```csharp
System.bool IncludeClearance2 {get; set;}
```

### C++/CLI

```cpp
property System.bool IncludeClearance2 {
   System.bool get();
   void set (    System.bool value);
}
```

### Property Value

-1 or true to specify clearance for non-touching faces, 0 or false to not

## VBA Syntax

See [CWContactComponent::IncludeClearance2](ms-its:cworksapivb6.chm::/CosmosWorksLib~CWContactComponent~IncludeClearance2.html).

## Remarks

To set this property, you can specify either the boolean or the integer.

## See Also

[ICWContactComponent Interface](SolidWorks.Interop.cosworks~SolidWorks.Interop.cosworks.ICWContactComponent.html)
[ICWContactComponent Members](SolidWorks.Interop.cosworks~SolidWorks.Interop.cosworks.ICWContactComponent_members.html)

## Availability

SOLIDWORKS Simulation API 2022 SP0
