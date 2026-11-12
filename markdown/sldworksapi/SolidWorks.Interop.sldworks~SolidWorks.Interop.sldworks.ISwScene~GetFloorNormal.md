---
title: "GetFloorNormal Method (ISwScene)"
project: "SOLIDWORKS API Help"
interface: "ISwScene"
member: "GetFloorNormal"
kind: "method"
source: "sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISwScene~GetFloorNormal.html"
---

# GetFloorNormal Method (ISwScene)

Gets the normal to the floor of this scene.

## Syntax

### Visual Basic (Declaration)

```vb
Sub GetFloorNormal( _
   ByRef Point As MathPoint, _
   ByRef Normal As MathVector _
)
```

### Visual Basic (Usage)

```vb
Dim instance As ISwScene
Dim Point As MathPoint
Dim Normal As MathVector

instance.GetFloorNormal(Point, Normal)
```

### C#

```csharp
void GetFloorNormal(
   out MathPoint Point,
   out MathVector Normal
)
```

### C++/CLI

```cpp
void GetFloorNormal(
   [Out] MathPoint^ Point,
   [Out] MathVector^ Normal
)
```

**NOTE:** See [Differences Between Unmanaged C++ and C++/CLI Code](DifferencesBetweenUnManagedAndCPPCLI.htm).

### Parameters

- `Point`: [IMathPoint](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IMathPoint.html)
- `Normal`: [IMathVector](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IMathVector.html)

## VBA Syntax

See [SwScene::GetFloorNormal](ms-its:sldworksapivb6.chm::/sldworks~SwScene~GetFloorNormal.html).

## Examples

See the [ISwScene](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISwScene.html) examples.

## See Also

[ISwScene Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISwScene.html)
[ISwScene Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISwScene_members.html)

## Availability

SOLIDWORKS 2015 FCS, Revision Number 23.0
