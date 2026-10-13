---
title: "GetTableAnnotationCount Method (IHoleTable)"
project: "SOLIDWORKS API Help"
interface: "IHoleTable"
member: "GetTableAnnotationCount"
kind: "method"
source: "sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IHoleTable~GetTableAnnotationCount.html"
---

# GetTableAnnotationCount Method (IHoleTable)

Gets the number of hole table annotations for this hole table.

## Syntax

### Visual Basic (Declaration)

```vb
Function GetTableAnnotationCount() As System.Integer
```

### Visual Basic (Usage)

```vb
Dim instance As IHoleTable
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

Number of hole table annotations for this hole table (see **Remarks**)

## VBA Syntax

See [HoleTable::GetTableAnnotationCount](ms-its:sldworksapivb6.chm::/sldworks~HoleTable~GetTableAnnotationCount.html).

## Remarks

Normally there is one hole table annotation per hole table feature. For example, if you split the table, then there are two separate table annotations.

Call this method before calling [IHoleTable::IGetTableAnnotations](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.IHoleTable~IGetTableAnnotations.html) if you want to get the total number of table annotations in the hole table, including split table annotations.

## See Also

[IHoleTable Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IHoleTable.html)
[IHoleTable Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IHoleTable_members.html)
[IHoleTable::GetTableAnnotations Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IHoleTable~GetTableAnnotations.html)

## Availability

SOLIDWORKS 2004 FCS, Revision Number 12.0
