---
title: "UseSameElementSize Property (ICWMeshControl)"
project: "SOLIDWORKS Simulation API Help"
interface: "ICWMeshControl"
member: "UseSameElementSize"
kind: "property"
source: "cworksapi/SolidWorks.Interop.cosworks~SolidWorks.Interop.cosworks.ICWMeshControl~UseSameElementSize.html"
---

# UseSameElementSize Property (ICWMeshControl)

Obsolete. Superseded by [ICWMeshControl::UseSameElementSize2](SolidWorks.Interop.cosworks~SolidWorks.Interop.cosworks.ICWMeshControl~UseSameElementSize2.html).

## Syntax

### Visual Basic (Declaration)

```vb
Property UseSameElementSize As System.Integer
```

### Visual Basic (Usage)

```vb
Dim instance As ICWMeshControl
Dim value As System.Integer

instance.UseSameElementSize = value

value = instance.UseSameElementSize
```

### C#

```csharp
System.int UseSameElementSize {get; set;}
```

### C++/CLI

```cpp
property System.int UseSameElementSize {
   System.int get();
   void set (    System.int value);
}
```

### Property Value

- 1 = Use same size for all components
- 0 = Use different sizes based on component mesh control

## VBA Syntax

See [CWMeshControl::UseSameElementSize](ms-its:cworksapivb6.chm::/CosmosWorksLib~CWMeshControl~UseSameElementSize.html).

## See Also

[ICWMeshControl Interface](SolidWorks.Interop.cosworks~SolidWorks.Interop.cosworks.ICWMeshControl.html)
[ICWMeshControl Members](SolidWorks.Interop.cosworks~SolidWorks.Interop.cosworks.ICWMeshControl_members.html)
[ICWMeshControl::ElementSize Property](SolidWorks.Interop.cosworks~SolidWorks.Interop.cosworks.ICWMeshControl~ElementSize.html)
[ICWMeshControl::NumofElementsforBeams Property](SolidWorks.Interop.cosworks~SolidWorks.Interop.cosworks.ICWMeshControl~NumofElementsforBeams.html)

## Availability

SOLIDWORKS Simulation API 2008 SP1.0
