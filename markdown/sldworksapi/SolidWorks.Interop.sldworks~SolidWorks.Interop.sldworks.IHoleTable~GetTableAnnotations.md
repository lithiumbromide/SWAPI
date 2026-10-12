---
title: "GetTableAnnotations Method (IHoleTable)"
project: "SOLIDWORKS API Help"
interface: "IHoleTable"
member: "GetTableAnnotations"
kind: "method"
source: "sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IHoleTable~GetTableAnnotations.html"
---

# GetTableAnnotations Method (IHoleTable)

Gets the hole table annotations for this hole table feature.

## Syntax

### Visual Basic (Declaration)

```vb
Function GetTableAnnotations() As System.Object
```

### Visual Basic (Usage)

```vb
Dim instance As IHoleTable
Dim value As System.Object

value = instance.GetTableAnnotations()
```

### C#

```csharp
System.object GetTableAnnotations()
```

### C++/CLI

```cpp
System.Object^ GetTableAnnotations();
```

**NOTE:** See [Differences Between Unmanaged C++ and C++/CLI Code](DifferencesBetweenUnManagedAndCPPCLI.htm).

### Return Value

Array of [IHoleTableAnnotation](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.IHoleTableAnnotation.html) objects for this hole table feature

## VBA Syntax

See [HoleTable::GetTableAnnotations](ms-its:sldworksapivb6.chm::/sldworks~HoleTable~GetTableAnnotations.html).

## Examples

[Hide or Show First Column in Hole Table (VB.NET)](Hide_or_Show_First_Column_in_Hole_Table_Example_VBNET.htm)
[Hide or Show First Column in Hole Table (VBA)](Hide_or_Show_First_Column_in_Hole_Table_Example_VB.htm)
[Hide or Show First Column in Hole Table (C#)](Hide_or_Show_First_Column_in_Hole_Table_Example_CSharp.htm)

## Remarks

Because many of the [ITableAnnotation](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.ITableAnnotation.html) APIs apply to all parts of a table annotation that has been split, you might not want all of the table annotations when just one table annotation would be sufficient.

## See Also

[IHoleTable Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IHoleTable.html)
[IHoleTable Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IHoleTable_members.html)
[IHoleTable::GetTableAnnotationCount Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IHoleTable~GetTableAnnotationCount.html)
[IHoleTable::IGetTableAnnotations Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IHoleTable~IGetTableAnnotations.html)

## Availability

SOLIDWORKS 2004 FCS, Revision Number 12.0
