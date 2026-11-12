---
title: "GetCustomBendAllowance Method (IJogFeatureData)"
project: "SOLIDWORKS API Help"
interface: "IJogFeatureData"
member: "GetCustomBendAllowance"
kind: "method"
source: "sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IJogFeatureData~GetCustomBendAllowance.html"
---

# GetCustomBendAllowance Method (IJogFeatureData)

Gets the custom bend allowance for this jog feature.

## Syntax

### Visual Basic (Declaration)

```vb
Function GetCustomBendAllowance() As CustomBendAllowance
```

### Visual Basic (Usage)

```vb
Dim instance As IJogFeatureData
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

Pointer to the [custom gend allowance](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.ICustomBendAllowance.html)

## VBA Syntax

See [JogFeatureData::GetCustomBendAllowance](ms-its:sldworksapivb6.chm::/sldworks~JogFeatureData~GetCustomBendAllowance.html).

## Examples

See [IJogFeatureData](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.IJogFeatureData.html) examples.

## Remarks

See [Accessing Selections that Define Features](sldworksAPIProgGuide.chm::/Miscellaneous/Accessing_Selections_that_Define_Features.htm) for additional details on using this method.

## See Also

[IJogFeatureData Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IJogFeatureData.html)
[IJogFeatureData Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IJogFeatureData_members.html)
[IJogFeatureData::SetCustomBendAllowance Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IJogFeatureData~SetCustomBendAllowance.html)
[IJogFeatureData::UseDefaultBendAllowance Property](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IJogFeatureData~UseDefaultBendAllowance.html)

## Availability

SOLIDWORKS 2003 FCS, Revision Number 11.0
