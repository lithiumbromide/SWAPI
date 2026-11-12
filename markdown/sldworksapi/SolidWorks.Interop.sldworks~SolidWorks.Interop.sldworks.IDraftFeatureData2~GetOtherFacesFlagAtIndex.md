---
title: "GetOtherFacesFlagAtIndex Method (IDraftFeatureData2)"
project: "SOLIDWORKS API Help"
interface: "IDraftFeatureData2"
member: "GetOtherFacesFlagAtIndex"
kind: "method"
source: "sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IDraftFeatureData2~GetOtherFacesFlagAtIndex.html"
---

# GetOtherFacesFlagAtIndex Method (IDraftFeatureData2)

Gets the value of the **Other Face** option at the specified index.

## Syntax

### Visual Basic (Declaration)

```vb
Function GetOtherFacesFlagAtIndex( _
   ByVal Index As System.Short _
) As System.Boolean
```

### Visual Basic (Usage)

```vb
Dim instance As IDraftFeatureData2
Dim Index As System.Short
Dim value As System.Boolean

value = instance.GetOtherFacesFlagAtIndex(Index)
```

### C#

```csharp
System.bool GetOtherFacesFlagAtIndex(
   System.short Index
)
```

### C++/CLI

```cpp
System.bool GetOtherFacesFlagAtIndex(
   System.short Index
)
```

**NOTE:** See [Differences Between Unmanaged C++ and C++/CLI Code](DifferencesBetweenUnManagedAndCPPCLI.htm).

### Parameters

- `Index`: Number indicating a segment of the parting line

### Return Value

True to specify a different draft direction for each segment of the parting line, false to not

## VBA Syntax

See [DraftFeatureData2::GetOtherFacesFlagAtIndex](ms-its:sldworksapivb6.chm::/sldworks~DraftFeatureData2~GetOtherFacesFlagAtIndex.html).

## Permissions

| Permission | Description |
| --- | --- |
| [New Item] |  |

## See Also

[IDraftFeatureData2 Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IDraftFeatureData2.html)
[IDraftFeatureData2 Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IDraftFeatureData2_members.html)
[IDraftFeatureData2::SetOtherFacesFlagAtIndex Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IDraftFeatureData2~SetOtherFacesFlagAtIndex.html)

## Availability

SOLIDWORKS 2001Plus FCS, Revision Number 10.0
