---
title: "Sandwich2 Property (ICWCompositeShellOptions)"
project: "SOLIDWORKS Simulation API Help"
interface: "ICWCompositeShellOptions"
member: "Sandwich2"
kind: "property"
source: "cworksapi/SolidWorks.Interop.cosworks~SolidWorks.Interop.cosworks.ICWCompositeShellOptions~Sandwich2.html"
---

# Sandwich2 Property (ICWCompositeShellOptions)

Gets or sets whether to use the sandwich composite formulation.

## Syntax

### Visual Basic (Declaration)

```vb
Property Sandwich2 As System.Boolean
```

### Visual Basic (Usage)

```vb
Dim instance As ICWCompositeShellOptions
Dim value As System.Boolean

instance.Sandwich2 = value

value = instance.Sandwich2
```

### C#

```csharp
System.bool Sandwich2 {get; set;}
```

### C++/CLI

```cpp
property System.bool Sandwich2 {
   System.bool get();
   void set (    System.bool value);
}
```

### Property Value

-1 or true to use the sandwich composite formulation, 0 or false to not

## Examples

See the [ICWCompositeShellOptions](SolidWorks.Interop.cosworks~SolidWorks.Interop.cosworks.ICWCompositeShellOptions.html) examples.

## Remarks

This property returns a boolean value which can be cast to an integer. To set this property, you can specify either the boolean or the integer.

## See Also

[ICWCompositeShellOptions Interface](SolidWorks.Interop.cosworks~SolidWorks.Interop.cosworks.ICWCompositeShellOptions.html)
[ICWCompositeShellOptions Members](SolidWorks.Interop.cosworks~SolidWorks.Interop.cosworks.ICWCompositeShellOptions_members.html)

## Availability

SOLIDWORKS 2022 FCS, Revision Number 30
