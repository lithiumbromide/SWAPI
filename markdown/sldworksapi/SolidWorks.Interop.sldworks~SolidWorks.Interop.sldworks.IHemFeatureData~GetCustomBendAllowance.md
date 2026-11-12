---
title: "GetCustomBendAllowance Method (IHemFeatureData)"
project: "SOLIDWORKS API Help"
interface: "IHemFeatureData"
member: "GetCustomBendAllowance"
kind: "method"
source: "sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IHemFeatureData~GetCustomBendAllowance.html"
---

# GetCustomBendAllowance Method (IHemFeatureData)

Gets the custom bend allowance for the hem feature.

## Syntax

### Visual Basic (Declaration)

```vb
Function GetCustomBendAllowance() As CustomBendAllowance
```

### Visual Basic (Usage)

```vb
Dim instance As IHemFeatureData
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

[Custom bend allowance](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.ICustomBendAllowance.html) for the hem feature

## VBA Syntax

See [HemFeatureData::GetCustomBendAllowance](ms-its:sldworksapivb6.chm::/sldworks~HemFeatureData~GetCustomBendAllowance.html).

## Examples

[Get All Sheet Metal Feature Data (VBA)](Get_All_Sheet_Metal_Feature_Data_Example_VB.htm)
[Get All Sheet Metal Feature Data (VB.NET)](Get_All_Sheet_Metal_Feature_Data_Example_VBNET.htm)
[Get All Sheet Metal Feature Data (C#)](Get_All_Sheet_Metal_Feature_Data_Example_CSharp.htm)

## Remarks

See [Accessing Selections that Define Features](sldworksAPIProgGuide.chm::/Miscellaneous/Accessing_Selections_that_Define_Features.htm) for additional details on using this method.

## See Also

[IHemFeatureData Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IHemFeatureData.html)
[IHemFeatureData Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IHemFeatureData_members.html)
[IHemFeatureData::SetCustomBendAllowance Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IHemFeatureData~SetCustomBendAllowance.html)
[IHemFeatureData::UseDefaultBendAllowance Property](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IHemFeatureData~UseDefaultBendAllowance.html)

## Availability

SOLIDWORKS 2003 FCS, Revision Number 11.0
