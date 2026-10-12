---
title: "GetDynamicMirror Method (ISketchManager)"
project: "SOLIDWORKS API Help"
interface: "ISketchManager"
member: "GetDynamicMirror"
kind: "method"
source: "sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISketchManager~GetDynamicMirror.html"
---

# GetDynamicMirror Method (ISketchManager)

Gets whether dynamic sketch mirroring, which is the automatic mirroring of newly created sketch entities about a selected centerline, is enabled.

## Syntax

### Visual Basic (Declaration)

```vb
Function GetDynamicMirror() As System.Boolean
```

### Visual Basic (Usage)

```vb
Dim instance As ISketchManager
Dim value As System.Boolean

value = instance.GetDynamicMirror()
```

### C#

```csharp
System.bool GetDynamicMirror()
```

### C++/CLI

```cpp
System.bool GetDynamicMirror();
```

**NOTE:** See [Differences Between Unmanaged C++ and C++/CLI Code](DifferencesBetweenUnManagedAndCPPCLI.htm).

### Return Value

True if dynamic sketch mirroring is enabled, false if not

## VBA Syntax

See [SketchManager::GetDynamicMirror](ms-its:sldworksapivb6.chm::/sldworks~SketchManager~GetDynamicMirror.html).

## See Also

[ISketchManager Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISketchManager.html)
[ISketchManager Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISketchManager_members.html)
[ISketchManager::SetDynamicMirror Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISketchManager~SetDynamicMirror.html)

## Availability

SOLIDWORKS 2005 FCS, Revision Number 13.0
