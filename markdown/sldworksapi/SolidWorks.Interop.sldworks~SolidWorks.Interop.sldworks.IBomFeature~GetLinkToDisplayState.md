---
title: "GetLinkToDisplayState Method (IBomFeature)"
project: "SOLIDWORKS API Help"
interface: "IBomFeature"
member: "GetLinkToDisplayState"
kind: "method"
source: "sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IBomFeature~GetLinkToDisplayState.html"
---

# GetLinkToDisplayState Method (IBomFeature)

Gets the name of the Display State linked to this BOM feature.

## Syntax

### Visual Basic (Declaration)

```vb
Function GetLinkToDisplayState() As System.String
```

### Visual Basic (Usage)

```vb
Dim instance As IBomFeature
Dim value As System.String

value = instance.GetLinkToDisplayState()
```

### C#

```csharp
System.string GetLinkToDisplayState()
```

### C++/CLI

```cpp
System.String^ GetLinkToDisplayState();
```

NOTE:

See

[Differences Between Unmanaged C++ and C++/CLI Code](DifferencesBetweenUnManagedAndCPPCLI.htm)

.

### Return Value

Name of the Display State linked to the BOM

## VBA Syntax

See

[BomFeature::GetLinkToDisplayState](ms-its:sldworksapivb6.chm::/sldworks~BomFeature~GetLinkToDisplayState.html)

.

## See Also

[IBomFeature Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IBomFeature.html)

[IBomFeature Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IBomFeature_members.html)

[IBomFeature::SetLinkToDisplayState Method ()](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IBomFeature~SetLinkToDisplayState.html)

## Availability

SOLIDWORKS 2025 SP01, Revision Number 33.1
