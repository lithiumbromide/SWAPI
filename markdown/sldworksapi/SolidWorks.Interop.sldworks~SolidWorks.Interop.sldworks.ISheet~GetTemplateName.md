---
title: "GetTemplateName Method (ISheet)"
project: "SOLIDWORKS API Help"
interface: "ISheet"
member: "GetTemplateName"
kind: "method"
source: "sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISheet~GetTemplateName.html"
---

# GetTemplateName Method (ISheet)

Gets the name of the template used by this sheet.

## Syntax

### Visual Basic (Declaration)

```vb
Function GetTemplateName() As System.String
```

### Visual Basic (Usage)

```vb
Dim instance As ISheet
Dim value As System.String

value = instance.GetTemplateName()
```

### C#

```csharp
System.string GetTemplateName()
```

### C++/CLI

```cpp
System.String^ GetTemplateName();
```

**NOTE:** See [Differences Between Unmanaged C++ and C++/CLI Code](DifferencesBetweenUnManagedAndCPPCLI.htm).

### Return Value

Template path name

## VBA Syntax

See [Sheet::GetTemplateName](ms-its:sldworksapivb6.chm::/sldworks~Sheet~GetTemplateName.html).

## Examples

[Get Name of Drawing Sheet Template (VBA)](Get_Name_and_Properties_of_Drawing_Sheet_Template_Example_VB.htm)
[Modify and Reload Sheet Format Template (C#)](Modify_and_Reload_Sheet_Format_Template_Example_CSharp.htm)
[Modify and Reload Sheet Format Template (VB.NET)](Modify_and_Reload_Sheet_Format_Template_Example_VBNET.htm)
[Modify and Reload Sheet Format Template (VBA)](Modify_and_Reload_Sheet_Format_Template_Example_VB.htm)

## Remarks

To ensure a correct return value, open the document in edit mode.

If the sheet does not use a template, i.e., uses a custom layout, this method returns "***.drt**".

## See Also

[ISheet Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISheet.html)
[ISheet Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISheet_members.html)
[ISheet::GetTemplateSketch Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISheet~GetTemplateSketch.html)
[ISheet::SetTemplateName Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISheet~SetTemplateName.html)
[ISheet::GetProperties Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISheet~GetProperties.html)
[ISheet::IGetProperties Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISheet~IGetProperties.html)
[ISheet::SetProperties Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISheet~SetProperties.html)
