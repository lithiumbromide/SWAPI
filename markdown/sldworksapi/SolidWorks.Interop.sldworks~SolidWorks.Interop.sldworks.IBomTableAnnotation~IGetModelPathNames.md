---
title: "IGetModelPathNames Method (IBomTableAnnotation)"
project: "SOLIDWORKS API Help"
interface: "IBomTableAnnotation"
member: "IGetModelPathNames"
kind: "method"
source: "sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IBomTableAnnotation~IGetModelPathNames.html"
---

# IGetModelPathNames Method (IBomTableAnnotation)

Gets the full pathnames of all documents in the specified row of this BOM table annotation. Also gets the item and part numbers associated with the specified row.

## Syntax

### Visual Basic (Declaration)

```vb
Function IGetModelPathNames( _
   ByVal RowIndex As System.Integer, _
   ByVal Count As System.Integer, _
   ByRef ItemNumber As System.String, _
   ByRef PartNumber As System.String _
) As System.String
```

### Visual Basic (Usage)

```vb
Dim instance As IBomTableAnnotation
Dim RowIndex As System.Integer
Dim Count As System.Integer
Dim ItemNumber As System.String
Dim PartNumber As System.String
Dim value As System.String

value = instance.IGetModelPathNames(RowIndex, Count, ItemNumber, PartNumber)
```

### C#

```csharp
System.string IGetModelPathNames(
   System.int RowIndex,
   System.int Count,
   out System.string ItemNumber,
   out System.string PartNumber
)
```

### C++/CLI

```cpp
System.String^ IGetModelPathNames(
   System.int RowIndex,
   System.int Count,
   [Out] System.String^ ItemNumber,
   [Out] System.String^ PartNumber
)
```

**NOTE:** See [Differences Between Unmanaged C++ and C++/CLI Code](DifferencesBetweenUnManagedAndCPPCLI.htm).

### Parameters

- `RowIndex`: Row in the BOM table; 0-based index
- `Count`: Number of model pathnames
- `ItemNumber`: Item number for the specified BOM table row
- `PartNumber`: Part number for the specified BOM table row

### Return Value

- in-process, unmanaged C++: Pointer to an array of model pathnames in the specified row

VBA, VB.NET, C#, and C++/CLI: Not supported

See [In-process Methods](sldworksapiprogguide.chm::/OVERVIEW/In-process_Methods.htm) for details about this type of method.

## Remarks

Before calling this method, call [IBomTableAnnotation::GetModelPathNamesCount](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.IBomTableAnnotation~GetModelPathNamesCount.html) to get the value of Count.

## See Also

[IBomTableAnnotation Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IBomTableAnnotation.html)
[IBomTableAnnotation Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IBomTableAnnotation_members.html)
[IBomTableAnnotation::GetModelPathNames Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IBomTableAnnotation~GetModelPathNames.html)

## Availability

SOLIDWORKS 2011 SP01, Revision Number 19.1
