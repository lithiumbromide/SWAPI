---
title: "Type Property (ITableAnnotation)"
project: "SOLIDWORKS API Help"
interface: "ITableAnnotation"
member: "Type"
kind: "property"
source: "sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ITableAnnotation~Type.html"
---

# Type Property (ITableAnnotation)

Gets the type of table.

## Syntax

### Visual Basic (Declaration)

```vb
ReadOnly Property Type As System.Integer
```

### Visual Basic (Usage)

```vb
Dim instance As ITableAnnotation
Dim value As System.Integer

value = instance.Type
```

### C#

```csharp
System.int Type {get;}
```

### C++/CLI

```cpp
property System.int Type {
   System.int get();
}
```

**NOTE:** See [Differences Between Unmanaged C++ and C++/CLI Code](DifferencesBetweenUnManagedAndCPPCLI.htm).

### Property Value

Type of table as defined in [swTableAnnotationType_e](ms-its:swconst.chm::/SOLIDWORKS.Interop.swconst~SOLIDWORKS.Interop.swconst.swTableAnnotationType_e.html)

## VBA Syntax

See [TableAnnotation::Type](ms-its:sldworksapivb6.chm::/sldworks~TableAnnotation~Type.html).

## Examples

[Get Table Annotation and Contents (VBA)](Get_Table_Annotation_and_Contents_Example_VB.htm)
[Insert Column in BOM Table (C#)](Insert_Column_in_BOM_Table_Example_CSharp.htm)
[Insert Column in BOM Table (VB.NET)](Insert_Column_in_BOM_Table_Example_VBNET.htm)
[Insert Column in BOM Table (VBA)](Insert_Column_in_BOM_Table_Example_VB.htm)

## See Also

[ITableAnnotation Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ITableAnnotation.html)
[ITableAnnotation Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ITableAnnotation_members.html)

## Availability

SOLIDWORKS 2004 FCS, Revisoin Number 12.0
