---
title: "Entities Property (IBreakCornerFeatureData)"
project: "SOLIDWORKS API Help"
interface: "IBreakCornerFeatureData"
member: "Entities"
kind: "property"
source: "sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IBreakCornerFeatureData~Entities.html"
---

# Entities Property (IBreakCornerFeatureData)

Gets or sets the faces or edges to which this break corner is applied.

## Syntax

### Visual Basic (Declaration)

```vb
Property Entities As System.Object
```

### Visual Basic (Usage)

```vb
Dim instance As IBreakCornerFeatureData
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

Array of [faces](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.IFace2.html) or [edges](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.IEdge.html)

## VBA Syntax

See [BreakCornerFeatureData::Entities](ms-its:sldworksapivb6.chm::/sldworks~BreakCornerFeatureData~Entities.html).

## Remarks

See [Accessing Selections that Define Features](sldworksAPIProgGuide.chm::/Miscellaneous/Accessing_Selections_that_Define_Features.htm) for additional details on using this property.

## See Also

[IBreakCornerFeatureData Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IBreakCornerFeatureData.html)
[IBreakCornerFeatureData Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IBreakCornerFeatureData_members.html)
[IBreakCornerFeatureData::IGetEntities Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IBreakCornerFeatureData~IGetEntities.html)
[IBreakCornerFeatureData::ISetEntities Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IBreakCornerFeatureData~ISetEntities.html)
[IBreakCornerFeatureData::GetEntitiesCount Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IBreakCornerFeatureData~GetEntitiesCount.html)

## Availability

SOLIDWORKS 2001Plus SP1, Revision Number 10.1
