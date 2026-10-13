---
title: "SetStringValue2 Method (IParameter)"
project: "SOLIDWORKS API Help"
interface: "IParameter"
member: "SetStringValue2"
kind: "method"
source: "sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IParameter~SetStringValue2.html"
---

# SetStringValue2 Method (IParameter)

Sets the double or integer value of a named configuration option parameter.

## Syntax

### Visual Basic (Declaration)

```vb
Function SetStringValue2( _
   ByVal StringValue As System.String, _
   ByVal ConfigurationOption As System.Integer, _
   ByVal ConfigurationName As System.String _
) As System.Boolean
```

### Visual Basic (Usage)

```vb
Dim instance As IParameter
Dim StringValue As System.String
Dim ConfigurationOption As System.Integer
Dim ConfigurationName As System.String
Dim value As System.Boolean

value = instance.SetStringValue2(StringValue, ConfigurationOption, ConfigurationName)
```

### C#

```csharp
System.bool SetStringValue2(
   System.string StringValue,
   System.int ConfigurationOption,
   System.string ConfigurationName
)
```

### C++/CLI

```cpp
System.bool SetStringValue2(
   System.String^ StringValue,
   System.int ConfigurationOption,
   System.String^ ConfigurationName
)
```

**NOTE:** See [Differences Between Unmanaged C++ and C++/CLI Code](DifferencesBetweenUnManagedAndCPPCLI.htm).

### Parameters

- `StringValue`: Value to store for the named configuration option
- `ConfigurationOption`: Configuration option as defined in [swInConfigurationOpts_e](ms-its:swconst.chm::/SOLIDWORKS.Interop.swconst~SOLIDWORKS.Interop.swconst.swInConfigurationOpts_e.html)
- `ConfigurationName`: Name of the configuration

### Return Value

True if successful, false if not

## VBA Syntax

See [Parameter::SetStringValue2](ms-its:sldworksapivb6.chm::/sldworks~Parameter~SetStringValue2.html).

## Examples

[Create Attribute (VBA)](Create_Attribute_Example_VB.htm)
[Delete Attribute (C#)](Delete_Attribute_Example_CSharp.htm)
[Delete Attribute (VB.NET)](Delete_Attribute_Example_VBNET.htm)
[Delete Attribute (VBA)](Delete_Attribute_Example_VB.htm)

## Remarks

The ConfigurationName argument is:

- Not required if ConfigurationOption is set to swThisConfiguration = 1 or swAllConfiguration = 2.
- Required if ConfigurationOption is set to swSpecifyConfiguration =3 .

Set ConfigurationOption to swAllConfiguration = 2 for drawing documents because they do not have configurations.

## See Also

[IParameter Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IParameter.html)
[IParameter Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IParameter_members.html)
[IParameter::GetStringValue Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IParameter~GetStringValue.html)

## Availability

SOLIDWORKS 2001 FCS, Revision Number 9.0
