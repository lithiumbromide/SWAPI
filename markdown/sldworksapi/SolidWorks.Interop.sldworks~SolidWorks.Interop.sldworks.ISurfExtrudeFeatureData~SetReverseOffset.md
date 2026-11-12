---
title: "SetReverseOffset Method (ISurfExtrudeFeatureData)"
project: "SOLIDWORKS API Help"
interface: "ISurfExtrudeFeatureData"
member: "SetReverseOffset"
kind: "method"
source: "sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISurfExtrudeFeatureData~SetReverseOffset.html"
---

# SetReverseOffset Method (ISurfExtrudeFeatureData)

Sets the reverse offset direction setting for the end condition of this extruded surface.

## Syntax

### Visual Basic (Declaration)

```vb
Sub SetReverseOffset( _
   ByVal Fwd As System.Boolean, _
   ByVal RevOffset As System.Boolean _
)
```

### Visual Basic (Usage)

```vb
Dim instance As ISurfExtrudeFeatureData
Dim Fwd As System.Boolean
Dim RevOffset As System.Boolean

instance.SetReverseOffset(Fwd, RevOffset)
```

### C#

```csharp
void SetReverseOffset(
   System.bool Fwd,
   System.bool RevOffset
)
```

### C++/CLI

```cpp
void SetReverseOffset(
   System.bool Fwd,
   System.bool RevOffset
)
```

**NOTE:** See [Differences Between Unmanaged C++ and C++/CLI Code](DifferencesBetweenUnManagedAndCPPCLI.htm).

### Parameters

- `Fwd`: True sets the reverse offset setting in the forward direction, false sets it in the reverse direction
- `RevOffset`: True enables the reverse offset setting, false disables it

## VBA Syntax

See [SurfExtrudeFeatureData::SetReverseOffset](ms-its:sldworksapivb6.chm::/sldworks~SurfExtrudeFeatureData~SetReverseOffset.html).

## Remarks

See [Accessing Selections that Define Features](sldworksAPIProgGuide.chm::/Miscellaneous/Accessing_Selections_that_Define_Features.htm) for additional details.

## See Also

[ISurfExtrudeFeatureData Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISurfExtrudeFeatureData.html)
[ISurfExtrudeFeatureData Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISurfExtrudeFeatureData_members.html)
[ISurfExtrudeFeatureData::GetReverseOffset Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISurfExtrudeFeatureData~GetReverseOffset.html)

## Availability

SOLIDWORKS 2001Plus SP1, Revision Number 10.1
