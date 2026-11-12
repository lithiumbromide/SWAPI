---
title: "Plane Property (IMirrorPatternFeatureData)"
project: "SOLIDWORKS API Help"
interface: "IMirrorPatternFeatureData"
member: "Plane"
kind: "property"
source: "sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IMirrorPatternFeatureData~Plane.html"
---

# Plane Property (IMirrorPatternFeatureData)

Gets or sets the plane about which to mirror the part.

## Syntax

### Visual Basic (Declaration)

```vb
Property Plane As System.Object
```

### Visual Basic (Usage)

```vb
Dim instance As IMirrorPatternFeatureData
Dim value As System.Object

instance.Plane = value

value = instance.Plane
```

### C#

```csharp
System.object Plane {get; set;}
```

### C++/CLI

```cpp
property System.Object^ Plane {
   System.Object^ get();
   void set (    System.Object^ value);
}
```

**NOTE:** See [Differences Between Unmanaged C++ and C++/CLI Code](DifferencesBetweenUnManagedAndCPPCLI.htm).

### Property Value

Plane about which to mirror the part

## VBA Syntax

See [MirrorPatternFeatureData::Plane](ms-its:sldworksapivb6.chm::/sldworks~MirrorPatternFeatureData~Plane.html).

## Examples

[Get Mirror Pattern Feature Data (C#)](Get_Mirror_Pattern_Feature_Data_Example_CSharp.htm)
[Get Mirror Pattern Feature Data (VB.NET)](Get_Mirror_Pattern_Feature_Data_Example_VBNET.htm)
[Get Mirror Pattern Feature Data (VBA)](Get_Mirror_Feature_Data_Example_VB.htm)

## Remarks

See [Accessing Selections that Define Features](sldworksAPIProgGuide.chm::/Miscellaneous/Accessing_Selections_that_Define_Features.htm) for additional details on using this property.

## See Also

[IMirrorPatternFeatureData Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IMirrorPatternFeatureData.html)
[IMirrorPatternFeatureData Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IMirrorPatternFeatureData_members.html)
[IMirrorPatternFeatureData::GetMirrorPlaneType Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IMirrorPatternFeatureData~GetMirrorPlaneType.html)

## Availability

SOLIDWORKS 2000 SP2, Revision Number 8.2
