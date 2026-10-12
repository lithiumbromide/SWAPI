---
title: "RotationAngle Property (IThreadFeatureData)"
project: "SOLIDWORKS API Help"
interface: "IThreadFeatureData"
member: "RotationAngle"
kind: "property"
source: "sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IThreadFeatureData~RotationAngle.html"
---

# RotationAngle Property (IThreadFeatureData)

Gets or sets the angle of rotation of the thread helix of this thread feature.

## Syntax

### Visual Basic (Declaration)

```vb
Property RotationAngle As System.Double
```

### Visual Basic (Usage)

```vb
Dim instance As IThreadFeatureData
Dim value As System.Double

instance.RotationAngle = value

value = instance.RotationAngle
```

### C#

```csharp
System.double RotationAngle {get; set;}
```

### C++/CLI

```cpp
property System.double RotationAngle {
   System.double get();
   void set (    System.double value);
}
```

**NOTE:** See [Differences Between Unmanaged C++ and C++/CLI Code](DifferencesBetweenUnManagedAndCPPCLI.htm).

### Property Value

0.0 (default) <= Angle of rotation <= 2*pi radians

## VBA Syntax

See [ThreadFeatureData::RotationAngle](ms-its:sldworksapivb6.chm::/sldworks~ThreadFeatureData~RotationAngle.html).

## Examples

See the [IThreadFeatureData](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IThreadFeatureData.html) examples.

## Remarks

Specify either a value or an equation that starts with an equal sign (=).

## See Also

[IThreadFeatureData Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IThreadFeatureData.html)
[IThreadFeatureData Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IThreadFeatureData_members.html)

## Availability

SOLIDWORKS 2018 FCS, Revision Number 26.0
