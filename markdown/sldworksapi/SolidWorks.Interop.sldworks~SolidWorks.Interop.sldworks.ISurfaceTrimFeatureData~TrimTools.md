---
title: "TrimTools Property (ISurfaceTrimFeatureData)"
project: "SOLIDWORKS API Help"
interface: "ISurfaceTrimFeatureData"
member: "TrimTools"
kind: "property"
source: "sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISurfaceTrimFeatureData~TrimTools.html"
---

# TrimTools Property (ISurfaceTrimFeatureData)

Gets the trim tools for surface trim feature.

**NOTE:** **This property is a get-only property.** **Set is not implemented**.

## Syntax

### Visual Basic (Declaration)

```vb
Property TrimTools As System.Object
```

### Visual Basic (Usage)

```vb
Dim instance As ISurfaceTrimFeatureData
Dim value As System.Object

instance.TrimTools = value

value = instance.TrimTools
```

### C#

```csharp
System.object TrimTools {get; set;}
```

### C++/CLI

```cpp
property System.Object^ TrimTools {
   System.Object^ get();
   void set (    System.Object^ value);
}
```

**NOTE:** See [Differences Between Unmanaged C++ and C++/CLI Code](DifferencesBetweenUnManagedAndCPPCLI.htm).

### Property Value

Array of trim tools

## VBA Syntax

See [SurfaceTrimFeatureData::TrimTools](ms-its:sldworksapivb6.chm::/sldworks~SurfaceTrimFeatureData~TrimTools.html).

## Examples

See the [ISurfaceTrimFeatureData](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISurfaceTrimFeatureData.html) examples.

## Remarks

See [Accessing Selections that Define Features](sldworksAPIProgGuide.chm::/Miscellaneous/Accessing_Selections_that_Define_Features.htm) for additional details.

## See Also

[ISurfaceTrimFeatureData Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISurfaceTrimFeatureData.html)
[ISurfaceTrimFeatureData Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISurfaceTrimFeatureData_members.html)
[ISurfaceTrimFeatureData::GetTrimToolsCount Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISurfaceTrimFeatureData~GetTrimToolsCount.html)
[ISurfaceTrimFeatureData::IGetTrimTools Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISurfaceTrimFeatureData~IGetTrimTools.html)
[ISurfaceTrimFeatureData::ISetTrimTools Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISurfaceTrimFeatureData~ISetTrimTools.html)

## Availability

SOLIDWORKS 2001Plus SP2, Revision Number 10.2
