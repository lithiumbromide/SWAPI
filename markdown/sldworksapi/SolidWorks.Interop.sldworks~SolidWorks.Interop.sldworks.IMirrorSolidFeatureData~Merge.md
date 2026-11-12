---
title: "Merge Property (IMirrorSolidFeatureData)"
project: "SOLIDWORKS API Help"
interface: "IMirrorSolidFeatureData"
member: "Merge"
kind: "property"
source: "sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IMirrorSolidFeatureData~Merge.html"
---

# Merge Property (IMirrorSolidFeatureData)

Gets or sets the merge results option for the mirrored solid feature in a multibody part.

## Syntax

### Visual Basic (Declaration)

```vb
Property Merge As System.Boolean
```

### Visual Basic (Usage)

```vb
Dim instance As IMirrorSolidFeatureData
Dim value As System.Boolean

instance.Merge = value

value = instance.Merge
```

### C#

```csharp
System.bool Merge {get; set;}
```

### C++/CLI

```cpp
property System.bool Merge {
   System.bool get();
   void set (    System.bool value);
}
```

**NOTE:** See [Differences Between Unmanaged C++ and C++/CLI Code](DifferencesBetweenUnManagedAndCPPCLI.htm).

### Property Value

True enables the merge results option, false does not

## VBA Syntax

See [MirrorSolidFeatureData::Merge](ms-its:sldworksapivb6.chm::/sldworks~MirrorSolidFeatureData~Merge.html).

## Examples

[Get Mirror Solid Feature Data (C#)](Get_Mirror_Solid_Feature_Data_Example_CSharp.htm)
[Get Mirror Solid Feature Data (VB.NET)](Get_Mirror_Solid_Feature_Data_Example_VBNET.htm)
[Get Mirror Solid Feature Data (VBA)](Get_Mirror_Solid_Data_Example_VB.htm)

## Remarks

The merge results option tells the SOLIDWORKS Design software whether to merge the new body or bodies with existing bodies in the multibody part. This property is set to True by default.

## See Also

[IMirrorSolidFeatureData Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IMirrorSolidFeatureData.html)
[IMirrorSolidFeatureData Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IMirrorSolidFeatureData_members.html)

## Availability

SOLIDWORKS 2003 FCS, Revision Number 11.0
