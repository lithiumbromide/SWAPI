---
title: "DimensionDisplay Property (ISketchBlockInstance)"
project: "SOLIDWORKS API Help"
interface: "ISketchBlockInstance"
member: "DimensionDisplay"
kind: "property"
source: "sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISketchBlockInstance~DimensionDisplay.html"
---

# DimensionDisplay Property (ISketchBlockInstance)

Gets whether dimensions are displayed.

## Syntax

### Visual Basic (Declaration)

```vb
Property DimensionDisplay As System.Boolean
```

### Visual Basic (Usage)

```vb
Dim instance As ISketchBlockInstance
Dim value As System.Boolean

instance.DimensionDisplay = value

value = instance.DimensionDisplay
```

### C#

```csharp
System.bool DimensionDisplay {get; set;}
```

### C++/CLI

```cpp
property System.bool DimensionDisplay {
   System.bool get();
   void set (    System.bool value);
}
```

**NOTE:** See [Differences Between Unmanaged C++ and C++/CLI Code](DifferencesBetweenUnManagedAndCPPCLI.htm).

### Property Value

True if dimensions are displayed, false if not

## VBA Syntax

See [SketchBlockInstance::DimensionDisplay](ms-its:sldworksapivb6.chm::/sldworks~SketchBlockInstance~DimensionDisplay.html).

## See Also

[ISketchBlockInstance Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISketchBlockInstance.html)
[ISketchBlockInstance Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISketchBlockInstance_members.html)
[ISketchBlockDefinition::GetDisplayDimensions Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISketchBlockDefinition~GetDisplayDimensions.html)
[ISketchBlockDefinition::IGetDisplayDimensions Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISketchBlockDefinition~IGetDisplayDimensions.html)
[ISketchBlockDefinition::GetDisplayDimensionCount Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISketchBlockDefinition~GetDisplayDimensionCount.html)

## Availability

SOLIDWORKS 2007 FCS, Revision Number 15.0
