---
title: "PullDirection Property (IWrapSketchFeatureData)"
project: "SOLIDWORKS API Help"
interface: "IWrapSketchFeatureData"
member: "PullDirection"
kind: "property"
source: "sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IWrapSketchFeatureData~PullDirection.html"
---

# PullDirection Property (IWrapSketchFeatureData)

Gets or sets the pull direction for this wrap feature.

## Syntax

### Visual Basic (Declaration)

```vb
Property PullDirection As System.Object
```

### Visual Basic (Usage)

```vb
Dim instance As IWrapSketchFeatureData
Dim value As System.Object

instance.PullDirection = value

value = instance.PullDirection
```

### C#

```csharp
System.object PullDirection {get; set;}
```

### C++/CLI

```cpp
property System.Object^ PullDirection {
   System.Object^ get();
   void set (    System.Object^ value);
}
```

**NOTE:** See [Differences Between Unmanaged C++ and C++/CLI Code](DifferencesBetweenUnManagedAndCPPCLI.htm).

### Property Value

Pointer one of the following entities as defined in [swSelectType_e](ms-its:swconst.chm::/SOLIDWORKS.Interop.swconst~SOLIDWORKS.Interop.swconst.swSelectType_e.html):

- swSelDATUMAXES
- swSelDATUMPLANES
- swSelEDGES
- swSelEXTSKETCHPOINTS
- swSelEXTSKETCHSEGS
- swSelFACES
- swSelLOCATIONS

## VBA Syntax

See [WrapSketchFeatureData::PullDirection](ms-its:sldworksapivb6.chm::/sldworks~WrapSketchFeatureData~PullDirection.html).

## Remarks

See [Accessing Selections that Define Features](sldworksAPIProgGuide.chm::/Miscellaneous/Accessing_Selections_that_Define_Features.htm) for additional details.

## See Also

[IWrapSketchFeatureData Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IWrapSketchFeatureData.html)
[IWrapSketchFeatureData Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IWrapSketchFeatureData_members.html)

## Availability

SOLIDWORKS 2005 FCS, Revision Number 13.0
