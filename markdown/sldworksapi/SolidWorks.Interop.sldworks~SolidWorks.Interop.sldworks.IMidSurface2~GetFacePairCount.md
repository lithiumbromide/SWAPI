---
title: "GetFacePairCount Method (IMidSurface2)"
project: "SOLIDWORKS API Help"
interface: "IMidSurface2"
member: "GetFacePairCount"
kind: "method"
source: "sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IMidSurface2~GetFacePairCount.html"
---

# GetFacePairCount Method (IMidSurface2)

Obsolete. Superseded by [IMidSurface3::GetFacePairCount](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.IMidSurface3~GetFacePairCount.html).

## Syntax

### Visual Basic (Declaration)

```vb
Function GetFacePairCount() As System.Integer
```

### Visual Basic (Usage)

```vb
Dim instance As IMidSurface2
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

See [MidSurface2::GetFacePairCount](ms-its:sldworksapivb6.chm::/sldworks~MidSurface2~GetFacePairCount.html).

## See Also

[IMidSurface2 Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IMidSurface2.html)
[IMidSurface2 Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IMidSurface2_members.html)
[IMidSurface2::GetFirstFacePair Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IMidSurface2~GetFirstFacePair.html)
[IMidSurface2::GetNextFacePair Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IMidSurface2~GetNextFacePair.html)
[IMidSurface2::IGetFirstFacePair Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IMidSurface2~IGetFirstFacePair.html)
[IMidSurface2::IGetNextFacePair Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IMidSurface2~IGetNextFacePair.html)

## Availability

SOLIDWORKS 2001Plus FCS, Revision Number 10.0
