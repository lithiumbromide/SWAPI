---
title: "AutoReliefType Property (ISheetMetalFeatureData)"
project: "SOLIDWORKS API Help"
interface: "ISheetMetalFeatureData"
member: "AutoReliefType"
kind: "property"
source: "sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISheetMetalFeatureData~AutoReliefType.html"
---

# AutoReliefType Property (ISheetMetalFeatureData)

Gets or sets the sheet metal bend relief type.

## Syntax

### Visual Basic (Declaration)

```vb
Property AutoReliefType As System.Integer
```

### Visual Basic (Usage)

```vb
Dim instance As ISheetMetalFeatureData
Dim value As System.Integer

instance.AutoReliefType = value

value = instance.AutoReliefType
```

### C#

```csharp
System.int AutoReliefType {get; set;}
```

### C++/CLI

```cpp
property System.int AutoReliefType {
   System.int get();
   void set (    System.int value);
}
```

**NOTE:** See [Differences Between Unmanaged C++ and C++/CLI Code](DifferencesBetweenUnManagedAndCPPCLI.htm).

### Property Value

Bend relief type as defined in [swSheetMetalReliefTypes_e](ms-its:swconst.chm::/SOLIDWORKS.Interop.swconst~SOLIDWORKS.Interop.swconst.swSheetMetalReliefTypes_e.html)

## VBA Syntax

See [SheetMetalFeatureData::AutoReliefType](ms-its:sldworksapivb6.chm::/sldworks~SheetMetalFeatureData~AutoReliefType.html).

## See Also

[ISheetMetalFeatureData Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISheetMetalFeatureData.html)
[ISheetMetalFeatureData Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISheetMetalFeatureData_members.html)
[ISheetMetalFeatureData::ReliefRatio Property](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISheetMetalFeatureData~ReliefRatio.html)
[ISheetMetalFeatureData::UseAutoRelief Property](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISheetMetalFeatureData~UseAutoRelief.html)
[IBaseFlangeFeatureData::Initialize Method ()](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IBaseFlangeFeatureData~Initialize.html)

## Availability

SOLIDWORKS 2001 SP1, Revision Number 9.1
