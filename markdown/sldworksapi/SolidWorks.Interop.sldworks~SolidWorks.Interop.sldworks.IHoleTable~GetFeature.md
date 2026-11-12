---
title: "GetFeature Method (IHoleTable)"
project: "SOLIDWORKS API Help"
interface: "IHoleTable"
member: "GetFeature"
kind: "method"
source: "sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IHoleTable~GetFeature.html"
---

# GetFeature Method (IHoleTable)

Gets the [IFeature](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.IFeature.html) object for this hole table.

## Syntax

### Visual Basic (Declaration)

```vb
Function GetFeature() As Feature
```

### Visual Basic (Usage)

```vb
Dim instance As IHoleTable
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

Pointer to the [IFeature](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.IFeature.html) object

## VBA Syntax

See [HoleTable::GetFeature](ms-its:sldworksapivb6.chm::/sldworks~HoleTable~GetFeature.html).

## See Also

[IHoleTable Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IHoleTable.html)
[IHoleTable Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IHoleTable_members.html)

## Availability

SOLIDWORKS 2004 FCS, Revision Number 12.0
