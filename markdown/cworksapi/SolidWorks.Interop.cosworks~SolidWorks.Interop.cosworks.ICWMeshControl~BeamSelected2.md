---
title: "BeamSelected2 Property (ICWMeshControl)"
project: "SOLIDWORKS Simulation API Help"
interface: "ICWMeshControl"
member: "BeamSelected2"
kind: "property"
source: "cworksapi/SolidWorks.Interop.cosworks~SolidWorks.Interop.cosworks.ICWMeshControl~BeamSelected2.html"
---

# BeamSelected2 Property (ICWMeshControl)

Gets and sets whether to select beams for this mesh control.

## Syntax

### Visual Basic (Declaration)

```vb
Property BeamSelected2 As System.Boolean
```

### Visual Basic (Usage)

```vb
Dim instance As ICWMeshControl
Dim value As System.Boolean

instance.BeamSelected2 = value

value = instance.BeamSelected2
```

### C#

```csharp
System.bool BeamSelected2 {get; set;}
```

### C++/CLI

```cpp
property System.bool BeamSelected2 {
   System.bool get();
   void set (    System.bool value);
}
```

### Property Value

-1 or true to select beams, 0 or false to not

## Examples

See the [ICWMeshControl](SolidWorks.Interop.cosworks~SolidWorks.Interop.cosworks.ICWMeshControl.html) examples.

## Remarks

This property returns a boolean value which can be cast to an integer. To set this property, you can specify either the boolean or the integer.

## See Also

[ICWMeshControl Interface](SolidWorks.Interop.cosworks~SolidWorks.Interop.cosworks.ICWMeshControl.html)
[ICWMeshControl Members](SolidWorks.Interop.cosworks~SolidWorks.Interop.cosworks.ICWMeshControl_members.html)

## Availability

SOLIDWORKS 2022 FCS, Revision Number 30
