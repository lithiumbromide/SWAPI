---
title: "GetAvailableGaugeNumbers Method (ISheetMetalGaugeTableParameters)"
project: "SOLIDWORKS API Help"
interface: "ISheetMetalGaugeTableParameters"
member: "GetAvailableGaugeNumbers"
kind: "method"
source: "sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISheetMetalGaugeTableParameters~GetAvailableGaugeNumbers.html"
---

# GetAvailableGaugeNumbers Method (ISheetMetalGaugeTableParameters)

Gets the available gauge numbers in this gauge table.

## Syntax

### Visual Basic (Declaration)

```vb
Function GetAvailableGaugeNumbers() As System.Object
```

### Visual Basic (Usage)

```vb
Dim instance As ISheetMetalGaugeTableParameters
Dim value As System.Object

value = instance.GetAvailableGaugeNumbers()
```

### C#

```csharp
System.object GetAvailableGaugeNumbers()
```

### C++/CLI

```cpp
System.Object^ GetAvailableGaugeNumbers();
```

**NOTE:** See [Differences Between Unmanaged C++ and C++/CLI Code](DifferencesBetweenUnManagedAndCPPCLI.htm).

### Return Value

Array of gauge number name strings

## VBA Syntax

See [SheetMetalGaugeTableParameters::GetAvailableGaugeNumbers](ms-its:sldworksapivb6.chm::/sldworks~SheetMetalGaugeTableParameters~GetAvailableGaugeNumbers.html).

## Examples

See the [ISheetMetalGaugeTableParameters](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISheetMetalGaugeTableParameters.html) examples.

## See Also

[ISheetMetalGaugeTableParameters Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISheetMetalGaugeTableParameters.html)
[ISheetMetalGaugeTableParameters Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISheetMetalGaugeTableParameters_members.html)
[ISheetMetalGaugeTableParameters::GetCurrentGaugeNumber Method ()](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISheetMetalGaugeTableParameters~GetCurrentGaugeNumber.html)
[ISheetMetalGaugeTableParameters::GetGaugeNumberCount Method ()](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISheetMetalGaugeTableParameters~GetGaugeNumberCount.html)
[ISheetMetalGaugeTableParameters::SetCurrentGaugeNumber Method ()](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISheetMetalGaugeTableParameters~SetCurrentGaugeNumber.html)
[ISheetMetalGaugeTableParameters::SetThickness Method ()](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISheetMetalGaugeTableParameters~SetThickness.html)

## Availability

SOLIDWORKS 2021 FCS, Revision Number 29
