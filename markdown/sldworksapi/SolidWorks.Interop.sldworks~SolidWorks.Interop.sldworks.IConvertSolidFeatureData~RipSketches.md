---
title: "RipSketches Property (IConvertSolidFeatureData)"
project: "SOLIDWORKS API Help"
interface: "IConvertSolidFeatureData"
member: "RipSketches"
kind: "property"
source: "sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IConvertSolidFeatureData~RipSketches.html"
---

# RipSketches Property (IConvertSolidFeatureData)

Gets or sets the sketches to use to define required rips in this convert solid feature.

## Syntax

### Visual Basic (Declaration)

```vb
Property RipSketches As System.Object
```

### Visual Basic (Usage)

```vb
Dim instance As IConvertSolidFeatureData
Dim value As System.Object

instance.RipSketches = value

value = instance.RipSketches
```

### C#

```csharp
System.object RipSketches {get; set;}
```

### C++/CLI

```cpp
property System.Object^ RipSketches {
   System.Object^ get();
   void set (    System.Object^ value);
}
```

NOTE:

See

[Differences Between Unmanaged C++ and C++/CLI Code](DifferencesBetweenUnManagedAndCPPCLI.htm)

.

### Property Value

Array of rip

[sketch](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISketch.html)

es

## VBA Syntax

See

[ConvertSolidFeatureData::RipSketches](ms-its:sldworksapivb6.chm::/sldworks~ConvertSolidFeatureData~RipSketches.html)

.

## See Also

[IConvertSolidFeatureData Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IConvertSolidFeatureData.html)

[IConvertSolidFeatureData Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IConvertSolidFeatureData_members.html)

## Availability

SOLIDWORKS 2025 SP02, Revision Number 33.2
