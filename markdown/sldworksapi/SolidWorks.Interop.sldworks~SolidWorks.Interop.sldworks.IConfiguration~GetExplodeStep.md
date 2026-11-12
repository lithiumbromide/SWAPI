---
title: "GetExplodeStep Method (IConfiguration)"
project: "SOLIDWORKS API Help"
interface: "IConfiguration"
member: "GetExplodeStep"
kind: "method"
source: "sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IConfiguration~GetExplodeStep.html"
---

# GetExplodeStep Method (IConfiguration)

Gets the specified explode step in this configuration's explode step sequence.

## Syntax

### Visual Basic (Declaration)

```vb
Function GetExplodeStep( _
   ByVal ExplodeStepIndex As System.Integer _
) As System.Object
```

### Visual Basic (Usage)

```vb
Dim instance As IConfiguration
Dim ExplodeStepIndex As System.Integer
Dim value As System.Object

value = instance.GetExplodeStep(ExplodeStepIndex)
```

### C#

```csharp
System.object GetExplodeStep(
   System.int ExplodeStepIndex
)
```

### C++/CLI

```cpp
System.Object^ GetExplodeStep(
   System.int ExplodeStepIndex
)
```

**NOTE:** See [Differences Between Unmanaged C++ and C++/CLI Code](DifferencesBetweenUnManagedAndCPPCLI.htm).

### Parameters

- `ExplodeStepIndex`: Index of the explode step in the explode step sequence

### Return Value

[Explode step](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.IExplodeStep.html)

## VBA Syntax

See [Configuration::GetExplodeStep](ms-its:sldworksapivb6.chm::/sldworks~Configuration~GetExplodeStep.html).

## Examples

See the [IExplodeStep](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IExplodeStep.html) examples.

## Examples

[Get Explode Step (C#)](Get_Explode_Step_Example_CSharp.htm)
[Get Explode Step (VB.NET)](Get_Explode_Step_Example_VBNET.htm)
[Get Explode Step (VBA)](Get_Explode_Step_Example_VB.htm)

## Remarks

Before calling this method, call [IConfiguration::GetNumberOfExplodeSteps](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.IConfiguration~GetNumberOfExplodeSteps.html) to get the number of explode steps in the explode step sequence.

## See Also

[IConfiguration Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IConfiguration.html)
[IConfiguration Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IConfiguration_members.html)
[IConfiguration::AddExplodeStep Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IConfiguration~AddExplodeStep.html)
[IConfiguration::DeleteExplodeStep Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IConfiguration~DeleteExplodeStep.html)
[IConfiguration::IGetExplodeStep Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IConfiguration~IGetExplodeStep.html)
[IConfiguration::IAddExplodeStep Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IConfiguration~IAddExplodeStep.html)
[IConfiguration::AddRadialExplodeStep Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IConfiguration~AddRadialExplodeStep.html)

## Availability

SOLIDWORKS 2001 FCS, Revision Number 9.0
