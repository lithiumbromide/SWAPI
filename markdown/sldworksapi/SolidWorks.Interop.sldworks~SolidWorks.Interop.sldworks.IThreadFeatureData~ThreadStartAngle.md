---
title: "ThreadStartAngle Property (IThreadFeatureData)"
project: "SOLIDWORKS API Help"
interface: "IThreadFeatureData"
member: "ThreadStartAngle"
kind: "property"
source: "sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IThreadFeatureData~ThreadStartAngle.html"
---

# ThreadStartAngle Property (IThreadFeatureData)

Gets or sets the start angle of the thread of this thread feature

## Syntax

### Visual Basic (Declaration)

```vb
Property ThreadStartAngle As System.Double
```

### Visual Basic (Usage)

```vb
Dim instance As IThreadFeatureData
Dim value As System.Double

instance.ThreadStartAngle = value

value = instance.ThreadStartAngle
```

### C#

```csharp
System.double ThreadStartAngle {get; set;}
```

### C++/CLI

```cpp
property System.double ThreadStartAngle {
   System.double get();
   void set (    System.double value);
}
```

**NOTE:** See [Differences Between Unmanaged C++ and C++/CLI Code](DifferencesBetweenUnManagedAndCPPCLI.htm).

### Property Value

0.0 (default) < Thread start angle < 2*pi radians

## VBA Syntax

See [ThreadFeatureData::ThreadStartAngle](ms-its:sldworksapivb6.chm::/sldworks~ThreadFeatureData~ThreadStartAngle.html).

## Examples

See the [IThreadFeatureData](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IThreadFeatureData.html) examples.

## Remarks

Specify either a value or an equation that starts with an equal sign (=).

## See Also

[IThreadFeatureData Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IThreadFeatureData.html)
[IThreadFeatureData Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IThreadFeatureData_members.html)

## Availability

SOLIDWORKS 2018 FCS, Revision Number 26.0
