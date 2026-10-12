---
title: "GetBodyIndexKept Method (ISurfaceCutFeatureData)"
project: "SOLIDWORKS API Help"
interface: "ISurfaceCutFeatureData"
member: "GetBodyIndexKept"
kind: "method"
source: "sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISurfaceCutFeatureData~GetBodyIndexKept.html"
---

# GetBodyIndexKept Method (ISurfaceCutFeatureData)

Gets the index of the body kept while resolving ambiguity for this surface-cut feature.

## Syntax

### Visual Basic (Declaration)

```vb
Function GetBodyIndexKept() As System.Short
```

### Visual Basic (Usage)

```vb
Dim instance As ISurfaceCutFeatureData
Dim value As System.Short

value = instance.GetBodyIndexKept()
```

### C#

```csharp
System.short GetBodyIndexKept()
```

### C++/CLI

```cpp
System.short GetBodyIndexKept();
```

**NOTE:** See [Differences Between Unmanaged C++ and C++/CLI Code](DifferencesBetweenUnManagedAndCPPCLI.htm).

### Return Value

Body index

## VBA Syntax

See [SurfCutFeatureData::GetBodyIndexKept](ms-its:sldworksapivb6.chm::/sldworks~SurfCutFeatureData~GetBodyIndexKept.html).

## Remarks

To access this interface, you must declare it as SurfCutFeatureData or ISurfCutFeatureData.

## See Also

[ISurfaceCutFeatureData Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISurfaceCutFeatureData.html)
[ISurfaceCutFeatureData Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISurfaceCutFeatureData_members.html)

## Availability

SOLIDWORKS 2001Plus FCS, Revision Number 10.0
