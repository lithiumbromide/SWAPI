---
title: "GetTableAnnotations Method (IPunchTable)"
project: "SOLIDWORKS API Help"
interface: "IPunchTable"
member: "GetTableAnnotations"
kind: "method"
source: "sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IPunchTable~GetTableAnnotations.html"
---

# GetTableAnnotations Method (IPunchTable)

Gets the punch table annotations for this punch table feature.

## Syntax

### Visual Basic (Declaration)

```vb
Function GetTableAnnotations() As System.Object
```

### Visual Basic (Usage)

```vb
Dim instance As IPunchTable
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

Array of [IPunchTableAnnotation](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.IPunchTableAnnotation.html) objects for this punch table feature

## VBA Syntax

See [PunchTable::GetTableAnnotations](ms-its:sldworksapivb6.chm::/sldworks~PunchTable~GetTableAnnotations.html).

## Examples

[Insert Punch Table (VBA)](Insert_Punch_Table_Example_VB.htm)
[Insert Punch Table (VB.NET)](Insert_Punch_Table_Example_VBNET.htm)
[Insert Punch Table (C#)](Insert_Punch_Table_Example_CSharp.htm)

## Remarks

This method gets all of the table annotations of a split table. Many of the [ITableAnnotation](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.ITableAnnotation.html) methods and properties get table annotation information that is common to all table annotations. You should apply these [ITableAnnotation](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.ITableAnnotation.html) methods and properties to only one of the split table annotations returned by this method. Otherwise, you will get redundant data.

## See Also

[IPunchTable Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IPunchTable.html)
[IPunchTable Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IPunchTable_members.html)
[IPunchTable::IGetTableAnnotations Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IPunchTable~IGetTableAnnotations.html)

## Availability

SOLIDWORKS 2012 FCS, Revision Number 20.0
