---
title: "DeleteShell Method (ICWShellManager)"
project: "SOLIDWORKS Simulation API Help"
interface: "ICWShellManager"
member: "DeleteShell"
kind: "method"
source: "cworksapi/SolidWorks.Interop.cosworks~SolidWorks.Interop.cosworks.ICWShellManager~DeleteShell.html"
---

# DeleteShell Method (ICWShellManager)

Deletes a shell from the study.

## Syntax

### Visual Basic (Declaration)

```vb
Sub DeleteShell( _
   ByVal SName As System.String _
)
```

### Visual Basic (Usage)

```vb
Dim instance As ICWShellManager
Dim SName As System.String

instance.DeleteShell(SName)
```

### C#

```csharp
void DeleteShell(
   System.string SName
)
```

### C++/CLI

```cpp
void DeleteShell(
   System.String^ SName
)
```

### Parameters

- `SName`: Name of the shell to delete

## VBA Syntax

See [CWShellManager::DeleteShell](ms-its:cworksapivb6.chm::/CosmosWorksLib~CWShellManager~DeleteShell.html).

## See Also

[ICWShellManager Interface](SolidWorks.Interop.cosworks~SolidWorks.Interop.cosworks.ICWShellManager.html)
[ICWShellManager Members](SolidWorks.Interop.cosworks~SolidWorks.Interop.cosworks.ICWShellManager_members.html)
[ICWShell::Name Property](SolidWorks.Interop.cosworks~SolidWorks.Interop.cosworks.ICWShell~Name.html)
[ICWShellManager::CreateShell Method](SolidWorks.Interop.cosworks~SolidWorks.Interop.cosworks.ICWShellManager~CreateShell.html)

## Availability

SOLIDWORKS Simulation API 2008 SP1.0
