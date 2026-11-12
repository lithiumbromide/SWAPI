---
title: "UseDefaultBendAllowance Property (IBendsFeatureData)"
project: "SOLIDWORKS API Help"
interface: "IBendsFeatureData"
member: "UseDefaultBendAllowance"
kind: "property"
source: "sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IBendsFeatureData~UseDefaultBendAllowance.html"
---

# UseDefaultBendAllowance Property (IBendsFeatureData)

Gets or sets whether to use the default bend allowance for this Flatten-Bends/Process-Bends feature.

## Syntax

### Visual Basic (Declaration)

```vb
Property UseDefaultBendAllowance As System.Boolean
```

### Visual Basic (Usage)

```vb
Dim instance As IBendsFeatureData
Dim value As System.Boolean

instance.UseDefaultBendAllowance = value

value = instance.UseDefaultBendAllowance
```

### C#

```csharp
System.bool UseDefaultBendAllowance {get; set;}
```

### C++/CLI

```cpp
property System.bool UseDefaultBendAllowance {
   System.bool get();
   void set (    System.bool value);
}
```

**NOTE:** See [Differences Between Unmanaged C++ and C++/CLI Code](DifferencesBetweenUnManagedAndCPPCLI.htm).

### Property Value

True to use the default bend allowance, false to not

## VBA Syntax

See [BendsFeatureData::UseDefaultBendAllowance](ms-its:sldworksapivb6.chm::/sldworks~BendsFeatureData~UseDefaultBendAllowance.html).

## Examples

[Get All Sheet Metal Feature Data (VBA)](Get_All_Sheet_Metal_Feature_Data_Example_VB.htm)
[Get All Sheet Metal Feature Data (VB.NET)](Get_All_Sheet_Metal_Feature_Data_Example_VBNET.htm)
[Get All Sheet Metal Feature Data (C#)](Get_All_Sheet_Metal_Feature_Data_Example_CSharp.htm)

## See Also

[IBendsFeatureData Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IBendsFeatureData.html)
[IBendsFeatureData Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IBendsFeatureData_members.html)
[IBendsFeatureData::GetCustomBendAllowance Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IBendsFeatureData~GetCustomBendAllowance.html)
[IBendsFeatureData::SetCustomBendAllowance Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IBendsFeatureData~SetCustomBendAllowance.html)

## Availability

SOLIDWORKS 2001 SP1, Revision Number 9.1
