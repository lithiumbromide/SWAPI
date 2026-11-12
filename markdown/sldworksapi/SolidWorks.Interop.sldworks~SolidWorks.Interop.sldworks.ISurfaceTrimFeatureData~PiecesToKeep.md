---
title: "PiecesToKeep Property (ISurfaceTrimFeatureData)"
project: "SOLIDWORKS API Help"
interface: "ISurfaceTrimFeatureData"
member: "PiecesToKeep"
kind: "property"
source: "sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISurfaceTrimFeatureData~PiecesToKeep.html"
---

# PiecesToKeep Property (ISurfaceTrimFeatureData)

Gets the pieces to keep for this surface trim feature.

**NOTE:** **This property is a get-only property.** **Set is not implemented**.

## Syntax

### Visual Basic (Declaration)

```vb
Property PiecesToKeep As System.Object
```

### Visual Basic (Usage)

```vb
Dim instance As ISurfaceTrimFeatureData
Dim value As System.Object

instance.PiecesToKeep = value

value = instance.PiecesToKeep
```

### C#

```csharp
System.object PiecesToKeep {get; set;}
```

### C++/CLI

```cpp
property System.Object^ PiecesToKeep {
   System.Object^ get();
   void set (    System.Object^ value);
}
```

**NOTE:** See [Differences Between Unmanaged C++ and C++/CLI Code](DifferencesBetweenUnManagedAndCPPCLI.htm).

### Property Value

Array of pieces to keep

## VBA Syntax

See [SurfaceTrimFeatureData::PiecesToKeep](ms-its:sldworksapivb6.chm::/sldworks~SurfaceTrimFeatureData~PiecesToKeep.html).

## Remarks

See [Accessing Selections that Define Features](sldworksAPIProgGuide.chm::/Miscellaneous/Accessing_Selections_that_Define_Features.htm) for additional details.

## See Also

[ISurfaceTrimFeatureData Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISurfaceTrimFeatureData.html)
[ISurfaceTrimFeatureData Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISurfaceTrimFeatureData_members.html)
[ISurfaceTrimFeatureData::GetPiecesToKeepCount Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISurfaceTrimFeatureData~GetPiecesToKeepCount.html)
[ISurfaceTrimFeatureData::IGetPiecesToKeep Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISurfaceTrimFeatureData~IGetPiecesToKeep.html)
[ISurfaceTrimFeatureData::ISetPiecesToKeep Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISurfaceTrimFeatureData~ISetPiecesToKeep.html)

## Availability

SOLIDWORKS 2001Plus SP2, Revision Number 10.2
