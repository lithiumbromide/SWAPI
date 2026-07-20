---
title: "SetLinkToDisplayState Method (IBomFeature)"
project: "SOLIDWORKS API Help"
interface: "IBomFeature"
member: "SetLinkToDisplayState"
kind: "method"
source: "sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IBomFeature~SetLinkToDisplayState.html"
---

# SetLinkToDisplayState Method (IBomFeature)

Sets the name of the Display State to which to link this BOM feature.

## Syntax

### Visual Basic (Declaration)

```vb
Function SetLinkToDisplayState( _
   ByVal DisplayStateName As System.String _
) As System.Integer
```

### Visual Basic (Usage)

```vb
Dim instance As IBomFeature
Dim DisplayStateName As System.String
Dim value As System.Integer

value = instance.SetLinkToDisplayState(DisplayStateName)
```

### C#

```csharp
System.int SetLinkToDisplayState(
   System.string DisplayStateName
)
```

### C++/CLI

```cpp
System.int SetLinkToDisplayState(
   System.String^ DisplayStateName
)
```

NOTE:

See

[Differences Between Unmanaged C++ and C++/CLI Code](DifferencesBetweenUnManagedAndCPPCLI.htm)

.

### Parameters

- `DisplayStateName`: Name of the Display State to link to the BOM

### Return Value

Return code as defined by

[swLinkBomToDisplayStateError_e](ms-its:swconst.chm::/SolidWorks.Interop.swconst~SolidWorks.Interop.swconst.swLinkBomToDisplayStateError_e.html)

## VBA Syntax

See

[BomFeature::SetLinkToDisplayState](ms-its:sldworksapivb6.chm::/sldworks~BomFeature~SetLinkToDisplayState.html)

.

## See Also

[IBomFeature Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IBomFeature.html)

[IBomFeature Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IBomFeature_members.html)

[IBomFeature::GetLinkToDisplayState Method ()](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IBomFeature~GetLinkToDisplayState.html)

## Availability

SOLIDWORKS 2025 SP01, Revision Number 33.1
