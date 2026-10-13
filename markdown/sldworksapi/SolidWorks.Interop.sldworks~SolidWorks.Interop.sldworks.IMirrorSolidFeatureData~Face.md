---
title: "Face Property (IMirrorSolidFeatureData)"
project: "SOLIDWORKS API Help"
interface: "IMirrorSolidFeatureData"
member: "Face"
kind: "property"
source: "sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IMirrorSolidFeatureData~Face.html"
---

# Face Property (IMirrorSolidFeatureData)

Gets or sets the end-condition face for this mirror solid feature.

## Syntax

### Visual Basic (Declaration)

```vb
Property Face As System.Object
```

### Visual Basic (Usage)

```vb
Dim instance As IMirrorSolidFeatureData
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

[Face](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.IFace2.html) that determines the end condition

## VBA Syntax

See [MirrorSolidFeatureData::Face](ms-its:sldworksapivb6.chm::/sldworks~MirrorSolidFeatureData~Face.html).

## Remarks

See [Accessing Selections that Define Features](sldworksAPIProgGuide.chm::/Miscellaneous/Accessing_Selections_that_Define_Features.htm) for additional details on using this property.

## See Also

[IMirrorSolidFeatureData Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IMirrorSolidFeatureData.html)
[IMirrorSolidFeatureData Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IMirrorSolidFeatureData_members.html)

## Availability

SOLIDWORKS 2001 FCS, Revision Number 9.0
