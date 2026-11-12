---
title: "IgnoreComplexSurfaces Property (IDragOperator)"
project: "SOLIDWORKS API Help"
interface: "IDragOperator"
member: "IgnoreComplexSurfaces"
kind: "property"
source: "sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IDragOperator~IgnoreComplexSurfaces.html"
---

# IgnoreComplexSurfaces Property (IDragOperator)

Gets or sets whether complex surfaces are ignored.

## Syntax

### Visual Basic (Declaration)

```vb
Property IgnoreComplexSurfaces As System.Boolean
```

### Visual Basic (Usage)

```vb
Dim instance As IDragOperator
Dim value As System.Boolean

instance.IgnoreComplexSurfaces = value

value = instance.IgnoreComplexSurfaces
```

### C#

```csharp
System.bool IgnoreComplexSurfaces {get; set;}
```

### C++/CLI

```cpp
property System.bool IgnoreComplexSurfaces {
   System.bool get();
   void set (    System.bool value);
}
```

**NOTE:** See [Differences Between Unmanaged C++ and C++/CLI Code](DifferencesBetweenUnManagedAndCPPCLI.htm).

### Property Value

True ignores complex surfaces, false does not

## VBA Syntax

See [DragOperator::IgnoreComplexSurfaces](ms-its:sldworksapivb6.chm::/sldworks~DragOperator~IgnoreComplexSurfaces.html).

## See Also

[IDragOperator Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IDragOperator.html)
[IDragOperator Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IDragOperator_members.html)

## Availability

SOLIDWORKS 2001Plus FCS, Revision Number 10.0
