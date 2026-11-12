---
title: "SetTemplateName Method (ISheet)"
project: "SOLIDWORKS API Help"
interface: "ISheet"
member: "SetTemplateName"
kind: "method"
source: "sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISheet~SetTemplateName.html"
---

# SetTemplateName Method (ISheet)

Sets the template name for the sheet format.

## Syntax

### Visual Basic (Declaration)

```vb
Sub SetTemplateName( _
   ByVal NameIn As System.String _
)
```

### Visual Basic (Usage)

```vb
Dim instance As ISheet
Dim NameIn As System.String

instance.SetTemplateName(NameIn)
```

### C#

```csharp
void SetTemplateName(
   System.string NameIn
)
```

### C++/CLI

```cpp
void SetTemplateName(
   System.String^ NameIn
)
```

**NOTE:** See [Differences Between Unmanaged C++ and C++/CLI Code](DifferencesBetweenUnManagedAndCPPCLI.htm).

### Parameters

- `NameIn`: Path name of the sheet format template

## VBA Syntax

See [Sheet::SetTemplateName](ms-its:sldworksapivb6.chm::/sldworks~Sheet~SetTemplateName.html).

## Examples

[Get and Set Whether to Hide Cutting Line Shoulders (C#)](Get_and_Set_Whether_to_Hide_Cutting_Line_Shoulders_Example_CSharp.htm)
[Get and Set Whether to Hide Cutting Line Shoulders (VB.NET)](Get_and_Set_Whether_to_Hide_Cutting_Line_Shoulders_Example_VBNET.htm)
[Get and Set Whether to Hide Cutting Line Shoulders (VBA)](Get_and_Set_Whether_to_Hide_Cutting_Line_Shoulders_Example_VB.htm)

## Remarks

If you want to use:

- a custom template name, before calling this method, call [ISheet::SetProperties](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.ISheet~SetProperties.html) and specify swDwgTemplates_e.swDwgTemplateCustom for the Templ parameter.
- one of the standard templates provided by SOLIDWORKS, then there is no need to call ISheet::SetTemplateName. Instead, call ISheet::SetProperties and specify the appropriate enumerator for the Templ parameter.

## See Also

[ISheet Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISheet.html)
[ISheet Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISheet_members.html)
[ISheet::GetTemplateName Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISheet~GetTemplateName.html)
[ISheet::GetTemplateSketch Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISheet~GetTemplateSketch.html)
[ISheet::GetProperties Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISheet~GetProperties.html)
[ISheet::IGetProperties Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISheet~IGetProperties.html)
