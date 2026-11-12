---
title: "Sandwich Property (ICWCompositeShellOptions)"
project: "SOLIDWORKS Simulation API Help"
interface: "ICWCompositeShellOptions"
member: "Sandwich"
kind: "property"
source: "cworksapi/SolidWorks.Interop.cosworks~SolidWorks.Interop.cosworks.ICWCompositeShellOptions~Sandwich.html"
---

# Sandwich Property (ICWCompositeShellOptions)

Obsolete. Superseded by [ICWCompositeShellOptions::Sandwich2](SolidWorks.Interop.cosworks~SolidWorks.Interop.cosworks.ICWCompositeShellOptions~Sandwich2.html).

## Syntax

### Visual Basic (Declaration)

```vb
Property Sandwich As System.Integer
```

### Visual Basic (Usage)

```vb
Dim instance As ICWCompositeShellOptions
Dim value As System.Integer

instance.Sandwich = value

value = instance.Sandwich
```

### C#

```csharp
System.int Sandwich {get; set;}
```

### C++/CLI

```cpp
property System.int Sandwich {
   System.int get();
   void set (    System.int value);
}
```

### Property Value

1 to use the sandwich composite formulation, 0 to not

## VBA Syntax

See [CWCompositeShellOptions::Sandwich](ms-its:cworksapivb6.chm::/CosmosWorksLib~CWCompositeShellOptions~Sandwich.html).

## See Also

[ICWCompositeShellOptions Interface](SolidWorks.Interop.cosworks~SolidWorks.Interop.cosworks.ICWCompositeShellOptions.html)
[ICWCompositeShellOptions Members](SolidWorks.Interop.cosworks~SolidWorks.Interop.cosworks.ICWCompositeShellOptions_members.html)
[ICWCompositeShellOptions::SetTotalPlies Method ()](SolidWorks.Interop.cosworks~SolidWorks.Interop.cosworks.ICWCompositeShellOptions~SetTotalPlies.html)
[ICWCompositeShellOptions::Symmetric Property ()](SolidWorks.Interop.cosworks~SolidWorks.Interop.cosworks.ICWCompositeShellOptions~Symmetric.html)

## Availability

SOLIDWORKS Simulation API 2015 SP3
