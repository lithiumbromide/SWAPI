---
title: "GetUserPreferenceToggle Method (IModelDoc2)"
project: "SOLIDWORKS API Help"
interface: "IModelDoc2"
member: "GetUserPreferenceToggle"
kind: "method"
source: "sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelDoc2~GetUserPreferenceToggle.html"
---

# GetUserPreferenceToggle Method (IModelDoc2)

Obsolete. Superseded by [IModelDocExtension::GetUserPreferenceToggle](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.IModelDocExtension~GetUserPreferenceToggle.html).

## Syntax

### Visual Basic (Declaration)

```vb
Function GetUserPreferenceToggle( _
   ByVal UserPreferenceToggle As System.Integer _
) As System.Boolean
```

### Visual Basic (Usage)

```vb
Dim instance As IModelDoc2
Dim UserPreferenceToggle As System.Integer
Dim value As System.Boolean

value = instance.GetUserPreferenceToggle(UserPreferenceToggle)
```

### C#

```csharp
System.bool GetUserPreferenceToggle(
   System.int UserPreferenceToggle
)
```

### C++/CLI

```cpp
System.bool GetUserPreferenceToggle(
   System.int UserPreferenceToggle
)
```

**NOTE:** See [Differences Between Unmanaged C++ and C++/CLI Code](DifferencesBetweenUnManagedAndCPPCLI.htm).

### Parameters

- `UserPreferenceToggle`: Value as defined in [swUserPreferenceToggle_e](ms-its:swconst.chm::/SOLIDWORKS.Interop.swconst~SOLIDWORKS.Interop.swconst.swUserPreferenceToggle_e.html)

### Return Value

True if the item specified by UserPreferenceToggle is currently toggled on, false if the item is currently toggled off

## VBA Syntax

See [ModelDoc2::GetUserPreferenceToggle](ms-its:sldworksapivb6.chm::/sldworks~ModelDoc2~GetUserPreferenceToggle.html).

## Examples

[Get Material Properties (VBA)](Get_Material_Properties_Example_VB.htm)
[Ignore Feature Colors (VBA)](Ignore_Feature_Colors_Example_VB.htm)

## Remarks

This method is equivalent to interactively getting document properties in the SOLIDWORKS Design software.

The value returned is true if the item is currently turned on, and false if the item is currently turned off. For example:

boolean curState = m_ModelDoc2.GetUserPreferenceToggle( swIgnoreFeatureColors )

See [System Options and Document Properties](sldworksapiprogguide.chm::/overview/System_Options_and_Document_Properties.htm) for details.

## See Also

[IModelDoc2 Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelDoc2.html)
[IModelDoc2 Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelDoc2_members.html)

## Availability

SOLIDWORKS 2001Plus FCS, Revision Number 10.0
