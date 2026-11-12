---
title: "InsertHoleTable3 Method (IView)"
project: "SOLIDWORKS API Help"
interface: "IView"
member: "InsertHoleTable3"
kind: "method"
source: "sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IView~InsertHoleTable3.html"
---

# InsertHoleTable3 Method (IView)

Inserts a hole table in this drawing view.

## Syntax

### Visual Basic (Declaration)

```vb
Function InsertHoleTable3( _
   ByVal UseAnchorPoint As System.Boolean, _
   ByVal X As System.Double, _
   ByVal Y As System.Double, _
   ByVal AnchorType As System.Integer, _
   ByVal StartValue As System.String, _
   ByVal Template As System.String, _
   ByVal TagOrder As System.Integer, _
   ByVal TagType As System.Integer, _
   ByVal ManualTags As System.Object _
) As System.Object
```

### Visual Basic (Usage)

```vb
Dim instance As IView
Dim UseAnchorPoint As System.Boolean
Dim X As System.Double
Dim Y As System.Double
Dim AnchorType As System.Integer
Dim StartValue As System.String
Dim Template As System.String
Dim TagOrder As System.Integer
Dim TagType As System.Integer
Dim ManualTags As System.Object
Dim value As System.Object

value = instance.InsertHoleTable3(UseAnchorPoint, X, Y, AnchorType, StartValue, Template, TagOrder, TagType, ManualTags)
```

### C#

```csharp
System.object InsertHoleTable3(
   System.bool UseAnchorPoint,
   System.double X,
   System.double Y,
   System.int AnchorType,
   System.string StartValue,
   System.string Template,
   System.int TagOrder,
   System.int TagType,
   System.object ManualTags
)
```

### C++/CLI

```cpp
System.Object^ InsertHoleTable3(
   System.bool UseAnchorPoint,
   System.double X,
   System.double Y,
   System.int AnchorType,
   System.String^ StartValue,
   System.String^ Template,
   System.int TagOrder,
   System.int TagType,
   System.Object^ ManualTags
)
```

**NOTE:** See [Differences Between Unmanaged C++ and C++/CLI Code](DifferencesBetweenUnManagedAndCPPCLI.htm).

### Parameters

- `UseAnchorPoint`: If true, and the sheet format anchor point exists, then insert table at the anchor point; if false, then insert the table at the location specified by the X and Y parameters
- `X`: X coordinate in meters for the anchor of this hole table
- `Y`: Y coordinate in meters for the anchor of this hole table
- `AnchorType`: Anchor type as defined by [swBomConfigurationAnchorType_e](ms-its:swconst.chm::/SOLIDWORKS.Interop.swconst~SOLIDWORKS.Interop.swconst.swBOMConfigurationAnchorType_e.html)
- `StartValue`: Starting value for the specified TagType
- `Template`: Path and filename of the hole table template that corresponds to the hole table you want to create (see Remarks)
- `TagOrder`: Tag numbering as defined in [swHoleTableTagOrder_e](ms-its:swconst.chm::/SOLIDWORKS.Interop.swconst~SOLIDWORKS.Interop.swconst.swHoleTableTagOrder_e.html)
- `TagType`: Tag type as defined in [swHoleTableTagStyle_e](ms-its:swconst.chm::/SOLIDWORKS.Interop.swconst~SOLIDWORKS.Interop.swconst.swHoleTableTagStyle_e.html)
- `ManualTags`: Array of custom tags; valid only if TagType is swHoleTableTagStyle_e.swHoleTable_ManualTags

### Return Value

[Hole table annotation](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.IHoleTableAnnotation.html)

## VBA Syntax

See [View::InsertHoleTable3](ms-its:sldworksapivb6.chm::/sldworks~View~InsertHoleTable3.html).

## Examples

[Insert Hole Table (VBA)](Insert_Hole_Table_Example_VB.htm)
[Insert Hole Table (VB.NET)](Insert_Hole_Table_Example_VBNET.htm)
[Insert Hole Table (C#)](Insert_Hole_Table_Example_CSharp.htm)

## Remarks

This method inserts a hole table with the following information for selected holes:

- Datum tag
- X-location of hole center
- Y-location of hole center
- Size of the hole

This method displays datum tags next to holes that have been pre-selected in the view. The location of the datum tags is relative to a datum origin that is also pre-selected in the view.

Before calling this method, call [IModelDocExtension::SelectByID2](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.IModelDocExtension~SelectByID2.html) to select the datum origin, hole edges, and faces (for multiple holes) as follows:

| Selection | Mark |
| --- | --- |
| Datum origin vertex | 1 |
| Hole edges and faces | 2 |
| Datum origin x axis direction reference | 4 |
| Datum origin y axis direction reference | 8 |

Specify Template using a hole table template (***.sldholtbt**):

- in install_dir\lang\`language`.
- that matches the table you want to create. For example, to insert a hole table with letter tags, specify Template using `install_dir`\lang\English\standard hole table--letters.sldholtbt.

## See Also

[IView Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IView.html)
[IView Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IView_members.html)

## Availability

SOLIDWORKS 2019 FCS, Revision Number 27.0
