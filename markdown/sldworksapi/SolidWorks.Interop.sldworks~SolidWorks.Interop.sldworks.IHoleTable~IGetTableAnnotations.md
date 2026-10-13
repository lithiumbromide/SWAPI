---
title: "IGetTableAnnotations Method (IHoleTable)"
project: "SOLIDWORKS API Help"
interface: "IHoleTable"
member: "IGetTableAnnotations"
kind: "method"
source: "sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IHoleTable~IGetTableAnnotations.html"
---

# IGetTableAnnotations Method (IHoleTable)

Gets the hole table annotations for this hole table feature.

## Syntax

### Visual Basic (Declaration)

```vb
Function IGetTableAnnotations( _
   ByVal Count As System.Integer _
) As HoleTableAnnotation
```

### Visual Basic (Usage)

```vb
Dim instance As IHoleTable
Dim Count As System.Integer
Dim value As HoleTableAnnotation

value = instance.IGetTableAnnotations(Count)
```

### C#

```csharp
HoleTableAnnotation IGetTableAnnotations(
   System.int Count
)
```

### C++/CLI

```cpp
HoleTableAnnotation^ IGetTableAnnotations(
   System.int Count
)
```

**NOTE:** See [Differences Between Unmanaged C++ and C++/CLI Code](DifferencesBetweenUnManagedAndCPPCLI.htm).

### Parameters

- `Count`: Number of hole table annotations for this hole table feature (see **Remarks**)

### Return Value

- in-process, unmanaged C++: Pointer to the [IHoleTableAnnotation](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.IHoleTableAnnotation.html) objects for this hole table feature

VBA, VB.NET, C#, and C++/CLI: Not supported

See [In-process Methods](sldworksapiprogguide.chm::/OVERVIEW/In-process_Methods.htm) for details about this type of method.

## Remarks

Because many of the [ITableAnnotation](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.ITableAnnotation.html) APIs apply to all parts of a table annotation that has been split, you might not want all of the table annotations when just one table annotation would be sufficient.

For example, if you change the thickness of the grid line, then changing it on one table annotation affects all splits of that table annotation. Thus, for this method, you might want to specify 1 for Count so that a single value is returned. Or, you can call [IHoleTable::GetTableAnnotationCount](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.IHoleTable~GetTableAnnotationCount.html) if you want the total number of table annotations, including any splits, for this hole table feature.

## See Also

[IHoleTable Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IHoleTable.html)
[IHoleTable Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IHoleTable_members.html)

## Availability

SOLIDWORKS 2004 FCS, Revision Number 12.0
