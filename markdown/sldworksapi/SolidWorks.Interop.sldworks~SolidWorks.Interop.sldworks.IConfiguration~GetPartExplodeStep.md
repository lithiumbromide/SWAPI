---
title: "GetPartExplodeStep Method (IConfiguration)"
project: "SOLIDWORKS API Help"
interface: "IConfiguration"
member: "GetPartExplodeStep"
kind: "method"
source: "sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IConfiguration~GetPartExplodeStep.html"
---

# GetPartExplodeStep Method (IConfiguration)

Gets the specified explode step of an explode view of a multibody part.

## Syntax

### Visual Basic (Declaration)

```vb
Function GetPartExplodeStep( _
   ByVal Index As System.Integer _
) As System.Object
```

### Visual Basic (Usage)

```vb
Dim instance As IConfiguration
Dim Index As System.Integer
Dim value As System.Object

value = instance.GetPartExplodeStep(Index)
```

### C#

```csharp
System.object GetPartExplodeStep(
   System.int Index
)
```

### C++/CLI

```cpp
System.Object^ GetPartExplodeStep(
   System.int Index
)
```

**NOTE:** See [Differences Between Unmanaged C++ and C++/CLI Code](DifferencesBetweenUnManagedAndCPPCLI.htm).

### Parameters

- `Index`: Index of the explode step (see **Remarks**)

### Return Value

[IPartExplodeStep](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IPartExplodeStep.html)

## VBA Syntax

See [Configuration::GetPartExplodeStep](ms-its:sldworksapivb6.chm::/sldworks~Configuration~GetPartExplodeStep.html).

## Remarks

This method is valid only for the active configuration.

Before calling this method, call [IPartDoc::ShowExploded](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IPartDoc~ShowExploded.html) to activate the explode view of interest.

To specify Index, call [IConfiguration::GetNumberOfPartExplodeSteps](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IConfiguration~GetNumberOfPartExplodeSteps.html) to get the number of explode steps in the explode view.

## See Also

[IConfiguration Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IConfiguration.html)
[IConfiguration Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IConfiguration_members.html)
[IConfiguration::AddPartExplodeStep Method ()](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IConfiguration~AddPartExplodeStep.html)
[IConfiguration::DeleteExplodeStep Method ()](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IConfiguration~DeleteExplodeStep.html)
[IConfiguration::GetCurrentPartExplodeViewName Method ()](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IConfiguration~GetCurrentPartExplodeViewName.html)

## Availability

SOLIDWORKS 2020 FCS, Revision Number 28.0
