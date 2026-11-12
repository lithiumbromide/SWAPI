---
title: "Suppressed Property (ISketchRelation)"
project: "SOLIDWORKS API Help"
interface: "ISketchRelation"
member: "Suppressed"
kind: "property"
source: "sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISketchRelation~Suppressed.html"
---

# Suppressed Property (ISketchRelation)

Gets or sets whether this relation is suppressed or not.

## Syntax

### Visual Basic (Declaration)

```vb
Property Suppressed As System.Boolean
```

### Visual Basic (Usage)

```vb
Dim instance As ISketchRelation
Dim value As System.Boolean

instance.Suppressed = value

value = instance.Suppressed
```

### C#

```csharp
System.bool Suppressed {get; set;}
```

### C++/CLI

```cpp
property System.bool Suppressed {
   System.bool get();
   void set (    System.bool value);
}
```

**NOTE:** See [Differences Between Unmanaged C++ and C++/CLI Code](DifferencesBetweenUnManagedAndCPPCLI.htm).

### Property Value

True the relation is suppressed, false it is not

## VBA Syntax

See [SketchRelation::Suppressed](ms-its:sldworksapivb6.chm::/sldworks~SketchRelation~Suppressed.html).

## Examples

[Replace Sketch Relation (VBA)](Replace_Sketch_Relation_Example_VB.htm)

## See Also

[ISketchRelation Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISketchRelation.html)
[ISketchRelation Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISketchRelation_members.html)

## Availability

SOLIDWORKS 2007 FCS, Revision Number 15.0
