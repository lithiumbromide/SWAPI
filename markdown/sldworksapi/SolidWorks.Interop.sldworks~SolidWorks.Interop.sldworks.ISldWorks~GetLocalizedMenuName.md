---
title: "GetLocalizedMenuName Method (ISldWorks)"
project: "SOLIDWORKS API Help"
interface: "ISldWorks"
member: "GetLocalizedMenuName"
kind: "method"
source: "sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISldWorks~GetLocalizedMenuName.html"
---

# GetLocalizedMenuName Method (ISldWorks)

Gets a localized menu name for the specified menu ID.

## Syntax

### Visual Basic (Declaration)

```vb
Function GetLocalizedMenuName( _
   ByVal MenuId As System.Integer _
) As System.String
```

### Visual Basic (Usage)

```vb
Dim instance As ISldWorks
Dim MenuId As System.Integer
Dim value As System.String

value = instance.GetLocalizedMenuName(MenuId)
```

### C#

```csharp
System.string GetLocalizedMenuName(
   System.int MenuId
)
```

### C++/CLI

```cpp
System.String^ GetLocalizedMenuName(
   System.int MenuId
)
```

**NOTE:** See [Differences Between Unmanaged C++ and C++/CLI Code](DifferencesBetweenUnManagedAndCPPCLI.htm).

### Parameters

- `MenuId`: Menu ID as defined in [swMenuIdentifiers_e](ms-its:swconst.chm::/SOLIDWORKS.Interop.swconst~SOLIDWORKS.Interop.swconst.swMenuIdentifiers_e.html)

### Return Value

String containing the localized menu name

## VBA Syntax

See [SldWorks::GetLocalizedMenuName](ms-its:sldworksapivb6.chm::/sldworks~SldWorks~GetLocalizedMenuName.html).

## Examples

[Get Language and Localized Menu Names (VBA)](Get_Language_and_Localized_Menu_Names_Example_VB.htm)

## Remarks

The string returned allows the application to provide a correctly localized string representing the menu name that menus and menu items can be when added to in the SOLIDWORKS Design user interface.

This method should be called before [ISldWorks::AddMenu](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.ISldWorks~AddMenu.html), [ISldWorks::AddMenuItem3](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.ISldWorks~AddMenuItem3.html), [IFrame::AddMenu](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.IFrame~AddMenu.html), or [IFrame::AddMenuItem2](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.IFrame~AddMenuItem2.html).

## See Also

[ISldWorks Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISldWorks.html)
[ISldWorks Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISldWorks_members.html)
