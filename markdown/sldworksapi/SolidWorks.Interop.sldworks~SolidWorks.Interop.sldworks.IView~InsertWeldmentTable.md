---
title: "InsertWeldmentTable Method (IView)"
project: "SOLIDWORKS API Help"
interface: "IView"
member: "InsertWeldmentTable"
kind: "method"
source: "sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IView~InsertWeldmentTable.html"
---

# InsertWeldmentTable Method (IView)

Inserts a weldment cut-list table into this drawing view.

## Syntax

### Visual Basic (Declaration)

```vb
Function InsertWeldmentTable( _
   ByVal UseAnchorPoint As System.Boolean, _
   ByVal X As System.Double, _
   ByVal Y As System.Double, _
   ByVal AnchorType As System.Integer, _
   ByVal Configuration As System.String, _
   ByVal TableTemplate As System.String _
) As WeldmentCutListAnnotation
```

### Visual Basic (Usage)

```vb
Dim instance As IView
Dim UseAnchorPoint As System.Boolean
Dim X As System.Double
Dim Y As System.Double
Dim AnchorType As System.Integer
Dim Configuration As System.String
Dim TableTemplate As System.String
Dim value As WeldmentCutListAnnotation

value = instance.InsertWeldmentTable(UseAnchorPoint, X, Y, AnchorType, Configuration, TableTemplate)
```

### C#

```csharp
WeldmentCutListAnnotation InsertWeldmentTable(
   System.bool UseAnchorPoint,
   System.double X,
   System.double Y,
   System.int AnchorType,
   System.string Configuration,
   System.string TableTemplate
)
```

### C++/CLI

```cpp
WeldmentCutListAnnotation^ InsertWeldmentTable(
   System.bool UseAnchorPoint,
   System.double X,
   System.double Y,
   System.int AnchorType,
   System.String^ Configuration,
   System.String^ TableTemplate
)
```

**NOTE:** See [Differences Between Unmanaged C++ and C++/CLI Code](DifferencesBetweenUnManagedAndCPPCLI.htm).

### Parameters

- `UseAnchorPoint`: If true and the appropriate sheet format anchor point exists, then insert table at this point; if false, then use the values specified for the X and Y arguments as the insertion point
- `X`: X coordinate for the placement of the weldment cut-list table; valid only if UserAnchorPoint = False
- `Y`: Y coordinate for the placement of the weldment cut-list table; valid only if UseAnchorPoint = False
- `AnchorType`: Anchor type as defined by [swBomConfigurationAnchorType_e](ms-its:swconst.chm::/SOLIDWORKS.Interop.swconst~SOLIDWORKS.Interop.swconst.swBOMConfigurationAnchorType_e.html)
- `Configuration`: Name of the "As Welded" configuration for the weldment cut-list table
- `TableTemplate`: Path and filename of the template that corresponds to this type of table (see Remarks)

### Return Value

[Weldment cut-list annotation](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.IWeldmentCutListAnnotation.html)

## VBA Syntax

See [View::InsertWeldmentTable](ms-its:sldworksapivb6.chm::/sldworks~View~InsertWeldmentTable.html).

## Examples

[Insert Weldment Cut List Table (VBA)](Insert_Weldment_Cut_List_Table_Example_VB.htm)
[Insert Weldment Cut List Table (VB.NET)](Insert_Weldment_Cut_List_Table_Example_VBNET.htm)
[Insert Weldment Cut List Table (C#)](Insert_Weldment_Cut_List_Table_Example_CSharp.htm)

## Remarks

The weldment cut-list table template installed with SOLIDWORKS is <`SOLIDWORKS_`install_dir>\lang\<language>\**cut list.sldwldtbt**.

## See Also

[IView Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IView.html)
[IView Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IView_members.html)
[IView::GetKeepLinkedToBOM Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IView~GetKeepLinkedToBOM.html)
[IView::GetKeepLinkedToBOMName Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IView~GetKeepLinkedToBOMName.html)
[IView::SetKeepLinkedToBOM Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IView~SetKeepLinkedToBOM.html)

## Availability

SOLIDWORKS 2007 FCS, Revision Number 15.0
