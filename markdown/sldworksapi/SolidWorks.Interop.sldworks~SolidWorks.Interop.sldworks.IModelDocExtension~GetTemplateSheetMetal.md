---
title: "GetTemplateSheetMetal Method (IModelDocExtension)"
project: "SOLIDWORKS API Help"
interface: "IModelDocExtension"
member: "GetTemplateSheetMetal"
kind: "method"
source: "sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelDocExtension~GetTemplateSheetMetal.html"
---

# GetTemplateSheetMetal Method (IModelDocExtension)

Gets the sheet metal folder feature from this sheet metal model created in SOLIDWORKS 2013 or later.

## Syntax

### Visual Basic (Declaration)

```vb
Function GetTemplateSheetMetal() As System.Object
```

### Visual Basic (Usage)

```vb
Dim instance As IModelDocExtension
Dim value As System.Object

value = instance.GetTemplateSheetMetal()
```

### C#

```csharp
System.object GetTemplateSheetMetal()
```

### C++/CLI

```cpp
System.Object^ GetTemplateSheetMetal();
```

**NOTE:** See [Differences Between Unmanaged C++ and C++/CLI Code](DifferencesBetweenUnManagedAndCPPCLI.htm).

### Return Value

[IFeature](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.IFeature.html); Null if this model was created with SOLIDWORKS 2012 or earlier

## VBA Syntax

See [ModelDocExtension::GetTemplateSheetMetal](ms-its:sldworksapivb6.chm::/sldworks~ModelDocExtension~GetTemplateSheetMetal.html).

## Examples

[Get Sheet Metal Feature Data (VBA)](Get_Template_Sheet_Metal_Feature_Data_Example_VB.htm)
[Get Sheet Metal Feature Data (VB.NET)](Get_Template_Sheet_Metal_Feature_Data_Example_VBNET.htm)
[Get Sheet Metal Feature Data (C#)](Get_Template_Sheet_Metal_Feature_Data_Example_CSharp.htm)

## Remarks

This method works only on sheet metal models created with SOLIDWORKS 2013 or later. To obtain sheet metal feature data for earlier models, follow the examples of [ISheetMetalFeatureData](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.ISheetMetalFeatureData.html).

## See Also

[IModelDocExtension Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelDocExtension.html)
[IModelDocExtension Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelDocExtension_members.html)

## Availability

SOLIDWORKS 2013 FCS, Revision Number 21.0
