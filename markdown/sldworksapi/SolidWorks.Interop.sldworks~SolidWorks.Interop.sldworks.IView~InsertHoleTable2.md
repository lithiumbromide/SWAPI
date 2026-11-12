---
title: "InsertHoleTable2 Method (IView)"
project: "SOLIDWORKS API Help"
interface: "IView"
member: "InsertHoleTable2"
kind: "method"
source: "sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IView~InsertHoleTable2.html"
---

# InsertHoleTable2 Method (IView)

Obsolete. Superseded by [IView::InsertHoleTable3](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IView~InsertHoleTable3.html).

## Syntax

### Visual Basic (Declaration)

```vb
Function InsertHoleTable2( _
   ByVal UseAnchorPoint As System.Boolean, _
   ByVal X As System.Double, _
   ByVal Y As System.Double, _
   ByVal AnchorType As System.Integer, _
   ByVal StartValue As System.String, _
   ByVal TableTemplate As System.String _
) As HoleTableAnnotation
```

### Visual Basic (Usage)

```vb
Dim instance As IView
Dim UseAnchorPoint As System.Boolean
Dim X As System.Double
Dim Y As System.Double
Dim AnchorType As System.Integer
Dim StartValue As System.String
Dim TableTemplate As System.String
Dim value As HoleTableAnnotation

value = instance.InsertHoleTable2(UseAnchorPoint, X, Y, AnchorType, StartValue, TableTemplate)
```

### C#

```csharp
HoleTableAnnotation InsertHoleTable2(
   System.bool UseAnchorPoint,
   System.double X,
   System.double Y,
   System.int AnchorType,
   System.string StartValue,
   System.string TableTemplate
)
```

### C++/CLI

```cpp
HoleTableAnnotation^ InsertHoleTable2(
   System.bool UseAnchorPoint,
   System.double X,
   System.double Y,
   System.int AnchorType,
   System.String^ StartValue,
   System.String^ TableTemplate
)
```

**NOTE:** See [Differences Between Unmanaged C++ and C++/CLI Code](DifferencesBetweenUnManagedAndCPPCLI.htm).

### Parameters

- `UseAnchorPoint`: If true, and the sheet format anchor point exists, then insert table at the anchor point; if false, then insert the table at the location specified by the X and Y parameters
- `X`: X coordinate in meters for the anchor of this hole table
- `Y`: Y coordinate in meters for the anchor of this hole table
- `AnchorType`: Anchor type as defined by [swBomConfigurationAnchorType_e](ms-its:swconst.chm::/SOLIDWORKS.Interop.swconst~SOLIDWORKS.Interop.swconst.swBOMConfigurationAnchorType_e.html)
- `StartValue`: Starting value for datum tags; a letter from A to Z, if TableTemplate uses letter tags; a positive integer, if TableTemplate uses number tags (see **Remarks**)
- `TableTemplate`: Path and filename of the table template that corresponds to the table you want to use (see Remarks)

### Return Value

[Hole table annotation](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.IHoleTableAnnotation.html)

## VBA Syntax

See [View::InsertHoleTable2](ms-its:sldworksapivb6.chm::/sldworks~View~InsertHoleTable2.html).

## Examples

[Get Labels of Datum Origin (C#)](Get_Labels_of_Datum_Origin_Example_CSharp.htm)
[Get Labels of Datum Origin (VB.NET)](Get_Labels_of_Datum_Origin_Example_VBNET.htm)
[Get Labels of Datum Origin (VBA)](Get_Labels_of_Datum_Origin_Example_VB.htm)

## Remarks

This method inserts a table with the following information for selected holes:

- Datum tag
- X-location of hole center
- Y-location of hole center
- Size

This method displays datum tags next to holes that have been pre-selected in the view. The location of the datum tags is relative to a datum origin that is also pre-selected in the view.

Before calling this method, call [IModelDocExtension::SelectByID2](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.IModelDocExtension~SelectByID2.html) to select the datum origin, hole edges, and faces (for multiple holes) as follows:

| Selection | Mark |
| --- | --- |
| Datum origin vertex | 1 |
| Hole edges and faces | 2 |
| Datum origin x axis direction reference | 4 |
| Datum origin y axis direction reference | 8 |

Specify TableTemplate using a hole table template (***.sldholtbt**) in install_dir\lang\`language`.

Specify a TableTemplate and StartValue that matches the table you want to create. For example, to insert a hole table with letter tags, specify TableTemplate using `install_dir`\lang\English\standard hole table--letters.sldholtbt and specify StartValue using a letter from A to Z.

## See Also

[IView Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IView.html)
[IView Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IView_members.html)

## Availability

SOLIDWORKS 2011 SP02, Revision 19.2
