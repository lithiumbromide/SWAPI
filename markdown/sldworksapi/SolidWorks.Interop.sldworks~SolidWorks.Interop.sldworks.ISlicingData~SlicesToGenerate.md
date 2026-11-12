---
title: "SlicesToGenerate Property (ISlicingData)"
project: "SOLIDWORKS API Help"
interface: "ISlicingData"
member: "SlicesToGenerate"
kind: "property"
source: "sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISlicingData~SlicesToGenerate.html"
---

# SlicesToGenerate Property (ISlicingData)

Gets or sets the slicing method.

## Syntax

### Visual Basic (Declaration)

```vb
Property SlicesToGenerate As System.Integer
```

### Visual Basic (Usage)

```vb
Dim instance As ISlicingData
Dim value As System.Integer

instance.SlicesToGenerate = value

value = instance.SlicesToGenerate
```

### C#

```csharp
System.int SlicesToGenerate {get; set;}
```

### C++/CLI

```cpp
property System.int SlicesToGenerate {
   System.int get();
   void set (    System.int value);
}
```

**NOTE:** See [Differences Between Unmanaged C++ and C++/CLI Code](DifferencesBetweenUnManagedAndCPPCLI.htm).

### Property Value

Slicing method as defined in [swSlicingTypes_e](ms-its:swconst.chm::/SolidWorks.Interop.swconst~SolidWorks.Interop.swconst.swSlicingTypes_e.html)

## VBA Syntax

See [SlicingData::SlicesToGenerate](ms-its:sldworksapivb6.chm::/sldworks~SlicingData~SlicesToGenerate.html).

## Examples

See the [ISlicingData](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISlicingData.html) example.

## See Also

[ISlicingData Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISlicingData.html)
[ISlicingData Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISlicingData_members.html)

## Availability

SOLIDWORKS 2020 FCS, Revision Number 28.0
