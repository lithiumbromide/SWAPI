---
title: "Visibility Property (IMotionPlotFeatureData)"
project: "SOLIDWORKS API Help"
interface: "IMotionPlotFeatureData"
member: "Visibility"
kind: "property"
source: "sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IMotionPlotFeatureData~Visibility.html"
---

# Visibility Property (IMotionPlotFeatureData)

Gets or sets whether a plot's feature data is visible.

## Syntax

### Visual Basic (Declaration)

```vb
Property Visibility As System.Boolean
```

### Visual Basic (Usage)

```vb
Dim instance As IMotionPlotFeatureData
Dim value As System.Boolean

instance.Visibility = value

value = instance.Visibility
```

### C#

```csharp
System.bool Visibility {get; set;}
```

### C++/CLI

```cpp
property System.bool Visibility {
   System.bool get();
   void set (    System.bool value);
}
```

**NOTE:** See [Differences Between Unmanaged C++ and C++/CLI Code](DifferencesBetweenUnManagedAndCPPCLI.htm).

### Property Value

True if the plot's feature data is visible, false if not

## VBA Syntax

See [MotionPlotFeatureData::Visibility](ms-its:sldworksapivb6.chm::/sldworks~MotionPlotFeatureData~Visibility.html).

## See Also

[IMotionPlotFeatureData Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IMotionPlotFeatureData.html)
[IMotionPlotFeatureData Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IMotionPlotFeatureData_members.html)

## Availability

SOLIDWORKS 2011 FCS, Revision Number 19.0
