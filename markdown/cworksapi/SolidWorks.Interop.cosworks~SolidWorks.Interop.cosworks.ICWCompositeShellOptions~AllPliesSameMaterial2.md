---
title: "AllPliesSameMaterial2 Property (ICWCompositeShellOptions)"
project: "SOLIDWORKS Simulation API Help"
interface: "ICWCompositeShellOptions"
member: "AllPliesSameMaterial2"
kind: "property"
source: "cworksapi/SolidWorks.Interop.cosworks~SolidWorks.Interop.cosworks.ICWCompositeShellOptions~AllPliesSameMaterial2.html"
---

# AllPliesSameMaterial2 Property (ICWCompositeShellOptions)

Gets or sets whether the same material is applied to all plies.

## Syntax

### Visual Basic (Declaration)

```vb
Property AllPliesSameMaterial2 As System.Boolean
```

### Visual Basic (Usage)

```vb
Dim instance As ICWCompositeShellOptions
Dim value As System.Boolean

instance.AllPliesSameMaterial2 = value

value = instance.AllPliesSameMaterial2
```

### C#

```csharp
System.bool AllPliesSameMaterial2 {get; set;}
```

### C++/CLI

```cpp
property System.bool AllPliesSameMaterial2 {
   System.bool get();
   void set (    System.bool value);
}
```

### Property Value

-1 or true applies the same material to all plies, 0 or false does not

## Examples

See the [ICWCompositeShellOptions](SolidWorks.Interop.cosworks~SolidWorks.Interop.cosworks.ICWCompositeShellOptions.html) examples.

## Remarks

This property returns a boolean value which can be cast to an integer. To set this property, you can specify either the boolean or the integer.

Before setting this property, call [ICWShell::SetLibraryMaterial](SolidWorks.Interop.cosworks~SolidWorks.Interop.cosworks.ICWShell~SetLibraryMaterial.html).

## See Also

[ICWCompositeShellOptions Interface](SolidWorks.Interop.cosworks~SolidWorks.Interop.cosworks.ICWCompositeShellOptions.html)
[ICWCompositeShellOptions Members](SolidWorks.Interop.cosworks~SolidWorks.Interop.cosworks.ICWCompositeShellOptions_members.html)

## Availability

SOLIDWORKS 2022 FCS, Revision Number 30
