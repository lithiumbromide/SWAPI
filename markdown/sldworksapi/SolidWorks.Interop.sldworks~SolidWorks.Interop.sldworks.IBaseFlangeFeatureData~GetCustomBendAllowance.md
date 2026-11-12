---
title: "GetCustomBendAllowance Method (IBaseFlangeFeatureData)"
project: "SOLIDWORKS API Help"
interface: "IBaseFlangeFeatureData"
member: "GetCustomBendAllowance"
kind: "method"
source: "sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IBaseFlangeFeatureData~GetCustomBendAllowance.html"
---

# GetCustomBendAllowance Method (IBaseFlangeFeatureData)

Gets the custom bend allowance object associated with this sheet metal base flange feature.

## Syntax

### Visual Basic (Declaration)

```vb
Function GetCustomBendAllowance() As System.Object
```

### Visual Basic (Usage)

```vb
Dim instance As IBaseFlangeFeatureData
Dim value As System.Object

value = instance.GetCustomBendAllowance()
```

### C#

```csharp
System.object GetCustomBendAllowance()
```

### C++/CLI

```cpp
System.Object^ GetCustomBendAllowance();
```

**NOTE:** See [Differences Between Unmanaged C++ and C++/CLI Code](DifferencesBetweenUnManagedAndCPPCLI.htm).

### Return Value

[Custom bend allowance](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.ICustomBendAllowance.html)

## VBA Syntax

See [BaseFlangeFeatureData::GetCustomBendAllowance](ms-its:sldworksapivb6.chm::/sldworks~BaseFlangeFeatureData~GetCustomBendAllowance.html).

## Examples

See the [IBaseFlangeFeatureData](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IBaseFlangeFeatureData.html) examples.

## Remarks

This method is valid only if [IBaseFlangeFeatureData::UseDefaultBendAllowance](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IBaseFlangeFeatureData~UseDefaultBendAllowance.html) is false.

You can change the custom bend allowance after it has been [initialized](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IBaseFlangeFeatureData~Initialize.html). Access the parent sheet metal to do so. See the Examples.

See [Accessing Selections that Define Features](sldworksAPIProgGuide.chm::/Miscellaneous/Accessing_Selections_that_Define_Features.htm) for additional details.

## See Also

[IBaseFlangeFeatureData Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IBaseFlangeFeatureData.html)
[IBaseFlangeFeatureData Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IBaseFlangeFeatureData_members.html)

## Availability

SOLIDWORKS 2022 FCS, Revision Number 30
