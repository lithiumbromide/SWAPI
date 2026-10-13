---
title: "GetModelPathNames Method (IBomTableAnnotation)"
project: "SOLIDWORKS API Help"
interface: "IBomTableAnnotation"
member: "GetModelPathNames"
kind: "method"
source: "sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IBomTableAnnotation~GetModelPathNames.html"
---

# GetModelPathNames Method (IBomTableAnnotation)

Gets the full pathnames of all documents in the specified row of this BOM table annotation. Also gets the item and part numbers associated with the specified row.

## Syntax

### Visual Basic (Declaration)

```vb
Function GetModelPathNames( _
   ByVal RowIndex As System.Integer, _
   ByRef ItemNumber As System.String, _
   ByRef PartNumber As System.String _
) As System.Object
```

### Visual Basic (Usage)

```vb
Dim instance As IBomTableAnnotation
Dim RowIndex As System.Integer
Dim ItemNumber As System.String
Dim PartNumber As System.String
Dim value As System.Object

value = instance.GetModelPathNames(RowIndex, ItemNumber, PartNumber)
```

### C#

```csharp
System.object GetModelPathNames(
   System.int RowIndex,
   out System.string ItemNumber,
   out System.string PartNumber
)
```

### C++/CLI

```cpp
System.Object^ GetModelPathNames(
   System.int RowIndex,
   [Out] System.String^ ItemNumber,
   [Out] System.String^ PartNumber
)
```

**NOTE:** See [Differences Between Unmanaged C++ and C++/CLI Code](DifferencesBetweenUnManagedAndCPPCLI.htm).

### Parameters

- `RowIndex`: Row in the BOM table; 0-based index
- `ItemNumber`: Item number for the specified BOM table row
- `PartNumber`: Part number for the specified BOM table row

### Return Value

Array of full pathnames of the models in the specified BOM table row

## VBA Syntax

See [BomTableAnnotation::GetModelPathNames](ms-its:sldworksapivb6.chm::/sldworks~BomTableAnnotation~GetModelPathNames.html).

## Examples

[Get Model Pathnames in BOM Table (C#)](Get_Model_Path_Names_in_BOM_Table_Example_CSharp.htm)
[Get Model Pathnames in BOM Table (VB.NET)](Get_Model_Path_Names_in_BOM_Table_Example_VBNET.htm)
[Get Model Pathnames in BOM Table (VBA)](Get_Model_Path_Names_in_BOM_Table_Example_VB.htm)

## See Also

[IBomTableAnnotation Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IBomTableAnnotation.html)
[IBomTableAnnotation Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IBomTableAnnotation_members.html)
[IBomTableAnnotation::IGetModelPathNames Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IBomTableAnnotation~IGetModelPathNames.html)
[IBomTableAnnotation::GetModelPathNamesCount Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IBomTableAnnotation~GetModelPathNamesCount.html)

## Availability

SOLIDWORKS 2011 SP01, Revision Number 19.1
