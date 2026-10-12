---
title: "GetIntersectionsToolsCount Method (IIntersectFeatureData)"
project: "SOLIDWORKS API Help"
interface: "IIntersectFeatureData"
member: "GetIntersectionsToolsCount"
kind: "method"
source: "sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IIntersectFeatureData~GetIntersectionsToolsCount.html"
---

# GetIntersectionsToolsCount Method (IIntersectFeatureData)

Gets the number of solids, surfaces, and planes used to create this intersect feature.

## Syntax

### Visual Basic (Declaration)

```vb
Function GetIntersectionsToolsCount() As System.Integer
```

### Visual Basic (Usage)

```vb
Dim instance As IIntersectFeatureData
Dim value As System.Integer

value = instance.GetIntersectionsToolsCount()
```

### C#

```csharp
System.int GetIntersectionsToolsCount()
```

### C++/CLI

```cpp
System.int GetIntersectionsToolsCount();
```

**NOTE:** See [Differences Between Unmanaged C++ and C++/CLI Code](DifferencesBetweenUnManagedAndCPPCLI.htm).

### Return Value

Number of solids, surfaces, and planes used to create this intersect feature

## VBA Syntax

See [IntersectFeatureData::GetIntersectionsToolsCount](ms-its:sldworksapivb6.chm::/sldworks~IntersectFeatureData~GetIntersectionsToolsCount.html).

## Examples

See the [IIntersectFeatureData](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.IIntersectFeatureData.html) examples.

## See Also

[IIntersectFeatureData Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IIntersectFeatureData.html)
[IIntersectFeatureData Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IIntersectFeatureData_members.html)
[IIntersectFeatureData::GetIntersectionsTools Method ()](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IIntersectFeatureData~GetIntersectionsTools.html)

## Availability

SOLIDWORKS 2015 FCS, Revision Number 23.0
