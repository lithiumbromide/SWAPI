---
title: "GetLowerText Method (IDisplayDimension)"
project: "SOLIDWORKS API Help"
interface: "IDisplayDimension"
member: "GetLowerText"
kind: "method"
source: "sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IDisplayDimension~GetLowerText.html"
---

# GetLowerText Method (IDisplayDimension)

Gets the text below the dimension line in a display dimension.

## Syntax

### Visual Basic (Declaration)

```vb
Function GetLowerText() As System.String
```

### Visual Basic (Usage)

```vb
Dim instance As IDisplayDimension
Dim value As System.String

value = instance.GetLowerText()
```

### C#

```csharp
System.string GetLowerText()
```

### C++/CLI

```cpp
System.String^ GetLowerText();
```

**NOTE:** See [Differences Between Unmanaged C++ and C++/CLI Code](DifferencesBetweenUnManagedAndCPPCLI.htm).

### Return Value

Text below the dimension line

## VBA Syntax

See [DisplayDimension::GetLowerText](ms-its:sldworksapivb6.chm::/sldworks~DisplayDimension~GetLowerText.html).

## Examples

[Get Chamfer Display Dimension (C#)](Get_Chamfer_Display_Dimension_Example_CSharp.htm)
[Get Chamfer Display Dimension (VB.NET)](Get_Chamfer_Display_Dimension_Example_VBNET.htm)
[Get Chamfer Display Dimension (VBA)](Get_Chamfer_Display_Dimension_Example_VB.htm)

## See Also

[IDisplayDimension Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IDisplayDimension.html)
[IDisplayDimension Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IDisplayDimension_members.html)
[IDisplayDimension::SetLowerText Method ()](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IDisplayDimension~SetLowerText.html)
[IModelDocExtension::EditDimensionProperties Method ()](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelDocExtension~EditDimensionProperties.html)
[IModelDocExtension::IEditDimensionProperties Method()](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelDocExtension~IEditDimensionProperties.html)
[IDisplayDimension::GetText Method ()](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IDisplayDimension~GetText.html)
[IDisplayDimension::SetText Method ()](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IDisplayDimension~SetText.html)

## Availability

SOLIDWORKS 2014 FCS, Revision Number 22.0
