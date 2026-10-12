---
title: "HoleTable Property (IHoleTableAnnotation)"
project: "SOLIDWORKS API Help"
interface: "IHoleTableAnnotation"
member: "HoleTable"
kind: "property"
source: "sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IHoleTableAnnotation~HoleTable.html"
---

# HoleTable Property (IHoleTableAnnotation)

Gets the hole table feature for this table annotation.

## Syntax

### Visual Basic (Declaration)

```vb
ReadOnly Property HoleTable As HoleTable
```

### Visual Basic (Usage)

```vb
Dim instance As IHoleTableAnnotation
Dim value As HoleTable

value = instance.HoleTable
```

### C#

```csharp
HoleTable HoleTable {get;}
```

### C++/CLI

```cpp
property HoleTable^ HoleTable {
   HoleTable^ get();
}
```

**NOTE:** See [Differences Between Unmanaged C++ and C++/CLI Code](DifferencesBetweenUnManagedAndCPPCLI.htm).

### Property Value

Pointer to the [IHoleTable](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.IHoleTable.html) object

## VBA Syntax

See [HoleTableAnnotation::HoleTable](ms-its:sldworksapivb6.chm::/sldworks~HoleTableAnnotation~HoleTable.html).

## Examples

[Get Labels of Datum Origin (C#)](Get_Labels_of_Datum_Origin_Example_CSharp.htm)
[Get Labels of Datum Origin (VB.NET)](Get_Labels_of_Datum_Origin_Example_VBNET.htm)
[Get Labels of Datum Origin (VBA)](Get_Labels_of_Datum_Origin_Example_VB.htm)

## See Also

[IHoleTableAnnotation Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IHoleTableAnnotation.html)
[IHoleTableAnnotation Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IHoleTableAnnotation_members.html)

## Availability

SOLIDWORKS 2004 FCS, Revision Number 12.0
