---
title: "GetDraftAngle Method (IExtrudeFeatureData2)"
project: "SOLIDWORKS API Help"
interface: "IExtrudeFeatureData2"
member: "GetDraftAngle"
kind: "method"
source: "sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IExtrudeFeatureData2~GetDraftAngle.html"
---

# GetDraftAngle Method (IExtrudeFeatureData2)

Gets the draft angle of the extrusion in the forward or reverse direction.

## Syntax

### Visual Basic (Declaration)

```vb
Function GetDraftAngle( _
   ByVal Forward As System.Boolean _
) As System.Double
```

### Visual Basic (Usage)

```vb
Dim instance As IExtrudeFeatureData2
Dim Forward As System.Boolean
Dim value As System.Double

value = instance.GetDraftAngle(Forward)
```

### C#

```csharp
System.double GetDraftAngle(
   System.bool Forward
)
```

### C++/CLI

```cpp
System.double GetDraftAngle(
   System.bool Forward
)
```

**NOTE:** See [Differences Between Unmanaged C++ and C++/CLI Code](DifferencesBetweenUnManagedAndCPPCLI.htm).

### Parameters

- `Forward`: True for forward direction, false for reverse

### Return Value

Draft angle of the extrusion in radians

## VBA Syntax

See [ExtrudeFeatureData2::GetDraftAngle](ms-its:sldworksapivb6.chm::/sldworks~ExtrudeFeatureData2~GetDraftAngle.html).

## See Also

[IExtrudeFeatureData2 Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IExtrudeFeatureData2.html)
[IExtrudeFeatureData2 Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IExtrudeFeatureData2_members.html)
[IExtrudeFeatureData2::GetDraftOutward Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IExtrudeFeatureData2~GetDraftOutward.html)
[IExtrudeFeatureData2::GetDraftWhileExtruding Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IExtrudeFeatureData2~GetDraftWhileExtruding.html)
[IExtrudeFeatureData2::SetDraftAngle Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IExtrudeFeatureData2~SetDraftAngle.html)
[IExtrudeFeatureData2::SetDraftOutward Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IExtrudeFeatureData2~SetDraftOutward.html)
[IExtrudeFeatureData2::SetDraftWhileExtruding Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IExtrudeFeatureData2~SetDraftWhileExtruding.html)

## Availability

SOLIDWORKS 2001Plus FCS, Revision Number 10.0
