---
title: "TrimTools Property (ISplitBodyFeatureData)"
project: "SOLIDWORKS API Help"
interface: "ISplitBodyFeatureData"
member: "TrimTools"
kind: "property"
source: "sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISplitBodyFeatureData~TrimTools.html"
---

# TrimTools Property (ISplitBodyFeatureData)

Gets the trimming surfaces used as trim tools in this Split feature.

**NOTE:** **This property is a get-only property.** **Set is not implemented**.

## Syntax

### Visual Basic (Declaration)

```vb
Property TrimTools As System.Object
```

### Visual Basic (Usage)

```vb
Dim instance As ISplitBodyFeatureData
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

Array of trimming surfaces used as trim tools:

- Planar and non-planar faces
- Reference planes
- Reference surfaces
- Sketches

## VBA Syntax

See [SplitBodyFeatureData::TrimTools](ms-its:sldworksapivb6.chm::/sldworks~SplitBodyFeatureData~TrimTools.html).

## Remarks

See [Accessing Selections that Define Features](sldworksAPIProgGuide.chm::/Miscellaneous/Accessing_Selections_that_Define_Features.htm) for additional details.

## See Also

[ISplitBodyFeatureData Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISplitBodyFeatureData.html)
[ISplitBodyFeatureData Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISplitBodyFeatureData_members.html)
[ISplitBodyFeatureData::GetTrimToolsCount Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISplitBodyFeatureData~GetTrimToolsCount.html)
[ISplitBodyFeatureData::IGetTrimTools Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISplitBodyFeatureData~IGetTrimTools.html)
[ISplitBodyFeatureData::ISetTrimTools Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISplitBodyFeatureData~ISetTrimTools.html)

## Availability

SOLIDWORKS 2005 FCS, Revision Number 13.0
