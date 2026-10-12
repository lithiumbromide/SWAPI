---
title: "SetZoneMargin Method (ISheet)"
project: "SOLIDWORKS API Help"
interface: "ISheet"
member: "SetZoneMargin"
kind: "method"
source: "sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISheet~SetZoneMargin.html"
---

# SetZoneMargin Method (ISheet)

Sets the specified zone margin.

## Syntax

### Visual Basic (Declaration)

```vb
Function SetZoneMargin( _
   ByVal ZoneMarginType As System.Integer, _
   ByVal MarginValue As System.Double _
) As System.Boolean
```

### Visual Basic (Usage)

```vb
Dim instance As ISheet
Dim ZoneMarginType As System.Integer
Dim MarginValue As System.Double
Dim value As System.Boolean

value = instance.SetZoneMargin(ZoneMarginType, MarginValue)
```

### C#

```csharp
System.bool SetZoneMargin(
   System.int ZoneMarginType,
   System.double MarginValue
)
```

### C++/CLI

```cpp
System.bool SetZoneMargin(
   System.int ZoneMarginType,
   System.double MarginValue
)
```

**NOTE:** See [Differences Between Unmanaged C++ and C++/CLI Code](DifferencesBetweenUnManagedAndCPPCLI.htm).

### Parameters

- `ZoneMarginType`: Margin type as defined in [swZoneMargin_e](ms-its:swconst.chm::/SolidWorks.Interop.swconst~SolidWorks.Interop.swconst.swZoneMargin_e.html)
- `MarginValue`: Margin

### Return Value

True if zone margin successfully set, false if not

## VBA Syntax

See [Sheet::SetZoneMargin](ms-its:sldworksapivb6.chm::/Sldworks~Sheet~SetZoneMargin.html).

## See Also

[ISheet Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISheet.html)
[ISheet Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISheet_members.html)

## Availability

SOLIDWORKS 2022 FCS, Revision Number 30
