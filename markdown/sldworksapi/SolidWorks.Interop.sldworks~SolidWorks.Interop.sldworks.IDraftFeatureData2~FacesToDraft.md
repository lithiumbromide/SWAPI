---
title: "FacesToDraft Property (IDraftFeatureData2)"
project: "SOLIDWORKS API Help"
interface: "IDraftFeatureData2"
member: "FacesToDraft"
kind: "property"
source: "sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IDraftFeatureData2~FacesToDraft.html"
---

# FacesToDraft Property (IDraftFeatureData2)

Gets or sets the faces that define this draft feature.

## Syntax

### Visual Basic (Declaration)

```vb
Property FacesToDraft As System.Object
```

### Visual Basic (Usage)

```vb
Dim instance As IDraftFeatureData2
Dim value As System.Object

instance.FacesToDraft = value

value = instance.FacesToDraft
```

### C#

```csharp
System.object FacesToDraft {get; set;}
```

### C++/CLI

```cpp
property System.Object^ FacesToDraft {
   System.Object^ get();
   void set (    System.Object^ value);
}
```

**NOTE:** See [Differences Between Unmanaged C++ and C++/CLI Code](DifferencesBetweenUnManagedAndCPPCLI.htm).

### Property Value

Array of [faces](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.IFace2.html)

## VBA Syntax

See [DraftFeatureData2::FacesToDraft](ms-its:sldworksapivb6.chm::/sldworks~DraftFeatureData2~FacesToDraft.html).

## Remarks

See [Accessing Selections that Define Features](sldworksAPIProgGuide.chm::/Miscellaneous/Accessing_Selections_that_Define_Features.htm) for additional details on using this property.

## See Also

[IDraftFeatureData2 Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IDraftFeatureData2.html)
[IDraftFeatureData2 Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IDraftFeatureData2_members.html)
[IDraftFeatureData2::GetFacesToDraftCount Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IDraftFeatureData2~GetFacesToDraftCount.html)
[IDraftFeatureData2::IGetFacesToDraft Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IDraftFeatureData2~IGetFacesToDraft.html)
[IDraftFeatureData2::ISetFacesToDraft Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IDraftFeatureData2~ISetFacesToDraft.html)

## Availability

SOLIDWORKS 2001Plus FCS, Revision 10.0
