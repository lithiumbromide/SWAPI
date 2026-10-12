---
title: "GetLightEnabledInRender Method (IModelDocExtension)"
project: "SOLIDWORKS API Help"
interface: "IModelDocExtension"
member: "GetLightEnabledInRender"
kind: "method"
source: "sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelDocExtension~GetLightEnabledInRender.html"
---

# GetLightEnabledInRender Method (IModelDocExtension)

Gets whether a light is on in this model.

## Syntax

### Visual Basic (Declaration)

```vb
Function GetLightEnabledInRender( _
   ByVal ID As System.Integer _
) As System.Boolean
```

### Visual Basic (Usage)

```vb
Dim instance As IModelDocExtension
Dim ID As System.Integer
Dim value As System.Boolean

value = instance.GetLightEnabledInRender(ID)
```

### C#

```csharp
System.bool GetLightEnabledInRender(
   System.int ID
)
```

### C++/CLI

```cpp
System.bool GetLightEnabledInRender(
   System.int ID
)
```

**NOTE:** See [Differences Between Unmanaged C++ and C++/CLI Code](DifferencesBetweenUnManagedAndCPPCLI.htm).

### Parameters

- `ID`: Light ID

### Return Value

True of the light is on, false if not

## VBA Syntax

See [ModelDocExtension::GetLightEnabledInRender](ms-its:sldworksapivb6.chm::/Sldworks~ModelDocExtension~GetLightEnabledInRender.html).

## See Also

[IModelDocExtension Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelDocExtension.html)
[IModelDocExtension Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelDocExtension_members.html)
[IModelDocExtension::SetLightEnabledInRender Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelDocExtension~SetLightEnabledInRender.html)

## Availability

SOLIDWORKS 2008 FCS, Revision Number 16.0
