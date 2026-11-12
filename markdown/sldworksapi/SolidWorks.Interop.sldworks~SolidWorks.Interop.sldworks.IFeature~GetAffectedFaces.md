---
title: "GetAffectedFaces Method (IFeature)"
project: "SOLIDWORKS API Help"
interface: "IFeature"
member: "GetAffectedFaces"
kind: "method"
source: "sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IFeature~GetAffectedFaces.html"
---

# GetAffectedFaces Method (IFeature)

Gets the faces modified by a feature, such as a draft feature.

## Syntax

### Visual Basic (Declaration)

```vb
Function GetAffectedFaces() As System.Object
```

### Visual Basic (Usage)

```vb
Dim instance As IFeature
Dim value As System.Object

value = instance.GetAffectedFaces()
```

### C#

```csharp
System.object GetAffectedFaces()
```

### C++/CLI

```cpp
System.Object^ GetAffectedFaces();
```

**NOTE:** See [Differences Between Unmanaged C++ and C++/CLI Code](DifferencesBetweenUnManagedAndCPPCLI.htm).

### Return Value

Array of the [faces](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.IFace2.html) modified by a feature

## VBA Syntax

See [Feature::GetAffectedFaces](ms-its:sldworksapivb6.chm::/sldworks~Feature~GetAffectedFaces.html).

## Examples

[Get Faces Affected By Feature (VBA)](Get_Faces_Affected_by_Feature_Example_VB.htm)

## See Also

[IFeature Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IFeature.html)
[IFeature Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IFeature_members.html)
[IFeature::GetAffectedFaceCount Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IFeature~GetAffectedFaceCount.html)
[IFeature::IGetAffectedFaces Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IFeature~IGetAffectedFaces.html)

## Availability

SOLIDWORKS 2005 FCS, Revision Number 13.0
