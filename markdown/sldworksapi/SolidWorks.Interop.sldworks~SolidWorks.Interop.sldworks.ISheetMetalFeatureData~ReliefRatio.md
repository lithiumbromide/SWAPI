---
title: "ReliefRatio Property (ISheetMetalFeatureData)"
project: "SOLIDWORKS API Help"
interface: "ISheetMetalFeatureData"
member: "ReliefRatio"
kind: "property"
source: "sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISheetMetalFeatureData~ReliefRatio.html"
---

# ReliefRatio Property (ISheetMetalFeatureData)

Gets or sets the relief ratio for this sheet metal feature.

## Syntax

### Visual Basic (Declaration)

```vb
Property ReliefRatio As System.Double
```

### Visual Basic (Usage)

```vb
Dim instance As ISheetMetalFeatureData
Dim value As System.Double

instance.ReliefRatio = value

value = instance.ReliefRatio
```

### C#

```csharp
System.double ReliefRatio {get; set;}
```

### C++/CLI

```cpp
property System.double ReliefRatio {
   System.double get();
   void set (    System.double value);
}
```

**NOTE:** See [Differences Between Unmanaged C++ and C++/CLI Code](DifferencesBetweenUnManagedAndCPPCLI.htm).

### Property Value

Value of the relief ratio

## VBA Syntax

See [SheetMetalFeatureData::ReliefRatio](ms-its:sldworksapivb6.chm::/sldworks~SheetMetalFeatureData~ReliefRatio.html).

## Examples

See the [IBaseFlangeFeatureData](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IBaseFlangeFeatureData.html) examples.

## See Also

[ISheetMetalFeatureData Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISheetMetalFeatureData.html)
[ISheetMetalFeatureData Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISheetMetalFeatureData_members.html)
[ISheetMetalFeatureData::UseAutoRelief Property](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISheetMetalFeatureData~UseAutoRelief.html)
[ISheetMetalFeatureData::AutoReliefType Property](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISheetMetalFeatureData~AutoReliefType.html)
[IBaseFlangeFeatureData::Initialize Method ()](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IBaseFlangeFeatureData~Initialize.html)

## Availability

SOLIDWORKS 2001 SP1, Revision Number 9.1
