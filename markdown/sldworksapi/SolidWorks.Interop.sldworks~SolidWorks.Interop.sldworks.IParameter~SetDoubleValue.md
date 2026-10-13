---
title: "SetDoubleValue Method (IParameter)"
project: "SOLIDWORKS API Help"
interface: "IParameter"
member: "SetDoubleValue"
kind: "method"
source: "sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IParameter~SetDoubleValue.html"
---

# SetDoubleValue Method (IParameter)

Obsolete. Superseded by [IParameter::SetDoubleValue2](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.IParameter~SetDoubleValue2.html).

## Syntax

### Visual Basic (Declaration)

```vb
Function SetDoubleValue( _
   ByVal Value As System.Double _
) As System.Boolean
```

### Visual Basic (Usage)

```vb
Dim instance As IParameter
Dim Value As System.Double
Dim value As System.Boolean

value = instance.SetDoubleValue(Value)
```

### C#

```csharp
System.bool SetDoubleValue(
   System.double Value
)
```

### C++/CLI

```cpp
System.bool SetDoubleValue(
   System.double Value
)
```

**NOTE:** See [Differences Between Unmanaged C++ and C++/CLI Code](DifferencesBetweenUnManagedAndCPPCLI.htm).

### Parameters

- `Value`:

## VBA Syntax

See [Parameter::SetDoubleValue](ms-its:sldworksapivb6.chm::/sldworks~Parameter~SetDoubleValue.html).

## See Also

[IParameter Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IParameter.html)
[IParameter Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IParameter_members.html)
