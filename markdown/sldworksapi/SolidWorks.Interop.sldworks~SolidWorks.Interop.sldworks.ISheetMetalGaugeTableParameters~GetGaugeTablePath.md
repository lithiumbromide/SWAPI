---
title: "GetGaugeTablePath Method (ISheetMetalGaugeTableParameters)"
project: "SOLIDWORKS API Help"
interface: "ISheetMetalGaugeTableParameters"
member: "GetGaugeTablePath"
kind: "method"
source: "sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISheetMetalGaugeTableParameters~GetGaugeTablePath.html"
---

# GetGaugeTablePath Method (ISheetMetalGaugeTableParameters)

Gets the full path name of this gauge table.

## Syntax

### Visual Basic (Declaration)

```vb
Function GetGaugeTablePath( _
   ByRef GaugeTablePath As System.String _
) As System.Boolean
```

### Visual Basic (Usage)

```vb
Dim instance As ISheetMetalGaugeTableParameters
Dim GaugeTablePath As System.String
Dim value As System.Boolean

value = instance.GetGaugeTablePath(GaugeTablePath)
```

### C#

```csharp
System.bool GetGaugeTablePath(
   out System.string GaugeTablePath
)
```

### C++/CLI

```cpp
System.bool GetGaugeTablePath(
   [Out] System.String^ GaugeTablePath
)
```

**NOTE:** See [Differences Between Unmanaged C++ and C++/CLI Code](DifferencesBetweenUnManagedAndCPPCLI.htm).

### Parameters

- `GaugeTablePath`: Full path name of the gauge table

### Return Value

True if gauge table path successfully retrieved, false if not

## VBA Syntax

See [SheetMetalGaugeTableParameters::GetGaugeTablePath](ms-its:sldworksapivb6.chm::/sldworks~SheetMetalGaugeTableParameters~GetGaugeTablePath.html).

## Examples

See the [ISheetMetalGaugeTableParameters](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISheetMetalGaugeTableParameters.html) examples.

## See Also

[ISheetMetalGaugeTableParameters Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISheetMetalGaugeTableParameters.html)
[ISheetMetalGaugeTableParameters Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISheetMetalGaugeTableParameters_members.html)
[ISheetMetalGaugeTableParameters::SetGaugeTablePath Method ()](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISheetMetalGaugeTableParameters~SetGaugeTablePath.html)

## Availability

SOLIDWORKS 2021 FCS, Revision Number 29
