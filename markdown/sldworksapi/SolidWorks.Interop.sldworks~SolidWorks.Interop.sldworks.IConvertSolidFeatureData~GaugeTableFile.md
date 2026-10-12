---
title: "GaugeTableFile Property (IConvertSolidFeatureData)"
project: "SOLIDWORKS API Help"
interface: "IConvertSolidFeatureData"
member: "GaugeTableFile"
kind: "property"
source: "sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IConvertSolidFeatureData~GaugeTableFile.html"
---

# GaugeTableFile Property (IConvertSolidFeatureData)

Gets or sets the gauge table file in this convert solid feature.

## Syntax

### Visual Basic (Declaration)

```vb
Property GaugeTableFile As System.String
```

### Visual Basic (Usage)

```vb
Dim instance As IConvertSolidFeatureData
Dim value As System.String

instance.GaugeTableFile = value

value = instance.GaugeTableFile
```

### C#

```csharp
System.string GaugeTableFile {get; set;}
```

### C++/CLI

```cpp
property System.String^ GaugeTableFile {
   System.String^ get();
   void set (    System.String^ value);
}
```

**NOTE:** See [Differences Between Unmanaged C++ and C++/CLI Code](DifferencesBetweenUnManagedAndCPPCLI.htm).

### Property Value

Pathname of gauge table file

## VBA Syntax

See [ConvertSolidFeatureData::GaugeTableFile](ms-its:sldworksapivb6.chm::/sldworks~ConvertSolidFeatureData~GaugeTableFile.html).

## See Also

[IConvertSolidFeatureData Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IConvertSolidFeatureData.html)
[IConvertSolidFeatureData Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IConvertSolidFeatureData_members.html)

## Availability

SOLIDWORKS 2025 SP03, Revision Number 33.3
