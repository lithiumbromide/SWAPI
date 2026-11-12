---
title: "GetTemplateSketch Method (ISheet)"
project: "SOLIDWORKS API Help"
interface: "ISheet"
member: "GetTemplateSketch"
kind: "method"
source: "sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISheet~GetTemplateSketch.html"
---

# GetTemplateSketch Method (ISheet)

Gets the sheet format sketch for this drawing sheet.

## Syntax

### Visual Basic (Declaration)

```vb
Function GetTemplateSketch() As Sketch
```

### Visual Basic (Usage)

```vb
Dim instance As ISheet
Dim value As Sketch

value = instance.GetTemplateSketch()
```

### C#

```csharp
Sketch GetTemplateSketch()
```

### C++/CLI

```cpp
Sketch^ GetTemplateSketch();
```

**NOTE:** See [Differences Between Unmanaged C++ and C++/CLI Code](DifferencesBetweenUnManagedAndCPPCLI.htm).

### Return Value

[Sketch](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.ISketch.html)

## VBA Syntax

See [Sheet::GetTemplateSketch](ms-its:sldworksapivb6.chm::/sldworks~Sheet~GetTemplateSketch.html).

## See Also

[ISheet Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISheet.html)
[ISheet Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISheet_members.html)
[ISheet::GetTemplateName Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISheet~GetTemplateName.html)
[ISheet::SetTemplateName Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISheet~SetTemplateName.html)

## Availability

SOLIDWORKS 2004 FCS, Revision Number 12.0
