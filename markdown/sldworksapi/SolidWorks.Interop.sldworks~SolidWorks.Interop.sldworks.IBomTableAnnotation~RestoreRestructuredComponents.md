---
title: "RestoreRestructuredComponents Method (IBomTableAnnotation)"
project: "SOLIDWORKS API Help"
interface: "IBomTableAnnotation"
member: "RestoreRestructuredComponents"
kind: "method"
source: "sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IBomTableAnnotation~RestoreRestructuredComponents.html"
---

# RestoreRestructuredComponents Method (IBomTableAnnotation)

Restores the previously dissolved subassembly or weldment at the specified row index of this BOM table annotation.

## Syntax

### Visual Basic (Declaration)

```vb
Function RestoreRestructuredComponents( _
   ByVal RowIndex As System.Integer _
) As System.Boolean
```

### Visual Basic (Usage)

```vb
Dim instance As IBomTableAnnotation
Dim RowIndex As System.Integer
Dim value As System.Boolean

value = instance.RestoreRestructuredComponents(RowIndex)
```

### C#

```csharp
System.bool RestoreRestructuredComponents(
   System.int RowIndex
)
```

### C++/CLI

```cpp
System.bool RestoreRestructuredComponents(
   System.int RowIndex
)
```

**NOTE:** See [Differences Between Unmanaged C++ and C++/CLI Code](DifferencesBetweenUnManagedAndCPPCLI.htm).

### Parameters

- `RowIndex`: 1-based row index, if more than one subassembly or weldment are dissolved; 0, if only one subassembly or weldment is dissolved

### Return Value

True if the subassembly or weldment is restored, false if not

## VBA Syntax

See [BomTableAnnotation::RestoreRestructuredComponents](ms-its:sldworksapivb6.chm::/sldworks~BomTableAnnotation~RestoreRestructuredComponents.html).

## Examples

[Dissolve Subassembly in a BOM Table (VBA)](Dissolve_Subassembly_in_a_BOM_Table_Example_VB.htm)
[Dissolve Subassembly in a BOM Table (VB.NET)](Dissolve_Subassembly_in_a_BOM_Table_Example_VBNET.htm)
[Dissolve Subassembly in a BOM Table (C#)](Dissolve_Subassembly_in_a_BOM_Table_Example_CSharp.htm)

## See Also

[IBomTableAnnotation Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IBomTableAnnotation.html)
[IBomTableAnnotation Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IBomTableAnnotation_members.html)
[IBomTableAnnotation::Dissolve Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IBomTableAnnotation~Dissolve.html)

## Availability

SOLIDWORKS 2012 SP5, Revision Number 20.5
