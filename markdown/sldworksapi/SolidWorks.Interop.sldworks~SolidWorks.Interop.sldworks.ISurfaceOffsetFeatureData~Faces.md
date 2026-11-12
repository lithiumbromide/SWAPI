---
title: "Faces Property (ISurfaceOffsetFeatureData)"
project: "SOLIDWORKS API Help"
interface: "ISurfaceOffsetFeatureData"
member: "Faces"
kind: "property"
source: "sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISurfaceOffsetFeatureData~Faces.html"
---

# Faces Property (ISurfaceOffsetFeatureData)

Obsolete. Superseded by [ISurfaceOffsetFeatureData::Entities](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.ISurfaceOffsetFeatureData~Entities.html).

## Syntax

### Visual Basic (Declaration)

```vb
Property Faces As System.Object
```

### Visual Basic (Usage)

```vb
Dim instance As ISurfaceOffsetFeatureData
Dim value As System.Object

instance.Faces = value

value = instance.Faces
```

### C#

```csharp
System.object Faces {get; set;}
```

### C++/CLI

```cpp
property System.Object^ Faces {
   System.Object^ get();
   void set (    System.Object^ value);
}
```

**NOTE:** See [Differences Between Unmanaged C++ and C++/CLI Code](DifferencesBetweenUnManagedAndCPPCLI.htm).

### Property Value

Array of [faces](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.IFace2.html)

## VBA Syntax

See [SurfaceOffsetFeatureData::Faces](ms-its:sldworksapivb6.chm::/sldworks~SurfaceOffsetFeatureData~Faces.html).

## Remarks

See [Accessing Selections that Define Features](sldworksAPIProgGuide.chm::/Miscellaneous/Accessing_Selections_that_Define_Features.htm) for additional details.

## See Also

[ISurfaceOffsetFeatureData Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISurfaceOffsetFeatureData.html)
[ISurfaceOffsetFeatureData Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISurfaceOffsetFeatureData_members.html)
[ISurfaceOffsetFeatureData::GetFacesCount Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISurfaceOffsetFeatureData~GetFacesCount.html)
[ISurfaceOffsetFeatureData::IGetFaces Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISurfaceOffsetFeatureData~IGetFaces.html)
[ISurfaceOffsetFeatureData::ISetFaces Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISurfaceOffsetFeatureData~ISetFaces.html)

## Availability

SOLIDWORKS 2001Plus SP1, Revision Number 10.1
