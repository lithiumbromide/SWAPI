---
title: "BomFeature Property (IBomTableAnnotation)"
project: "SOLIDWORKS API Help"
interface: "IBomTableAnnotation"
member: "BomFeature"
kind: "property"
source: "sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IBomTableAnnotation~BomFeature.html"
---

# BomFeature Property (IBomTableAnnotation)

Gets the BOM for this table annotation.

## Syntax

### Visual Basic (Declaration)

```vb
ReadOnly Property BomFeature As BomFeature
```

### Visual Basic (Usage)

```vb
Dim instance As IBomTableAnnotation
Dim value As BomFeature

value = instance.BomFeature
```

### C#

```csharp
BomFeature BomFeature {get;}
```

### C++/CLI

```cpp
property BomFeature^ BomFeature {
   BomFeature^ get();
}
```

**NOTE:** See [Differences Between Unmanaged C++ and C++/CLI Code](DifferencesBetweenUnManagedAndCPPCLI.htm).

### Property Value

Pointer to the [IBomFeature](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.IBomFeature.html) object for this table annotation

## VBA Syntax

See [BomTableAnnotation::BomFeature](ms-its:sldworksapivb6.chm::/sldworks~BomTableAnnotation~BomFeature.html).

## Examples

[Insert and Show BOM Table and BOM Balloon (C#)](Insert_and_Show_BOM_Table_and_BOM_Balloon_Example_CSharp.htm)
[Insert and Show BOM Table and BOM Balloon (VB.NET)](Insert_and_Show_BOM_Table_and_BOM_Balloon_Example_VBNET.htm)
[Insert and Show BOM Table and BOM Balloon (VBA)](Insert_and_Show_BOM_Table_and_BOM_Balloon_Example_VB.htm)

## See Also

[IBomTableAnnotation Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IBomTableAnnotation.html)
[IBomTableAnnotation Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IBomTableAnnotation_members.html)

## Availability

SOLIDWORKS 2004 FCS, Revision Number 12
