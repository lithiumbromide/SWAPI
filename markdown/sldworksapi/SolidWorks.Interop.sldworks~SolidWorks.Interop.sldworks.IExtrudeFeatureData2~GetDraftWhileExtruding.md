---
title: "GetDraftWhileExtruding Method (IExtrudeFeatureData2)"
project: "SOLIDWORKS API Help"
interface: "IExtrudeFeatureData2"
member: "GetDraftWhileExtruding"
kind: "method"
source: "sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IExtrudeFeatureData2~GetDraftWhileExtruding.html"
---

# GetDraftWhileExtruding Method (IExtrudeFeatureData2)

Gets whether the feature is drafted while extruding in the forward or reverse direction.

## Syntax

### Visual Basic (Declaration)

```vb
Function GetDraftWhileExtruding( _
   ByVal Forward As System.Boolean _
) As System.Boolean
```

### Visual Basic (Usage)

```vb
Dim instance As IExtrudeFeatureData2
Dim Forward As System.Boolean
Dim value As System.Boolean

value = instance.GetDraftWhileExtruding(Forward)
```

### C#

```csharp
System.bool GetDraftWhileExtruding(
   System.bool Forward
)
```

### C++/CLI

```cpp
System.bool GetDraftWhileExtruding(
   System.bool Forward
)
```

**NOTE:** See [Differences Between Unmanaged C++ and C++/CLI Code](DifferencesBetweenUnManagedAndCPPCLI.htm).

### Parameters

- `Forward`: True for forward direction, false for reverse

### Return Value

True if feature is drafted while extruding, false if not

## VBA Syntax

See [ExtrudeFeatureData2::GetDraftWhileExtruding](ms-its:sldworksapivb6.chm::/sldworks~ExtrudeFeatureData2~GetDraftWhileExtruding.html).

## See Also

[IExtrudeFeatureData2 Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IExtrudeFeatureData2.html)
[IExtrudeFeatureData2 Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IExtrudeFeatureData2_members.html)
[IExtrudeFeatureData2::GetDraftAngle Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IExtrudeFeatureData2~GetDraftAngle.html)
[IExtrudeFeatureData2::GetDraftOutward Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IExtrudeFeatureData2~GetDraftOutward.html)
[IExtrudeFeatureData2::SetDraftAngle Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IExtrudeFeatureData2~SetDraftAngle.html)
[IExtrudeFeatureData2::SetDraftOutward Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IExtrudeFeatureData2~SetDraftOutward.html)
[IExtrudeFeatureData2::SetDraftWhileExtruding Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IExtrudeFeatureData2~SetDraftWhileExtruding.html)

## Availability

SOLIDWORKS 2001Plus FCS, Revision Number 10.0
