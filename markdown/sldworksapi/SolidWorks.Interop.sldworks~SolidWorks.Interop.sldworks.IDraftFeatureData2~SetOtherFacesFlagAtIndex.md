---
title: "SetOtherFacesFlagAtIndex Method (IDraftFeatureData2)"
project: "SOLIDWORKS API Help"
interface: "IDraftFeatureData2"
member: "SetOtherFacesFlagAtIndex"
kind: "method"
source: "sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IDraftFeatureData2~SetOtherFacesFlagAtIndex.html"
---

# SetOtherFacesFlagAtIndex Method (IDraftFeatureData2)

Sets the **Other Face** option.

## Syntax

### Visual Basic (Declaration)

```vb
Sub SetOtherFacesFlagAtIndex( _
   ByVal Index As System.Short, _
   ByVal Flag As System.Boolean _
)
```

### Visual Basic (Usage)

```vb
Dim instance As IDraftFeatureData2
Dim Index As System.Short
Dim Flag As System.Boolean

instance.SetOtherFacesFlagAtIndex(Index, Flag)
```

### C#

```csharp
void SetOtherFacesFlagAtIndex(
   System.short Index,
   System.bool Flag
)
```

### C++/CLI

```cpp
void SetOtherFacesFlagAtIndex(
   System.short Index,
   System.bool Flag
)
```

**NOTE:** See [Differences Between Unmanaged C++ and C++/CLI Code](DifferencesBetweenUnManagedAndCPPCLI.htm).

### Parameters

- `Index`: Number indicating a segment of the parting line
- `Flag`: True to specify a different draft direction for each segment of the parting line,
  false to not

## VBA Syntax

See [DraftFeatureData2::SetOtherFacesFlagAtIndex](ms-its:sldworksapivb6.chm::/sldworks~DraftFeatureData2~SetOtherFacesFlagAtIndex.html).

## See Also

[IDraftFeatureData2 Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IDraftFeatureData2.html)
[IDraftFeatureData2 Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IDraftFeatureData2_members.html)
[IDraftFeatureData2::GetOtherFacesFlagAtIndex Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IDraftFeatureData2~GetOtherFacesFlagAtIndex.html)

## Availability

SOLIDWORKS 2001Plus FCS, Revision Number 10.0
