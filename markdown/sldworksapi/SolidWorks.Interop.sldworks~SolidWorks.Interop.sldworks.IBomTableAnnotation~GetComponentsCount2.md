---
title: "GetComponentsCount2 Method (IBomTableAnnotation)"
project: "SOLIDWORKS API Help"
interface: "IBomTableAnnotation"
member: "GetComponentsCount2"
kind: "method"
source: "sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IBomTableAnnotation~GetComponentsCount2.html"
---

# GetComponentsCount2 Method (IBomTableAnnotation)

Gets the number of components, the item number, and the part number in the specified row for the specified configuration in this BOM table annotation.

## Syntax

### Visual Basic (Declaration)

```vb
Function GetComponentsCount2( _
   ByVal RowIndex As System.Integer, _
   ByVal Configuration As System.String, _
   ByRef ItemNumber As System.String, _
   ByRef PartNumber As System.String _
) As System.Integer
```

### Visual Basic (Usage)

```vb
Dim instance As IBomTableAnnotation
Dim RowIndex As System.Integer
Dim Configuration As System.String
Dim ItemNumber As System.String
Dim PartNumber As System.String
Dim value As System.Integer

value = instance.GetComponentsCount2(RowIndex, Configuration, ItemNumber, PartNumber)
```

### C#

```csharp
System.int GetComponentsCount2(
   System.int RowIndex,
   System.string Configuration,
   out System.string ItemNumber,
   out System.string PartNumber
)
```

### C++/CLI

```cpp
System.int GetComponentsCount2(
   System.int RowIndex,
   System.String^ Configuration,
   [Out] System.String^ ItemNumber,
   [Out] System.String^ PartNumber
)
```

**NOTE:** See [Differences Between Unmanaged C++ and C++/CLI Code](DifferencesBetweenUnManagedAndCPPCLI.htm).

### Parameters

- `RowIndex`: Row in the BOM table where to get the number of components; 0-based index
- `Configuration`: Configuration for which to count components in top-level only BOMs; specify an empty string for parts only and indented BOMs
- `ItemNumber`: Item number of the specified row
- `PartNumber`: Part number of the specified row

### Return Value

Number of components in the specified row for the specified configuration

## VBA Syntax

See [BomTableAnnotation::GetComponentsCount2](ms-its:sldworksapivb6.chm::/sldworks~BomTableAnnotation~GetComponentsCount2.html).

## Examples

[Get Components in Each BOM Table Row (VBA)](Get_Components_in_Each_BOM_Table_Row_VB.htm)
[Get Components in Each BOM Table Row (VB.NET)](Get_Components_in_Each_BOM_Table_Row_Example_VBNET.htm)
[Get Components in Each BOM Table Row (C#)](Get_Components_in_Each_BOM_Table_Row_Example_CSharp.htm)

## Remarks

Call this method before calling [IBomTableAnnotation::IGetComponents2](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.IBomTableAnnotation~IGetComponents2.html) to determine the size of the array for that method.

## See Also

[IBomTableAnnotation Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IBomTableAnnotation.html)
[IBomTableAnnotation Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IBomTableAnnotation_members.html)
[IBomTableAnnotation::GetComponents2 Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IBomTableAnnotation~GetComponents2.html)

## Availability

SOLIDWORKS 2011 SP03 , Revision Number 19.3
