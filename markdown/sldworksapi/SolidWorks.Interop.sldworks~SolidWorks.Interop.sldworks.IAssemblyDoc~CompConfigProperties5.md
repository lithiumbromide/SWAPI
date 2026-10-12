---
title: "CompConfigProperties5 Method (IAssemblyDoc)"
project: "SOLIDWORKS API Help"
interface: "IAssemblyDoc"
member: "CompConfigProperties5"
kind: "method"
source: "sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IAssemblyDoc~CompConfigProperties5.html"
---

# CompConfigProperties5 Method (IAssemblyDoc)

Obsolete. Superseded by [IAssemblyDoc::CompConfigProperties6](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IAssemblyDoc~CompConfigProperties6.html).

## Syntax

### Visual Basic (Declaration)

```vb
Function CompConfigProperties5( _
   ByVal Suppression As System.Integer, _
   ByVal Solving As System.Integer, _
   ByVal Visibility As System.Boolean, _
   ByVal UseNamedRefConfig As System.Boolean, _
   ByVal RefConfigName As System.String, _
   ByVal ExcludeFromBOM As System.Boolean, _
   ByVal IsEnvelope As System.Boolean _
) As System.Boolean
```

### Visual Basic (Usage)

```vb
Dim instance As IAssemblyDoc
Dim Suppression As System.Integer
Dim Solving As System.Integer
Dim Visibility As System.Boolean
Dim UseNamedRefConfig As System.Boolean
Dim RefConfigName As System.String
Dim ExcludeFromBOM As System.Boolean
Dim IsEnvelope As System.Boolean
Dim value As System.Boolean

value = instance.CompConfigProperties5(Suppression, Solving, Visibility, UseNamedRefConfig, RefConfigName, ExcludeFromBOM, IsEnvelope)
```

### C#

```csharp
System.bool CompConfigProperties5(
   System.int Suppression,
   System.int Solving,
   System.bool Visibility,
   System.bool UseNamedRefConfig,
   System.string RefConfigName,
   System.bool ExcludeFromBOM,
   System.bool IsEnvelope
)
```

### C++/CLI

```cpp
System.bool CompConfigProperties5(
   System.int Suppression,
   System.int Solving,
   System.bool Visibility,
   System.bool UseNamedRefConfig,
   System.String^ RefConfigName,
   System.bool ExcludeFromBOM,
   System.bool IsEnvelope
)
```

**NOTE:** See [Differences Between Unmanaged C++ and C++/CLI Code](DifferencesBetweenUnManagedAndCPPCLI.htm).

### Parameters

- `Suppression`: Suppression state of this component as defined in [swComponentSuppressionState_e](ms-its:swconst.chm::/SOLIDWORKS.Interop.swconst~SOLIDWORKS.Interop.swconst.swComponentSuppressionState_e.html)
- `Solving`: Solving state of this component as defined in [swComponentSolvingOption_e](ms-its:swconst.chm::/SOLIDWORKS.Interop.swconst~SOLIDWORKS.Interop.swconst.swComponentSolvingOption_e.html)
- `Visibility`: True if you want to show the selected component in the graphics area, false if not
- `UseNamedRefConfig`: Not used
- `RefConfigName`: - If a non-empty string is specified, then the referenced configuration of the selected component is changed to this named configuration
  - If an empty string is specified, then the default referenced configuration is used
- `ExcludeFromBOM`: True to exclude the configuration from the BOM, false to not
- `IsEnvelope`: True if the component is an envelope, false if not

### Return Value

True if setting the properties of the selected component in the specified configuration is successful, false if not

## VBA Syntax

See [AssemblyDoc::CompConfigProperties5](ms-its:sldworksapivb6.chm::/sldworks~AssemblyDoc~CompConfigProperties5.html).

## Remarks

You can use configurations to save certain display characteristics with each of the assembly components and retrieve that configuration in the future. SOLIDWORKS Design applies the settings that you specify with this method to the active configuration.

You cannot set a component to lightweight.

Known reasons for failure of this method include:

- Invalid suppression state specified.
- Not preselecting a component.

## See Also

[IAssemblyDoc Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IAssemblyDoc.html)
[IAssemblyDoc Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IAssemblyDoc_members.html)
[IComponent2::SetSuppression2 Method ()](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IComponent2~SetSuppression2.html)
[IComponent2::ReferencedConfiguration Property ()](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IComponent2~ReferencedConfiguration.html)
[IComponent2::IsEnvelope Method ()](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IComponent2~IsEnvelope.html)
[IComponent2::Solving Property ()](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IComponent2~Solving.html)
[IComponent2::ExcludeFromBOM Property ()](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IComponent2~ExcludeFromBOM.html)
[IComponent2::Visible Property ()](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IComponent2~Visible.html)

## Availability

SOLIDWORKS 2017 FCS, Revision Number 25.0
