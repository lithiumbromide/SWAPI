---
title: "GetEnvironment Method (ISldWorks)"
project: "SOLIDWORKS API Help"
interface: "ISldWorks"
member: "GetEnvironment"
kind: "method"
source: "sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISldWorks~GetEnvironment.html"
---

# GetEnvironment Method (ISldWorks)

Gets the [IEnvironment](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.IEnvironment.html) object.

## Syntax

### Visual Basic (Declaration)

```vb
Function GetEnvironment() As System.Object
```

### Visual Basic (Usage)

```vb
Dim instance As ISldWorks
Dim value As System.Object

value = instance.GetEnvironment()
```

### C#

```csharp
System.object GetEnvironment()
```

### C++/CLI

```cpp
System.Object^ GetEnvironment();
```

**NOTE:** See [Differences Between Unmanaged C++ and C++/CLI Code](DifferencesBetweenUnManagedAndCPPCLI.htm).

### Return Value

[IEnvironment](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.IEnvironment.html) object

## VBA Syntax

See [SldWorks::GetEnvironment](ms-its:sldworksapivb6.chm::/sldworks~SldWorks~GetEnvironment.html).

## Examples

[Analyze Text and Geometry in GTol Symbol (C#)](Analyze_Text_and_Geometry_in_GTol_Flat_Symbol_Example_CSharp.htm)
[Analyze Text and Geometry in GTol Symbol (VB.NET)](Analyze_Text_and_Geometry_in_GTol_Flat_Symbol_Example_VBNET.htm)
[Analyze Text and Geometry in GTol Symbol (VBA)](Analyze_Text_and_Geometry_in_GTol_Flat_Symbol_Example_VB.htm)

## Remarks

All numeric values returned from the IEnvironment object are relative to a unit text height of 1.0.; i.e., if a symbol has a text height of 0.15, then multiply the numeric values returned by 0.15.

## See Also

[ISldWorks Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISldWorks.html)
[ISldWorks Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISldWorks_members.html)
[ISldWorks::IGetEnvironment Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISldWorks~IGetEnvironment.html)
