---
title: "InsertTitleBlockTable Method (IModelDocExtension)"
project: "SOLIDWORKS API Help"
interface: "IModelDocExtension"
member: "InsertTitleBlockTable"
kind: "method"
source: "sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelDocExtension~InsertTitleBlockTable.html"
---

# InsertTitleBlockTable Method (IModelDocExtension)

Inserts a title block table in a part or assembly document.

## Syntax

### Visual Basic (Declaration)

```vb
Function InsertTitleBlockTable( _
   ByVal TemplateName As System.String, _
   ByVal X As System.Integer, _
   ByVal Y As System.Integer _
) As TitleBlockTableAnnotation
```

### Visual Basic (Usage)

```vb
Dim instance As IModelDocExtension
Dim TemplateName As System.String
Dim X As System.Integer
Dim Y As System.Integer
Dim value As TitleBlockTableAnnotation

value = instance.InsertTitleBlockTable(TemplateName, X, Y)
```

### C#

```csharp
TitleBlockTableAnnotation InsertTitleBlockTable(
   System.string TemplateName,
   System.int X,
   System.int Y
)
```

### C++/CLI

```cpp
TitleBlockTableAnnotation^ InsertTitleBlockTable(
   System.String^ TemplateName,
   System.int X,
   System.int Y
)
```

**NOTE:** See [Differences Between Unmanaged C++ and C++/CLI Code](DifferencesBetweenUnManagedAndCPPCLI.htm).

### Parameters

- `TemplateName`: Fully qualified path and name of the title block table template
- `X`: x coordinate for upper-left corner of title block table
- `Y`: y coordinate for upper-left corner of title block table

### Return Value

[Title block table annotation](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.ITitleBlockTableAnnotation.html)

## VBA Syntax

See [ModelDocExtension::InsertTitleBlockTable](ms-its:sldworksapivb6.chm::/sldworks~ModelDocExtension~InsertTitleBlockTable.html).

## Examples

[Get Title Block Tables (VBA)](Get_Title_Block_Tables_Example_VB6.htm)
[Get Title Block Tables (VB.NET)](Get_Title_Block_Tables_Example_VBNET.htm)
[Get Title Block Tables (C#)](Get_Title_Block_Tables_Example_CSharp.htm)

## Remarks

Title block table templates have a filename extension of .sldtbt.

## See Also

[IModelDocExtension Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelDocExtension.html)
[IModelDocExtension Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelDocExtension_members.html)
[IModelDocExtension::InsertGeneralTableAnnotation Method ()](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelDocExtension~InsertGeneralTableAnnotation.html)

## Availability

SOLIDWORKS 2010 FCS, Revision Number 18.0
