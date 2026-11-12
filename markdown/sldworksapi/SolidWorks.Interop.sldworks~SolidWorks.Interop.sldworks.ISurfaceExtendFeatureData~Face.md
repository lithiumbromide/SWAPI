---
title: "Face Property (ISurfaceExtendFeatureData)"
project: "SOLIDWORKS API Help"
interface: "ISurfaceExtendFeatureData"
member: "Face"
kind: "property"
source: "sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISurfaceExtendFeatureData~Face.html"
---

# Face Property (ISurfaceExtendFeatureData)

Gets or sets the end-condition face for this surface-extend feature.

## Syntax

### Visual Basic (Declaration)

```vb
Property Face As System.Object
```

### Visual Basic (Usage)

```vb
Dim instance As ISurfaceExtendFeatureData
Dim value As System.Object

instance.Face = value

value = instance.Face
```

### C#

```csharp
System.object Face {get; set;}
```

### C++/CLI

```cpp
property System.Object^ Face {
   System.Object^ get();
   void set (    System.Object^ value);
}
```

**NOTE:** See [Differences Between Unmanaged C++ and C++/CLI Code](DifferencesBetweenUnManagedAndCPPCLI.htm).

### Property Value

End-condition [face](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.IFace2.html)

## VBA Syntax

See [SurfaceExtendFeatureData::Face](ms-its:sldworksapivb6.chm::/sldworks~SurfaceExtendFeatureData~Face.html).

## Remarks

See [Accessing Selections that Define Features](sldworksAPIProgGuide.chm::/Miscellaneous/Accessing_Selections_that_Define_Features.htm) for additional details.

## See Also

[ISurfaceExtendFeatureData Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISurfaceExtendFeatureData.html)
[ISurfaceExtendFeatureData Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISurfaceExtendFeatureData_members.html)
[ISurfaceExtendFeatureData::IFace Property](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISurfaceExtendFeatureData~IFace.html)

## Availability

SOLIDWORKS 2001Plus SP1, Revision Number 10.1
