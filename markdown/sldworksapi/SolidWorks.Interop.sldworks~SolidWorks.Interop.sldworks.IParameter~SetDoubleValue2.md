---
title: "SetDoubleValue2 Method (IParameter)"
project: "SOLIDWORKS API Help"
interface: "IParameter"
member: "SetDoubleValue2"
kind: "method"
source: "sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IParameter~SetDoubleValue2.html"
---

# SetDoubleValue2 Method (IParameter)

Sets the double or integer value of a named configuration option parameter.

## Syntax

### Visual Basic (Declaration)

```vb
Function SetDoubleValue2( _
   ByVal Value As System.Double, _
   ByVal ConfigurationOption As System.Integer, _
   ByVal ConfigurationName As System.String _
) As System.Boolean
```

### Visual Basic (Usage)

```vb
Dim instance As IParameter
Dim Value As System.Double
Dim ConfigurationOption As System.Integer
Dim ConfigurationName As System.String
Dim value As System.Boolean

value = instance.SetDoubleValue2(Value, ConfigurationOption, ConfigurationName)
```

### C#

```csharp
System.bool SetDoubleValue2(
   System.double Value,
   System.int ConfigurationOption,
   System.string ConfigurationName
)
```

### C++/CLI

```cpp
System.bool SetDoubleValue2(
   System.double Value,
   System.int ConfigurationOption,
   System.String^ ConfigurationName
)
```

**NOTE:** See [Differences Between Unmanaged C++ and C++/CLI Code](DifferencesBetweenUnManagedAndCPPCLI.htm).

### Parameters

- `Value`: Value to store for the named configuration option
- `ConfigurationOption`: Configuration option as defined in [swSetValueInConfiguration_e](ms-its:swconst.chm::/SOLIDWORKS.Interop.swconst~SOLIDWORKS.Interop.swconst.swSetValueInConfiguration_e.html)
- `ConfigurationName`: Name of the configuration

### Return Value

True if successful, false if not

## VBA Syntax

See [Parameter::SetDoubleValue2](ms-its:sldworksapivb6.chm::/sldworks~Parameter~SetDoubleValue2.html).

## Examples

[Create Attribute (VBA)](Create_Attribute_Example_VB.htm)
[Delete Attribute (C#)](Delete_Attribute_Example_CSharp.htm)
[Delete Attribute (VB.NET)](Delete_Attribute_Example_VBNET.htm)
[Delete Attribute (VBA)](Delete_Attribute_Example_VB.htm)

## Remarks

The ConfigurationName argument is:

- Not required if ConfigurationOption is set to swSetValue_InThisConfiguration = 1 or swSetValue_InAllConfigurations = 2.
- Required if ConfigurationOption is set to swSetValue_InSpecificConfigurations = 3.

Set ConfigurationOption to swSetValue_InAllConfigurations = 2 for drawing documents because they do not have configurations.

## See Also

[IParameter Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IParameter.html)
[IParameter Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IParameter_members.html)
[IParameter::GetDoubleValue Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IParameter~GetDoubleValue.html)

## Availability

SOLIDWORKS 2001 FCS, Revision Number 9.0
