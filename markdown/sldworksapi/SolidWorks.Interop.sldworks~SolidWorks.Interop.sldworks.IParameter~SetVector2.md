---
title: "SetVector2 Method (IParameter)"
project: "SOLIDWORKS API Help"
interface: "IParameter"
member: "SetVector2"
kind: "method"
source: "sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IParameter~SetVector2.html"
---

# SetVector2 Method (IParameter)

Sets the vector values of a named configuration option parameter.

## Syntax

### Visual Basic (Declaration)

```vb
Function SetVector2( _
   ByVal X As System.Double, _
   ByVal Y As System.Double, _
   ByVal Z As System.Double, _
   ByVal ConfigurationOption As System.Integer, _
   ByVal ConfigurationName As System.String _
) As System.Boolean
```

### Visual Basic (Usage)

```vb
Dim instance As IParameter
Dim X As System.Double
Dim Y As System.Double
Dim Z As System.Double
Dim ConfigurationOption As System.Integer
Dim ConfigurationName As System.String
Dim value As System.Boolean

value = instance.SetVector2(X, Y, Z, ConfigurationOption, ConfigurationName)
```

### C#

```csharp
System.bool SetVector2(
   System.double X,
   System.double Y,
   System.double Z,
   System.int ConfigurationOption,
   System.string ConfigurationName
)
```

### C++/CLI

```cpp
System.bool SetVector2(
   System.double X,
   System.double Y,
   System.double Z,
   System.int ConfigurationOption,
   System.String^ ConfigurationName
)
```

**NOTE:** See [Differences Between Unmanaged C++ and C++/CLI Code](DifferencesBetweenUnManagedAndCPPCLI.htm).

### Parameters

- `X`: x value to store for the named configuration option
- `Y`: y value to store for the named configuration option
- `Z`: z value to store for the named configuration option
- `ConfigurationOption`: Configuration option as defined in [swInConfigurationOpts_e](ms-its:swconst.chm::/SOLIDWORKS.Interop.swconst~SOLIDWORKS.Interop.swconst.swInConfigurationOpts_e.html)
- `ConfigurationName`: Name of the configuration

### Return Value

True if successful, false if not

## VBA Syntax

See [Parameter::SetVector2](ms-its:sldworksapivb6.chm::/sldworks~Parameter~SetVector2.html).

## Remarks

The ConfigurationName argument is:

- Not required if ConfigurationOption is set to swThisConfiguration = 1 or swAllConfiguration = 2.
- Required if ConfigurationOption is set to swSpecifyConfiguration = 3.

Set the ConfigurationOption argument to swAllConfiguration = 2 for Drawing Docs as they do not have configurations.

## See Also

[IParameter Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IParameter.html)
[IParameter Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IParameter_members.html)
[IParameter::GetVector Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IParameter~GetVector.html)
[IParameter::GetVectorVB Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IParameter~GetVectorVB.html)
