---
title: "InsertGeneralTableAnnotation Method (IModelDocExtension)"
project: "SOLIDWORKS API Help"
interface: "IModelDocExtension"
member: "InsertGeneralTableAnnotation"
kind: "method"
source: "sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelDocExtension~InsertGeneralTableAnnotation.html"
---

# InsertGeneralTableAnnotation Method (IModelDocExtension)

Inserts the a general table annotation in this model document.

## Syntax

### Visual Basic (Declaration)

```vb
Function InsertGeneralTableAnnotation( _
   ByVal UseAnchorPoint As System.Boolean, _
   ByVal X As System.Double, _
   ByVal Y As System.Double, _
   ByVal AnchorType As System.Integer, _
   ByVal TableTemplate As System.String, _
   ByVal Rows As System.Integer, _
   ByVal Columns As System.Integer _
) As TableAnnotation
```

### Visual Basic (Usage)

```vb
Dim instance As IModelDocExtension
Dim UseAnchorPoint As System.Boolean
Dim X As System.Double
Dim Y As System.Double
Dim AnchorType As System.Integer
Dim TableTemplate As System.String
Dim Rows As System.Integer
Dim Columns As System.Integer
Dim value As TableAnnotation

value = instance.InsertGeneralTableAnnotation(UseAnchorPoint, X, Y, AnchorType, TableTemplate, Rows, Columns)
```

### C#

```csharp
TableAnnotation InsertGeneralTableAnnotation(
   System.bool UseAnchorPoint,
   System.double X,
   System.double Y,
   System.int AnchorType,
   System.string TableTemplate,
   System.int Rows,
   System.int Columns
)
```

### C++/CLI

```cpp
TableAnnotation^ InsertGeneralTableAnnotation(
   System.bool UseAnchorPoint,
   System.double X,
   System.double Y,
   System.int AnchorType,
   System.String^ TableTemplate,
   System.int Rows,
   System.int Columns
)
```

**NOTE:** See [Differences Between Unmanaged C++ and C++/CLI Code](DifferencesBetweenUnManagedAndCPPCLI.htm).

### Parameters

- `UseAnchorPoint`: True to anchor the table by AnchorType and ignore any coordinates specified by X and Y, false to use the coordinates specified by X and Y
- `X`: X coordinate of this table annotation
- `Y`: Y coordinate of this table annotation
- `AnchorType`: Type of anchor as defined in [swBOMConfigurationAnchorType_e](ms-its:swconst.chm::/SOLIDWORKS.Interop.swconst~SOLIDWORKS.Interop.swconst.swBOMConfigurationAnchorType_e.html); valid only if UseAnchorPoint is true and TableTemplate is empty (see **Remarks**)
- `TableTemplate`: Path and file name of the general table template to use (see Remarks)
- `Rows`: Number of rows in the table annotation; valid only if TableTemplate is empty (see **Remarks**)
- `Columns`: Number of columns in the table annotation; valid only if TableTemplate is empty (see **Remarks**)

### Return Value

[ITableAnnotation](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.ITableAnnotation.html)

## VBA Syntax

See [ModelDocExtension::InsertGeneralTableAnnotation](ms-its:sldworksapivb6.chm::/sldworks~ModelDocExtension~InsertGeneralTableAnnotation.html).

## Examples

[Insert General Table in Part (VBA)](Insert_General_Table_in_Part_Example_VB.htm)
[Insert General Table in Part (VB.NET)](Insert_General_Table_in_Part_Example_VBNET.htm)
[Insert General Table in Part (C#)](Insert_General_Table_in_Part_Example_CSharp.htm)

## Remarks

| If TableTemplate is... | Then.. |
| --- | --- |
| A valid path and file name | AnchorType, Rows, and Columns are ignored, and a general table based on TableTemplate is inserted |
| Empty | General table based only on all of the specified parameters, except TableTemplate, is inserted |

## See Also

[IModelDocExtension Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelDocExtension.html)
[IModelDocExtension Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelDocExtension_members.html)
[IDrawingDoc::InsertTableAnnotation2 Method ()](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IDrawingDoc~InsertTableAnnotation2.html)
[IModelDocExtension::InsertBomTable3 Method ()](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelDocExtension~InsertBomTable3.html)
[IModelDocExtension::InsertTitleBlockTable Method ()](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelDocExtension~InsertTitleBlockTable.html)
[IModelDocExtension::GetGeneralTableAnnotation Method ()](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelDocExtension~GetGeneralTableAnnotation.html)

## Availability

SOLIDWORKS 2014 FCS, Revision Number 22.0
