---
title: "GetFixedFace Method (IBendsFeatureData)"
project: "SOLIDWORKS API Help"
interface: "IBendsFeatureData"
member: "GetFixedFace"
kind: "method"
source: "sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IBendsFeatureData~GetFixedFace.html"
---

# GetFixedFace Method (IBendsFeatureData)

Gets the fixed face of a flatten-bends feature.

## Syntax

### Visual Basic (Declaration)

```vb
Function GetFixedFace() As System.Object
```

### Visual Basic (Usage)

```vb
Dim instance As IBendsFeatureData
Dim value As System.Object

value = instance.GetFixedFace()
```

### C#

```csharp
System.object GetFixedFace()
```

### C++/CLI

```cpp
System.Object^ GetFixedFace();
```

**NOTE:** See [Differences Between Unmanaged C++ and C++/CLI Code](DifferencesBetweenUnManagedAndCPPCLI.htm).

### Return Value

[IFace2](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.IFace2.html)

## VBA Syntax

See [BendsFeatureData::GetFixedFace](ms-its:sldworksapivb6.chm::/sldworks~BendsFeatureData~GetFixedFace.html).

## Examples

[Get Fixed Face of Flatten-Bends Feature (VBA)](Get_Fixed_Face_of_Flatten-Bends_Feature_Example_VB.htm)
[Get Fixed Face of Flatten-Bends Feature (VB.NET)](Get_Fixed_Face_of_Flatten-Bends_Feature_Example_VBNET.htm)
[Get Fixed Face of Flatten-Bends Feature (C#)](Get_Fixed_Face_of_Flatten-Bends_Feature_Example_CSharp.htm)

## Remarks

See [Accessing Selections that Define Features](sldworksAPIProgGuide.chm::/Miscellaneous/Accessing_Selections_that_Define_Features.htm) for additional details on using this method.

## See Also

[IBendsFeatureData Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IBendsFeatureData.html)
[IBendsFeatureData Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IBendsFeatureData_members.html)

## Availability

SOLIDWORKS 2012 FCS, Revision Number 20.0
