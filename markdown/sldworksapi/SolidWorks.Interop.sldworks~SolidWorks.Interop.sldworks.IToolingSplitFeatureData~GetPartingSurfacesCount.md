---
title: "GetPartingSurfacesCount Method (IToolingSplitFeatureData)"
project: "SOLIDWORKS API Help"
interface: "IToolingSplitFeatureData"
member: "GetPartingSurfacesCount"
kind: "method"
source: "sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IToolingSplitFeatureData~GetPartingSurfacesCount.html"
---

# GetPartingSurfacesCount Method (IToolingSplitFeatureData)

Gets the number of parting surface bodies in this tooling split feature.

## Syntax

### Visual Basic (Declaration)

```vb
Function GetPartingSurfacesCount() As System.Integer
```

### Visual Basic (Usage)

```vb
Dim instance As IToolingSplitFeatureData
Dim value As System.Integer

value = instance.GetPartingSurfacesCount()
```

### C#

```csharp
System.int GetPartingSurfacesCount()
```

### C++/CLI

```cpp
System.int GetPartingSurfacesCount();
```

**NOTE:** See [Differences Between Unmanaged C++ and C++/CLI Code](DifferencesBetweenUnManagedAndCPPCLI.htm).

### Return Value

Number of parting surface bodies

## VBA Syntax

See [ToolingSplitFeatureData::GetPartingSurfacesCount](ms-its:sldworksapivb6.chm::/sldworks~ToolingSplitFeatureData~GetPartingSurfacesCount.html).

## Examples

See the [IToolingSplitFeatureData](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IToolingSplitFeatureData.html) examples.

## Remarks

Call this method before calling [IToolingSplitFeatureData::IGetPartingSurfaces](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.IToolingSplitFeatureData~IGetPartingSurfaces.html) to get the size of the array for that method.

## See Also

[IToolingSplitFeatureData Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IToolingSplitFeatureData.html)
[IToolingSplitFeatureData Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IToolingSplitFeatureData_members.html)
[IToolingSplitFeatureData::ISetPartingSurfaces Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IToolingSplitFeatureData~ISetPartingSurfaces.html)
[IToolingSplitFeatureData::PartingSurfaces Property](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IToolingSplitFeatureData~PartingSurfaces.html)

## Availability

SOLIDWORKS 2005 FCS, Revision Number 13.0
