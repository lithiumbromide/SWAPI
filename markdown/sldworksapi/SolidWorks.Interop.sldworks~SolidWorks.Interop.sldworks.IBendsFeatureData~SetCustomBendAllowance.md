---
title: "SetCustomBendAllowance Method (IBendsFeatureData)"
project: "SOLIDWORKS API Help"
interface: "IBendsFeatureData"
member: "SetCustomBendAllowance"
kind: "method"
source: "sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IBendsFeatureData~SetCustomBendAllowance.html"
---

# SetCustomBendAllowance Method (IBendsFeatureData)

Sets the custom bend allowance for the Flatten-Bends/Process-Bends feature.

## Syntax

### Visual Basic (Declaration)

```vb
Sub SetCustomBendAllowance( _
   ByVal PBendData As CustomBendAllowance _
)
```

### Visual Basic (Usage)

```vb
Dim instance As IBendsFeatureData
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

- `PBendData`: [ICustomBendAllowance](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.ICustomBendAllowance.html)

## VBA Syntax

See [BendsFeatureData::SetCustomBendAllowance](ms-its:sldworksapivb6.chm::/sldworks~BendsFeatureData~SetCustomBendAllowance.html).

## Remarks

See [Accessing Selections that Define Features](sldworksAPIProgGuide.chm::/Miscellaneous/Accessing_Selections_that_Define_Features.htm) for additional details on using this method.

## See Also

[IBendsFeatureData Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IBendsFeatureData.html)
[IBendsFeatureData Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IBendsFeatureData_members.html)
[IBendsFeatureData::GetCustomBendAllowance Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IBendsFeatureData~GetCustomBendAllowance.html)
[IBendsFeatureData::UseDefaultBendAllowance Property](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IBendsFeatureData~UseDefaultBendAllowance.html)

## Availability

SOLIDWORKS 2003 FCS, Revision Number 11.0
