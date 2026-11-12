---
title: "Entities Property (ISurfaceKnitFeatureData)"
project: "SOLIDWORKS API Help"
interface: "ISurfaceKnitFeatureData"
member: "Entities"
kind: "property"
source: "sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISurfaceKnitFeatureData~Entities.html"
---

# Entities Property (ISurfaceKnitFeatureData)

Gets or sets the knitted faces and surfaces.

## Syntax

### Visual Basic (Declaration)

```vb
Property Entities As System.Object
```

### Visual Basic (Usage)

```vb
Dim instance As ISurfaceKnitFeatureData
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

Array of knit entities ([faces](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.IFace2.html) and [surfaces](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.ISurface.html))

## VBA Syntax

See [SurfaceKnitFeatureData::Entities](ms-its:sldworksapivb6.chm::/sldworks~SurfaceKnitFeatureData~Entities.html).

## Examples

[Get Knit Surface Data (VBA)](Get_Knit_Surface_Data_Example_VB.htm)

## Remarks

See [Accessing Selections that Define Features](sldworksAPIProgGuide.chm::/Miscellaneous/Accessing_Selections_that_Define_Features.htm) for additional details.

## See Also

[ISurfaceKnitFeatureData Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISurfaceKnitFeatureData.html)
[ISurfaceKnitFeatureData Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISurfaceKnitFeatureData_members.html)
[ISurfaceKnitFeatureData::GetEntitiesCount Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISurfaceKnitFeatureData~GetEntitiesCount.html)
[ISurfaceKnitFeatureData::IGetEntities Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISurfaceKnitFeatureData~IGetEntities.html)
[ISurfaceKnitFeatureData::ISetEntities Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISurfaceKnitFeatureData~ISetEntities.html)

## Availability

SOLIDWORKS 2001Plus SP1, Revision Number 10.1
