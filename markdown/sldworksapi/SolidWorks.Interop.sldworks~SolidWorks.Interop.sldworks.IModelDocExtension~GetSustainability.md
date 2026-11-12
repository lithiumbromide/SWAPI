---
title: "GetSustainability Method (IModelDocExtension)"
project: "SOLIDWORKS API Help"
interface: "IModelDocExtension"
member: "GetSustainability"
kind: "method"
source: "sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelDocExtension~GetSustainability.html"
---

# GetSustainability Method (IModelDocExtension)

Gets the entry-point interface to the SOLIDWORKS Sustainability API.

## Syntax

### Visual Basic (Declaration)

```vb
Function GetSustainability() As System.Object
```

### Visual Basic (Usage)

```vb
Dim instance As IModelDocExtension
Dim value As System.Object

value = instance.GetSustainability()
```

### C#

```csharp
System.object GetSustainability()
```

### C++/CLI

```cpp
System.Object^ GetSustainability();
```

**NOTE:** See [Differences Between Unmanaged C++ and C++/CLI Code](DifferencesBetweenUnManagedAndCPPCLI.htm).

### Return Value

[ISustainabilityApp](ms-its:sustainabilityapi.chm::/SOLIDWORKS.Interop.sustainability~SOLIDWORKS.Interop.sustainability.ISustainabilityApp.html)

## VBA Syntax

See [ModelDocExtension::GetSustainability](ms-its:sldworksapivb6.chm::/sldworks~ModelDocExtension~GetSustainability.html).

## Examples

[Calculate Environmental Impact of Part (VBA)](Calculate_Environmental_Impact_of_Part_Example_VB.htm)
[Calculate Environmental Impact of Part (VB.NET)](Calculate_Environmental_Impact_of_Part_Example_VBNET.htm)
[Calculate Environmental Impact of Part (C#)](Calculate_Environmental_Impact_of_Part_Example_CSharp.htm)
[Calculate Environmental Impact of Assembly (VBA)](Calculate_Environmental_Impact_of_Assembly_Example_VB.htm)
[Calculate Environmental Impact of Assembly (VB.NET)](Calculate_Environmental_Impact_of_Assembly_Example_VBNET.htm)
[Calculate Environmental Impact of Assembly (C#)](Calculate_Environmental_Impact_of_Assembly_Example_CSharp.htm)

## Remarks

SOLIDWORKS Sustainability and its API are only available in SOLIDWORKS Professional and SOLIDWORKS Premium.

## See Also

[IModelDocExtension Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelDocExtension.html)
[IModelDocExtension Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelDocExtension_members.html)

## Availability

SOLIDWORKS 2013 FCS, Revision Number 21.0
