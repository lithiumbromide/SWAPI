---
title: "Revolutions Property (IThreadFeatureData)"
project: "SOLIDWORKS API Help"
interface: "IThreadFeatureData"
member: "Revolutions"
kind: "property"
source: "sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IThreadFeatureData~Revolutions.html"
---

# Revolutions Property (IThreadFeatureData)

Gets or sets the number of revolutions in the helix of this thread feature, taking into account any offset.

## Syntax

### Visual Basic (Declaration)

```vb
Property Revolutions As System.Double
```

### Visual Basic (Usage)

```vb
Dim instance As IThreadFeatureData
Dim value As System.Double

instance.Revolutions = value

value = instance.Revolutions
```

### C#

```csharp
System.double Revolutions {get; set;}
```

### C++/CLI

```cpp
property System.double Revolutions {
   System.double get();
   void set (    System.double value);
}
```

**NOTE:** See [Differences Between Unmanaged C++ and C++/CLI Code](DifferencesBetweenUnManagedAndCPPCLI.htm).

### Property Value

0.0 < Number of revolutions in the thread helix; default is 10.0 (see **Remarks**)

## VBA Syntax

See [ThreadFeatureData::Revolutions](ms-its:sldworksapivb6.chm::/sldworks~ThreadFeatureData~Revolutions.html).

## Remarks

This property is valid only if [IThreadFeatureData::EndCondition](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IThreadFeatureData~EndCondition.html) is set to [swThreadEndCondition_e](ms-its:swconst.chm::/SolidWorks.Interop.swconst~SolidWorks.Interop.swconst.swThreadEndCondition_e.html).swThreadEndCondition_Revolutions.

Specify either a value or an equation that starts with an equal sign (=).

## See Also

[IThreadFeatureData Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IThreadFeatureData.html)
[IThreadFeatureData Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IThreadFeatureData_members.html)

## Availability

SOLIDWORKS 2018 FCS, Revision Number 26.0
