---
title: "InsertBomTable2 Method (IModelDocExtension)"
project: "SOLIDWORKS API Help"
interface: "IModelDocExtension"
member: "InsertBomTable2"
kind: "method"
source: "sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelDocExtension~InsertBomTable2.html"
---

# InsertBomTable2 Method (IModelDocExtension)

Obsolete. Superseded by [IModelDocExtension::InsertBomTable3](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.IModelDocExtension~InsertBomTable3.html).

## Syntax

### Visual Basic (Declaration)

```vb
Function InsertBomTable2( _
   ByVal TemplateName As System.String, _
   ByVal X As System.Integer, _
   ByVal Y As System.Integer, _
   ByVal BomType As System.Integer, _
   ByVal ConfigurationName As System.String, _
   ByVal Hidden As System.Boolean _
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
Dim Hidden As System.Boolean
Dim value As BomTableAnnotation

value = instance.InsertBomTable2(TemplateName, X, Y, BomType, ConfigurationName, Hidden)
```

### C#

```csharp
BomTableAnnotation InsertBomTable2(
   System.string TemplateName,
   System.int X,
   System.int Y,
   System.int BomType,
   System.string ConfigurationName,
   System.bool Hidden
)
```

### C++/CLI

```cpp
BomTableAnnotation^ InsertBomTable2(
   System.String^ TemplateName,
   System.int X,
   System.int Y,
   System.int BomType,
   System.String^ ConfigurationName,
   System.bool Hidden
)
```

**NOTE:** See [Differences Between Unmanaged C++ and C++/CLI Code](DifferencesBetweenUnManagedAndCPPCLI.htm).

### Parameters

- `TemplateName`: Path and name of BOM table template (see **Remarks**)
- `X`: X coordinate for the placement of the BOM table
- `Y`: Y coordinate for the placement of the BOM table
- `BomType`: Type of BOM table as defined by [swBomType_e](ms-its:swconst.chm::/SOLIDWORKS.Interop.swconst~SOLIDWORKS.Interop.swconst.swBomType_e.html)
- `ConfigurationName`: Name of the configuration for this BOM table (see Remarks)
- `Hidden`: True to hide the BOM table, false to show it

### Return Value

[BOM table annotation](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.IBomTableAnnotation.html)

## VBA Syntax

See [ModelDocExtension::InsertBomTable2](ms-its:sldworksapivb6.chm::/sldworks~ModelDocExtension~InsertBomTable2.html).

## Remarks

The system does not default to the Default configuration when you specify an empty string for Configuration. You must specify the configuration.

BOM table templates are in the <`SOLIDWORKS_`install_dir>\lang\<language> folder and have a filename extension of .sldbomtbt. The template and table must be of the same type. For example, you could specify C:\Program Files\SOLIDWORKS\lang\English\bom-standard.sldbomtbt for TemplateName if you wanted to insert an English-version of the standard BOM table template.

If the BOM table is a parts-only or indented-style BOM and ConfigurationName is invalid, then the BOM is not created.

## See Also

[IModelDocExtension Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelDocExtension.html)
[IModelDocExtension Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelDocExtension_members.html)
[IView::InsertBomTable3 Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IView~InsertBomTable3.html)

## Availability

SOLIDWORKS 2010 FCS, Revision Number 18.0
