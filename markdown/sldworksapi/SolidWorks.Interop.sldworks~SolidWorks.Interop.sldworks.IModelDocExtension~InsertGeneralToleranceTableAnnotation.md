---
title: "InsertGeneralToleranceTableAnnotation Method (IModelDocExtension)"
project: "SOLIDWORKS API Help"
interface: "IModelDocExtension"
member: "InsertGeneralToleranceTableAnnotation"
kind: "method"
source: "sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelDocExtension~InsertGeneralToleranceTableAnnotation.html"
---

# InsertGeneralToleranceTableAnnotation Method (IModelDocExtension)

Inserts a general tolerance table annotation in this model document.

## Syntax

### Visual Basic (Declaration)

```vb
Function InsertGeneralToleranceTableAnnotation( _
   ByVal TemplateName As System.String, _
   ByVal X As System.Integer, _
   ByVal Y As System.Integer _
) As GeneralToleranceTableAnnotation
```

### Visual Basic (Usage)

```vb
Dim instance As IModelDocExtension
Dim TemplateName As System.String
Dim X As System.Integer
Dim Y As System.Integer
Dim value As GeneralToleranceTableAnnotation

value = instance.InsertGeneralToleranceTableAnnotation(TemplateName, X, Y)
```

### C#

```csharp
GeneralToleranceTableAnnotation InsertGeneralToleranceTableAnnotation(
   System.string TemplateName,
   System.int X,
   System.int Y
)
```

### C++/CLI

```cpp
GeneralToleranceTableAnnotation^ InsertGeneralToleranceTableAnnotation(
   System.String^ TemplateName,
   System.int X,
   System.int Y
)
```

**NOTE:** See [Differences Between Unmanaged C++ and C++/CLI Code](DifferencesBetweenUnManagedAndCPPCLI.htm).

### Parameters

- `TemplateName`: Path and file name of the table template to use (see **Remarks**)
- `X`: X coordinate of this table annotation
- `Y`: Y coordinate of this table annotation

### Return Value

[IGeneralToleranceTableAnnotation](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IGeneralToleranceTableAnnotation.html)

## VBA Syntax

See [ModelDocExtension::InsertGeneralToleranceTableAnnotation](ms-its:sldworksapivb6.chm::/sldworks~ModelDocExtension~InsertGeneralToleranceTableAnnotation.html).

## Examples

[Insert General Tolerance Table (VBA)](Insert_General_Tolerance_Table_Example_VB.htm)
[Insert General Tolerance Table (VB.NET)](Insert_General_Tolerance_Table_Example_VBNET.htm)
[Insert General Tolerance Table (C#)](Insert_General_Tolerance_Table_Example_CSharp.htm)

## Remarks

Specify TemplateName with `install_dir`**\lang\**`lang`**\bom-standard.sldbomtbt**.

## See Also

[IModelDocExtension Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelDocExtension.html)
[IModelDocExtension Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelDocExtension_members.html)
[IGeneralToleranceTableFeature Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IGeneralToleranceTableFeature.html)

## Availability

SOLIDWORKS 2018 FCS, Revision Number 26.0
