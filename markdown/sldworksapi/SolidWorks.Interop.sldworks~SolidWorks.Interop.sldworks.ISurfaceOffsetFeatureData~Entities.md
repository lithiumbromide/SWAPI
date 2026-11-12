---
title: "Entities Property (ISurfaceOffsetFeatureData)"
project: "SOLIDWORKS API Help"
interface: "ISurfaceOffsetFeatureData"
member: "Entities"
kind: "property"
source: "sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISurfaceOffsetFeatureData~Entities.html"
---

# Entities Property (ISurfaceOffsetFeatureData)

Gets or sets the offset surfaces and faces of this surface offset feature.

## Syntax

### Visual Basic (Declaration)

```vb
Property Entities As System.Object
```

### Visual Basic (Usage)

```vb
Dim instance As ISurfaceOffsetFeatureData
Dim value As System.Object

instance.Entities = value

value = instance.Entities
```

### C#

```csharp
System.object Entities {get; set;}
```

### C++/CLI

```cpp
property System.Object^ Entities {
   System.Object^ get();
   void set (    System.Object^ value);
}
```

**NOTE:** See [Differences Between Unmanaged C++ and C++/CLI Code](DifferencesBetweenUnManagedAndCPPCLI.htm).

### Property Value

Array of offset surface or face feature [entities](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.IEntity.html)

## VBA Syntax

See [SurfaceOffsetFeatureData::Entities](ms-its:sldworksapivb6.chm::/sldworks~SurfaceOffsetFeatureData~Entities.html).

## Examples

[Get Offset Surface Data (VBA)](Get_Offset_Surface_Data_Example_VB.htm)
[Get Offset Surface Data (VB.NET)](Get_Offset_Surface_Data_Example_VBNET.htm)
[Get Offset Surface Data (C#)](Get_Offset_Surface_Data_Example_CSharp.htm)

## Remarks

See [Accessing Selections that Define Features](sldworksAPIProgGuide.chm::/Miscellaneous/Accessing_Selections_that_Define_Features.htm) for additional details.

## See Also

[ISurfaceOffsetFeatureData Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISurfaceOffsetFeatureData.html)
[ISurfaceOffsetFeatureData Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISurfaceOffsetFeatureData_members.html)
[ISurfaceOffsetFeatureData::GetEntitiesCount Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISurfaceOffsetFeatureData~GetEntitiesCount.html)
[ISurfaceOffsetFeatureData::IGetEntities Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISurfaceOffsetFeatureData~IGetEntities.html)
[ISurfaceOffsetFeatureData::ISetEntities Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISurfaceOffsetFeatureData~ISetEntities.html)

## Availability

SOLIDWORKS 2012 SP04, Revision Number 20.4
