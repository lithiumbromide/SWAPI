---
title: "RotateZeroDegreeReference2 Property (ICWCompositeShellOptions)"
project: "SOLIDWORKS Simulation API Help"
interface: "ICWCompositeShellOptions"
member: "RotateZeroDegreeReference2"
kind: "property"
source: "cworksapi/SolidWorks.Interop.cosworks~SolidWorks.Interop.cosworks.ICWCompositeShellOptions~RotateZeroDegreeReference2.html"
---

# RotateZeroDegreeReference2 Property (ICWCompositeShellOptions)

Gets or sets whether to redefine the stripes on the composite shell so that the previous 90° ply angle now corresponds to the 0° ply angle.

## Syntax

### Visual Basic (Declaration)

```vb
Property RotateZeroDegreeReference2 As System.Boolean
```

### Visual Basic (Usage)

```vb
Dim instance As ICWCompositeShellOptions
Dim value As System.Boolean

instance.RotateZeroDegreeReference2 = value

value = instance.RotateZeroDegreeReference2
```

### C#

```csharp
System.bool RotateZeroDegreeReference2 {get; set;}
```

### C++/CLI

```cpp
property System.bool RotateZeroDegreeReference2 {
   System.bool get();
   void set (    System.bool value);
}
```

### Property Value

-1 or true to rotate the 0° ply angle reference, 0 or false to not

## Examples

See the [ICWCompositeShellOptions](SolidWorks.Interop.cosworks~SolidWorks.Interop.cosworks.ICWCompositeShellOptions.html) examples.

## Remarks

This property returns a boolean value which can be cast to an integer. To set this property, you can specify either the boolean or the integer.

## See Also

[ICWCompositeShellOptions Interface](SolidWorks.Interop.cosworks~SolidWorks.Interop.cosworks.ICWCompositeShellOptions.html)
[ICWCompositeShellOptions Members](SolidWorks.Interop.cosworks~SolidWorks.Interop.cosworks.ICWCompositeShellOptions_members.html)

## Availability

SOLIDWORKS 2022 FCS, Revision Number 30
