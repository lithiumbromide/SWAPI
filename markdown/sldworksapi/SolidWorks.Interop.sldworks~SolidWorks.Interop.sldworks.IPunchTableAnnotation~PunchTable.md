---
title: "PunchTable Property (IPunchTableAnnotation)"
project: "SOLIDWORKS API Help"
interface: "IPunchTableAnnotation"
member: "PunchTable"
kind: "property"
source: "sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IPunchTableAnnotation~PunchTable.html"
---

# PunchTable Property (IPunchTableAnnotation)

Gets the punch table feature for this table annotation.

## Syntax

### Visual Basic (Declaration)

```vb
ReadOnly Property PunchTable As PunchTable
```

### Visual Basic (Usage)

```vb
Dim instance As IPunchTableAnnotation
Dim value As PunchTable

value = instance.PunchTable
```

### C#

```csharp
PunchTable PunchTable {get;}
```

### C++/CLI

```cpp
property PunchTable^ PunchTable {
   PunchTable^ get();
}
```

**NOTE:** See [Differences Between Unmanaged C++ and C++/CLI Code](DifferencesBetweenUnManagedAndCPPCLI.htm).

### Property Value

[IPunchTable](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.IPunchTable.html)

## VBA Syntax

See [PunchTableAnnotation::PunchTable](ms-its:sldworksapivb6.chm::/sldworks~PunchTableAnnotation~PunchTable.html).

## Examples

[Insert Punch Table (C#)](Insert_Punch_Table_Example_CSharp.htm)
[Insert Punch Table (VB.NET)](Insert_Punch_Table_Example_VBNET.htm)
[Insert Punch Table (VBA)](Insert_Punch_Table_Example_VB.htm)

## See Also

[IPunchTableAnnotation Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IPunchTableAnnotation.html)
[IPunchTableAnnotation Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IPunchTableAnnotation_members.html)

## Availability

SOLIDWORKS 2012 FCS, Revision Number 20.0
