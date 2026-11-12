---
title: "ProjectionOption Property (IMeasure)"
project: "SOLIDWORKS API Help"
interface: "IMeasure"
member: "ProjectionOption"
kind: "property"
source: "sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IMeasure~ProjectionOption.html"
---

# ProjectionOption Property (IMeasure)

Gets or sets whether the distance between the selected entities is projected.

## Syntax

### Visual Basic (Declaration)

```vb
Property ProjectionOption As System.Integer
```

### Visual Basic (Usage)

```vb
Dim instance As IMeasure
Dim value As System.Integer

instance.ProjectionOption = value

value = instance.ProjectionOption
```

### C#

```csharp
System.int ProjectionOption {get; set;}
```

### C++/CLI

```cpp
property System.int ProjectionOption {
   System.int get();
   void set (    System.int value);
}
```

**NOTE:** See [Differences Between Unmanaged C++ and C++/CLI Code](DifferencesBetweenUnManagedAndCPPCLI.htm).

### Property Value

Distance between the selected entities is projected as defined by [swMeasureProjectOnOption_e](ms-its:swconst.chm::/SOLIDWORKS.Interop.swconst~SOLIDWORKS.Interop.swconst.swMeasureProjectOnOption_e.html)

## VBA Syntax

See [Measure::ProjectionOption](ms-its:sldworksapivb6.chm::/Sldworks~Measure~ProjectionOption.html).

## See Also

[IMeasure Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IMeasure.html)
[IMeasure Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IMeasure_members.html)
[IMeasure::SetProjectionEntity Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IMeasure~SetProjectionEntity.html)
[IMeasure::Projection Property](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IMeasure~Projection.html)

## Availability

SOLIDWORKS 2008 FCS, Revision Number 16.0
