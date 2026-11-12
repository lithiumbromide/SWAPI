---
title: "InsertBendTable Method (IView)"
project: "SOLIDWORKS API Help"
interface: "IView"
member: "InsertBendTable"
kind: "method"
source: "sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IView~InsertBendTable.html"
---

# InsertBendTable Method (IView)

Inserts a bend table for this drawing view.

## Syntax

### Visual Basic (Declaration)

```vb
Function InsertBendTable( _
   ByVal UseAnchorPoint As System.Boolean, _
   ByVal X As System.Double, _
   ByVal Y As System.Double, _
   ByVal AnchorType As System.Integer, _
   ByVal StartValue As System.String, _
   ByVal TableTemplate As System.String _
) As BendTableAnnotation
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
Dim value As BendTableAnnotation

value = instance.InsertBendTable(UseAnchorPoint, X, Y, AnchorType, StartValue, TableTemplate)
```

### C#

```csharp
BendTableAnnotation InsertBendTable(
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
BendTableAnnotation^ InsertBendTable(
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

- `UseAnchorPoint`: True to insert the bend table at the sheet format anchor point, false to insert it at the point specified by the X and Y parameters of this method
- `X`: X-coordinate for placement of the bend table; valid only when UseAnchorPoint is false
- `Y`: Y-coordinate for placement of the bend table; valid only when UseAnchorPoint is false
- `AnchorType`: Anchor type as defined in [swBomConfigurationAnchorType_e](ms-its:swconst.chm::/SOLIDWORKS.Interop.swconst~SOLIDWORKS.Interop.swconst.swBomConfigurationAnchorType_e.html)
- `StartValue`: Starting datum tag; a value from A to Z for letter tags; a positive integer for number tags
- `TableTemplate`: Full pathname of the template (e.g., `install_dir`\**lang\**`language\`**bendtable-standard.sldbndtbt**)

### Return Value

[IBendTableAnnotation](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.IBendTableAnnotation.html)

## VBA Syntax

See [View::InsertBendTable](ms-its:sldworksapivb6.chm::/sldworks~View~InsertBendTable.html).

## Examples

[Insert Bend Table (VBA)](Insert_Bend_Table_Example_VB.htm)
[Insert Bend Table (VB.NET)](Insert_Bend_Table_Example_VBNET.htm)
[Insert Bend Table (C#)](Insert_Bend_Table_Example_CSharp.htm)

## See Also

[IView Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IView.html)
[IView Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IView_members.html)
[IBendTable Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IBendTable.html)
[IPartDoc::InsertBendTable Method ()](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IPartDoc~InsertBendTable.html)

## Availability

SOLIDWORKS 2012 FCS, Revision Number 20.0
