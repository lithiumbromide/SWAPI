---
title: "SetDraftWhileExtruding Method (IExtrudeFeatureData2)"
project: "SOLIDWORKS API Help"
interface: "IExtrudeFeatureData2"
member: "SetDraftWhileExtruding"
kind: "method"
source: "sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IExtrudeFeatureData2~SetDraftWhileExtruding.html"
---

# SetDraftWhileExtruding Method (IExtrudeFeatureData2)

Sets whether the feature is drafted while extruding in the forward or reverse direction.

## Syntax

### Visual Basic (Declaration)

```vb
Sub SetDraftWhileExtruding( _
   ByVal Forward As System.Boolean, _
   ByVal DraftWhileExtrude As System.Boolean _
)
```

### Visual Basic (Usage)

```vb
Dim instance As IExtrudeFeatureData2
Dim Forward As System.Boolean
Dim DraftWhileExtrude As System.Boolean

instance.SetDraftWhileExtruding(Forward, DraftWhileExtrude)
```

### C#

```csharp
void SetDraftWhileExtruding(
   System.bool Forward,
   System.bool DraftWhileExtrude
)
```

### C++/CLI

```cpp
void SetDraftWhileExtruding(
   System.bool Forward,
   System.bool DraftWhileExtrude
)
```

**NOTE:** See [Differences Between Unmanaged C++ and C++/CLI Code](DifferencesBetweenUnManagedAndCPPCLI.htm).

### Parameters

- `Forward`: True for forward direction, false for reverse
- `DraftWhileExtrude`: True if the feature is drafted while extruding, false if not

## VBA Syntax

See [ExtrudeFeatureData2::SetDraftWhileExtruding](ms-its:sldworksapivb6.chm::/sldworks~ExtrudeFeatureData2~SetDraftWhileExtruding.html).

## See Also

[IExtrudeFeatureData2 Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IExtrudeFeatureData2.html)
[IExtrudeFeatureData2 Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IExtrudeFeatureData2_members.html)
[IExtrudeFeatureData2::GetDraftWhileExtruding Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IExtrudeFeatureData2~GetDraftWhileExtruding.html)
[IExtrudeFeatureData2::GetDraftAngle Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IExtrudeFeatureData2~GetDraftAngle.html)
[IExtrudeFeatureData2::GetDraftOutward Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IExtrudeFeatureData2~GetDraftOutward.html)
[IExtrudeFeatureData2::SetDraftAngle Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IExtrudeFeatureData2~SetDraftAngle.html)
[IExtrudeFeatureData2::SetDraftOutward Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IExtrudeFeatureData2~SetDraftOutward.html)

## Availability

SOLIDWORKS 2001Plus FCS, Revision Number 10.0
