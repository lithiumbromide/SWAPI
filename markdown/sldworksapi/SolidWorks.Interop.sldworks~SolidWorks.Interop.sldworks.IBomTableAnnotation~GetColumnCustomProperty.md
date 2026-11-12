---
title: "GetColumnCustomProperty Method (IBomTableAnnotation)"
project: "SOLIDWORKS API Help"
interface: "IBomTableAnnotation"
member: "GetColumnCustomProperty"
kind: "method"
source: "sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IBomTableAnnotation~GetColumnCustomProperty.html"
---

# GetColumnCustomProperty Method (IBomTableAnnotation)

Gets the custom property used to fill the values in a specified user-defined column.

## Syntax

### Visual Basic (Declaration)

```vb
Function GetColumnCustomProperty( _
   ByVal Index As System.Integer _
) As System.String
```

### Visual Basic (Usage)

```vb
Dim instance As IBomTableAnnotation
Dim Index As System.Integer
Dim value As System.String

value = instance.GetColumnCustomProperty(Index)
```

### C#

```csharp
System.string GetColumnCustomProperty(
   System.int Index
)
```

### C++/CLI

```cpp
System.String^ GetColumnCustomProperty(
   System.int Index
)
```

**NOTE:** See [Differences Between Unmanaged C++ and C++/CLI Code](DifferencesBetweenUnManagedAndCPPCLI.htm).

### Parameters

- `Index`: Column from which to get the custom property

### Return Value

Custom property used to fill the values in this user-defined column

## VBA Syntax

See [BomTableAnnotation::GetColumnCustomProperty](ms-its:sldworksapivb6.chm::/sldworks~BomTableAnnotation~GetColumnCustomProperty.html).

## Examples

[Get Custom Properties for BOM Table Columns (VBA)](Get_Custom_Properties_for_BOM_Table_Columns_Example_VB.htm)

## Remarks

This method will return an empty string if the column is not a user-defined column.

To get the list of custom properties, use [IBomTableAnnotation::GetAllCustomProperties](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.IBomTableAnnotation~GetAllCustomProperties.html) or [IBomTableAnnotation::IGetAllCustomProperties](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.IBomTableAnnotation~IGetAllCustomProperties.html). The list of possible custom properties includes all of the items in the BOM table, which includes items from the file summary items and file custom properties that have been set.

## See Also

[IBomTableAnnotation Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IBomTableAnnotation.html)
[IBomTableAnnotation Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IBomTableAnnotation_members.html)
[IBomTableAnnotation::GetAllCustomPropertiesCount Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IBomTableAnnotation~GetAllCustomPropertiesCount.html)
[IBomTableAnnotation::SetColumnCustomProperty Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IBomTableAnnotation~SetColumnCustomProperty.html)

## Availability

SOLIDWORKS 2004 SP1, Revision number 12
