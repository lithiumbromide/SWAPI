---
title: "Symmetric Property (ICWCompositeShellOptions)"
project: "SOLIDWORKS Simulation API Help"
interface: "ICWCompositeShellOptions"
member: "Symmetric"
kind: "property"
source: "cworksapi/SolidWorks.Interop.cosworks~SolidWorks.Interop.cosworks.ICWCompositeShellOptions~Symmetric.html"
---

# Symmetric Property (ICWCompositeShellOptions)

Obsolete. Superseded by [ICWCompositeShellOptions::Symmetric2](SolidWorks.Interop.cosworks~SolidWorks.Interop.cosworks.ICWCompositeShellOptions~Symmetric2.html).

## Syntax

### Visual Basic (Declaration)

```vb
Property Symmetric As System.Integer
```

### Visual Basic (Usage)

```vb
Dim instance As ICWCompositeShellOptions
Dim value As System.Integer

instance.Symmetric = value

value = instance.Symmetric
```

### C#

```csharp
System.int Symmetric {get; set;}
```

### C++/CLI

```cpp
property System.int Symmetric {
   System.int get();
   void set (    System.int value);
}
```

### Property Value

1 if the laminate layup is symmetric about the laminate mid-surface, 0 if not

## VBA Syntax

See [CWCompositeShellOptions::Symmetric](ms-its:cworksapivb6.chm::/CosmosWorksLib~CWCompositeShellOptions~Symmetric.html).

## Remarks

Setting this property is only valid if [ICWCompositeShellOptions::Sandwich](SolidWorks.Interop.cosworks~SolidWorks.Interop.cosworks.ICWCompositeShellOptions~Sandwich.html) is set to 0.

## See Also

[ICWCompositeShellOptions Interface](SolidWorks.Interop.cosworks~SolidWorks.Interop.cosworks.ICWCompositeShellOptions.html)
[ICWCompositeShellOptions Members](SolidWorks.Interop.cosworks~SolidWorks.Interop.cosworks.ICWCompositeShellOptions_members.html)

## Availability

SOLIDWORKS Simulation API 2015 SP3
