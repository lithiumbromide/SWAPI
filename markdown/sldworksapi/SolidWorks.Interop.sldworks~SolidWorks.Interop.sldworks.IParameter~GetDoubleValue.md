---
title: "GetDoubleValue Method (IParameter)"
project: "SOLIDWORKS API Help"
interface: "IParameter"
member: "GetDoubleValue"
kind: "method"
source: "sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IParameter~GetDoubleValue.html"
---

# GetDoubleValue Method (IParameter)

Gets an attribute value of type double.

## Syntax

### Visual Basic (Declaration)

```vb
Function GetDoubleValue() As System.Double
```

### Visual Basic (Usage)

```vb
Dim instance As IParameter
Dim value As System.Double

value = instance.GetDoubleValue()
```

### C#

```csharp
System.double GetDoubleValue()
```

### C++/CLI

```cpp
System.double GetDoubleValue();
```

**NOTE:** See [Differences Between Unmanaged C++ and C++/CLI Code](DifferencesBetweenUnManagedAndCPPCLI.htm).

### Return Value

Attribute value of type double

## VBA Syntax

See [Parameter::GetDoubleValue](ms-its:sldworksapivb6.chm::/sldworks~Parameter~GetDoubleValue.html).

## Examples

[Find Attribute (C#)](Find_Attribute_Example_CSharp.htm)
[Find Attribute (VB.NET)](Find_Attribute_Example_VBNET.htm)
[Find Attribute (VBA)](Find_Attribute_Example_VB.htm)

## Remarks

Value of the parameter in system units

## See Also

[IParameter Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IParameter.html)
[IParameter Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IParameter_members.html)
[IParameter::SetDoubleValue2 Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IParameter~SetDoubleValue2.html)
