---
title: "DisplayedText2 Property (ITableAnnotation)"
project: "SOLIDWORKS API Help"
interface: "ITableAnnotation"
member: "DisplayedText2"
kind: "property"
source: "sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ITableAnnotation~DisplayedText2.html"
---

# DisplayedText2 Property (ITableAnnotation)

Gets the actual text displayed in the specified cell in this table.

## Syntax

### Visual Basic (Declaration)

```vb
ReadOnly Property DisplayedText2( _
   ByVal Row As System.Integer, _
   ByVal Column As System.Integer, _
   ByVal IncludeHidden As System.Boolean _
) As System.String
```

### Visual Basic (Usage)

```vb
Dim instance As ITableAnnotation
Dim Row As System.Integer
Dim Column As System.Integer
Dim IncludeHidden As System.Boolean
Dim value As System.String

value = instance.DisplayedText2(Row, Column, IncludeHidden)
```

### C#

```csharp
System.string DisplayedText2(
   System.int Row,
   System.int Column,
   System.bool IncludeHidden
) {get;}
```

### C++/CLI

```cpp
property System.String^ DisplayedText2 {
   System.String^ get(System.int Row, System.int Column, System.bool IncludeHidden);
}
```

**NOTE:** See [Differences Between Unmanaged C++ and C++/CLI Code](DifferencesBetweenUnManagedAndCPPCLI.htm).

### Parameters

- `Row`: Index of the row
- `Column`: Index of the column
- `IncludeHidden`: True to get the text displayed in the hidden cell, false to not

### Property Value

Actual text displayed in the specified cell

## VBA Syntax

See [TableAnnotation::DisplayedText2](ms-its:sldworksapivb6.chm::/sldworks~TableAnnotation~DisplayedText2.html).

## Examples

[Get Table Annotation and Contents (VBA)](Get_Table_Annotation_and_Contents_Example_VB.htm)

## Remarks

Index for both rows and columns is 0-based.

To get the parameterized string that drives this displayed text, use [ITableAnnotation::Text2](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ITableAnnotation~Text2.html).

## See Also

[ITableAnnotation Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ITableAnnotation.html)
[ITableAnnotation Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ITableAnnotation_members.html)

## Availability

SOLIDWORKS 2018 FCS, Revision Number 26.0
