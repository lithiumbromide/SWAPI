---
title: "ComponentName Property (ICWSolidComponent)"
project: "SOLIDWORKS Simulation API Help"
interface: "ICWSolidComponent"
member: "ComponentName"
kind: "property"
source: "cworksapi/SolidWorks.Interop.cosworks~SolidWorks.Interop.cosworks.ICWSolidComponent~ComponentName.html"
---

# ComponentName Property (ICWSolidComponent)

Gets the name of the solid component.

## Syntax

### Visual Basic (Declaration)

```vb
ReadOnly Property ComponentName As System.String
```

### Visual Basic (Usage)

```vb
Dim instance As ICWSolidComponent
Dim value As System.String

value = instance.ComponentName
```

### C#

```csharp
System.string ComponentName {get;}
```

### C++/CLI

```cpp
property System.String^ ComponentName {
   System.String^ get();
}
```

### Property Value

Name of solid component

## VBA Syntax

See [CWSolidComponent::ComponentName](ms-its:cworksapivb6.chm::/CosmosWorksLib~CWSolidComponent~ComponentName.html).

## Examples

[Create Nonlinear Study and Apply Materials (C#)](Create_Nonlinear_Study_and_Apply_Materials_Example_CSharp.htm)
[Create Nonlinear Study and Apply Materials (VB.NET)](Create_Nonlinear_Study_and_Apply_Materials_Example_VBNET.htm)
[Create Nonlinear Study and Apply Materials (VBA)](Create_Nonlinear_Study_and_Apply_Materials_Example_VB.htm)

## See Also

[ICWSolidComponent Interface](SolidWorks.Interop.cosworks~SolidWorks.Interop.cosworks.ICWSolidComponent.html)
[ICWSolidComponent Members](SolidWorks.Interop.cosworks~SolidWorks.Interop.cosworks.ICWSolidComponent_members.html)

## Availability

SOLIDWORKS Simulation API 2008 SP1.0
