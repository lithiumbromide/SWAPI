---
title: "AutomaticTransition2 Property (ICWMesh)"
project: "SOLIDWORKS Simulation API Help"
interface: "ICWMesh"
member: "AutomaticTransition2"
kind: "property"
source: "cworksapi/SolidWorks.Interop.cosworks~SolidWorks.Interop.cosworks.ICWMesh~AutomaticTransition2.html"
---

# AutomaticTransition2 Property (ICWMesh)

Gets or sets whether mesh controls are automatically applied to small features, holes, fillets, and other fine details in the model.

## Syntax

### Visual Basic (Declaration)

```vb
Property AutomaticTransition2 As System.Boolean
```

### Visual Basic (Usage)

```vb
Dim instance As ICWMesh
Dim value As System.Boolean

instance.AutomaticTransition2 = value

value = instance.AutomaticTransition2
```

### C#

```csharp
System.bool AutomaticTransition2 {get; set;}
```

### C++/CLI

```cpp
property System.bool AutomaticTransition2 {
   System.bool get();
   void set (    System.bool value);
}
```

### Property Value

-1 or true if automatic transition is on, 0 or false if not

## Remarks

This property returns a boolean value which can be cast to an integer. To set this property, you can specify either the boolean or the integer.

## See Also

[ICWMesh Interface](SolidWorks.Interop.cosworks~SolidWorks.Interop.cosworks.ICWMesh.html)
[ICWMesh Members](SolidWorks.Interop.cosworks~SolidWorks.Interop.cosworks.ICWMesh_members.html)

## Availability

SOLIDWORKS 2022 FCS, Revision Number 30
