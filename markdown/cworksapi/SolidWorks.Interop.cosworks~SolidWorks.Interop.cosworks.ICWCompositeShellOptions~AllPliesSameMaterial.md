---
title: "AllPliesSameMaterial Property (ICWCompositeShellOptions)"
project: "SOLIDWORKS Simulation API Help"
interface: "ICWCompositeShellOptions"
member: "AllPliesSameMaterial"
kind: "property"
source: "cworksapi/SolidWorks.Interop.cosworks~SolidWorks.Interop.cosworks.ICWCompositeShellOptions~AllPliesSameMaterial.html"
---

# AllPliesSameMaterial Property (ICWCompositeShellOptions)

Obsolete. Superseded by [ICWCompositeShellOptions::AllPliesSameMaterial2](SolidWorks.Interop.cosworks~SolidWorks.Interop.cosworks.ICWCompositeShellOptions~AllPliesSameMaterial2.html).

## Syntax

### Visual Basic (Declaration)

```vb
Property AllPliesSameMaterial As System.Integer
```

### Visual Basic (Usage)

```vb
Dim instance As ICWCompositeShellOptions
Dim value As System.Integer

instance.AllPliesSameMaterial = value

value = instance.AllPliesSameMaterial
```

### C#

```csharp
System.int AllPliesSameMaterial {get; set;}
```

### C++/CLI

```cpp
property System.int AllPliesSameMaterial {
   System.int get();
   void set (    System.int value);
}
```

### Property Value

1 applies the same material to all plies, 0 does not

## VBA Syntax

See [CWCompositeShellOptions::AllPliesSameMaterial](ms-its:cworksapivb6.chm::/CosmosWorksLib~CWCompositeShellOptions~AllPliesSameMaterial.html).

## Remarks

Before setting this property, call [ICWShell::SetLibraryMaterial](SolidWorks.Interop.cosworks~SolidWorks.Interop.cosworks.ICWShell~SetLibraryMaterial.html).

## See Also

[ICWCompositeShellOptions Interface](SolidWorks.Interop.cosworks~SolidWorks.Interop.cosworks.ICWCompositeShellOptions.html)
[ICWCompositeShellOptions Members](SolidWorks.Interop.cosworks~SolidWorks.Interop.cosworks.ICWCompositeShellOptions_members.html)

## Availability

SOLIDWORKS Simulation API 2015 SP3
