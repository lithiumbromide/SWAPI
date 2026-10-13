---
title: "SetSceneBkgDIBx64 Method (IModelDocExtension)"
project: "SOLIDWORKS API Help"
interface: "IModelDocExtension"
member: "SetSceneBkgDIBx64"
kind: "method"
source: "sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelDocExtension~SetSceneBkgDIBx64.html"
---

# SetSceneBkgDIBx64 Method (IModelDocExtension)

Sets the background image in 64-bit applications.

## Syntax

### Visual Basic (Declaration)

```vb
Sub SetSceneBkgDIBx64( _
   ByVal L_dib As System.Long _
)
```

### Visual Basic (Usage)

```vb
Dim instance As IModelDocExtension
Dim L_dib As System.Long

instance.SetSceneBkgDIBx64(L_dib)
```

### C#

```csharp
void SetSceneBkgDIBx64(
   System.long L_dib
)
```

### C++/CLI

```cpp
void SetSceneBkgDIBx64(
   System.int64 L_dib
)
```

**NOTE:** See [Differences Between Unmanaged C++ and C++/CLI Code](DifferencesBetweenUnManagedAndCPPCLI.htm).

### Parameters

- `L_dib`: Background image as DIBSECTION

## VBA Syntax

See [ModelDocExtension::SetSceneBkgDIBx64](ms-its:sldworksapivb6.chm::/sldworks~ModelDocExtension~SetSceneBkgDIBx64.html).

## Remarks

This method is only available through early binding and with 64-bit versions of the SOLIDWORKS Design software.

Old background images are deleted automatically.

For more information about DIBSECTION, see MicroSoft's documentation.

## See Also

[IModelDocExtension Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelDocExtension.html)
[IModelDocExtension Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelDocExtension_members.html)
[IModelDocExtension::GetSceneBkgDIBx64 Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelDocExtension~GetSceneBkgDIBx64.html)
[IModelDoc2::GetSceneBkgDIB Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelDoc2~GetSceneBkgDIB.html)
[IModelDoc2::SetSceneBkgDIB Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelDoc2~SetSceneBkgDIB.html)
[IModelDoc2::InsertBkgImage Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelDoc2~InsertBkgImage.html)
[IModelDoc2::SceneBkgImageFileName Property](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelDoc2~SceneBkgImageFileName.html)

## Availability

SOLIDWORKS 2006 SP2, Revision Number 14.2
