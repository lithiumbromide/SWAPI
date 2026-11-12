---
title: "SetCustomBendAllowance Method (ISheetMetalFeatureData)"
project: "SOLIDWORKS API Help"
interface: "ISheetMetalFeatureData"
member: "SetCustomBendAllowance"
kind: "method"
source: "sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISheetMetalFeatureData~SetCustomBendAllowance.html"
---

# SetCustomBendAllowance Method (ISheetMetalFeatureData)

Sets the custom bend allowance for this sheet metal feature.

## Syntax

### Visual Basic (Declaration)

```vb
Sub SetCustomBendAllowance( _
   ByVal PBendData As CustomBendAllowance _
)
```

### Visual Basic (Usage)

```vb
Dim instance As ISheetMetalFeatureData
Dim PBendData As CustomBendAllowance

instance.SetCustomBendAllowance(PBendData)
```

### C#

```csharp
void SetCustomBendAllowance(
   CustomBendAllowance PBendData
)
```

### C++/CLI

```cpp
void SetCustomBendAllowance(
   CustomBendAllowance^ PBendData
)
```

**NOTE:** See [Differences Between Unmanaged C++ and C++/CLI Code](DifferencesBetweenUnManagedAndCPPCLI.htm).

### Parameters

- `PBendData`: [Custom bend allowance](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.ICustomBendAllowance.html)

## VBA Syntax

See [SheetMetalFeatureData::SetCustomBendAllowance](ms-its:sldworksapivb6.chm::/sldworks~SheetMetalFeatureData~SetCustomBendAllowance.html).

## Remarks

See [Accessing Selections that Define Features](sldworksAPIProgGuide.chm::/Miscellaneous/Accessing_Selections_that_Define_Features.htm) for additional details.

## See Also

[ISheetMetalFeatureData Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISheetMetalFeatureData.html)
[ISheetMetalFeatureData Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISheetMetalFeatureData_members.html)
[ISheetMetalFeatureData::GetCustomBendAllowance Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISheetMetalFeatureData~GetCustomBendAllowance.html)
[IBaseFlangeFeatureData::Initialize Method ()](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IBaseFlangeFeatureData~Initialize.html)

## Availability

SOLIDWORKS 2003 FCS, Revision Number 11.0
