---
title: "CoreSurfaces Property (IToolingSplitFeatureData)"
project: "SOLIDWORKS API Help"
interface: "IToolingSplitFeatureData"
member: "CoreSurfaces"
kind: "property"
source: "sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IToolingSplitFeatureData~CoreSurfaces.html"
---

# CoreSurfaces Property (IToolingSplitFeatureData)

Gets or sets the core surface bodies for this tooling split feature.

## Syntax

### Visual Basic (Declaration)

```vb
Property CoreSurfaces As System.Object
```

### Visual Basic (Usage)

```vb
Dim instance As IToolingSplitFeatureData
Dim value As System.Object

instance.CoreSurfaces = value

value = instance.CoreSurfaces
```

### C#

```csharp
System.object CoreSurfaces {get; set;}
```

### C++/CLI

```cpp
property System.Object^ CoreSurfaces {
   System.Object^ get();
   void set (    System.Object^ value);
}
```

**NOTE:** See [Differences Between Unmanaged C++ and C++/CLI Code](DifferencesBetweenUnManagedAndCPPCLI.htm).

### Property Value

Array of core surface [bodies](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.IBody2.html)

## VBA Syntax

See [ToolingSplitFeatureData::CoreSurfaces](ms-its:sldworksapivb6.chm::/sldworks~ToolingSplitFeatureData~CoreSurfaces.html).

## Examples

See the [IToolingSplitFeatureData](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IToolingSplitFeatureData.html) examples.

## Remarks

See [Accessing Selections that Define Features](sldworksAPIProgGuide.chm::/Miscellaneous/Accessing_Selections_that_Define_Features.htm) for additional details.

## See Also

[IToolingSplitFeatureData Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IToolingSplitFeatureData.html)
[IToolingSplitFeatureData Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IToolingSplitFeatureData_members.html)
[IToolingSplitFeatureData::GetCoreSurfacesCount Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IToolingSplitFeatureData~GetCoreSurfacesCount.html)
[IToolingSplitFeatureData::IGetCoreSurfaces Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IToolingSplitFeatureData~IGetCoreSurfaces.html)
[IToolingSplitFeatureData::ISetCoreSurfaces Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IToolingSplitFeatureData~ISetCoreSurfaces.html)

## Availability

SOLIDWORKS 2005 FCS, Revision Number 13.0
