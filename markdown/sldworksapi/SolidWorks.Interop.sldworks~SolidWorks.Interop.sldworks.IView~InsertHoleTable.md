---
title: "InsertHoleTable Method (IView)"
project: "SOLIDWORKS API Help"
interface: "IView"
member: "InsertHoleTable"
kind: "method"
source: "sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IView~InsertHoleTable.html"
---

# InsertHoleTable Method (IView)

Obsolete. Superseded by [IView::InsertHoleTable2](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.IView~InsertHoleTable2.html).

## Syntax

### Visual Basic (Declaration)

```vb
Function InsertHoleTable( _
   ByVal UseAnchorPoint As System.Boolean, _
   ByVal X As System.Double, _
   ByVal Y As System.Double, _
   ByVal AnchorType As System.Integer, _
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
Dim TableTemplate As System.String
Dim value As HoleTableAnnotation

value = instance.InsertHoleTable(UseAnchorPoint, X, Y, AnchorType, TableTemplate)
```

### C#

```csharp
HoleTableAnnotation InsertHoleTable(
   System.bool UseAnchorPoint,
   System.double X,
   System.double Y,
   System.int AnchorType,
   System.string TableTemplate
)
```

### C++/CLI

```cpp
HoleTableAnnotation^ InsertHoleTable(
   System.bool UseAnchorPoint,
   System.double X,
   System.double Y,
   System.int AnchorType,
   System.String^ TableTemplate
)
```

**NOTE:** See [Differences Between Unmanaged C++ and C++/CLI Code](DifferencesBetweenUnManagedAndCPPCLI.htm).

### Parameters

- `UseAnchorPoint`: If True and the appropriate sheet format anchor point exists, then insert table at this point; if false, then use the values specified for the X and Y arguments as the insertion point
- `X`: X coordinate for the placement of this hole table
- `Y`: Y coordinate for the placement of this hole table
- `AnchorType`: Anchor type as defined by [swBomConfigurationAnchorType_e](ms-its:swconst.chm::/SOLIDWORKS.Interop.swconst~SOLIDWORKS.Interop.swconst.swBOMConfigurationAnchorType_e.html)
- `TableTemplate`: Path and filename of the template that you want to use that corresponds to this type of table (see Remarks)

### Return Value

[Hole table annotation](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.IHoleTableAnnotation.html)

## VBA Syntax

See [View::InsertHoleTable](ms-its:sldworksapivb6.chm::/sldworks~View~InsertHoleTable.html).

## Remarks

This method requires ordered preselection of various entities:

- datum = 1
- hole = 2
- x axis = 4
- y axis = 8

See [IModelDocExtension::SelectByID2](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.IModelDocExtension~SelectByID2.html) for details.

By default, the hole table templates are in the <install_dir>\lang\<language> folder and have a filename extension of .sldholtbt. The template and table must be of the same type. For example, you could specify C:\Program Files\SOLIDWORKS\lang\English\standard hole table--letters.sldholetbt for TableTemplate if you wanted to insert an English-version of the standard hole letters table template.

## See Also

[IView Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IView.html)
[IView Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IView_members.html)

## Availability

SOLIDWORKS 2004 FCS, Revision Number 12.0
