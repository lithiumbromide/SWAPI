---
title: "OffsetToGeometry Method (ISwScene)"
project: "SOLIDWORKS API Help"
interface: "ISwScene"
member: "OffsetToGeometry"
kind: "method"
source: "sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISwScene~OffsetToGeometry.html"
---

# OffsetToGeometry Method (ISwScene)

Resets the floor offset.

## Syntax

### Visual Basic (Declaration)

```vb
Function OffsetToGeometry() As System.Boolean
```

### Visual Basic (Usage)

```vb
Dim instance As ISwScene
Dim value As System.Boolean

value = instance.OffsetToGeometry()
```

### C#

```csharp
System.bool OffsetToGeometry()
```

### C++/CLI

```cpp
System.bool OffsetToGeometry();
```

**NOTE:** See [Differences Between Unmanaged C++ and C++/CLI Code](DifferencesBetweenUnManagedAndCPPCLI.htm).

### Return Value

True if successful, false if not

## VBA Syntax

See [SwScene::OffsetToGeometry](ms-its:sldworksapivb6.chm::/sldworks~SwScene~OffsetToGeometry.html).

## Remarks

Calling this method invalidates previous calls to [ISwScene::FloorOffset](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISwScene~FloorOffset.html) and [ISwScene::FloorOffsetDirection](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISwScene~FloorOffsetDirection.html).

## See Also

[ISwScene Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISwScene.html)
[ISwScene Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISwScene_members.html)

## Availability

SOLIDWORKS 2015 FCS, Revision Number 23.0
