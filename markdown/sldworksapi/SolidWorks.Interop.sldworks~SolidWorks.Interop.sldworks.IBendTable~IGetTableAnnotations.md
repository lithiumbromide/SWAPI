---
title: "IGetTableAnnotations Method (IBendTable)"
project: "SOLIDWORKS API Help"
interface: "IBendTable"
member: "IGetTableAnnotations"
kind: "method"
source: "sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IBendTable~IGetTableAnnotations.html"
---

# IGetTableAnnotations Method (IBendTable)

Gets the annotations for this bend table.

## Syntax

### Visual Basic (Declaration)

```vb
Function IGetTableAnnotations( _
   ByVal Count As System.Integer _
) As BendTableAnnotation
```

### Visual Basic (Usage)

```vb
Dim instance As IBendTable
Dim Count As System.Integer
Dim value As BendTableAnnotation

value = instance.IGetTableAnnotations(Count)
```

### C#

```csharp
BendTableAnnotation IGetTableAnnotations(
   System.int Count
)
```

### C++/CLI

```cpp
BendTableAnnotation^ IGetTableAnnotations(
   System.int Count
)
```

**NOTE:** See [Differences Between Unmanaged C++ and C++/CLI Code](DifferencesBetweenUnManagedAndCPPCLI.htm).

### Parameters

- `Count`: Number of bend table annotations

### Return Value

- In-process, unmanaged C++: Pointer to an array of [IBendTableAnnotation](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.IBendTableAnnotation.html)s
- VBA, VB.NET, C#, and C++/CLI: Not supported

See [In-process Methods](sldworksapiprogguide.chm::/OVERVIEW/In-process_Methods.htm) for details about this type of method.

## Remarks

Before calling this method, call [IBendTable::GetTableAnnotationCount](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.IBendTable~GetTableAnnotationCount.html) to populate Count.

## See Also

[IBendTable Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IBendTable.html)
[IBendTable Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IBendTable_members.html)
[IBendTable::GetTableAnnotations Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IBendTable~GetTableAnnotations.html)

## Availability

SOLIDWORKS 2012 FCS, Revision Number 20.0
