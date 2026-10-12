---
title: "GetComponents2 Method (IBomTableAnnotation)"
project: "SOLIDWORKS API Help"
interface: "IBomTableAnnotation"
member: "GetComponents2"
kind: "method"
source: "sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IBomTableAnnotation~GetComponents2.html"
---

# GetComponents2 Method (IBomTableAnnotation)

Gets the components in the specified row for the specified configuration in this BOM table annotation.

## Syntax

### Visual Basic (Declaration)

```vb
Function GetComponents2( _
   ByVal RowIndex As System.Integer, _
   ByVal Configuration As System.String _
) As System.Object
```

### Visual Basic (Usage)

```vb
Dim instance As IBomTableAnnotation
Dim RowIndex As System.Integer
Dim Configuration As System.String
Dim value As System.Object

value = instance.GetComponents2(RowIndex, Configuration)
```

### C#

```csharp
System.object GetComponents2(
   System.int RowIndex,
   System.string Configuration
)
```

### C++/CLI

```cpp
System.Object^ GetComponents2(
   System.int RowIndex,
   System.String^ Configuration
)
```

**NOTE:** See [Differences Between Unmanaged C++ and C++/CLI Code](DifferencesBetweenUnManagedAndCPPCLI.htm).

### Parameters

- `RowIndex`: Row in the BOM table where to get the components; 0-based index
- `Configuration`: Configuration for which to get components in top-level only BOMs; specify an empty string for parts only and indented BOMs

### Return Value

Array of [components](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.IComponent2.html) in the specified row for the specified configuration

## VBA Syntax

See [BomTableAnnotation::GetComponents2](ms-its:sldworksapivb6.chm::/sldworks~BomTableAnnotation~GetComponents2.html).

## Examples

[Get Components in Each BOM Table Row (VBA)](Get_Components_in_Each_BOM_Table_Row_VB.htm)
[Get Components in Each BOM Table Row (VB.NET)](Get_Components_in_Each_BOM_Table_Row_Example_VBNET.htm)
[Get Components in Each BOM Table Row (C#)](Get_Components_in_Each_BOM_Table_Row_Example_CSharp.htm)

## See Also

[IBomTableAnnotation Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IBomTableAnnotation.html)
[IBomTableAnnotation Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IBomTableAnnotation_members.html)
[IBomTableAnnotation::GetComponentsCount2 Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IBomTableAnnotation~GetComponentsCount2.html)
[IBomTableAnnotation::IGetComponents2 Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IBomTableAnnotation~IGetComponents2.html)

## Availability

SOLIDWORKS 2011 SP03 , Revision Number 19.3
