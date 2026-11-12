---
title: "SetDraftAngle Method (IExtrudeFeatureData2)"
project: "SOLIDWORKS API Help"
interface: "IExtrudeFeatureData2"
member: "SetDraftAngle"
kind: "method"
source: "sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IExtrudeFeatureData2~SetDraftAngle.html"
---

# SetDraftAngle Method (IExtrudeFeatureData2)

Sets the draft angle of the extrusion in the forward or reverse direction.

## Syntax

### Visual Basic (Declaration)

```vb
Sub SetDraftAngle( _
   ByVal Forward As System.Boolean, _
   ByVal DraftAngle As System.Double _
)
```

### Visual Basic (Usage)

```vb
Dim instance As IExtrudeFeatureData2
Dim Forward As System.Boolean
Dim DraftAngle As System.Double

instance.SetDraftAngle(Forward, DraftAngle)
```

### C#

```csharp
void SetDraftAngle(
   System.bool Forward,
   System.double DraftAngle
)
```

### C++/CLI

```cpp
void SetDraftAngle(
   System.bool Forward,
   System.double DraftAngle
)
```

**NOTE:** See [Differences Between Unmanaged C++ and C++/CLI Code](DifferencesBetweenUnManagedAndCPPCLI.htm).

### Parameters

- `Forward`: True for forward direction, false for reverse
- `DraftAngle`: Draft angle of the extrusion in radians

## VBA Syntax

See [ExtrudeFeatureData2::SetDraftAngle](ms-its:sldworksapivb6.chm::/sldworks~ExtrudeFeatureData2~SetDraftAngle.html).

## See Also

[IExtrudeFeatureData2 Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IExtrudeFeatureData2.html)
[IExtrudeFeatureData2 Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IExtrudeFeatureData2_members.html)
[IExtrudedFeatureData2::GetDraftAngle Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IExtrudeFeatureData2~GetDraftAngle.html)
[IExtrudedFeatureData2::GetDraftOutward Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IExtrudeFeatureData2~GetDraftOutward.html)
[IExtrudedFeatureData2::GetDraftWhileExtruding Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IExtrudeFeatureData2~GetDraftWhileExtruding.html)
[IExtrudedFeatureData2::SetDraftOutward Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IExtrudeFeatureData2~SetDraftOutward.html)
[IExtrudedFeatureData2::SetDraftWhileExtruding Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IExtrudeFeatureData2~SetDraftWhileExtruding.html)

## Availability

SOLIDWORKS 2001Plus FCS, Revision Number 10.0
