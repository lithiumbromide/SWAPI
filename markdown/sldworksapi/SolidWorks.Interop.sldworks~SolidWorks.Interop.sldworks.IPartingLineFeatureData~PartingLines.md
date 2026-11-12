---
title: "PartingLines Property (IPartingLineFeatureData)"
project: "SOLIDWORKS API Help"
interface: "IPartingLineFeatureData"
member: "PartingLines"
kind: "property"
source: "sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IPartingLineFeatureData~PartingLines.html"
---

# PartingLines Property (IPartingLineFeatureData)

Gets and sets the edges for the parting lines.

## Syntax

### Visual Basic (Declaration)

```vb
Property PartingLines As System.Object
```

### Visual Basic (Usage)

```vb
Dim instance As IPartingLineFeatureData
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

Array of [edges](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.IEdge.html)

## VBA Syntax

See [PartingLineFeatureData::PartingLines](ms-its:sldworksapivb6.chm::/sldworks~PartingLineFeatureData~PartingLines.html).

## Remarks

See [Accessing Selections that Define Features](sldworksAPIProgGuide.chm::/Miscellaneous/Accessing_Selections_that_Define_Features.htm) for additional details on using this method.

## See Also

[IPartingLineFeatureData Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IPartingLineFeatureData.html)
[IPartingLineFeatureData Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IPartingLineFeatureData_members.html)
[IPartingLineFeatureData::IGetPartingLines Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IPartingLineFeatureData~IGetPartingLines.html)
[IPartingLineFeatureData::ISetPartingLines Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IPartingLineFeatureData~ISetPartingLines.html)
[IPartingLineFeatureData::GetPartingLinesCount Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IPartingLineFeatureData~GetPartingLinesCount.html)

## Availability

SOLIDWORKS 2005 FCS, Revision Number 13.0
