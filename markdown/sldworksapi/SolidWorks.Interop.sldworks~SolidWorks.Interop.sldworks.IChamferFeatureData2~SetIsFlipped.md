---
title: "SetIsFlipped Method (IChamferFeatureData2)"
project: "SOLIDWORKS API Help"
interface: "IChamferFeatureData2"
member: "SetIsFlipped"
kind: "method"
source: "sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IChamferFeatureData2~SetIsFlipped.html"
---

# SetIsFlipped Method (IChamferFeatureData2)

Gets whether the chamfer feature is flipped.

## Syntax

### Visual Basic (Declaration)

```vb
Sub SetIsFlipped( _
   ByVal Entity As System.Object, _
   ByVal Flip As System.Boolean _
)
```

### Visual Basic (Usage)

```vb
Dim instance As IChamferFeatureData2
Dim Entity As System.Object
Dim Flip As System.Boolean

instance.SetIsFlipped(Entity, Flip)
```

### C#

```csharp
void SetIsFlipped(
   System.object Entity,
   System.bool Flip
)
```

### C++/CLI

```cpp
void SetIsFlipped(
   System.Object^ Entity,
   System.bool Flip
)
```

**NOTE:** See [Differences Between Unmanaged C++ and C++/CLI Code](DifferencesBetweenUnManagedAndCPPCLI.htm).

### Parameters

- `Entity`: Chamfer feature
- `Flip`: True flips the chamfer feature, false does not

## VBA Syntax

See [ChamferFeatureData2::SetIsFlipped](ms-its:sldworksapivb6.chm::/sldworks~ChamferFeatureData2~SetIsFlipped.html).

## See Also

[IChamferFeatureData2 Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IChamferFeatureData2.html)
[IChamferFeatureData2 Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IChamferFeatureData2_members.html)
[IChamferFeatureData2::GetIsFlipped Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IChamferFeatureData2~GetIsFlipped.html)

## Availability

SOLIDWORKS 2001Plus FCS, Revision Number 10.0
