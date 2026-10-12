---
title: "DepthReference Property (IBrokenOutSectionFeatureData)"
project: "SOLIDWORKS API Help"
interface: "IBrokenOutSectionFeatureData"
member: "DepthReference"
kind: "property"
source: "sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IBrokenOutSectionFeatureData~DepthReference.html"
---

# DepthReference Property (IBrokenOutSectionFeatureData)

Gets or sets the geometry reference that defines the depth of exposure of inner details of the model in the broken-out section feature.

## Syntax

### Visual Basic (Declaration)

```vb
Property DepthReference As Entity
```

### Visual Basic (Usage)

```vb
Dim instance As IBrokenOutSectionFeatureData
Dim value As Entity

instance.DepthReference = value

value = instance.DepthReference
```

### C#

```csharp
Entity DepthReference {get; set;}
```

### C++/CLI

```cpp
property Entity^ DepthReference {
   Entity^ get();
   void set (    Entity^ value);
}
```

**NOTE:** See [Differences Between Unmanaged C++ and C++/CLI Code](DifferencesBetweenUnManagedAndCPPCLI.htm).

### Property Value

[IEntity](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.IEntity.html) (see **Remarks**)

## VBA Syntax

See [BrokenOutSectionFeatureData::DepthReference](ms-its:sldworksapivb6.chm::/sldworks~BrokenOutSectionFeatureData~DepthReference.html).

## Examples

[Get Broken-Out Section Feature Data (VBA)](Get_Broken_Out_Section_Feature_Data_Example_VB.htm)
[Get Broken-Out Section Feature Data (VB.NET)](Get_Broken_Out_Section_Feature_Data_Example_VBNET.htm)
[Get Broken-Out Section Feature Data (C#)](Get_Broken_Out_Section_Feature_Data_Example_CSharp.htm)

## Remarks

Before setting this property, you must set [IBrokenOutSectionFeatureData::EditSketch](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.IBrokenOutSectionFeatureData~EditSketch.html) to false.

To set the depth reference you can either:

- Set this property to an [IEntity](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.IEntity.html) object.

-or-

- Set this property to null and select the depth geometry in the drawing view.

## See Also

[IBrokenOutSectionFeatureData Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IBrokenOutSectionFeatureData.html)
[IBrokenOutSectionFeatureData Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IBrokenOutSectionFeatureData_members.html)
[IBrokenOutSectionFeatureData::Depth Property](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IBrokenOutSectionFeatureData~Depth.html)

## Availability

SOLIDWORKS 2012 FCS, Revision Number 20.0
