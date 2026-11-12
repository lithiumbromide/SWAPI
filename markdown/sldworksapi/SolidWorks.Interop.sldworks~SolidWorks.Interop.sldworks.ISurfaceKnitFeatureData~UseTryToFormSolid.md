---
title: "UseTryToFormSolid Property (ISurfaceKnitFeatureData)"
project: "SOLIDWORKS API Help"
interface: "ISurfaceKnitFeatureData"
member: "UseTryToFormSolid"
kind: "property"
source: "sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISurfaceKnitFeatureData~UseTryToFormSolid.html"
---

# UseTryToFormSolid Property (ISurfaceKnitFeatureData)

Gets or sets whether to try to form a solid body when creating the Surface-Knit feature.

## Syntax

### Visual Basic (Declaration)

```vb
Property UseTryToFormSolid As System.Boolean
```

### Visual Basic (Usage)

```vb
Dim instance As ISurfaceKnitFeatureData
Dim value As System.Boolean

instance.UseTryToFormSolid = value

value = instance.UseTryToFormSolid
```

### C#

```csharp
System.bool UseTryToFormSolid {get; set;}
```

### C++/CLI

```cpp
property System.bool UseTryToFormSolid {
   System.bool get();
   void set (    System.bool value);
}
```

**NOTE:** See [Differences Between Unmanaged C++ and C++/CLI Code](DifferencesBetweenUnManagedAndCPPCLI.htm).

### Property Value

True to true to form a solid body, false to not

## VBA Syntax

See [SurfaceKnitFeatureData::UseTryToFormSolid](ms-its:sldworksapivb6.chm::/sldworks~SurfaceKnitFeatureData~UseTryToFormSolid.html).

## Examples

[Create Knit Surface Feature (VB.NET)](Create_Surface_Knit_Feature_Example_VBNET.htm)
[Create Knit Surface Feature (VBA)](Create_Surface_Knit_Feature_Example_VB6.htm)
[Create Knit Surface Feature (C#)](Create_Surface_Knit_Feature_Example_CSharp.htm)

## Remarks

If [ISurfaceKnitFeatureData::UseGapFilters](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.ISurfaceKnitFeatureData~UseGapFilters.html) is true, then this property is automatically enabled or disabled depending on whether a solid body can be created from the input bodies.

If you set this property to true, then [knit tolerance](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.ISurfaceKnitFeatureData~KnitTolerance.html) is automatically updated so that the Surface-Knit feature can be created as a solid body.

See [Accessing Selections that Define Features](sldworksAPIProgGuide.chm::/Miscellaneous/Accessing_Selections_that_Define_Features.htm) for additional details.

## See Also

[ISurfaceKnitFeatureData Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISurfaceKnitFeatureData.html)
[ISurfaceKnitFeatureData Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISurfaceKnitFeatureData_members.html)

## Availability

SOLIDWORKS 2010 FCS, Revision Number 18.0
