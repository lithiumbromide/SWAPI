---
title: "InsertTableAnnotation2 Method (IDrawingDoc)"
project: "SOLIDWORKS API Help"
interface: "IDrawingDoc"
member: "InsertTableAnnotation2"
kind: "method"
source: "sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IDrawingDoc~InsertTableAnnotation2.html"
---

# InsertTableAnnotation2 Method (IDrawingDoc)

Inserts a table annotation in this drawing.

## Syntax

### Visual Basic (Declaration)

```vb
Function InsertTableAnnotation2( _
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
Dim instance As IDrawingDoc
Dim UseAnchorPoint As System.Boolean
Dim X As System.Double
Dim Y As System.Double
Dim AnchorType As System.Integer
Dim TableTemplate As System.String
Dim Rows As System.Integer
Dim Columns As System.Integer
Dim value As TableAnnotation

value = instance.InsertTableAnnotation2(UseAnchorPoint, X, Y, AnchorType, TableTemplate, Rows, Columns)
```

### C#

```csharp
TableAnnotation InsertTableAnnotation2(
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
TableAnnotation^ InsertTableAnnotation2(
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

- `UseAnchorPoint`: True to anchor the table to the general table anchor point and ignore any coordinates specified for X and Y, or false to use the coordinates specified for X and Y
- `X`: X coordinate to insert this table annotation
- `Y`: Y coordinate to insert this table annotation
- `AnchorType`: Type of anchor as defined in [swBOMConfigurationAnchorType_e](ms-its:swconst.chm::/SOLIDWORKS.Interop.swconst~SOLIDWORKS.Interop.swconst.swBOMConfigurationAnchorType_e.html) (see **Remarks**)
- `TableTemplate`: Path and filename of the general table template to use (see Remarks)
- `Rows`: Number of rows in the table annotation
- `Columns`: Number of columns in the table annotation

### Return Value

Pointer to the [ITableAnnotation](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.ITableAnnotation.html) object

## VBA Syntax

See [DrawingDoc::InsertTableAnnotation2](ms-its:sldworksapivb6.chm::/sldworks~DrawingDoc~InsertTableAnnotation2.html).

## Examples

[Insert General Table (VBA)](Insert_General_Table_Example_VB.htm)
[Get General Table Feature (C#)](Get_General_Table_Feature_Example_CSharp.htm)
[Get General Table Feature (VB.NET)](Get_General_Table_Feature_Example_VBNET.htm)
[Get General Table Feature (VBA)](Get_General_Table_Feature_Example_VB.htm)

## Remarks

| If TableTemplate is... | Then.. |
| --- | --- |
| A valid path and filename | AnchorType and Columns are ignored, and the information from the table template is used instead |
| Empty | General table is inserted based only on the other input arguments |

## See Also

[IDrawingDoc Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IDrawingDoc.html)
[IDrawingDoc Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IDrawingDoc_members.html)
[IModelDocExtension::InsertGeneralTableAnnotation Method ()](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelDocExtension~InsertGeneralTableAnnotation.html)

## Availability

SOLIDWORKS 2006 FCS, Revision Number 14.0
