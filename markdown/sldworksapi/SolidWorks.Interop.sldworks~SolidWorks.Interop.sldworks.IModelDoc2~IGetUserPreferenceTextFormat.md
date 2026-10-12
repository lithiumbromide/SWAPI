---
title: "IGetUserPreferenceTextFormat Method (IModelDoc2)"
project: "SOLIDWORKS API Help"
interface: "IModelDoc2"
member: "IGetUserPreferenceTextFormat"
kind: "method"
source: "sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelDoc2~IGetUserPreferenceTextFormat.html"
---

# IGetUserPreferenceTextFormat Method (IModelDoc2)

Obsolete. Superseded by [IModelDocExtension::GetUserPreferenceTextFormat](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.IModelDocExtension~GetUserPreferenceTextFormat.html).

## Syntax

### Visual Basic (Declaration)

```vb
Function IGetUserPreferenceTextFormat( _
   ByVal UserPreferenceValue As System.Integer _
) As TextFormat
```

### Visual Basic (Usage)

```vb
Dim instance As IModelDoc2
Dim UserPreferenceValue As System.Integer
Dim value As TextFormat

value = instance.IGetUserPreferenceTextFormat(UserPreferenceValue)
```

### C#

```csharp
TextFormat IGetUserPreferenceTextFormat(
   System.int UserPreferenceValue
)
```

### C++/CLI

```cpp
TextFormat^ IGetUserPreferenceTextFormat(
   System.int UserPreferenceValue
)
```

**NOTE:** See [Differences Between Unmanaged C++ and C++/CLI Code](DifferencesBetweenUnManagedAndCPPCLI.htm).

### Parameters

- `UserPreferenceValue`: Value as defined in [swUserPreferenceTextFormat_e](ms-its:swconst.chm::/SOLIDWORKS.Interop.swconst~SOLIDWORKS.Interop.swconst.swUserPreferenceTextFormat_e.html)

### Return Value

[Text format](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.ITextFormat.html) associated with UserPreferenceValue

## VBA Syntax

See [ModelDoc2::IGetUserPreferenceTextFormat](ms-its:sldworksapivb6.chm::/sldworks~ModelDoc2~IGetUserPreferenceTextFormat.html).

## Remarks

This method is equivalent to interactively getting document properties in the SOLIDWORKS Design software. See [System Options and Document Properties](sldworksapiprogguide.chm::/overview/System_Options_and_Document_Properties.htm) for details.

## See Also

[IModelDoc2 Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelDoc2.html)
[IModelDoc2 Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelDoc2_members.html)

## Availability

SOLIDWORKS 2001Plus FCS, Revision Number 10.0
