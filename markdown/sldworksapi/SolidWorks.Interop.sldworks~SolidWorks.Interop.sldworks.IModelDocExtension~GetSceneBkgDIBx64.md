---
title: "GetSceneBkgDIBx64 Method (IModelDocExtension)"
project: "SOLIDWORKS API Help"
interface: "IModelDocExtension"
member: "GetSceneBkgDIBx64"
kind: "method"
source: "sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelDocExtension~GetSceneBkgDIBx64.html"
---

# GetSceneBkgDIBx64 Method (IModelDocExtension)

Gets the background image as DIBSECTION in 64-bit applications.

## Syntax

### Visual Basic (Declaration)

```vb
Function GetSceneBkgDIBx64() As System.Long
```

### Visual Basic (Usage)

```vb
Dim instance As IModelDocExtension
Dim value As System.Long

value = instance.GetSceneBkgDIBx64()
```

### C#

```csharp
System.long GetSceneBkgDIBx64()
```

### C++/CLI

```cpp
System.int64 GetSceneBkgDIBx64();
```

**NOTE:** See [Differences Between Unmanaged C++ and C++/CLI Code](DifferencesBetweenUnManagedAndCPPCLI.htm).

### Return Value

Background image as DIBSECTION

## VBA Syntax

See [ModelDocExtension::GetSceneBkgDIBx64](ms-its:sldworksapivb6.chm::/Sldworks~ModelDocExtension~GetSceneBkgDIBx64.html).

## Remarks

This method is only available through early binding and with 64-bit versions of the SOLIDWORKS Design software.

The memory for the image bits ( DIBSECTION.dsBm.bmBits) and this structure are allocated by the SOLIDWORKS Design application and must be deleted by the caller.

## See Also

[IModelDocExtension Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelDocExtension.html)
[IModelDocExtension Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelDocExtension_members.html)
[IModelDocExtension::SetSceneBkgDIBx64 Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelDocExtension~SetSceneBkgDIBx64.html)
[IModelDoc2::GetSceneBkgDIB Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelDoc2~GetSceneBkgDIB.html)
[IModelDoc2::SetSceneBkgDIB Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelDoc2~SetSceneBkgDIB.html)
[IModelDoc2::InsertBkgImage Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelDoc2~InsertBkgImage.html)
[IModelDoc2::SceneBkgImageFileName Property](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelDoc2~SceneBkgImageFileName.html)

## Availability

SOLIDWORKS 2006 SP2, Revision Number 14.2
