---
title: "UseDefaultBendAllowance Property (IOneBendFeatureData)"
project: "SOLIDWORKS API Help"
interface: "IOneBendFeatureData"
member: "UseDefaultBendAllowance"
kind: "property"
source: "sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IOneBendFeatureData~UseDefaultBendAllowance.html"
---

# UseDefaultBendAllowance Property (IOneBendFeatureData)

Gets or sets whether to use the default bend allowance for this bend.

## Syntax

### Visual Basic (Declaration)

```vb
Property UseDefaultBendAllowance As System.Boolean
```

### Visual Basic (Usage)

```vb
Dim instance As IOneBendFeatureData
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

See [OneBendFeatureData::UseDefaultBendAllowance](ms-its:sldworksapivb6.chm::/sldworks~OneBendFeatureData~UseDefaultBendAllowance.html).

## Examples

[Get All Sheet Metal Feature Data (VBA)](Get_All_Sheet_Metal_Feature_Data_Example_VB.htm)
[Get All Sheet Metal Feature Data (VB.NET)](Get_All_Sheet_Metal_Feature_Data_Example_VBNET.htm)
[Get All Sheet Metal Feature Data (C#)](Get_All_Sheet_Metal_Feature_Data_Example_CSharp.htm)

## See Also

[IOneBendFeatureData Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IOneBendFeatureData.html)
[IOneBendFeatureData Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IOneBendFeatureData_members.html)
[IOneBendFeatureData::GetCustomBendAllowance Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IOneBendFeatureData~GetCustomBendAllowance.html)
[IOneBendFeatureData::SetCustomBendAllowance Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IOneBendFeatureData~SetCustomBendAllowance.html)
[IOneBendFeatureData::BendAngle Property](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IOneBendFeatureData~BendAngle.html)
[IOneBendFeatureData::BendDown Property](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IOneBendFeatureData~BendDown.html)
[IOneBendFeatureData::BendOrder Property](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IOneBendFeatureData~BendOrder.html)
[IOneBendFeatureData::UseDefaultBendRadius Property](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IOneBendFeatureData~UseDefaultBendRadius.html)
[IOneBendFeatureData::BendRadius Property](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IOneBendFeatureData~BendRadius.html)

## Availability

SOLIDWORKS 2001 SP1, Revision Number 9.1
