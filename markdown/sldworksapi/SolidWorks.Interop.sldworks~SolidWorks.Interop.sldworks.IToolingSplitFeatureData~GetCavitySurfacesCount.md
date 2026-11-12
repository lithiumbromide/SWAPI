---
title: "GetCavitySurfacesCount Method (IToolingSplitFeatureData)"
project: "SOLIDWORKS API Help"
interface: "IToolingSplitFeatureData"
member: "GetCavitySurfacesCount"
kind: "method"
source: "sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IToolingSplitFeatureData~GetCavitySurfacesCount.html"
---

# GetCavitySurfacesCount Method (IToolingSplitFeatureData)

Gets the number of cavity surface bodies in this tooling split feature.

## Syntax

### Visual Basic (Declaration)

```vb
Function GetCavitySurfacesCount() As System.Integer
```

### Visual Basic (Usage)

```vb
Dim instance As IToolingSplitFeatureData
Dim value As System.Integer

value = instance.GetCavitySurfacesCount()
```

### C#

```csharp
System.int GetCavitySurfacesCount()
```

### C++/CLI

```cpp
System.int GetCavitySurfacesCount();
```

**NOTE:** See [Differences Between Unmanaged C++ and C++/CLI Code](DifferencesBetweenUnManagedAndCPPCLI.htm).

### Return Value

Number of cavity surface bodies

## VBA Syntax

See [ToolingSplitFeatureData::GetCavitySurfacesCount](ms-its:sldworksapivb6.chm::/sldworks~ToolingSplitFeatureData~GetCavitySurfacesCount.html).

## Examples

See the [IToolingSplitFeatureData](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IToolingSplitFeatureData.html) examples.

## Remarks

Call this method before calling [IToolingSplitFeatureData::IGetCavitySurfaces](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.IToolingSplitFeatureData~IGetCavitySurfaces.html) to get the size of the array for that method.

## See Also

[IToolingSplitFeatureData Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IToolingSplitFeatureData.html)
[IToolingSplitFeatureData Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IToolingSplitFeatureData_members.html)
[IToolingSplitFeatureData::CavitySurfaces Property](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IToolingSplitFeatureData~CavitySurfaces.html)
[IToolingSplitFeatureData::ISetCavitySurfaces Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IToolingSplitFeatureData~ISetCavitySurfaces.html)

## Availability

SOLIDWORKS 2005 FCS, Revision Number 13.0
