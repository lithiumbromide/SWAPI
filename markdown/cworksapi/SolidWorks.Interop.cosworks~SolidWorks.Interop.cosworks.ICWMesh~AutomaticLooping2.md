---
title: "AutomaticLooping2 Property (ICWMesh)"
project: "SOLIDWORKS Simulation API Help"
interface: "ICWMesh"
member: "AutomaticLooping2"
kind: "property"
source: "cworksapi/SolidWorks.Interop.cosworks~SolidWorks.Interop.cosworks.ICWMesh~AutomaticLooping2.html"
---

# AutomaticLooping2 Property (ICWMesh)

Gets or sets whether to automatically retry to mesh the model using a different global element size for solids.

## Syntax

### Visual Basic (Declaration)

```vb
Property AutomaticLooping2 As System.Boolean
```

### Visual Basic (Usage)

```vb
Dim instance As ICWMesh
Dim value As System.Boolean

instance.AutomaticLooping2 = value

value = instance.AutomaticLooping2
```

### C#

```csharp
System.bool AutomaticLooping2 {get; set;}
```

### C++/CLI

```cpp
property System.bool AutomaticLooping2 {
   System.bool get();
   void set (    System.bool value);
}
```

### Property Value

-1 or true if automatic looping is on, 0 or false if not

## Remarks

This property returns a boolean value which can be cast to an integer. To set this property, you can specify either the boolean or the integer.

## See Also

[ICWMesh Interface](SolidWorks.Interop.cosworks~SolidWorks.Interop.cosworks.ICWMesh.html)
[ICWMesh Members](SolidWorks.Interop.cosworks~SolidWorks.Interop.cosworks.ICWMesh_members.html)

## Availability

SOLIDWORKS 2022 FCS, Revision Number 30
