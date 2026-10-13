---
title: "Angle Property (ICountersinkElementData)"
project: "SOLIDWORKS API Help"
interface: "ICountersinkElementData"
member: "Angle"
kind: "property"
source: "sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ICountersinkElementData~Angle.html"
---

# Angle Property (ICountersinkElementData)

Gets or sets the angle of this countersink hole element.

## Syntax

### Visual Basic (Declaration)

```vb
Property Angle As System.Double
```

### Visual Basic (Usage)

```vb
Dim instance As ICountersinkElementData
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

See [CountersinkElementData::Angle](ms-its:sldworksapivb6.chm::/sldworks~CountersinkElementData~Angle.html).

## Remarks

This property is valid only if [ICountersinkElementData::AngleOverride](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ICountersinkElementData~AngleOverride.html) is set to true.

## See Also

[ICountersinkElementData Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ICountersinkElementData.html)
[ICountersinkElementData Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ICountersinkElementData_members.html)

## Availability

SOLIDWORKS 2018 FCS, Revision Number 26.0
