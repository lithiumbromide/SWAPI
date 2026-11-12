---
title: "Symmetric2 Property (ICWCompositeShellOptions)"
project: "SOLIDWORKS Simulation API Help"
interface: "ICWCompositeShellOptions"
member: "Symmetric2"
kind: "property"
source: "cworksapi/SolidWorks.Interop.cosworks~SolidWorks.Interop.cosworks.ICWCompositeShellOptions~Symmetric2.html"
---

# Symmetric2 Property (ICWCompositeShellOptions)

Gets or sets whether the laminate layup is symmetric about the laminate mid-surface.

## Syntax

### Visual Basic (Declaration)

```vb
Property Symmetric2 As System.Boolean
```

### Visual Basic (Usage)

```vb
Dim instance As ICWCompositeShellOptions
Dim value As System.Boolean

instance.Symmetric2 = value

value = instance.Symmetric2
```

### C#

```csharp
System.bool Symmetric2 {get; set;}
```

### C++/CLI

```cpp
property System.bool Symmetric2 {
   System.bool get();
   void set (    System.bool value);
}
```

### Property Value

-1 or true if the laminate layup is symmetric about the laminate mid-surface, 0 or false if not

## Examples

See the [ICWCompositeShellOptions](SolidWorks.Interop.cosworks~SolidWorks.Interop.cosworks.ICWCompositeShellOptions.html) examples.

## Remarks

This property returns a boolean value which can be cast to an integer. To set this property, you can specify either the boolean or the integer.

Setting this property is only valid if [ICWCompositeShellOptions::Sandwich2](SolidWorks.Interop.cosworks~SolidWorks.Interop.cosworks.ICWCompositeShellOptions~Sandwich2.html) is set to 0.

## See Also

[ICWCompositeShellOptions Interface](SolidWorks.Interop.cosworks~SolidWorks.Interop.cosworks.ICWCompositeShellOptions.html)
[ICWCompositeShellOptions Members](SolidWorks.Interop.cosworks~SolidWorks.Interop.cosworks.ICWCompositeShellOptions_members.html)

## Availability

SOLIDWORKS 2022 FCS, Revision Number 30
