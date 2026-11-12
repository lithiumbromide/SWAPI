---
title: "CreateAttachSTEP242 Property (IMBD3DPdfData)"
project: "SOLIDWORKS API Help"
interface: "IMBD3DPdfData"
member: "CreateAttachSTEP242"
kind: "property"
source: "sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IMBD3DPdfData~CreateAttachSTEP242.html"
---

# CreateAttachSTEP242 Property (IMBD3DPdfData)

Gets or sets whether to export SOLIDWORKS parts and assemblies to STEP 242 format and attach the STEP 242 file to the SOLIDWORKS MBD 3D PDF.

## Syntax

### Visual Basic (Declaration)

```vb
Property CreateAttachSTEP242 As System.Boolean
```

### Visual Basic (Usage)

```vb
Dim instance As IMBD3DPdfData
Dim value As System.Boolean

instance.CreateAttachSTEP242 = value

value = instance.CreateAttachSTEP242
```

### C#

```csharp
System.bool CreateAttachSTEP242 {get; set;}
```

### C++/CLI

```cpp
property System.bool CreateAttachSTEP242 {
   System.bool get();
   void set (    System.bool value);
}
```

**NOTE:** See [Differences Between Unmanaged C++ and C++/CLI Code](DifferencesBetweenUnManagedAndCPPCLI.htm).

### Property Value

True to export SOLIDWORKS parts and assemblies to STEP 242 format and attach the STEP 242 file to SOLIDWORKS MBD 3D PDF, false to not

## VBA Syntax

See [MBD3DPdfData::CreateAttachSTEP242](ms-its:sldworksapivb6.chm::/sldworks~MBD3DPdfData~CreateAttachSTEP242.html).

## Examples

[Attach Files to MBD 3D PDF (C#)](Attach_Files_to_MBD_3D_PDF_Example_CSharp.htm)
[Attach Files to MBD 3D PDF (VB.NET)](Attach_Files_to_MBD_3D_PDF_Example_VBNET.htm)
[Attach Files to MBD 3D PDF (VBA)](Attach_Files_to_MBD_3D_PDF_Example_VB.htm)

## See Also

[IMBD3DPdfData Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IMBD3DPdfData.html)
[IMBD3DPdfData Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IMBD3DPdfData_members.html)
[IModelDocExtension::PublishSTEP242File Method ()](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelDocExtension~PublishSTEP242File.html)

## Availability

SOLIDWORKS 2017 FCS, Revision Number 25.0
