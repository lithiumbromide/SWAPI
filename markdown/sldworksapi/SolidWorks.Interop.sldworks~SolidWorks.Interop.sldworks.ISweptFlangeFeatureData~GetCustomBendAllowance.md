---
title: "GetCustomBendAllowance Method (ISweptFlangeFeatureData)"
project: "SOLIDWORKS API Help"
interface: "ISweptFlangeFeatureData"
member: "GetCustomBendAllowance"
kind: "method"
source: "sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISweptFlangeFeatureData~GetCustomBendAllowance.html"
---

# GetCustomBendAllowance Method (ISweptFlangeFeatureData)

Gets the custom bend allowance object.

## Syntax

### Visual Basic (Declaration)

```vb
Function GetCustomBendAllowance() As System.Object
```

### Visual Basic (Usage)

```vb
Dim instance As ISweptFlangeFeatureData
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

[ICustomBendAllowance](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ICustomBendAllowance.html)

## VBA Syntax

See [SweptFlangeFeatureData::GetCustomBendAllowance](ms-its:sldworksapivb6.chm::/sldworks~SweptFlangeFeatureData~GetCustomBendAllowance.html).

## Remarks

This method is valid only if [ISweptFlangeFeatureData::UseDefaultBendAllowance](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISweptFlangeFeatureData~UseDefaultBendAllowance.html) is false.

## See Also

[ISweptFlangeFeatureData Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISweptFlangeFeatureData.html)
[ISweptFlangeFeatureData Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISweptFlangeFeatureData_members.html)
[ISweptFlangeFeatureData::SetCustomBendAllowance Method ()](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISweptFlangeFeatureData~SetCustomBendAllowance.html)

## Availability

SOLIDWORKS 2021 FCS, Revision Number 29
