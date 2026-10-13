---
title: "IGetTableAnnotations Method (IPunchTable)"
project: "SOLIDWORKS API Help"
interface: "IPunchTable"
member: "IGetTableAnnotations"
kind: "method"
source: "sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IPunchTable~IGetTableAnnotations.html"
---

# IGetTableAnnotations Method (IPunchTable)

Gets the punch table annotations for this punch table feature.

## Syntax

### Visual Basic (Declaration)

```vb
Function IGetTableAnnotations( _
   ByVal Count As System.Integer _
) As PunchTableAnnotation
```

### Visual Basic (Usage)

```vb
Dim instance As IPunchTable
Dim Count As System.Integer
Dim value As PunchTableAnnotation

value = instance.IGetTableAnnotations(Count)
```

### C#

```csharp
PunchTableAnnotation IGetTableAnnotations(
   System.int Count
)
```

### C++/CLI

```cpp
PunchTableAnnotation^ IGetTableAnnotations(
   System.int Count
)
```

**NOTE:** See [Differences Between Unmanaged C++ and C++/CLI Code](DifferencesBetweenUnManagedAndCPPCLI.htm).

### Parameters

- `Count`: Number of punch table annotations for this punch table feature (see **Remarks**)

### Return Value

- In-process, unmanaged C++: Pointer to the [IPunchTableAnnotation](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.IPunchTableAnnotation.html) objects for this punch table feature

- VBA, VB.NET, C#, and C++/CLI: Not supported

See [In-process Methods](sldworksapiprogguide.chm::/OVERVIEW/In-process_Methods.htm) for details about this type of method.

## Remarks

This method gets all of the table annotations of a split table. Many of the [ITableAnnotation](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.ITableAnnotation.html) methods and properties get table annotation information that is common to all table annotations. You should apply these [ITableAnnotation](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.ITableAnnotation.html) methods and properties to only one of the split table annotations returned by this method. Otherwise, you will get redundant data.

For example, if you change the thickness of the grid line, then changing it on one table annotation affects all splits of that table annotation. Thus, for this method, you might want to specify 1 for Count so that a single value is returned. Or, you can call [IPunchTable::GetTableAnnotationCount](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.IPunchTable~GetTableAnnotationCount.html) if you want the total number of table annotations, including any splits, for this punch table feature.

## See Also

[IPunchTable Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IPunchTable.html)
[IPunchTable Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IPunchTable_members.html)
[IPunchTable::GetTableAnnotations Method ()](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IPunchTable~GetTableAnnotations.html)

## Availability

SOLIDWORKS 2012 FCS, Revision Number 20.0
