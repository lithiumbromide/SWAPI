---
title: "UseDefaultBendAllowance Property (IHemFeatureData)"
project: "SOLIDWORKS API Help"
interface: "IHemFeatureData"
member: "UseDefaultBendAllowance"
kind: "property"
source: "sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IHemFeatureData~UseDefaultBendAllowance.html"
---

# UseDefaultBendAllowance Property (IHemFeatureData)

Gets or sets whether to use the default bend allowance state for this hem feature.

## Syntax

### Visual Basic (Declaration)

```vb
Property UseDefaultBendAllowance As System.Boolean
```

### Visual Basic (Usage)

```vb
Dim instance As IHemFeatureData
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

True uses the default bend allowance, false does not

## VBA Syntax

See [HemFeatureData::UseDefaultBendAllowance](ms-its:sldworksapivb6.chm::/sldworks~HemFeatureData~UseDefaultBendAllowance.html).

## See Also

[IHemFeatureData Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IHemFeatureData.html)
[IHemFeatureData Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IHemFeatureData_members.html)
[IHemFeatureData::GetCustomBendAllowance Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IHemFeatureData~GetCustomBendAllowance.html)
[IHemFeatureData::SetCustomBendAllowance Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IHemFeatureData~SetCustomBendAllowance.html)

## Availability

SOLIDWORKS 2003 FCS, Revision Number 11.0
