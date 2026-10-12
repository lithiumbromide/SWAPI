---
title: "AccuracyFactor Property (ISurfaceFlattenFeatureData)"
project: "SOLIDWORKS API Help"
interface: "ISurfaceFlattenFeatureData"
member: "AccuracyFactor"
kind: "property"
source: "sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISurfaceFlattenFeatureData~AccuracyFactor.html"
---

# AccuracyFactor Property (ISurfaceFlattenFeatureData)

Gets or sets the accuracy of the flattened triangle mesh.

## Syntax

### Visual Basic (Declaration)

```vb
Property AccuracyFactor As System.Integer
```

### Visual Basic (Usage)

```vb
Dim instance As ISurfaceFlattenFeatureData
Dim value As System.Integer

instance.AccuracyFactor = value

value = instance.AccuracyFactor
```

### C#

```csharp
System.int AccuracyFactor {get; set;}
```

### C++/CLI

```cpp
property System.int AccuracyFactor {
   System.int get();
   void set (    System.int value);
}
```

**NOTE:** See [Differences Between Unmanaged C++ and C++/CLI Code](DifferencesBetweenUnManagedAndCPPCLI.htm).

### Property Value

10 >= Accuracy of flattened triangle mesh >= 1; 1 is highest accuracy

## VBA Syntax

See [SurfaceFlattenFeatureData::AccuracyFactor](ms-its:sldworksapivb6.chm::/sldworks~SurfaceFlattenFeatureData~AccuracyFactor.html).

## Examples

[Get Data for Surface-flatten Feature (C#)](Get_Data_for_Surface_Flatten_Feature_Example_CSharp.htm)
[Get Data for Surface-flatten Feature (VB.NET)](Get_Data_for_Surface_Flatten_Feature_Example_VBNET.htm)
[Get Data for Surface-flatten Feature (VBA)](Get_Data_for_Surface_Flatten_Feature_Example_VB.htm)

## See Also

[ISurfaceFlattenFeatureData Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISurfaceFlattenFeatureData.html)
[ISurfaceFlattenFeatureData Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISurfaceFlattenFeatureData_members.html)

## Availability

SOLIDWORKS 2015 FCS, Revision Number 23.0
