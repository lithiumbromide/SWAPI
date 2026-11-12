---
title: "FamilyTableFeature Property (IFamilyTableAnnotation)"
project: "SOLIDWORKS API Help"
interface: "IFamilyTableAnnotation"
member: "FamilyTableFeature"
kind: "property"
source: "sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IFamilyTableAnnotation~FamilyTableFeature.html"
---

# FamilyTableFeature Property (IFamilyTableAnnotation)

Gets the family table feature for this annotation.

## Syntax

### Visual Basic (Declaration)

```vb
ReadOnly Property FamilyTableFeature As System.Object
```

### Visual Basic (Usage)

```vb
Dim instance As IFamilyTableAnnotation
Dim value As System.Object

value = instance.FamilyTableFeature
```

### C#

```csharp
System.object FamilyTableFeature {get;}
```

### C++/CLI

```cpp
property System.Object^ FamilyTableFeature {
   System.Object^ get();
}
```

**NOTE:** See [Differences Between Unmanaged C++ and C++/CLI Code](DifferencesBetweenUnManagedAndCPPCLI.htm).

### Property Value

[IFamilyTableFeature](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IFamilyTableFeature.html)

## VBA Syntax

See [FamilyTableAnnotation::FamilyTableFeature](ms-its:sldworksapivb6.chm::/sldworks~FamilyTableAnnotation~FamilyTableFeature.html).

## See Also

[IFamilyTableAnnotation Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IFamilyTableAnnotation.html)
[IFamilyTableAnnotation Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IFamilyTableAnnotation_members.html)

## Availability

SOLIDWORKS 2026 FCS, Revision Number 34
