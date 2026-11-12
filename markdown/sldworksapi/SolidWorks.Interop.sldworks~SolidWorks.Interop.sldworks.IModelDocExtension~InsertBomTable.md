---
title: "InsertBomTable Method (IModelDocExtension)"
project: "SOLIDWORKS API Help"
interface: "IModelDocExtension"
member: "InsertBomTable"
kind: "method"
source: "sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelDocExtension~InsertBomTable.html"
---

# InsertBomTable Method (IModelDocExtension)

Obsolete. Superseded by [IModelDocExtension::InsertBomTable2](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.IModelDocExtension~InsertBomTable2.html).

## Syntax

### Visual Basic (Declaration)

```vb
Function InsertBomTable( _
   ByVal TemplateName As System.String, _
   ByVal X As System.Integer, _
   ByVal Y As System.Integer, _
   ByVal BomType As System.Integer, _
   ByVal ConfigurationName As System.String _
) As BomTableAnnotation
```

### Visual Basic (Usage)

```vb
Dim instance As IModelDocExtension
Dim TemplateName As System.String
Dim X As System.Integer
Dim Y As System.Integer
Dim BomType As System.Integer
Dim ConfigurationName As System.String
Dim value As BomTableAnnotation

value = instance.InsertBomTable(TemplateName, X, Y, BomType, ConfigurationName)
```

### C#

```csharp
BomTableAnnotation InsertBomTable(
   System.string TemplateName,
   System.int X,
   System.int Y,
   System.int BomType,
   System.string ConfigurationName
)
```

### C++/CLI

```cpp
BomTableAnnotation^ InsertBomTable(
   System.String^ TemplateName,
   System.int X,
   System.int Y,
   System.int BomType,
   System.String^ ConfigurationName
)
```

**NOTE:** See [Differences Between Unmanaged C++ and C++/CLI Code](DifferencesBetweenUnManagedAndCPPCLI.htm).

### Parameters

- `TemplateName`: Path and name of BOM table template (see **Remarks**)
- `X`: X coordinate for the placement of the BOM table
- `Y`: Y coordinate for the placement of the BOM table
- `BomType`: Type of BOM table as defined by [swBomType_e](ms-its:swconst.chm::/SOLIDWORKS.Interop.swconst~SOLIDWORKS.Interop.swconst.swBomType_e.html)
- `ConfigurationName`: Name of the configuration for this BOM table (see Remarks)

### Return Value

[BOM table annotation](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.IBomTableAnnotation.html)

## VBA Syntax

See [ModelDocExtension::InsertBomTable](ms-its:sldworksapivb6.chm::/sldworks~ModelDocExtension~InsertBomTable.html).

## Examples

[Insert BOM Table and Stacked Balloon (VB.NET)](Insert_BOM_Table_and_Stacked_Balloon_Example_VBNET.htm)
[Insert BOM Table and Stacked Balloon (VBA)](Insert_BOM_Table_and_Stacked_Balloon_Example_VB.htm)

## Remarks

The system will not default to the default configuration when you specify an empty string for Configuration. You must specify the configuration.

By default, the BOM table templates are in the <install_dir>\lang\<language> folder and have a filename extension of .sldbomtbt. The template and table must be of the same type. For example, you could specify C:\Program Files\SOLIDWORKS\lang\English\bom-standard.sldbomtbt for TemplateName if you wanted to insert an English-version of the standard BOM table template.

If the BOM table is a parts-only or indented-style BOM and ConfigurationName is invalid, then the BOM is not created.

## See Also

[IModelDocExtension Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelDocExtension.html)
[IModelDocExtension Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelDocExtension_members.html)
[IView::InsertBomTable2 Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IView~InsertBomTable2.html)

## Availability

SOLIDWORKS 2009 FCS, Revision Number 17.0
