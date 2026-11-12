---
title: "GetNameForSelection Method (IDisplayDimension)"
project: "SOLIDWORKS API Help"
interface: "IDisplayDimension"
member: "GetNameForSelection"
kind: "method"
source: "sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IDisplayDimension~GetNameForSelection.html"
---

# GetNameForSelection Method (IDisplayDimension)

Gets the name of the selected display dimension needed by [IModelDocExtension::SelectByID2](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.IModelDocExtension~SelectByID2.html).

## Syntax

### Visual Basic (Declaration)

```vb
Function GetNameForSelection() As System.String
```

### Visual Basic (Usage)

```vb
Dim instance As IDisplayDimension
Dim value As System.String

value = instance.GetNameForSelection()
```

### C#

```csharp
System.string GetNameForSelection()
```

### C++/CLI

```cpp
System.String^ GetNameForSelection();
```

**NOTE:** See [Differences Between Unmanaged C++ and C++/CLI Code](DifferencesBetweenUnManagedAndCPPCLI.htm).

### Return Value

Name of selected display dimension

## VBA Syntax

See [DisplayDimension::GetNameForSelection](ms-its:sldworksapivb6.chm::/sldworks~DisplayDimension~GetNameForSelection.html).

## Examples

[Get Chamfer Display Dimension (C#)](Get_Chamfer_Display_Dimension_Example_CSharp.htm)
[Get Chamfer Display Dimension (VB.NET)](Get_Chamfer_Display_Dimension_Example_VBNET.htm)
[Get Chamfer Display Dimension (VBA)](Get_Chamfer_Display_Dimension_Example_VB.htm)

## See Also

[IDisplayDimension Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IDisplayDimension.html)
[IDisplayDimension Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IDisplayDimension_members.html)
[IDimension::GetNameForSelection Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IDimension~GetNameForSelection.html)

## Availability

SOLIDWORKS 2009 FCS, Revision Numbe 17.0
