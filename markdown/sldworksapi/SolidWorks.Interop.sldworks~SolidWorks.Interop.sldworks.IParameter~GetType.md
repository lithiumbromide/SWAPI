---
title: "GetType Method (IParameter)"
project: "SOLIDWORKS API Help"
interface: "IParameter"
member: "GetType"
kind: "method"
source: "sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IParameter~GetType.html"
---

# GetType Method (IParameter)

Gets the type of data stored on the parameter.

## Syntax

### Visual Basic (Declaration)

```vb
Function GetType() As System.Integer
```

### Visual Basic (Usage)

```vb
Dim instance As IParameter
Dim value As System.Integer

value = instance.GetType()
```

### C#

```csharp
System.int GetType()
```

### C++/CLI

```cpp
System.int GetType();
```

**NOTE:** See [Differences Between Unmanaged C++ and C++/CLI Code](DifferencesBetweenUnManagedAndCPPCLI.htm).

### Return Value

Type of data stored on the parameter as defined in [swParam_Type_e](ms-its:swconst.chm::/SOLIDWORKS.Interop.swconst~SOLIDWORKS.Interop.swconst.swParamType_e.html)

## VBA Syntax

See [Parameter::GetType](ms-its:sldworksapivb6.chm::/sldworks~Parameter~GetType.html).

## Examples

[Enumerate Bodies (C++)](Enumerate_Bodies_Example_CPlusPlus_COM.htm)
[Get Document Information (VBA)](Get_Document_Information_Example_VB.htm)
[Create Note (VBA)](Create_Note_Example_VB.htm)

## See Also

[IParameter Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IParameter.html)
[IParameter Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IParameter_members.html)
