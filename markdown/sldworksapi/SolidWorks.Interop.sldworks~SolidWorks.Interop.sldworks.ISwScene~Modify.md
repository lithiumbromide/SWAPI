---
title: "Modify Method (ISwScene)"
project: "SOLIDWORKS API Help"
interface: "ISwScene"
member: "Modify"
kind: "method"
source: "sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISwScene~Modify.html"
---

# Modify Method (ISwScene)

Modifies and saves this scene.

## Syntax

### Visual Basic (Declaration)

```vb
Function Modify() As System.Boolean
```

### Visual Basic (Usage)

```vb
Dim instance As ISwScene
Dim value As System.Boolean

value = instance.Modify()
```

### C#

```csharp
System.bool Modify()
```

### C++/CLI

```cpp
System.bool Modify();
```

**NOTE:** See [Differences Between Unmanaged C++ and C++/CLI Code](DifferencesBetweenUnManagedAndCPPCLI.htm).

### Return Value

True if the scene is successfully modified and saved, false if not

## VBA Syntax

See [SwScene::Modify](ms-its:sldworksapivb6.chm::/sldworks~SwScene~Modify.html).

## See Also

[ISwScene Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISwScene.html)
[ISwScene Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISwScene_members.html)

## Availability

SOLIDWORKS 2015 FCS, Revision Number 23.0
