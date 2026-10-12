---
title: "SetStringValue Method (IParameter)"
project: "SOLIDWORKS API Help"
interface: "IParameter"
member: "SetStringValue"
kind: "method"
source: "sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IParameter~SetStringValue.html"
---

# SetStringValue Method (IParameter)

Obsolete. Superseded by [IParameter::SetStringValue2](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.IParameter~SetStringValue2.html).

## Syntax

### Visual Basic (Declaration)

```vb
Function SetStringValue( _
   ByVal StringValue As System.String _
) As System.Boolean
```

### Visual Basic (Usage)

```vb
Dim instance As IParameter
Dim StringValue As System.String
Dim value As System.Boolean

value = instance.SetStringValue(StringValue)
```

### C#

```csharp
System.bool SetStringValue(
   System.string StringValue
)
```

### C++/CLI

```cpp
System.bool SetStringValue(
   System.String^ StringValue
)
```

**NOTE:** See [Differences Between Unmanaged C++ and C++/CLI Code](DifferencesBetweenUnManagedAndCPPCLI.htm).

### Parameters

- `StringValue`:

### Return Value

ms-its:swconst.chm::/SOLIDWORKS.Interop.swconst~SOLIDWORKS.Interop.swconst.swInConfigurationOpts_e.html

## VBA Syntax

See [Parameter::SetStringValue](ms-its:sldworksapivb6.chm::/sldworks~Parameter~SetStringValue.html).

## See Also

[IParameter Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IParameter.html)
[IParameter Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IParameter_members.html)
