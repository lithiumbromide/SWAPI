---
title: "GetTableAnnotationCount Method (IBendTable)"
project: "SOLIDWORKS API Help"
interface: "IBendTable"
member: "GetTableAnnotationCount"
kind: "method"
source: "sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IBendTable~GetTableAnnotationCount.html"
---

# GetTableAnnotationCount Method (IBendTable)

Gets the number of bend table annotations.

## Syntax

### Visual Basic (Declaration)

```vb
Function GetTableAnnotationCount() As System.Integer
```

### Visual Basic (Usage)

```vb
Dim instance As IBendTable
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

Number of bend table annotations (see **Remarks**)

## VBA Syntax

See [BendTable::GetTableAnnotationCount](ms-its:sldworksapivb6.chm::/sldworks~BendTable~GetTableAnnotationCount.html).

## Examples

[Insert Bend Table (VBA)](Insert_Bend_Table_Example_VB.htm)
[Insert Bend Table (VB.NET)](Insert_Bend_Table_Example_VBNET.htm)
[Insert Bend Table (C#)](Insert_Bend_Table_Example_CSharp.htm)

## Remarks

There is usually only one annotation for each bend table. If a bend table is split, there are two annotations associated with it.

## See Also

[IBendTable Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IBendTable.html)
[IBendTable Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IBendTable_members.html)
[IBendTable::GetTableAnnotations Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IBendTable~GetTableAnnotations.html)
[IGetTableAnnotations Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IBendTable~IGetTableAnnotations.html)

## Availability

SOLIDWORKS 2012 FCS, Revision Number 20.0
