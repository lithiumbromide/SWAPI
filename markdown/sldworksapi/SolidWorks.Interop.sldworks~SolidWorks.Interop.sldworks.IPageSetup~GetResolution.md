---
title: "GetResolution Method (IPageSetup)"
project: "SOLIDWORKS API Help"
interface: "IPageSetup"
member: "GetResolution"
kind: "method"
source: "sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IPageSetup~GetResolution.html"
---

# GetResolution Method (IPageSetup)

Gets the current printer resolution on documents and drawing sheets.

## Syntax

### Visual Basic (Declaration)

```vb
Function GetResolution() As System.Integer
```

### Visual Basic (Usage)

```vb
Dim instance As IPageSetup
Dim value As System.Integer

value = instance.GetResolution()
```

### C#

```csharp
System.int GetResolution()
```

### C++/CLI

```cpp
System.int GetResolution();
```

**NOTE:** See [Differences Between Unmanaged C++ and C++/CLI Code](DifferencesBetweenUnManagedAndCPPCLI.htm).

### Return Value

Current printer resolution

## VBA Syntax

See [PageSetup::GetResolution](ms-its:sldworksapivb6.chm::/sldworks~PageSetup~GetResolution.html).

## See Also

[IPageSetup Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IPageSetup.html)
[IPageSetup Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IPageSetup_members.html)
[IPageSetup::GetUseDefaultResolution Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IPageSetup~GetUseDefaultResolution.html)
[IPageSetup::SetResolution Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IPageSetup~SetResolution.html)

## Availability

SOLIDWORKS 2004 FCS, Revision Number 12.0
