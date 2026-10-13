---
title: "SetDraftOutward Method (IExtrudeFeatureData2)"
project: "SOLIDWORKS API Help"
interface: "IExtrudeFeatureData2"
member: "SetDraftOutward"
kind: "method"
source: "sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IExtrudeFeatureData2~SetDraftOutward.html"
---

# SetDraftOutward Method (IExtrudeFeatureData2)

Sets whether the extrusion feature should draft outward in the forward or reverse direction.

## Syntax

### Visual Basic (Declaration)

```vb
Sub SetDraftOutward( _
   ByVal Forward As System.Boolean, _
   ByVal DraftOutward As System.Boolean _
)
```

### Visual Basic (Usage)

```vb
Dim instance As IExtrudeFeatureData2
Dim Forward As System.Boolean
Dim DraftOutward As System.Boolean

instance.SetDraftOutward(Forward, DraftOutward)
```

### C#

```csharp
void SetDraftOutward(
   System.bool Forward,
   System.bool DraftOutward
)
```

### C++/CLI

```cpp
void SetDraftOutward(
   System.bool Forward,
   System.bool DraftOutward
)
```

**NOTE:** See [Differences Between Unmanaged C++ and C++/CLI Code](DifferencesBetweenUnManagedAndCPPCLI.htm).

### Parameters

- `Forward`: True for forward direction, false for reverse
- `DraftOutward`: True if feature is drafted outward, false if not

## VBA Syntax

See [ExtrudeFeatureData2::SetDraftOutward](ms-its:sldworksapivb6.chm::/sldworks~ExtrudeFeatureData2~SetDraftOutward.html).

## See Also

[IExtrudeFeatureData2 Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IExtrudeFeatureData2.html)
[IExtrudeFeatureData2 Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IExtrudeFeatureData2_members.html)
[IExtrudeFeatureData2::SetDraftAngle Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IExtrudeFeatureData2~SetDraftAngle.html)
[IExtrudeFeatureData2::SetDraftWhileExtruding Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IExtrudeFeatureData2~SetDraftWhileExtruding.html)
[IExtrudeFeatureData2::GetDraftAngle Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IExtrudeFeatureData2~GetDraftAngle.html)
[IExtrudeFeatureData2::GetDraftOutward Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IExtrudeFeatureData2~GetDraftOutward.html)
[IExtrudeFeatureData2::GetDraftWhileExtruding Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IExtrudeFeatureData2~GetDraftWhileExtruding.html)

## Availability

SOLIDWORKS 2001Plus FCS, Revision Number 10.0
