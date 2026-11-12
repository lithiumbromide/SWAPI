---
title: "IsAppliedToAllConfigurations Method (IDimension)"
project: "SOLIDWORKS API Help"
interface: "IDimension"
member: "IsAppliedToAllConfigurations"
kind: "method"
source: "sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IDimension~IsAppliedToAllConfigurations.html"
---

# IsAppliedToAllConfigurations Method (IDimension)

Gets whether a dimension is currently applied to all configurations of the model or to just the current configuration.

## Syntax

### Visual Basic (Declaration)

```vb
Function IsAppliedToAllConfigurations() As System.Boolean
```

### Visual Basic (Usage)

```vb
Dim instance As IDimension
Dim value As System.Boolean

value = instance.IsAppliedToAllConfigurations()
```

### C#

```csharp
System.bool IsAppliedToAllConfigurations()
```

### C++/CLI

```cpp
System.bool IsAppliedToAllConfigurations();
```

**NOTE:** See [Differences Between Unmanaged C++ and C++/CLI Code](DifferencesBetweenUnManagedAndCPPCLI.htm).

### Return Value

True if the dimension is applied to all configurations, false if the dimension is applied only to the current configuration

## VBA Syntax

See [Dimension::IsAppliedToAllConfigurations](ms-its:sldworksapivb6.chm::/sldworks~Dimension~IsAppliedToAllConfigurations.html).

## Examples

[Get Dimension Values in All Configurations (VBA)](Get_Dimension_Values_in_All_Configurations_Example_VB.htm)

## Remarks

If there is only one configuration of a part, this method returns True.

This method applies only to dimensions that are driven by or drive geometry. For example, this method does not apply to reference dimensions (see [IDimension::IsReference](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.IDimension~IsReference.html) and [IDimension::DrivenState](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.IDimension~DrivenState.html)). This method returns True for reference dimensions.

## See Also

[IDimension Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IDimension.html)
[IDimension Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IDimension_members.html)

## Availability

SolidWork s98Plus, datecode 1999005
