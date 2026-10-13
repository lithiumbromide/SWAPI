---
title: "InsertBomTable3 Method (IModelDocExtension)"
project: "SOLIDWORKS API Help"
interface: "IModelDocExtension"
member: "InsertBomTable3"
kind: "method"
source: "sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelDocExtension~InsertBomTable3.html"
---

# InsertBomTable3 Method (IModelDocExtension)

Obsolete. Superseded by [IModelDocExtension::InsertBomTable4](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelDocExtension~InsertBomTable4.html).

## Syntax

### Visual Basic (Declaration)

```vb
Function InsertBomTable3( _
   ByVal TemplateName As System.String, _
   ByVal X As System.Integer, _
   ByVal Y As System.Integer, _
   ByVal BomType As System.Integer, _
   ByVal ConfigurationName As System.String, _
   ByVal Hidden As System.Boolean, _
   ByVal IndentedNumberingType As System.Integer, _
   ByVal DetailedCutList As System.Boolean _
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
Dim IndentedNumberingType As System.Integer
Dim DetailedCutList As System.Boolean
Dim value As BomTableAnnotation

value = instance.InsertBomTable3(TemplateName, X, Y, BomType, ConfigurationName, Hidden, IndentedNumberingType, DetailedCutList)
```

### C#

```csharp
BomTableAnnotation InsertBomTable3(
   System.string TemplateName,
   System.int X,
   System.int Y,
   System.int BomType,
   System.string ConfigurationName,
   System.bool Hidden,
   System.int IndentedNumberingType,
   System.bool DetailedCutList
)
```

### C++/CLI

```cpp
BomTableAnnotation^ InsertBomTable3(
   System.String^ TemplateName,
   System.int X,
   System.int Y,
   System.int BomType,
   System.String^ ConfigurationName,
   System.bool Hidden,
   System.int IndentedNumberingType,
   System.bool DetailedCutList
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
- `IndentedNumberingType`: Type of numbering as defined by [swNumberingType_e](ms-its:swconst.chm::/SOLIDWORKS.Interop.swconst~SOLIDWORKS.Interop.swconst.swNumberingType_e.html); valid only if BomType = swBomType_e.swBomType_Indented
- `DetailedCutList`: True to show the detailed cut list, false to not; valid only if BomType = swBomType_e.swBomType_Indented

### Return Value

[BOM table annotation](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.IBomTableAnnotation.html)

## VBA Syntax

See [ModelDocExtension::InsertBomTable3](ms-its:sldworksapivb6.chm::/sldworks~ModelDocExtension~InsertBomTable3.html).

## Remarks

The system does not default to the Default configuration when you specify an empty string for Configuration. You must specify the configuration.

BOM table templates are in the <`SOLIDWORKS_`install_dir>\lang\<language> folder and have a filename extension of .sldbomtbt. The template and table must be of the same type. For example, you could specify C:\Program Files\SOLIDWORKS\lang\English\bom-standard.sldbomtbt for TemplateName if you wanted to insert an English-version of the standard BOM table template.

If the BOM table is a parts-only or indented-style BOM and ConfigurationName is invalid, then the BOM is not created.

## See Also

[IModelDocExtension Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelDocExtension.html)
[IModelDocExtension Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelDocExtension_members.html)
[IView::InsertBomTable4 Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IView~InsertBomTable4.html)
[IModelDocExtension::InsertGeneralTableAnnotation Method ()](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelDocExtension~InsertGeneralTableAnnotation.html)

## Availability

SOLIDWORKS 2013 FCS, Revision Number 21.0
