---
title: "PublishSTEP242File Method (IModelDocExtension)"
project: "SOLIDWORKS API Help"
interface: "IModelDocExtension"
member: "PublishSTEP242File"
kind: "method"
source: "sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelDocExtension~PublishSTEP242File.html"
---

# PublishSTEP242File Method (IModelDocExtension)

Exports the SOLIDWORKS MBD 3D part or assembly to a STEP 242 file.

## Syntax

### Visual Basic (Declaration)

```vb
Function PublishSTEP242File( _
   ByVal Path As System.String _
) As System.Integer
```

### Visual Basic (Usage)

```vb
Dim instance As IModelDocExtension
Dim Path As System.String
Dim value As System.Integer

value = instance.PublishSTEP242File(Path)
```

### C#

```csharp
System.int PublishSTEP242File(
   System.string Path
)
```

### C++/CLI

```cpp
System.int PublishSTEP242File(
   System.String^ Path
)
```

NOTE:

See

[Differences Between Unmanaged C++ and C++/CLI Code](DifferencesBetweenUnManagedAndCPPCLI.htm)

.

### Parameters

- `Path`: Full qualified path to which to export the SOLIDWORKS MBD 3D part or assembly; use

.STP

for the file name extension

### Return Value

Status as defined in

[swStep242Error_e](ms-its:swconst.chm::/SolidWorks.Interop.swconst~SolidWorks.Interop.swconst.swStep242Error_e.html)

## VBA Syntax

See

[ModelDocExtension::PublishSTEP242File](ms-its:sldworksapivb6.chm::/sldworks~ModelDocExtension~PublishSTEP242File.html)

.

## Examples

[Export SOLIDWORKS MBD to STEP 242 (C#)](Export_SOLIDWORKS_MBD_to_STEP_242_Example_CSharp.htm)

[Export SOLIDWORKS MBD to STEP 242 (VB.NET)](Export_SOLIDWORKS_MBD_to_STEP_242_Example_VBNET.htm)

[Export SOLIDWORKS MBD to STEP 242 (VBA)](Export_SOLIDWORKS_MBD_to_STEP_242_Example_VB.htm)

## Remarks

This method requires that the SOLDWORKS MBD add-in be loaded. ([ISldWorks::LoadAddIn](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISldWorks~LoadAddIn.html))

## See Also

[IModelDocExtension Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelDocExtension.html)

[IModelDocExtension Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelDocExtension_members.html)

[IModelDocExtension::PublishTo3DPDF Method ()](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelDocExtension~PublishTo3DPDF.html)

[IMBD3DPdfData::CreateAttachSTEP242 Property ()](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IMBD3DPdfData~CreateAttachSTEP242.html)

## Availability

SOLIDWORKS 2017 FCS, Revision Number 25.0
