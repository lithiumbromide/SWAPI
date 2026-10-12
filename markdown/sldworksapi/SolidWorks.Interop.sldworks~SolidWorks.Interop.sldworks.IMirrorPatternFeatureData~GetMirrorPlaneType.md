---
title: "GetMirrorPlaneType Method (IMirrorPatternFeatureData)"
project: "SOLIDWORKS API Help"
interface: "IMirrorPatternFeatureData"
member: "GetMirrorPlaneType"
kind: "method"
source: "sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IMirrorPatternFeatureData~GetMirrorPlaneType.html"
---

# GetMirrorPlaneType Method (IMirrorPatternFeatureData)

Gets whether the mirror plane is a face or a reference plane.

## Syntax

### Visual Basic (Declaration)

```vb
Function GetMirrorPlaneType() As System.Integer
```

### Visual Basic (Usage)

```vb
Dim instance As IMirrorPatternFeatureData
Dim value As System.Integer

value = instance.GetMirrorPlaneType()
```

### C#

```csharp
System.int GetMirrorPlaneType()
```

### C++/CLI

```cpp
System.int GetMirrorPlaneType();
```

**NOTE:** See [Differences Between Unmanaged C++ and C++/CLI Code](DifferencesBetweenUnManagedAndCPPCLI.htm).

### Return Value

Type of object specified as the mirror plane:

- 0 = face
- 1 = plane

## VBA Syntax

See [MirrorPatternFeatureData::GetMirrorPlaneType](ms-its:sldworksapivb6.chm::/sldworks~MirrorPatternFeatureData~GetMirrorPlaneType.html).

## Examples

[Get Mirror Pattern Feature Data (C#)](Get_Mirror_Pattern_Feature_Data_Example_CSharp.htm)
[Get Mirror Pattern Feature Data (VB.NET)](Get_Mirror_Pattern_Feature_Data_Example_VBNET.htm)
[Get Mirror Pattern Feature Data (VBA)](Get_Mirror_Feature_Data_Example_VB.htm)

## See Also

[IMirrorPatternFeatureData Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IMirrorPatternFeatureData.html)
[IMirrorPatternFeatureData Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IMirrorPatternFeatureData_members.html)
[IMirrorPatternFeatureData::Plane Property](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IMirrorPatternFeatureData~Plane.html)

## Availability

SOLIDWORKS 2000 SP2, Revision Number 8.2
