---
title: "GetUseDefaultResolution Method (IPageSetup)"
project: "SOLIDWORKS API Help"
interface: "IPageSetup"
member: "GetUseDefaultResolution"
kind: "method"
source: "sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IPageSetup~GetUseDefaultResolution.html"
---

# GetUseDefaultResolution Method (IPageSetup)

Gets whether the printer default resolution is in use on documents and drawing sheets.

## Syntax

### Visual Basic (Declaration)

```vb
Function GetUseDefaultResolution() As System.Boolean
```

### Visual Basic (Usage)

```vb
Dim instance As IPageSetup
Dim value As System.Boolean

value = instance.GetUseDefaultResolution()
```

### C#

```csharp
System.bool GetUseDefaultResolution()
```

### C++/CLI

```cpp
System.bool GetUseDefaultResolution();
```

**NOTE:** See [Differences Between Unmanaged C++ and C++/CLI Code](DifferencesBetweenUnManagedAndCPPCLI.htm).

### Return Value

True if printer default resolution is in use, false if not

## VBA Syntax

See [PageSetup::GetUseDefaultResolution](ms-its:sldworksapivb6.chm::/sldworks~PageSetup~GetUseDefaultResolution.html).

## See Also

[IPageSetup Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IPageSetup.html)
[IPageSetup Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IPageSetup_members.html)
[IPageSetup::GetResolution Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IPageSetup~GetResolution.html)
[IPageSetup::SetResolution Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IPageSetup~SetResolution.html)

## Availability

SOLIDWORKS 2004 FCS, Revision Number 12.0
