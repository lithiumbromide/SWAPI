---
title: "IGetFeatureScopeBodies Method (ISurfaceCutFeatureData)"
project: "SOLIDWORKS API Help"
interface: "ISurfaceCutFeatureData"
member: "IGetFeatureScopeBodies"
kind: "method"
source: "sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISurfaceCutFeatureData~IGetFeatureScopeBodies.html"
---

# IGetFeatureScopeBodies Method (ISurfaceCutFeatureData)

Gets the solid bodies that the surface-cut feature affects in a multibody part.

## Syntax

### Visual Basic (Declaration)

```vb
Function IGetFeatureScopeBodies( _
   ByVal Count As System.Integer _
) As Body2
```

### Visual Basic (Usage)

```vb
Dim instance As ISurfaceCutFeatureData
Dim Count As System.Integer
Dim value As Body2

value = instance.IGetFeatureScopeBodies(Count)
```

### C#

```csharp
Body2 IGetFeatureScopeBodies(
   System.int Count
)
```

### C++/CLI

```cpp
Body2^ IGetFeatureScopeBodies(
   System.int Count
)
```

**NOTE:** See [Differences Between Unmanaged C++ and C++/CLI Code](DifferencesBetweenUnManagedAndCPPCLI.htm).

### Parameters

- `Count`: Number of solid bodies to affect

### Return Value

- in-process, unmanaged C++: Pointer to an array of solid [bodies](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.IBody2.html) of size Count
- VBA, VB.NET, C#, and C++/CLI: Not supported

See [In-process Methods](sldworksapiprogguide.chm::/OVERVIEW/In-process_Methods.htm) for details about this type of method.

## VBA Syntax

See [SurfCutFeatureData::IGetFeatureScopeBodies](ms-its:sldworksapivb6.chm::/sldworks~SurfCutFeatureData~IGetFeatureScopeBodies.html).

## Remarks

To access this interface, you must declare it as SurfCutFeatureData or ISurfCutFeatureData.

Before calling this method, call [ISurfaceCutFeatureData::GetFeatureScopeBodiesCount](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.ISurfaceCutFeatureData~IGetFeatureScopeBodies.html) to get Count.

## See Also

[ISurfaceCutFeatureData Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISurfaceCutFeatureData.html)
[ISurfaceCutFeatureData Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISurfaceCutFeatureData_members.html)
[ISurfaceCutFeatureData::ISetFeatureScopeBodies Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISurfaceCutFeatureData~ISetFeatureScopeBodies.html)
[ISurfaceCutFeatureData::AutoSelect](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISurfaceCutFeatureData~AutoSelect.html)
[ISurfaceCutFeatureData::FeatureScope Property](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISurfaceCutFeatureData~FeatureScope.html)
[ISurfaceCutFeatureData::FeatureScopeBodies Property](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISurfaceCutFeatureData~FeatureScopeBodies.html)

## Availability

SOLIDWORKS 2013 SP1, Revision Number 21.1
