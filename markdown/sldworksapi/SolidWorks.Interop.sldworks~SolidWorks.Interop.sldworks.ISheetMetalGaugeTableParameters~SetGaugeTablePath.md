---
title: "SetGaugeTablePath Method (ISheetMetalGaugeTableParameters)"
project: "SOLIDWORKS API Help"
interface: "ISheetMetalGaugeTableParameters"
member: "SetGaugeTablePath"
kind: "method"
source: "sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISheetMetalGaugeTableParameters~SetGaugeTablePath.html"
---

# SetGaugeTablePath Method (ISheetMetalGaugeTableParameters)

Sets the full path name of this gauge table.

## Syntax

### Visual Basic (Declaration)

```vb
Function SetGaugeTablePath( _
   ByVal GaugeTablePath As System.String _
) As System.Boolean
```

### Visual Basic (Usage)

```vb
Dim instance As ISheetMetalGaugeTableParameters
Dim GaugeTablePath As System.String
Dim value As System.Boolean

value = instance.SetGaugeTablePath(GaugeTablePath)
```

### C#

```csharp
System.bool SetGaugeTablePath(
   System.string GaugeTablePath
)
```

### C++/CLI

```cpp
System.bool SetGaugeTablePath(
   System.String^ GaugeTablePath
)
```

**NOTE:** See [Differences Between Unmanaged C++ and C++/CLI Code](DifferencesBetweenUnManagedAndCPPCLI.htm).

### Parameters

- `GaugeTablePath`: Full path name

### Return Value

True if gauge table path successfully set, false if not

## VBA Syntax

See [SheetMetalGaugeTableParameters::SetGaugeTablePath](ms-its:sldworksapivb6.chm::/sldworks~SheetMetalGaugeTableParameters~SetGaugeTablePath.html).

## Examples

See the [ISheetMetalGaugeTableParameters](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISheetMetalGaugeTableParameters.html) examples.

## Remarks

Installed sheet metal gauge tables are located in `install_dir`**\lang\english\Sheet Metal Gauge Tables**.

## See Also

[ISheetMetalGaugeTableParameters Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISheetMetalGaugeTableParameters.html)
[ISheetMetalGaugeTableParameters Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISheetMetalGaugeTableParameters_members.html)
[ISheetMetalGaugeTableParameters::GetGaugeTablePath Method ()](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISheetMetalGaugeTableParameters~GetGaugeTablePath.html)

## Availability

SOLIDWORKS 2021 FCS, Revision Number 29
