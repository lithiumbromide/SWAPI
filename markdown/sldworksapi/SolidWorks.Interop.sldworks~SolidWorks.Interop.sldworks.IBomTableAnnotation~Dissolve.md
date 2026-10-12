---
title: "Dissolve Method (IBomTableAnnotation)"
project: "SOLIDWORKS API Help"
interface: "IBomTableAnnotation"
member: "Dissolve"
kind: "method"
source: "sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IBomTableAnnotation~Dissolve.html"
---

# Dissolve Method (IBomTableAnnotation)

Dissolves into individual components the subassembly or weldment at the specified row index of this BOM table annotation.

## Syntax

### Visual Basic (Declaration)

```vb
Function Dissolve( _
   ByVal RowIndex As System.Integer _
) As System.Boolean
```

### Visual Basic (Usage)

```vb
Dim instance As IBomTableAnnotation
Dim RowIndex As System.Integer
Dim value As System.Boolean

value = instance.Dissolve(RowIndex)
```

### C#

```csharp
System.bool Dissolve(
   System.int RowIndex
)
```

### C++/CLI

```cpp
System.bool Dissolve(
   System.int RowIndex
)
```

**NOTE:** See [Differences Between Unmanaged C++ and C++/CLI Code](DifferencesBetweenUnManagedAndCPPCLI.htm).

### Parameters

- `RowIndex`: 1-based row index of the subassembly or weldment to dissolve

### Return Value

True if the subassembly or weldment is dissolved, false if not

## VBA Syntax

See [BomTableAnnotation::Dissolve](ms-its:sldworksapivb6.chm::/sldworks~BomTableAnnotation~Dissolve.html).

## Examples

[Dissolve Subassembly in a BOM Table (VBA)](Dissolve_Subassembly_in_a_BOM_Table_Example_VB.htm)
[Dissolve Subassembly in a BOM Table (VB.NET)](Dissolve_Subassembly_in_a_BOM_Table_Example_VBNET.htm)
[Dissolve Subassembly in a BOM Table (C#)](Dissolve_Subassembly_in_a_BOM_Table_Example_CSharp.htm)

## See Also

[IBomTableAnnotation Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IBomTableAnnotation.html)
[IBomTableAnnotation Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IBomTableAnnotation_members.html)
[IBomTableAnnotation::RestoreRestructuredComponents Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IBomTableAnnotation~RestoreRestructuredComponents.html)
[IBomTableAnnotation::Collapse Method ()](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IBomTableAnnotation~Collapse.html)
[IBomTableAnnotation::Expand Method ()](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IBomTableAnnotation~Expand.html)

## Availability

SOLIDWORKS 2012 SP5, Revision Number 20.5
