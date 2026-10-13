---
title: "SolidBodyCount Property (ICWSolidComponent)"
project: "SOLIDWORKS Simulation API Help"
interface: "ICWSolidComponent"
member: "SolidBodyCount"
kind: "property"
source: "cworksapi/SolidWorks.Interop.cosworks~SolidWorks.Interop.cosworks.ICWSolidComponent~SolidBodyCount.html"
---

# SolidBodyCount Property (ICWSolidComponent)

Gets the number of solid bodies in the solid component.

## Syntax

### Visual Basic (Declaration)

```vb
ReadOnly Property SolidBodyCount As System.Integer
```

### Visual Basic (Usage)

```vb
Dim instance As ICWSolidComponent
Dim value As System.Integer

value = instance.SolidBodyCount
```

### C#

```csharp
System.int SolidBodyCount {get;}
```

### C++/CLI

```cpp
property System.int SolidBodyCount {
   System.int get();
}
```

### Property Value

Number of solid bodies in the solid component

## VBA Syntax

See [CWSolidComponent::SolidBodyCount](ms-its:cworksapivb6.chm::/CosmosWorksLib~CWSolidComponent~SolidBodyCount.html).

## Examples

[Create Frequency Study with Solid Mesh (C#)](Create_Frequency_Study_with_Solid_Mesh_Example_CSharp.htm)
[Create Frequency Study with Solid Mesh (VB.NET)](Create_Frequency_Study_with_Solid_Mesh_Example_VBNET.htm)
[Create Frequency Study with Solid Mesh (VBA)](Create_Frequency_Study_with_Solid_Mesh_Example_VB.htm)

## See Also

[ICWSolidComponent Interface](SolidWorks.Interop.cosworks~SolidWorks.Interop.cosworks.ICWSolidComponent.html)
[ICWSolidComponent Members](SolidWorks.Interop.cosworks~SolidWorks.Interop.cosworks.ICWSolidComponent_members.html)

## Availability

SOLIDWORKS Simulation API 2008 SP1.0
