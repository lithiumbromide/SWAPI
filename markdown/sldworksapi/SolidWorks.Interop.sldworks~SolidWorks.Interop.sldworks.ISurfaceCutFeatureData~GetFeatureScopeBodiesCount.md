---
title: "GetFeatureScopeBodiesCount Method (ISurfaceCutFeatureData)"
project: "SOLIDWORKS API Help"
interface: "ISurfaceCutFeatureData"
member: "GetFeatureScopeBodiesCount"
kind: "method"
source: "sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISurfaceCutFeatureData~GetFeatureScopeBodiesCount.html"
---

# GetFeatureScopeBodiesCount Method (ISurfaceCutFeatureData)

Gets the number of bodies affected by this surface-cut feature.

## Syntax

### Visual Basic (Declaration)

```vb
Function GetFeatureScopeBodiesCount() As System.Integer
```

### Visual Basic (Usage)

```vb
Dim instance As ISurfaceCutFeatureData
Dim value As System.Integer

value = instance.GetFeatureScopeBodiesCount()
```

### C#

```csharp
System.int GetFeatureScopeBodiesCount()
```

### C++/CLI

```cpp
System.int GetFeatureScopeBodiesCount();
```

**NOTE:** See [Differences Between Unmanaged C++ and C++/CLI Code](DifferencesBetweenUnManagedAndCPPCLI.htm).

### Return Value

Number of bodies affected by this surface-cut feature

## VBA Syntax

See [SurfCutFeatureData::GetFeatureScopeBodiesCount](ms-its:sldworksapivb6.chm::/sldworks~SurfCutFeatureData~GetFeatureScopeBodiesCount.html).

## Examples

[Insert Surface-cut Feature (C#)](Insert_Surface-cut_Feature_Example_CSharp.htm)
[Insert Surface-cut Feature (VB.NET)](Insert_Surface-cut_Feature_Example_VBNET.htm)
[Insert Surface-cut Feature (VBA)](Insert_Surface-cut_Feature_Example_VB.htm)

## Remarks

To access this interface, you must declare it as SurfCutFeatureData or ISurfCutFeatureData.

Call this method before calling [ISurfaceCutFeatureData::IGetFeatureScopeBodies](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.ISurfaceCutFeatureData~IGetFeatureScopeBodies.html) to determine the size of the array for that method.

If [ISurfaceCutFeatureData::FeatureScope](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.ISurfaceCutFeatureData~FeatureScope.html) is false, then this method's return value is 0.

## See Also

[ISurfaceCutFeatureData Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISurfaceCutFeatureData.html)
[ISurfaceCutFeatureData Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISurfaceCutFeatureData_members.html)
[ISurfaceCutFeatureData::ISetFeatureScopeBodies Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISurfaceCutFeatureData~ISetFeatureScopeBodies.html)
[ISurfaceCutFeatureData::FeatureScopeBodies Property](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISurfaceCutFeatureData~FeatureScopeBodies.html)
[ISurfaceCutFeatureData::AutoSelect Property](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISurfaceCutFeatureData~AutoSelect.html)

## Availability

SOLIDWORKS 2013 SP1, Revision Number 21.1
