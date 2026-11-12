---
title: "SetCustomBendAllowance Method (IJogFeatureData)"
project: "SOLIDWORKS API Help"
interface: "IJogFeatureData"
member: "SetCustomBendAllowance"
kind: "method"
source: "sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IJogFeatureData~SetCustomBendAllowance.html"
---

# SetCustomBendAllowance Method (IJogFeatureData)

Sets the custom bend allowance for this jog feature.

## Syntax

### Visual Basic (Declaration)

```vb
Sub SetCustomBendAllowance( _
   ByVal PBendData As CustomBendAllowance _
)
```

### Visual Basic (Usage)

```vb
Dim instance As IJogFeatureData
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

- `PBendData`: Pointer to the [custom bend allowance](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.ICustomBendAllowance.html)

## VBA Syntax

See [JogFeatureData::SetCustomBendAllowance](ms-its:sldworksapivb6.chm::/sldworks~JogFeatureData~SetCustomBendAllowance.html).

## Remarks

See [Accessing Selections that Define Features](sldworksAPIProgGuide.chm::/Miscellaneous/Accessing_Selections_that_Define_Features.htm) for additional details on using this method.

## See Also

[IJogFeatureData Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IJogFeatureData.html)
[IJogFeatureData Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IJogFeatureData_members.html)
[IJogFeatureData::GetCustomBendAllowance Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IJogFeatureData~GetCustomBendAllowance.html)
[IJogFeatureData::UseDefaultBendAllowance Property](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IJogFeatureData~UseDefaultBendAllowance.html)

## Availability

SOLIDWORKS 2003 FCS, Revision Number 11.0
