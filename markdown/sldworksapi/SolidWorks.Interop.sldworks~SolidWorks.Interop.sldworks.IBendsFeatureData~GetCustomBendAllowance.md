---
title: "GetCustomBendAllowance Method (IBendsFeatureData)"
project: "SOLIDWORKS API Help"
interface: "IBendsFeatureData"
member: "GetCustomBendAllowance"
kind: "method"
source: "sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IBendsFeatureData~GetCustomBendAllowance.html"
---

# GetCustomBendAllowance Method (IBendsFeatureData)

Gets the custom bend allowance for this Flatten-Bends/Process-Bends feature.

## Syntax

### Visual Basic (Declaration)

```vb
Function GetCustomBendAllowance() As CustomBendAllowance
```

### Visual Basic (Usage)

```vb
Dim instance As IBendsFeatureData
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

[ICustomBendAllowance](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.ICustomBendAllowance.html)

## VBA Syntax

See [BendsFeatureData::GetCustomBendAllowance](ms-its:sldworksapivb6.chm::/sldworks~BendsFeatureData~GetCustomBendAllowance.html).

## Remarks

See [Accessing Selections that Define Features](sldworksAPIProgGuide.chm::/Miscellaneous/Accessing_Selections_that_Define_Features.htm) for additional details on using this method.

## See Also

[IBendsFeatureData Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IBendsFeatureData.html)
[IBendsFeatureData Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IBendsFeatureData_members.html)
[IBendsFeatureData::SetCustomBendAllowance Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IBendsFeatureData~SetCustomBendAllowance.html)
[IBendsFeatureData::UseDefaultBendAllowance Property](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IBendsFeatureData~UseDefaultBendAllowance.html)

## Availability

SOLIDWORKS 2003 FCS, Revision Number 11.0
