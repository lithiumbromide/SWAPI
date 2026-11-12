---
title: "GetP2SFileName Method (ISwScene)"
project: "SOLIDWORKS API Help"
interface: "ISwScene"
member: "GetP2SFileName"
kind: "method"
source: "sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISwScene~GetP2SFileName.html"
---

# GetP2SFileName Method (ISwScene)

Gets the scene file for this scene.

## Syntax

### Visual Basic (Declaration)

```vb
Sub GetP2SFileName( _
   ByRef Val As System.String _
)
```

### Visual Basic (Usage)

```vb
Dim instance As ISwScene
Dim Val As System.String

instance.GetP2SFileName(Val)
```

### C#

```csharp
void GetP2SFileName(
   out System.string Val
)
```

### C++/CLI

```cpp
void GetP2SFileName(
   [Out] System.String^ Val
)
```

**NOTE:** See [Differences Between Unmanaged C++ and C++/CLI Code](DifferencesBetweenUnManagedAndCPPCLI.htm).

### Parameters

- `Val`: Fully qualilfied path to a scene file (***.p2s**)

## VBA Syntax

See [SwScene::GetP2SFileName](ms-its:sldworksapivb6.chm::/sldworks~SwScene~GetP2SFileName.html).

## Examples

See the [ISwScene](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISwScene.html) examples.

## See Also

[ISwScene Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISwScene.html)
[ISwScene Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISwScene_members.html)

## Availability

SOLIDWORKS 2015 FCS, Revision Number 23.0
