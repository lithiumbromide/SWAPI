---
title: "GetFeature Method (ITableAnchor)"
project: "SOLIDWORKS API Help"
interface: "ITableAnchor"
member: "GetFeature"
kind: "method"
source: "sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ITableAnchor~GetFeature.html"
---

# GetFeature Method (ITableAnchor)

Gets the feature for this table anchor.

## Syntax

### Visual Basic (Declaration)

```vb
Function GetFeature() As Feature
```

### Visual Basic (Usage)

```vb
Dim instance As ITableAnchor
Dim value As Feature

value = instance.GetFeature()
```

### C#

```csharp
Feature GetFeature()
```

### C++/CLI

```cpp
Feature^ GetFeature();
```

**NOTE:** See [Differences Between Unmanaged C++ and C++/CLI Code](DifferencesBetweenUnManagedAndCPPCLI.htm).

### Return Value

[IFeature](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.IFeature.html) object for this table anchor

## VBA Syntax

See [TableAnchor::GetFeature](ms-its:sldworksapivb6.chm::/sldworks~TableAnchor~GetFeature.html).

## See Also

[ITableAnchor Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ITableAnchor.html)
[ITableAnchor Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ITableAnchor_members.html)

## Availability

SOLIDWORKS 2006 FCS, Revision Number 14.0
