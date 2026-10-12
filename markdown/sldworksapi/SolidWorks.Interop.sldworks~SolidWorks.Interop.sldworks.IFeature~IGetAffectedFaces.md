---
title: "IGetAffectedFaces Method (IFeature)"
project: "SOLIDWORKS API Help"
interface: "IFeature"
member: "IGetAffectedFaces"
kind: "method"
source: "sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IFeature~IGetAffectedFaces.html"
---

# IGetAffectedFaces Method (IFeature)

Gets the faces modified by a feature, such as a draft feature.

## Syntax

### Visual Basic (Declaration)

```vb
Function IGetAffectedFaces( _
   ByRef NCount As System.Integer _
) As Face2
```

### Visual Basic (Usage)

```vb
Dim instance As IFeature
Dim NCount As System.Integer
Dim value As Face2

value = instance.IGetAffectedFaces(NCount)
```

### C#

```csharp
Face2 IGetAffectedFaces(
   ref System.int NCount
)
```

### C++/CLI

```cpp
Face2^ IGetAffectedFaces(
   System.int% NCount
)
```

**NOTE:** See [Differences Between Unmanaged C++ and C++/CLI Code](DifferencesBetweenUnManagedAndCPPCLI.htm).

### Parameters

- `NCount`: Number of faces modified by a feature

### Return Value

- in-process, unmanaged C++: Pointer to array of [faces](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.IFace2.html)

VBA, VB.NET, C#, and C++/CLI: Not supported

See [In-process Methods](sldworksapiprogguide.chm::/OVERVIEW/In-process_Methods.htm) for details about this type of method.

## Remarks

To determine size the of the array, call [IFeature::GetAffectedFaceCount](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.IFeature~GetAffectedFaceCount.html) before calling this method.

## See Also

[IFeature Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IFeature.html)
[IFeature Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IFeature_members.html)
[IFeature::GetAffectedFaceCount Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IFeature~GetAffectedFaceCount.html)
[IFeature::GetAffectedFaces Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IFeature~GetAffectedFaces.html)

## Availability

SOLIDWORKS 2005 FCS, Revision Number 13.0
