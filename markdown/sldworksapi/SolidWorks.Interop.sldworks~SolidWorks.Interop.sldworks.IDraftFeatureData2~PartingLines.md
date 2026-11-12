---
title: "PartingLines Property (IDraftFeatureData2)"
project: "SOLIDWORKS API Help"
interface: "IDraftFeatureData2"
member: "PartingLines"
kind: "property"
source: "sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IDraftFeatureData2~PartingLines.html"
---

# PartingLines Property (IDraftFeatureData2)

Gets or sets the parting lines for this draft feature.

## Syntax

### Visual Basic (Declaration)

```vb
Property PartingLines As System.Object
```

### Visual Basic (Usage)

```vb
Dim instance As IDraftFeatureData2
Dim value As System.Object

instance.PartingLines = value

value = instance.PartingLines
```

### C#

```csharp
System.object PartingLines {get; set;}
```

### C++/CLI

```cpp
property System.Object^ PartingLines {
   System.Object^ get();
   void set (    System.Object^ value);
}
```

**NOTE:** See [Differences Between Unmanaged C++ and C++/CLI Code](DifferencesBetweenUnManagedAndCPPCLI.htm).

### Property Value

Array of [parting lines](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.IEdge.html)

## VBA Syntax

See [DraftFeatureData2::PartingLines](ms-its:sldworksapivb6.chm::/sldworks~DraftFeatureData2~PartingLines.html).

## Remarks

See [Accessing Selections that Define Features](sldworksAPIProgGuide.chm::/Miscellaneous/Accessing_Selections_that_Define_Features.htm) for additional details on using this property.

## See Also

[IDraftFeatureData2 Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IDraftFeatureData2.html)
[IDraftFeatureData2 Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IDraftFeatureData2_members.html)
[IDraftFeatureData2::GetPartingLinesCount Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IDraftFeatureData2~GetPartingLinesCount.html)
[IDraftFeatureData2::IGetPartingLines Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IDraftFeatureData2~IGetPartingLines.html)
[IDraftFeatureData2::ISetPartingLines Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IDraftFeatureData2~ISetPartingLines.html)

## Availability

SOLIDWORKS 2001Plus FCS, Revision Number 10.0
