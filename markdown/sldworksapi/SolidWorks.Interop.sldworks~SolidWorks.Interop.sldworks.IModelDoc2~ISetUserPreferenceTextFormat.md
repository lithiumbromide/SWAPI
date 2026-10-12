---
title: "ISetUserPreferenceTextFormat Method (IModelDoc2)"
project: "SOLIDWORKS API Help"
interface: "IModelDoc2"
member: "ISetUserPreferenceTextFormat"
kind: "method"
source: "sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelDoc2~ISetUserPreferenceTextFormat.html"
---

# ISetUserPreferenceTextFormat Method (IModelDoc2)

Obsolete. Superseded by [IModelDocExtension::SetUserPreferenceTextFormat](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.IModelDocExtension~SetUserPreferenceTextFormat.html).

## Syntax

### Visual Basic (Declaration)

```vb
Function ISetUserPreferenceTextFormat( _
   ByVal UserPreferenceValue As System.Integer, _
   ByVal Value As TextFormat _
) As System.Boolean
```

### Visual Basic (Usage)

```vb
Dim instance As IModelDoc2
Dim UserPreferenceValue As System.Integer
Dim Value As TextFormat
Dim value As System.Boolean

value = instance.ISetUserPreferenceTextFormat(UserPreferenceValue, Value)
```

### C#

```csharp
System.bool ISetUserPreferenceTextFormat(
   System.int UserPreferenceValue,
   TextFormat Value
)
```

### C++/CLI

```cpp
System.bool ISetUserPreferenceTextFormat(
   System.int UserPreferenceValue,
   TextFormat^ Value
)
```

**NOTE:** See [Differences Between Unmanaged C++ and C++/CLI Code](DifferencesBetweenUnManagedAndCPPCLI.htm).

### Parameters

- `UserPreferenceValue`: User preference to change as defined in [swUserPreferenceTextFormat_e](ms-its:swconst.chm::/SOLIDWORKS.Interop.swconst~SOLIDWORKS.Interop.swconst.swUserPreferenceTextFormat_e.html)
- `Value`: Text format to which to assign the user preference specified in UserPreferenceValue

### Return Value

True if the setting is changed successfully, false if not

## VBA Syntax

See [ModelDoc2::ISetUserPreferenceTextFormat](ms-its:sldworksapivb6.chm::/sldworks~ModelDoc2~ISetUserPreferenceTextFormat.html).

## Remarks

This method is

- intended for setting detailing text formats.
- equivalent to interactively setting document options in the SOLIDWORKS Design software.

See [System Options and Document Properties](sldworksapiprogguide.chm::/overview/System_Options_and_Document_Properties.htm) for details.

## See Also

[IModelDoc2 Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelDoc2.html)
[IModelDoc2 Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelDoc2_members.html)

## Availability

SOLIDWORKS 2001Plus FCS, Revision Number 10.0
