---
title: "BlockSkinning Method (ISldWorks)"
project: "SOLIDWORKS API Help"
interface: "ISldWorks"
member: "BlockSkinning"
kind: "method"
source: "sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISldWorks~BlockSkinning.html"
---

# BlockSkinning Method (ISldWorks)

Blocks skinning a window, which prevents a window from looking like a SOLIDWORKS window.

## Syntax

### Visual Basic (Declaration)

```vb
Function BlockSkinning() As System.Boolean
```

### Visual Basic (Usage)

```vb
Dim instance As ISldWorks
Dim value As System.Boolean

value = instance.BlockSkinning()
```

### C#

```csharp
System.bool BlockSkinning()
```

### C++/CLI

```cpp
System.bool BlockSkinning();
```

**NOTE:** See [Differences Between Unmanaged C++ and C++/CLI Code](DifferencesBetweenUnManagedAndCPPCLI.htm).

### Return Value

True if successful, false if not

## VBA Syntax

See [SldWorks::BlockSkinning](ms-its:sldworksapivb6.chm::/Sldworks~SldWorks~BlockSkinning.html).

## Remarks

You must call [ISldWorks::ResumeSkinning](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.ISldWorks~ResumeSkinning.html) after creating your unskinned window so that new windows created by SOLIDWORKS and other add-ins are displayed as intended.

## See Also

[ISldWorks Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISldWorks.html)
[ISldWorks Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISldWorks_members.html)

## Availability

SOLIDWORKS 2008 FCS, Revision Number 16.0
