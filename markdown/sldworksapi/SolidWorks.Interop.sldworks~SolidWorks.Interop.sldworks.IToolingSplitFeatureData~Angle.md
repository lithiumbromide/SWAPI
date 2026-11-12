---
title: "Angle Property (IToolingSplitFeatureData)"
project: "SOLIDWORKS API Help"
interface: "IToolingSplitFeatureData"
member: "Angle"
kind: "property"
source: "sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IToolingSplitFeatureData~Angle.html"
---

# Angle Property (IToolingSplitFeatureData)

Gets or sets the draft angle for this tooling split feature if an [interlock surface](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.IToolingSplitFeatureData~InterlockSurface.html) exists.

## Syntax

### Visual Basic (Declaration)

```vb
Property Angle As System.Double
```

### Visual Basic (Usage)

```vb
Dim instance As IToolingSplitFeatureData
Dim value As System.Double

instance.Angle = value

value = instance.Angle
```

### C#

```csharp
System.double Angle {get; set;}
```

### C++/CLI

```cpp
property System.double Angle {
   System.double get();
   void set (    System.double value);
}
```

**NOTE:** See [Differences Between Unmanaged C++ and C++/CLI Code](DifferencesBetweenUnManagedAndCPPCLI.htm).

### Property Value

Angle in radians

## VBA Syntax

See [ToolingSplitFeatureData::Angle](ms-its:sldworksapivb6.chm::/sldworks~ToolingSplitFeatureData~Angle.html).

## Examples

See the [IToolingSplitFeatureData](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IToolingSplitFeatureData.html) examples.

## Remarks

See [Accessing Selections that Define Features](sldworksAPIProgGuide.chm::/Miscellaneous/Accessing_Selections_that_Define_Features.htm) for additional details.

## See Also

[IToolingSplitFeatureData Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IToolingSplitFeatureData.html)
[IToolingSplitFeatureData Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IToolingSplitFeatureData_members.html)

## Availability

SOLIDWORKS 2005 FCS, Revision Number 13.0
