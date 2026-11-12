---
title: "GetAffectedFaceCount Method (IFeature)"
project: "SOLIDWORKS API Help"
interface: "IFeature"
member: "GetAffectedFaceCount"
kind: "method"
source: "sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IFeature~GetAffectedFaceCount.html"
---

# GetAffectedFaceCount Method (IFeature)

Gets the number of faces modified by a feature, such as a draft feature.

## Syntax

### Visual Basic (Declaration)

```vb
Function GetAffectedFaceCount() As System.Integer
```

### Visual Basic (Usage)

```vb
Dim instance As IFeature
Dim value As System.Integer

value = instance.GetAffectedFaceCount()
```

### C#

```csharp
System.int GetAffectedFaceCount()
```

### C++/CLI

```cpp
System.int GetAffectedFaceCount();
```

**NOTE:** See [Differences Between Unmanaged C++ and C++/CLI Code](DifferencesBetweenUnManagedAndCPPCLI.htm).

### Return Value

Number of faces modified by a feature

## VBA Syntax

See [Feature::GetAffectedFaceCount](ms-its:sldworksapivb6.chm::/sldworks~Feature~GetAffectedFaceCount.html).

## Examples

[Get Faces Affected By Feature (VBA)](Get_Faces_Affected_by_Feature_Example_VB.htm)

## Remarks

Call this method before calling [IFeature::IGetAffectedFaces](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.IFeature~IGetAffectedFaces.html).

## See Also

[IFeature Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IFeature.html)
[IFeature Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IFeature_members.html)
[IFace2::GetAffectedFaces Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IFeature~GetAffectedFaces.html)

## Availability

SOLIDWORKS 2005 FCS, Revision Number 13.0
