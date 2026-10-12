---
title: "GetFacePairCount Method (IMidSurface3)"
project: "SOLIDWORKS API Help"
interface: "IMidSurface3"
member: "GetFacePairCount"
kind: "method"
source: "sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IMidSurface3~GetFacePairCount.html"
---

# GetFacePairCount Method (IMidSurface3)

Gets the number of parallel pairs of faces found in the original part body that were used to calculate the midsurface feature.

## Syntax

### Visual Basic (Declaration)

```vb
Function GetFacePairCount() As System.Integer
```

### Visual Basic (Usage)

```vb
Dim instance As IMidSurface3
Dim value As System.Integer

value = instance.GetFacePairCount()
```

### C#

```csharp
System.int GetFacePairCount()
```

### C++/CLI

```cpp
System.int GetFacePairCount();
```

**NOTE:** See [Differences Between Unmanaged C++ and C++/CLI Code](DifferencesBetweenUnManagedAndCPPCLI.htm).

### Return Value

Number of parallel face pairs from the original part body

## VBA Syntax

See [MidSurface3::GetFacePairCount](ms-its:sldworksapivb6.chm::/sldworks~MidSurface3~GetFacePairCount.html).

## See Also

[IMidSurface3 Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IMidSurface3.html)
[IMidSurface3 Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IMidSurface3_members.html)
[IMidSurface3::GetFirstFacePair Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IMidSurface3~GetFirstFacePair.html)
[IMidSurface3::GetNextFacePair Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IMidSurface3~GetNextFacePair.html)
[IMidSurface3::IGetFirstFacePair Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IMidSurface3~IGetFirstFacePair.html)
[IMidSurface3::IGetNextFacePair Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IMidSurface3~IGetNextFacePair.html)

## Availability

SOLIDWORKS 2009 FCS, Revision Number 17.0
