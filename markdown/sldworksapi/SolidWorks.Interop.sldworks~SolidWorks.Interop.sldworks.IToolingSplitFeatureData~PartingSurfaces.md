---
title: "PartingSurfaces Property (IToolingSplitFeatureData)"
project: "SOLIDWORKS API Help"
interface: "IToolingSplitFeatureData"
member: "PartingSurfaces"
kind: "property"
source: "sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IToolingSplitFeatureData~PartingSurfaces.html"
---

# PartingSurfaces Property (IToolingSplitFeatureData)

Gets or sets the parting surface bodies for this tooling split feature.

## Syntax

### Visual Basic (Declaration)

```vb
Property PartingSurfaces As System.Object
```

### Visual Basic (Usage)

```vb
Dim instance As IToolingSplitFeatureData
Dim value As System.Object

instance.PartingSurfaces = value

value = instance.PartingSurfaces
```

### C#

```csharp
System.object PartingSurfaces {get; set;}
```

### C++/CLI

```cpp
property System.Object^ PartingSurfaces {
   System.Object^ get();
   void set (    System.Object^ value);
}
```

**NOTE:** See [Differences Between Unmanaged C++ and C++/CLI Code](DifferencesBetweenUnManagedAndCPPCLI.htm).

### Property Value

Array of parting surface [bodies](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.IBody2.html)

## VBA Syntax

See [ToolingSplitFeatureData::PartingSurfaces](ms-its:sldworksapivb6.chm::/sldworks~ToolingSplitFeatureData~PartingSurfaces.html).

## Examples

See the [IToolingSplitFeatureData](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IToolingSplitFeatureData.html) examples.

## Remarks

See [Accessing Selections that Define Features](sldworksAPIProgGuide.chm::/Miscellaneous/Accessing_Selections_that_Define_Features.htm) for additional details.

## See Also

[IToolingSplitFeatureData Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IToolingSplitFeatureData.html)
[IToolingSplitFeatureData Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IToolingSplitFeatureData_members.html)
[IToolingSplitFeatureData::GetPartingSurfacesCount Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IToolingSplitFeatureData~GetPartingSurfacesCount.html)
[IToolingSplitFeatureData::IGetPartingSurfaces Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IToolingSplitFeatureData~IGetPartingSurfaces.html)
[IToolingSplitFeatureData::ISetPartingSurfaces Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IToolingSplitFeatureData~ISetPartingSurfaces.html)

## Availability

SOLIDWORKS 2005 FCS, Revision Number 13.0
