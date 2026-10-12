---
title: "GetCoreSurfacesCount Method (IToolingSplitFeatureData)"
project: "SOLIDWORKS API Help"
interface: "IToolingSplitFeatureData"
member: "GetCoreSurfacesCount"
kind: "method"
source: "sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IToolingSplitFeatureData~GetCoreSurfacesCount.html"
---

# GetCoreSurfacesCount Method (IToolingSplitFeatureData)

Gets the number of core surface bodies in this tooling split feature.

## Syntax

### Visual Basic (Declaration)

```vb
Function GetCoreSurfacesCount() As System.Integer
```

### Visual Basic (Usage)

```vb
Dim instance As IToolingSplitFeatureData
Dim value As System.Integer

value = instance.GetCoreSurfacesCount()
```

### C#

```csharp
System.int GetCoreSurfacesCount()
```

### C++/CLI

```cpp
System.int GetCoreSurfacesCount();
```

**NOTE:** See [Differences Between Unmanaged C++ and C++/CLI Code](DifferencesBetweenUnManagedAndCPPCLI.htm).

### Return Value

Number of core surface bodies

## VBA Syntax

See [ToolingSplitFeatureData::GetCoreSurfacesCount](ms-its:sldworksapivb6.chm::/sldworks~ToolingSplitFeatureData~GetCoreSurfacesCount.html).

## Examples

See the [IToolingSplitFeatureData](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IToolingSplitFeatureData.html) examples.

## Remarks

Call this method before calling [IToolingSplitFeatureData::IGetCoreSurfaces](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.IToolingSplitFeatureData~IGetCoreSurfaces.html) to get the size of the array for that method.

## See Also

[IToolingSplitFeatureData Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IToolingSplitFeatureData.html)
[IToolingSplitFeatureData Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IToolingSplitFeatureData_members.html)
[IToolingSplitFeatureData::ISetCoreSurfaces Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IToolingSplitFeatureData~ISetCoreSurfaces.html)
[IToolingSplitFeatureData::CoreSurfaces Property](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IToolingSplitFeatureData~CoreSurfaces.html)

## Availability

SOLIDWORKS 2005 FCS, Revision Number 13.0
