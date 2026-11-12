---
title: "GetFaces Method (ISimpleFilletFeatureData2)"
project: "SOLIDWORKS API Help"
interface: "ISimpleFilletFeatureData2"
member: "GetFaces"
kind: "method"
source: "sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISimpleFilletFeatureData2~GetFaces.html"
---

# GetFaces Method (ISimpleFilletFeatureData2)

Gets the faces on which to create a simple fillet.

## Syntax

### Visual Basic (Declaration)

```vb
Function GetFaces( _
   ByVal WhichFaceList As System.Integer _
) As System.Object
```

### Visual Basic (Usage)

```vb
Dim instance As ISimpleFilletFeatureData2
Dim WhichFaceList As System.Integer
Dim value As System.Object

value = instance.GetFaces(WhichFaceList)
```

### C#

```csharp
System.object GetFaces(
   System.int WhichFaceList
)
```

### C++/CLI

```cpp
System.Object^ GetFaces(
   System.int WhichFaceList
)
```

**NOTE:** See [Differences Between Unmanaged C++ and C++/CLI Code](DifferencesBetweenUnManagedAndCPPCLI.htm).

### Parameters

- `WhichFaceList`: Face as defined in [swSimpleFilletWhichFaces_e](ms-its:swconst.chm::/SOLIDWORKS.Interop.swconst~SOLIDWORKS.Interop.swconst.swSimpleFilletWhichFaces_e.html)

### Return Value

Array of [faces](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.IFace2.html)

## VBA Syntax

See [SimpleFilletFeatureData2::GetFaces](ms-its:sldworksapivb6.chm::/sldworks~SimpleFilletFeatureData2~GetFaces.html).

## Remarks

See [Accessing Selections that Define Features](sldworksAPIProgGuide.chm::/Miscellaneous/Accessing_Selections_that_Define_Features.htm) for additional details.

## See Also

[ISimpleFilletFeatureData2 Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISimpleFilletFeatureData2.html)
[ISimpleFilletFeatureData2 Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISimpleFilletFeatureData2_members.html)
[ISimpleFilletFeatureData2::GetFaceCount Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISimpleFilletFeatureData2~GetFaceCount.html)
[ISimpleFilletFeatureData2::IGetFaces Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISimpleFilletFeatureData2~IGetFaces.html)
[ISimpleFilletFeatureData2::ISetFaces Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISimpleFilletFeatureData2~ISetFaces.html)
[ISimpleFilletFeatureData2::SetFaces Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISimpleFilletFeatureData2~SetFaces.html)

## Availability

SOLIDWORKS 2003 FCS, Revision Number 11.0
