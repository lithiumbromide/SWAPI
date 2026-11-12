---
title: "PlyRelativeAngle2 Property (ICWCompositeShellOptions)"
project: "SOLIDWORKS Simulation API Help"
interface: "ICWCompositeShellOptions"
member: "PlyRelativeAngle2"
kind: "property"
source: "cworksapi/SolidWorks.Interop.cosworks~SolidWorks.Interop.cosworks.ICWCompositeShellOptions~PlyRelativeAngle2.html"
---

# PlyRelativeAngle2 Property (ICWCompositeShellOptions)

Gets or sets whether ply angles are relative to the angle of ply 1.

## Syntax

### Visual Basic (Declaration)

```vb
Property PlyRelativeAngle2 As System.Boolean
```

### Visual Basic (Usage)

```vb
Dim instance As ICWCompositeShellOptions
Dim value As System.Boolean

instance.PlyRelativeAngle2 = value

value = instance.PlyRelativeAngle2
```

### C#

```csharp
System.bool PlyRelativeAngle2 {get; set;}
```

### C++/CLI

```cpp
property System.bool PlyRelativeAngle2 {
   System.bool get();
   void set (    System.bool value);
}
```

### Property Value

-1 or true if ply angles are relative to the angle of ply 1, 0 or false if not

## Examples

See the [ICWCompositeShellOptions](SolidWorks.Interop.cosworks~SolidWorks.Interop.cosworks.ICWCompositeShellOptions.html) examples.

## Remarks

This property returns a boolean value which can be cast to an integer. To set this property, you can specify either the boolean or the integer.

## See Also

[ICWCompositeShellOptions Interface](SolidWorks.Interop.cosworks~SolidWorks.Interop.cosworks.ICWCompositeShellOptions.html)
[ICWCompositeShellOptions Members](SolidWorks.Interop.cosworks~SolidWorks.Interop.cosworks.ICWCompositeShellOptions_members.html)

## Availability

SOLIDWORKS 2022 FCS, Revision Number 30
