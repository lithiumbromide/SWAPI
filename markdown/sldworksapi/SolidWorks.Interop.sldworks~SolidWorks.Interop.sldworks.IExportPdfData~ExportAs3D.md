---
title: "ExportAs3D Property (IExportPdfData)"
project: "SOLIDWORKS API Help"
interface: "IExportPdfData"
member: "ExportAs3D"
kind: "property"
source: "sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IExportPdfData~ExportAs3D.html"
---

# ExportAs3D Property (IExportPdfData)

Gets or sets whether to export this part or drawing document to 3D PDF.

## Syntax

### Visual Basic (Declaration)

```vb
Property ExportAs3D As System.Boolean
```

### Visual Basic (Usage)

```vb
Dim instance As IExportPdfData
Dim value As System.Boolean

instance.ExportAs3D = value

value = instance.ExportAs3D
```

### C#

```csharp
System.bool ExportAs3D {get; set;}
```

### C++/CLI

```cpp
property System.bool ExportAs3D {
   System.bool get();
   void set (    System.bool value);
}
```

**NOTE:** See [Differences Between Unmanaged C++ and C++/CLI Code](DifferencesBetweenUnManagedAndCPPCLI.htm).

### Property Value

True to export this part or drawing document to 3D PDF, false to not

## VBA Syntax

See [ExportPdfData::ExportAs3D](ms-its:sldworksapivb6.chm::/sldworks~ExportPdfData~ExportAs3D.html).

## Remarks

Call [IModelDocExtension::SaveAs](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.IModelDocExtension~SaveAs.html) after setting this property.

## See Also

[IExportPdfData Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IExportPdfData.html)
[IExportPdfData Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IExportPdfData_members.html)

## Availability

SOLIDWORKS 2008 SP1, Revision Number 16.1
