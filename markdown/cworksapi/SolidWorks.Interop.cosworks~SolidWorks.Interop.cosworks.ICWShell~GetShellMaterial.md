---
title: "GetShellMaterial Method (ICWShell)"
project: "SOLIDWORKS Simulation API Help"
interface: "ICWShell"
member: "GetShellMaterial"
kind: "method"
source: "cworksapi/SolidWorks.Interop.cosworks~SolidWorks.Interop.cosworks.ICWShell~GetShellMaterial.html"
---

# GetShellMaterial Method (ICWShell)

Gets the material applied to the shell for analysis.

## Syntax

### Visual Basic (Declaration)

```vb
Function GetShellMaterial() As CWMaterial
```

### Visual Basic (Usage)

```vb
Dim instance As ICWShell
Dim value As CWMaterial

value = instance.GetShellMaterial()
```

### C#

```csharp
CWMaterial GetShellMaterial()
```

### C++/CLI

```cpp
CWMaterial^ GetShellMaterial();
```

### Return Value

[Material](SOLIDWORKS.Interop.cosworks~SOLIDWORKS.Interop.cosworks.ICWMaterial.html) or Nothing or null if no material was applied to the shell

## VBA Syntax

See [CWShell::GetShellMaterial](ms-its:cworksapivb6.chm::/CosmosWorksLib~CWShell~GetShellMaterial.html).

## See Also

[ICWShell Interface](SolidWorks.Interop.cosworks~SolidWorks.Interop.cosworks.ICWShell.html)
[ICWShell Members](SolidWorks.Interop.cosworks~SolidWorks.Interop.cosworks.ICWShell_members.html)
[ICWShell::GetDefaultMaterial Method](SolidWorks.Interop.cosworks~SolidWorks.Interop.cosworks.ICWShell~GetDefaultMaterial.html)
[ICWShell::SetLibraryMaterial Method](SolidWorks.Interop.cosworks~SolidWorks.Interop.cosworks.ICWShell~SetLibraryMaterial.html)
[ICWShell::SetShellMaterial Method](SolidWorks.Interop.cosworks~SolidWorks.Interop.cosworks.ICWShell~SetShellMaterial.html)

## Availability

SOLIDWORKS Simulation API 2008 SP1.0
