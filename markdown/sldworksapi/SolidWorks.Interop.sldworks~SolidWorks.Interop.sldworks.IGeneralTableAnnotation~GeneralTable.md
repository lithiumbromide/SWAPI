---
title: "GeneralTable Property (IGeneralTableAnnotation)"
project: "SOLIDWORKS API Help"
interface: "IGeneralTableAnnotation"
member: "GeneralTable"
kind: "property"
source: "sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IGeneralTableAnnotation~GeneralTable.html"
---

# GeneralTable Property (IGeneralTableAnnotation)

Gets the general table feature for this annotation.

## Syntax

### Visual Basic (Declaration)

```vb
ReadOnly Property GeneralTable As GeneralTableFeature
```

### Visual Basic (Usage)

```vb
Dim instance As IGeneralTableAnnotation
Dim value As GeneralTableFeature

value = instance.GeneralTable
```

### C#

```csharp
GeneralTableFeature GeneralTable {get;}
```

### C++/CLI

```cpp
property GeneralTableFeature^ GeneralTable {
   GeneralTableFeature^ get();
}
```

**NOTE:** See [Differences Between Unmanaged C++ and C++/CLI Code](DifferencesBetweenUnManagedAndCPPCLI.htm).

### Property Value

[IGeneralTableFeature](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.IGeneralTableFeature.html)

## VBA Syntax

See [GeneralTableAnnotation::GeneralTable](ms-its:sldworksapivb6.chm::/sldworks~GeneralTableAnnotation~GeneralTable.html).

## See Also

[IGeneralTableAnnotation Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IGeneralTableAnnotation.html)
[IGeneralTableAnnotation Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IGeneralTableAnnotation_members.html)

## Availability

SOLIDWORKS 2012 FCS, Revision Number 20.0
