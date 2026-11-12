---
title: "InsertBomTable2 Method (IView)"
project: "SOLIDWORKS API Help"
interface: "IView"
member: "InsertBomTable2"
kind: "method"
source: "sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IView~InsertBomTable2.html"
---

# InsertBomTable2 Method (IView)

Obsolete. Superseded by [IView::InsertBomTable3](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.IView~InsertBomTable3.html).

## Syntax

### Visual Basic (Declaration)

```vb
Function InsertBomTable2( _
   ByVal UseAnchorPoint As System.Boolean, _
   ByVal X As System.Double, _
   ByVal Y As System.Double, _
   ByVal AnchorType As System.Integer, _
   ByVal BomType As System.Integer, _
   ByVal Configuration As System.String, _
   ByVal TableTemplate As System.String _
) As BomTableAnnotation
```

### Visual Basic (Usage)

```vb
Dim instance As IView
Dim UseAnchorPoint As System.Boolean
Dim X As System.Double
Dim Y As System.Double
Dim AnchorType As System.Integer
Dim BomType As System.Integer
Dim Configuration As System.String
Dim TableTemplate As System.String
Dim value As BomTableAnnotation

value = instance.InsertBomTable2(UseAnchorPoint, X, Y, AnchorType, BomType, Configuration, TableTemplate)
```

### C#

```csharp
BomTableAnnotation InsertBomTable2(
   System.bool UseAnchorPoint,
   System.double X,
   System.double Y,
   System.int AnchorType,
   System.int BomType,
   System.string Configuration,
   System.string TableTemplate
)
```

### C++/CLI

```cpp
BomTableAnnotation^ InsertBomTable2(
   System.bool UseAnchorPoint,
   System.double X,
   System.double Y,
   System.int AnchorType,
   System.int BomType,
   System.String^ Configuration,
   System.String^ TableTemplate
)
```

**NOTE:** See [Differences Between Unmanaged C++ and C++/CLI Code](DifferencesBetweenUnManagedAndCPPCLI.htm).

### Parameters

- `UseAnchorPoint`: If true and the appropriate sheet format anchor point exists, then insert table at this point; if false, then use the values specified for the X and Y arguments as the insertion point
- `X`: X coordinate for the placement of the BOM table
- `Y`: Y coordinate for the placement of the BOM table
- `AnchorType`: Anchor type as defined by [swBomConfigurationAnchorType_e](ms-its:swconst.chm::/SOLIDWORKS.Interop.swconst~SOLIDWORKS.Interop.swconst.swBOMConfigurationAnchorType_e.html)
- `BomType`: Type of BOM table as defined by [swBomType_e](ms-its:swconst.chm::/SOLIDWORKS.Interop.swconst~SOLIDWORKS.Interop.swconst.swBomType_e.html)
- `Configuration`: Name of the configuration for this BOM table (see Remarks)
- `TableTemplate`: Path and filename of the template that you want to use that corresponds to this type of table (see Remarks)

### Return Value

[BOM table annotation](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.IBomTableAnnotation.html)

## VBA Syntax

See [View::InsertBomTable2](ms-its:sldworksapivb6.chm::/sldworks~View~InsertBomTable2.html).

## Examples

[Insert BOM Table (C#)](Insert_BOM_Table_Example_CSharp.htm)
[Insert BOM Table (VB.NET)](Insert_BOM_Table_Example_VBNET.htm)
[Insert Bom Table (VBA)](Insert_BOM_Table_Example_VB.htm)

## Remarks

If BomType is swBomType_TopLevelOnly, then do not specify Configuration. Instead, use [IBomFeature::GetConfigurations](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.IBomFeature~GetConfigurations.html) or [IBomFeature::IGetConfigurations](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.IBomFeature~IGetConfigurations.html) and [IBomFeature::SetConfigurations](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.IBomFeature~SetConfigurations.html) or [IBomFeature::ISetConfigurations](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.IBomFeature~ISetConfigurations.html) to work with configurations in BOM tables.

If the drawing was created using a configuration other than the Default configuration, then the configuration active at the time the drawing was created is the configuration used in the BOM table when an empty string is specified for the Configuration parameter.

By default, the BOM table templates are in the install_dir\lang\<language> folder and have a filename extension of .sldbomtbt. The template and table must be of the same type. For example, you could specify C:\Program Files\SOLIDWORKS\lang\English\bom-standard.sldbomtbt for TableTemplate if you wanted to insert an English-version of the standard BOM table template.

If the BOM table is a parts-only or indented-style BOM and the Configuration specified is invalid, then the BOM is not created.

NOTE: Use [IView::InsertBomTable](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.IView~InsertBomTable.html) or [IView::IInsertBomTable](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.IView~IInsertBomTable.html) to insert a BOM using Microsoft Excel.

## See Also

[IView Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IView.html)
[IView Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IView_members.html)
[IView::GetKeepLinkedToBOM Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IView~GetKeepLinkedToBOM.html)
[IView::GetKeepLinkedToBOMName Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IView~GetKeepLinkedToBOMName.html)
[IView::SetKeepLinkedToBOM Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IView~SetKeepLinkedToBOM.html)

## Availability

SOLIDWORKS 2004 FCS, Revision Number 12.0
