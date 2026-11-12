---
title: "PublishSTEP242File2 Method (IModelDocExtension)"
project: "SOLIDWORKS API Help"
interface: "IModelDocExtension"
member: "PublishSTEP242File2"
kind: "method"
source: "sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelDocExtension~PublishSTEP242File2.html"
---

# PublishSTEP242File2 Method (IModelDocExtension)

Exports the SOLIDWORKS MBD 3D part or assembly to a STEP 242 file.

## Syntax

### Visual Basic (Declaration)

```vb
Function PublishSTEP242File2( _
   ByVal MBDSTEP242Data As System.Object _
) As System.Integer
```

### Visual Basic (Usage)

```vb
Dim instance As IModelDocExtension
Dim MBDSTEP242Data As System.Object
Dim value As System.Integer

value = instance.PublishSTEP242File2(MBDSTEP242Data)
```

### C#

```csharp
System.int PublishSTEP242File2(
   System.object MBDSTEP242Data
)
```

### C++/CLI

```cpp
System.int PublishSTEP242File2(
   System.Object^ MBDSTEP242Data
)
```

**NOTE:** See [Differences Between Unmanaged C++ and C++/CLI Code](DifferencesBetweenUnManagedAndCPPCLI.htm).

### Parameters

- `MBDSTEP242Data`: [IMBDSTEP242Data](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IMBDSTEP242Data.html)

### Return Value

Status as defined by [swStep242Error_e](ms-its:swconst.chm::/SolidWorks.Interop.swconst~SolidWorks.Interop.swconst.swStep242Error_e.html)

## VBA Syntax

See [ModelDocExtension::PublishSTEP242File2](ms-its:sldworksapivb6.chm::/sldworks~ModelDocExtension~PublishSTEP242File2.html).

## Examples

See the IMBDSTEP242Data example.

## Remarks

This method requires that the SOLDWORKS MBD add-in be loaded. ([ISldWorks::LoadAddIn](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISldWorks~LoadAddIn.html))

See the SOLIDWORKS Help for details about MBD.

## See Also

[IModelDocExtension Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelDocExtension.html)
[IModelDocExtension Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelDocExtension_members.html)
[IModelDocExtension::PublishTo3DPDF Method ()](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelDocExtension~PublishTo3DPDF.html)
[IMBD3DPdfData::CreateAttachSTEP242 Property ()](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IMBD3DPdfData~CreateAttachSTEP242.html)

## Availability

SOLIDWORKS 2025 SP03, Revision Number 33.3
