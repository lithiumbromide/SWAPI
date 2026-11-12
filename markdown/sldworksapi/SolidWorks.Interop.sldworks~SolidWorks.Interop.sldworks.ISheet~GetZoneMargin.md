---
title: "GetZoneMargin Method (ISheet)"
project: "SOLIDWORKS API Help"
interface: "ISheet"
member: "GetZoneMargin"
kind: "method"
source: "sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISheet~GetZoneMargin.html"
---

# GetZoneMargin Method (ISheet)

Gets the specified zone margin.

## Syntax

### Visual Basic (Declaration)

```vb
Function GetZoneMargin( _
   ByVal ZoneMargin As System.Integer _
) As System.Double
```

### Visual Basic (Usage)

```vb
Dim instance As ISheet
Dim ZoneMargin As System.Integer
Dim value As System.Double

value = instance.GetZoneMargin(ZoneMargin)
```

### C#

```csharp
System.double GetZoneMargin(
   System.int ZoneMargin
)
```

### C++/CLI

```cpp
System.double GetZoneMargin(
   System.int ZoneMargin
)
```

**NOTE:** See [Differences Between Unmanaged C++ and C++/CLI Code](DifferencesBetweenUnManagedAndCPPCLI.htm).

### Parameters

- `ZoneMargin`: Margin type to retrieve as defined in [swZoneMargin_e](ms-its:swconst.chm::/SolidWorks.Interop.swconst~SolidWorks.Interop.swconst.swZoneMargin_e.html)

### Return Value

Zone margin

## VBA Syntax

See [Sheet::GetZoneMargin](ms-its:sldworksapivb6.chm::/Sldworks~Sheet~GetZoneMargin.html).

## See Also

[ISheet Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISheet.html)
[ISheet Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISheet_members.html)

## Availability

SOLIDWORKS 2022 FCS, Revision Number 30
