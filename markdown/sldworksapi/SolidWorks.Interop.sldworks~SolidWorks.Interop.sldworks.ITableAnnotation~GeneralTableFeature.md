---
title: "GeneralTableFeature Property (ITableAnnotation)"
project: "SOLIDWORKS API Help"
interface: "ITableAnnotation"
member: "GeneralTableFeature"
kind: "property"
source: "sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ITableAnnotation~GeneralTableFeature.html"
---

# GeneralTableFeature Property (ITableAnnotation)

Gets the general table feature for this general table annotation.

## Syntax

### Visual Basic (Declaration)

```vb
ReadOnly Property GeneralTableFeature As GeneralTableFeature
```

### Visual Basic (Usage)

```vb
Dim instance As ITableAnnotation
Dim value As GeneralTableFeature

value = instance.GeneralTableFeature
```

### C#

```csharp
GeneralTableFeature GeneralTableFeature {get;}
```

### C++/CLI

```cpp
property GeneralTableFeature^ GeneralTableFeature {
   GeneralTableFeature^ get();
}
```

**NOTE:** See [Differences Between Unmanaged C++ and C++/CLI Code](DifferencesBetweenUnManagedAndCPPCLI.htm).

### Property Value

[IGeneralTableFeature](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.IGeneralTableFeature.html) object

## VBA Syntax

See [TableAnnotation::GeneralTableFeature](ms-its:sldworksapivb6.chm::/sldworks~TableAnnotation~GeneralTableFeature.html).

## See Also

[ITableAnnotation Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ITableAnnotation.html)
[ITableAnnotation Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ITableAnnotation_members.html)

## Availability

SOLIDWORKS 2006 FCS, Revision Number 14.0
