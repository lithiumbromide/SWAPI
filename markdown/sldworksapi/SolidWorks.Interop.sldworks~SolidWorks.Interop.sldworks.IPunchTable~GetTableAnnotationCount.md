---
title: "GetTableAnnotationCount Method (IPunchTable)"
project: "SOLIDWORKS API Help"
interface: "IPunchTable"
member: "GetTableAnnotationCount"
kind: "method"
source: "sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IPunchTable~GetTableAnnotationCount.html"
---

# GetTableAnnotationCount Method (IPunchTable)

Gets the number of punch table annotations for this punch table.

## Syntax

### Visual Basic (Declaration)

```vb
Function GetTableAnnotationCount() As System.Integer
```

### Visual Basic (Usage)

```vb
Dim instance As IPunchTable
Dim value As System.Integer

value = instance.GetTableAnnotationCount()
```

### C#

```csharp
System.int GetTableAnnotationCount()
```

### C++/CLI

```cpp
System.int GetTableAnnotationCount();
```

**NOTE:** See [Differences Between Unmanaged C++ and C++/CLI Code](DifferencesBetweenUnManagedAndCPPCLI.htm).

### Return Value

Number of punch table annotations for this punch table (see **Remarks**)

## VBA Syntax

See [PunchTable::GetTableAnnotationCount](ms-its:sldworksapivb6.chm::/sldworks~PunchTable~GetTableAnnotationCount.html).

## Examples

[Insert Punch Table (C#)](Insert_Punch_Table_Example_CSharp.htm)
[Insert Punch Table (VB.NET)](Insert_Punch_Table_Example_VBNET.htm)
[Insert Punch Table (VBA)](Insert_Punch_Table_Example_VB.htm)

## Remarks

Normally there is one punch table annotation per punch table feature. Split tables have two separate table annotations.

Call this method before calling [IPunchTable::IGetTableAnnotations](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.IPunchTable~IGetTableAnnotations.html) to get the total number of table annotations in the punch table, including split table annotations.

## See Also

[IPunchTable Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IPunchTable.html)
[IPunchTable Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IPunchTable_members.html)
[IPunchTable::GetTableAnnotations Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IPunchTable~GetTableAnnotations.html)

## Availability

SOLIDWORKS 2012 FCS, Revision Number 20.0
