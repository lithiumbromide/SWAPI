---
title: "AngleOverride Property (ICountersinkElementData)"
project: "SOLIDWORKS API Help"
interface: "ICountersinkElementData"
member: "AngleOverride"
kind: "property"
source: "sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ICountersinkElementData~AngleOverride.html"
---

# AngleOverride Property (ICountersinkElementData)

Gets or sets whether to override the angle of this countersink hole element.

## Syntax

### Visual Basic (Declaration)

```vb
Property AngleOverride As System.Boolean
```

### Visual Basic (Usage)

```vb
Dim instance As ICountersinkElementData
Dim value As System.Boolean

instance.AngleOverride = value

value = instance.AngleOverride
```

### C#

```csharp
System.bool AngleOverride {get; set;}
```

### C++/CLI

```cpp
property System.bool AngleOverride {
   System.bool get();
   void set (    System.bool value);
}
```

**NOTE:** See [Differences Between Unmanaged C++ and C++/CLI Code](DifferencesBetweenUnManagedAndCPPCLI.htm).

### Property Value

True to override the angle, false to not

## VBA Syntax

See [CountersinkElementData::AngleOverride](ms-its:sldworksapivb6.chm::/sldworks~CountersinkElementData~AngleOverride.html).

## Examples

See the [ICountersinkElementData](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ICountersinkElementData.html) examples.

## See Also

[ICountersinkElementData Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ICountersinkElementData.html)
[ICountersinkElementData Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ICountersinkElementData_members.html)
[ICountersinkElementData::Angle Property ()](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ICountersinkElementData~Angle.html)

## Availability

SOLIDWORKS 2018 FCS, Revision Number 26.0
