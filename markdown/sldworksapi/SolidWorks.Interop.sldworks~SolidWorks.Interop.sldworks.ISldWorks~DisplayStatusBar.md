---
title: "DisplayStatusBar Method (ISldWorks)"
project: "SOLIDWORKS API Help"
interface: "ISldWorks"
member: "DisplayStatusBar"
kind: "method"
source: "sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISldWorks~DisplayStatusBar.html"
---

# DisplayStatusBar Method (ISldWorks)

Sets whether to display the status bar.

## Syntax

### Visual Basic (Declaration)

```vb
Sub DisplayStatusBar( _
   ByVal OnOff As System.Boolean _
)
```

### Visual Basic (Usage)

```vb
Dim instance As ISldWorks
Dim OnOff As System.Boolean

instance.DisplayStatusBar(OnOff)
```

### C#

```csharp
void DisplayStatusBar(
   System.bool OnOff
)
```

### C++/CLI

```cpp
void DisplayStatusBar(
   System.bool OnOff
)
```

**NOTE:** See [Differences Between Unmanaged C++ and C++/CLI Code](DifferencesBetweenUnManagedAndCPPCLI.htm).

### Parameters

- `OnOff`: True if you want the status bar displayed, false if not

## VBA Syntax

See [SldWorks::DisplayStatusBar](ms-its:sldworksapivb6.chm::/sldworks~SldWorks~DisplayStatusBar.html).

## See Also

[ISldWorks Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISldWorks.html)
[ISldWorks Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISldWorks_members.html)
[IModelDoc2::Lock Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelDoc2~Lock.html)
[IModelDoc2::UnLock Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelDoc2~UnLock.html)
[IStatusBarPane Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IStatusBarPane.html)
