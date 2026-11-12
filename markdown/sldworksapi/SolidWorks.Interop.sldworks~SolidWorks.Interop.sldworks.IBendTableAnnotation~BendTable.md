---
title: "BendTable Property (IBendTableAnnotation)"
project: "SOLIDWORKS API Help"
interface: "IBendTableAnnotation"
member: "BendTable"
kind: "property"
source: "sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IBendTableAnnotation~BendTable.html"
---

# BendTable Property (IBendTableAnnotation)

Gets the bend table feature for this bend table annotation.

## Syntax

### Visual Basic (Declaration)

```vb
ReadOnly Property BendTable As BendTable
```

### Visual Basic (Usage)

```vb
Dim instance As IBendTableAnnotation
Dim value As BendTable

value = instance.BendTable
```

### C#

```csharp
BendTable BendTable {get;}
```

### C++/CLI

```cpp
property BendTable^ BendTable {
   BendTable^ get();
}
```

**NOTE:** See [Differences Between Unmanaged C++ and C++/CLI Code](DifferencesBetweenUnManagedAndCPPCLI.htm).

### Property Value

[IBendTable](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.IBendTable.html)

## VBA Syntax

See [BendTableAnnotation::BendTable](ms-its:sldworksapivb6.chm::/sldworks~BendTableAnnotation~BendTable.html).

## Examples

[Insert Bend Table (C#)](Insert_Bend_Table_Example_CSharp.htm)
[Insert Bend Table (VB.NET)](Insert_Bend_Table_Example_VBNET.htm)
[Insert Bend Table (VBA)](Insert_Bend_Table_Example_VB.htm)

## See Also

[IBendTableAnnotation Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IBendTableAnnotation.html)
[IBendTableAnnotation Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IBendTableAnnotation_members.html)

## Availability

SOLIDWORKS 2012 FCS, Revision Number 20.0
