---
title: "GetCustomBendAllowance Method (ISheetMetalFeatureData)"
project: "SOLIDWORKS API Help"
interface: "ISheetMetalFeatureData"
member: "GetCustomBendAllowance"
kind: "method"
source: "sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISheetMetalFeatureData~GetCustomBendAllowance.html"
---

# GetCustomBendAllowance Method (ISheetMetalFeatureData)

Gets custom bend allowance for this sheet metal feature.

## Syntax

### Visual Basic (Declaration)

```vb
Function GetCustomBendAllowance() As CustomBendAllowance
```

### Visual Basic (Usage)

```vb
Dim instance As ISheetMetalFeatureData
Dim value As CustomBendAllowance

value = instance.GetCustomBendAllowance()
```

### C#

```csharp
CustomBendAllowance GetCustomBendAllowance()
```

### C++/CLI

```cpp
CustomBendAllowance^ GetCustomBendAllowance();
```

**NOTE:** See [Differences Between Unmanaged C++ and C++/CLI Code](DifferencesBetweenUnManagedAndCPPCLI.htm).

### Return Value

[Custom bend allowance](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.ICustomBendAllowance.html)

## VBA Syntax

See [SheetMetalFeatureData::GetCustomBendAllowance](ms-its:sldworksapivb6.chm::/sldworks~SheetMetalFeatureData~GetCustomBendAllowance.html).

## Examples

See the [ISheetMetalFeatureData](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.ISheetMetalFeatureData.html) examples.

See the [IBaseFlangeFeatureData](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IBaseFlangeFeatureData.html) examples.

## Remarks

See [Accessing Selections that Define Features](sldworksAPIProgGuide.chm::/Miscellaneous/Accessing_Selections_that_Define_Features.htm) for additional details.

## See Also

[ISheetMetalFeatureData Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISheetMetalFeatureData.html)
[ISheetMetalFeatureData Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISheetMetalFeatureData_members.html)
[ISheetMetalFeatureData::SetCustomBendAllowance Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISheetMetalFeatureData~SetCustomBendAllowance.html)

## Availability

SOLIDWORKS 2003 FCS, Revision Number 11.0
